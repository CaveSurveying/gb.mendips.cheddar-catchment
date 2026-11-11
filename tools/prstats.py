"""What a pull request changes in the surveys' figures, for its comment.

    python3 -m tools.prstats --base https://cavesurveying.github.io/gb.mendips.cheddar-catchment/ \\
                             --head site > pr-diff/stats.md

Reads the catchment's survey list (files/files.json, which cave-viewer
writes with every survey's length, depth and number of legs) from this
build and from the base (the published site, or an earlier build's
folder), and writes a Markdown summary: the catchment's totals, and every
survey whose figures changed. Plain text only: the PR comment escapes it.
"""
import argparse
import json
import os
import urllib.error
import urllib.parse
import urllib.request

UA = 'gb.mendips.cheddar-catchment PR diff (https://github.com/CaveSurveying/gb.mendips.cheddar-catchment)'
LIST = 'files/files.json'


def load(base):
    """The catchment's survey list, or None if the base hasn't got one."""
    if not base.startswith(('http://', 'https://')):
        path = os.path.join(base, LIST)
        return json.load(open(path, encoding='utf-8')) if os.path.exists(path) else None
    url = urllib.parse.urljoin(base if base.endswith('/') else base + '/', LIST)
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA}), timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def change(a, b, unit=''):
    if a == b:
        return f'{b:,}{unit}'
    if a is None:
        return f'{b:,}{unit} (new)'
    if b is None:
        return f'~~{a:,}{unit}~~'
    return f'{a:,}{unit} → **{b:,}{unit}** ({b - a:+,})'


def main(argv=None):
    ap = argparse.ArgumentParser(prog='python3 -m tools.prstats', description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--base', required=True, help="URL of the published site, or an earlier build's folder")
    ap.add_argument('--head', default='site', help='the site just built')
    a = ap.parse_args(argv)
    head = load(a.head) or {}
    base = load(a.base) or {}
    ht, bt = head.get('survey') or {}, base.get('survey') or {}
    out = ['| The catchment | |', '|---|--:|']
    for key, label, unit in (('length', 'Surveyed length', ' m'), ('depth', 'Depth', ' m'),
                             ('shots', 'Survey legs', ''), ('stations', 'Stations', '')):
        if key in ht:
            out.append(f'| {label} | {change(bt.get(key), ht[key], unit)} |')
    hs = {s['id']: s for s in head.get('surveys', [])}
    bs = {s['id']: s for s in base.get('surveys', [])}
    rows = []
    for sid in sorted(set(hs) | set(bs), key=lambda i: -(hs.get(i) or bs.get(i))['length']):
        h, b = hs.get(sid, {}), bs.get(sid, {})
        if all(h.get(k) == b.get(k) for k in ('length', 'depth', 'shots')):
            continue
        rows.append(f"| {sid} | {change(b.get('length'), h.get('length'), ' m')} | "
                    f"{change(b.get('depth'), h.get('depth'), ' m')} | {change(b.get('shots'), h.get('shots'))} |")
    out.append('')
    if not base:
        out.append("The published site's figures couldn't be read, so these aren't compared.")
    elif rows:
        out += ['| Survey | Length | Depth | Legs |', '|---|--:|--:|--:|', *rows]
    else:
        out.append('No survey\'s length, depth or number of legs changed.')
    print('\n'.join(out) + '\n')


if __name__ == '__main__':
    main()
