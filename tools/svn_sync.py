#!/usr/bin/env python3
"""Bring the Cave Registry's Subversion repository's new revisions into this git repository,
one commit for each, as its history here was brought in: the revision's author, date and message,
and "SVN-Revision: rN" and "SVN-URL: ..." at the end of the message, which is how the next run
knows where it got to.

  python3 tools/svn_sync.py [--url URL] [--to REV] [--dry-run]

Run from the repository's root, on main. It fetches only what each revision changed (svn log
lists the paths; svn cat fetches the files), so it needs no Subversion checkout. Commits; doesn't
push. Needs svn (Subversion's client) and git.

The registry is the source of truth until the switch: nothing here goes back to it.
"""
import argparse
import os
import re
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
from urllib.parse import quote

URL = 'https://www.cave-registry.org.uk/svn/CheddarCatchment'
# the registry's usernames, as the people they are (others are kept as they are)
AUTHORS = {
    'aa.wotcc.org.uk': 'Andrew Atkinson',
    'andrew': 'Andrew Atkinson',
    'graham': 'Graham Mullan',
    'grahammullan': 'Graham Mullan',
    'JohnCooper': 'John Cooper',
}
# the git repository's own files, which the registry doesn't have: never touched by a sync
OURS = {'.git', '.github', '.gitignore', 'README.md', 'requirements.txt', 'tools', 'docs', 'caves.json'}
# the registry's folders that are access-restricted there, and so never brought in
RESTRICTED = {'Outputs', 'PocketTopo'}


def svn(*args, binary=False):
    r = subprocess.run(['svn', '--non-interactive', *args], capture_output=True, check=True)
    return r.stdout if binary else r.stdout.decode('utf-8')


def git(*args, env=None):
    return subprocess.run(['git', *args], capture_output=True, text=True, check=True,
                          env={**os.environ, **(env or {})}).stdout


def last_synced():
    """The last revision brought in, from the newest commit that says one."""
    try:
        log = git('log', '--format=%B', '--grep=^SVN-Revision: r', '-n', '1')
    except subprocess.CalledProcessError:      # (a new repository, with no commits yet)
        return 0
    m = re.search(r'^SVN-Revision: r(\d+)', log, re.M)
    return int(m.group(1)) if m else 0


def head_revision(url):
    info = ET.fromstring(svn('info', '--xml', url))
    return int(info.find('entry').get('revision'))


def at(url, path, rev):
    """A path's URL at a revision (peg revision, so a file deleted later is still found)."""
    return f"{url}{quote(path)}@{rev}"


def fetch(url, path, rev):
    """A file's contents at a revision into the working tree."""
    dest = path.lstrip('/')
    if dest.split('/')[0] in OURS:
        print(f'  skipped {dest}: one of this repository\'s own paths', file=sys.stderr)
        return
    if dest.split('/')[0] in RESTRICTED:
        return
    os.makedirs(os.path.dirname(dest) or '.', exist_ok=True)
    with open(dest, 'wb') as f:
        f.write(svn('cat', at(url, path, rev), binary=True))


def fetch_dir(url, path, rev):
    """A directory, all of it (a copied or added folder's contents aren't listed in the log)."""
    if path.lstrip('/').split('/')[0] in OURS | RESTRICTED:
        return
    os.makedirs(path.lstrip('/'), exist_ok=True)
    for entry in svn('list', '-R', at(url, path, rev)).splitlines():
        if entry.endswith('/'):
            os.makedirs(os.path.join(path.lstrip('/'), entry), exist_ok=True)
        else:
            fetch(url, f"{path.rstrip('/')}/{entry}", rev)


def remove(path):
    dest = path.lstrip('/')
    if dest.split('/')[0] in OURS | RESTRICTED:
        return
    if os.path.isdir(dest):
        shutil.rmtree(dest)
    elif os.path.exists(dest):
        os.remove(dest)


def apply(url, entry):
    """One revision's changes, to the working tree: deletions first, then the rest in order."""
    rev = int(entry.get('revision'))
    paths = entry.find('paths')
    changes = [(p.get('action'), p.get('kind'), p.text) for p in (paths if paths is not None else [])]
    for action, kind, path in changes:
        if action in ('D', 'R'):
            remove(path)
    for action, kind, path in sorted(changes, key=lambda c: c[2].count('/')):
        if action == 'D':
            continue
        if kind == 'dir':
            if action in ('A', 'R'):
                fetch_dir(url, path, rev)
        elif action in ('A', 'M', 'R'):
            fetch(url, path, rev)
    return rev


def commit(url, entry, rev):
    who = (entry.findtext('author') or 'unknown').strip()
    name = AUTHORS.get(who, who)
    email = f'{who}@cave-registry.invalid'
    date = entry.findtext('date')
    msg = (entry.findtext('msg') or '').strip() or f'Registry revision {rev}'
    git('add', '-A', '--', '.', *[f':!{p}' for p in OURS | RESTRICTED if p != '.git'])
    env = {'GIT_AUTHOR_NAME': name, 'GIT_AUTHOR_EMAIL': email, 'GIT_AUTHOR_DATE': date,
           'GIT_COMMITTER_NAME': name, 'GIT_COMMITTER_EMAIL': email, 'GIT_COMMITTER_DATE': date}
    git('commit', '--allow-empty', '-q', '-m', f'{msg}\n\nSVN-Revision: r{rev}\nSVN-URL: {url}', env=env)
    print(f'r{rev}: {msg.splitlines()[0][:70]} ({name})', file=sys.stderr)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('--url', default=URL)
    ap.add_argument('--to', type=int, help='stop at this revision (default: the newest)')
    ap.add_argument('--dry-run', action='store_true', help='say what would come in, and change nothing')
    a = ap.parse_args()
    url = a.url.rstrip('/')
    since, head = last_synced(), a.to or head_revision(url)
    if since >= head:
        print(f'Up to date at r{since}.', file=sys.stderr)
        return
    log = ET.fromstring(svn('log', '--xml', '-v', '-r', f'{since + 1}:{head}', url))
    entries = log.findall('logentry')
    print(f'r{since + 1} to r{head}: {len(entries)} revisions', file=sys.stderr)
    for entry in entries:
        if a.dry_run:
            print(f"r{entry.get('revision')}: {(entry.findtext('msg') or '').strip()[:70]}")
            continue
        commit(url, entry, apply(url, entry))


if __name__ == '__main__':
    main()
