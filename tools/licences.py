"""What each cave's data says about its licence and who made it.

    python3 -m tools.licences            # writes LICENCES.md

For every cave folder (a top-level folder with Therion or Survex files in
it): the licence and copyright statements in its files (Therion's
`copyright` lines, and any licence file), the credits on its title box,
who surveyed it (`team` lines, most often first) and who committed it
(from git, where there is history). It only reports what the files say:
where they say nothing, nothing is assumed.
"""
import collections
import json
import os
import re
import subprocess
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCES = ('.th', '.th2', '.svx', '.thconfig')
COPYRIGHT = re.compile(r'^\s*copyright\s+(\S+)\s+"([^"]+)"', re.I)
TEAM = re.compile(r'^\s*(?:team|explo-team)\s+"([^"]+)"', re.I)
SKIP = {'.git', '.github', 'tools', 'build', 'site', 'lidar', 'Outputs', 'Symbols', 'PocketTopo', 'Other_Sites'}


def caves(root=ROOT):
    for d in sorted(os.listdir(root)):
        p = os.path.join(root, d)
        if d in SKIP or d.startswith('.') or not os.path.isdir(p):
            continue
        if any(f.endswith(SOURCES) for _, _, fs in os.walk(p) for f in fs):
            yield d


def title_box(path):
    """The text of a title box (.odt or .pdf), as lines."""
    try:
        if path.endswith('.odt'):
            xml = zipfile.ZipFile(path).read('content.xml').decode('utf-8', 'replace')
            text = re.sub(r'<text:(p|h)[^>]*>', '\n', xml)
            text = re.sub(r'<[^>]+>', '', text)
        else:
            text = subprocess.run(['pdftotext', path, '-'], capture_output=True, text=True).stdout
    except (OSError, zipfile.BadZipFile, KeyError):
        return []
    text = text.replace('&apos;', "'").replace('&amp;', '&')
    return [l.strip() for l in text.splitlines() if l.strip()]


def scan(cave, root=ROOT):
    rights, team, licence_files, boxes = collections.Counter(), collections.Counter(), [], []
    for d, dirs, fs in os.walk(os.path.join(root, cave)):
        for f in fs:
            p = os.path.join(d, f)
            rel = os.path.relpath(p, root)
            if re.match(r'licen[cs]e|copying', f, re.I):
                licence_files.append((rel, open(p, encoding='utf-8', errors='replace').read().strip()))
            if re.search(r'title_?box', f, re.I) and f.endswith(('.odt', '.pdf')):
                boxes.append((rel, title_box(p)))
            if f.endswith(SOURCES):
                for line in open(p, encoding='utf-8', errors='replace'):
                    m = COPYRIGHT.match(line)
                    if m:
                        rights[m.group(2).strip()] += 1
                    m = TEAM.match(line)
                    if m:
                        team[m.group(1).strip()] += 1
    try:
        log = subprocess.run(['git', '-C', root, 'log', '--format=%an', '--', cave], capture_output=True, text=True).stdout
        committers = collections.Counter(l for l in log.splitlines() if l)
    except OSError:
        committers = collections.Counter()
    return {'rights': rights, 'team': team, 'licence_files': licence_files, 'boxes': boxes, 'committers': committers}


CREDIT = re.compile(r'produced by|survey data|published by|copyright|licen|creative|drawn by|surveyed by', re.I)


def markdown(found):
    out = ['# What the data says about its licences', '',
           'Made by `python3 -m tools.licences` from the files themselves: each cave\'s',
           'licence and copyright statements, title-box credits, surveyors and',
           'committers. Where a cave\'s files say nothing about a licence, that is',
           'what is shown: nothing is assumed. Questions still open, and who to ask,',
           'are in the README.', '',
           '| Cave | Licence and copyright, as stated | Credits on its title box | Surveyed by (most often first) |',
           '|---|---|---|---|']
    for cave, s in found.items():
        stated = [f'{t} (×{n})' if n > 1 else t for t, n in s['rights'].most_common()]
        stated += [f'`{p}`: {" ".join(txt.split())[:160]}' for p, txt in s['licence_files']]
        credits = list(dict.fromkeys(l.rstrip(',') for p, lines in s['boxes'] for l in lines if CREDIT.search(l)))   # (a title box as .odt and .pdf says it twice)
        team = [t for t, n in s['team'].most_common(8) if len(t) > 2]
        cell = lambda xs: '<br>'.join(x.replace('|', '\\|') for x in xs) or '—'
        out.append(f'| {cave} | {cell(stated) if stated else "**None stated**"} | {cell(credits)} | {cell(team)} |')
    return '\n'.join(out) + '\n'


def top_boxes(root=ROOT):
    """The title boxes at the top of the data, for more than one cave."""
    out = []
    for f in sorted(os.listdir(root)):
        if re.search(r'title_?box', f, re.I) and f.endswith(('.odt', '.pdf')):
            lines = [l for l in title_box(os.path.join(root, f)) if CREDIT.search(l)]
            out += ['', f'**{f}**: ' + ' · '.join(lines)]
    return ['', '## Title boxes for more than one cave'] + out if out else []


def main():
    found = {c: scan(c) for c in caves()}
    text = markdown(found) + '\n'.join(top_boxes()) + '\n'
    open(os.path.join(ROOT, 'LICENCES.md'), 'w', encoding='utf-8').write(text)
    summary = {c: {'rights': dict(s['rights']), 'licence_files': [p for p, _ in s['licence_files']],
                   'team': [t for t, _ in s['team'].most_common(8)]} for c, s in found.items()}
    os.makedirs(os.path.join(ROOT, 'build'), exist_ok=True)
    json.dump(summary, open(os.path.join(ROOT, 'build', 'licences.json'), 'w'), indent=1)
    none = [c for c, s in found.items() if not s['rights'] and not s['licence_files']]
    print(f'LICENCES.md: {len(found)} caves, {len(none)} with no licence stated')


if __name__ == '__main__':
    main()
