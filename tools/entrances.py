"""Names for the catchment page's entrances: catchment-names.json.

    python3 -m tools.entrances      # after a build of the catchment (build/catchment/cave.3d)

Every station the survey flags as an entrance, named after its cave: the
cave's title in its Therion file where it has one, else its folder's name
split into words, else NAMES below. Where a cave has more than one
entrance, each is told apart by the part of the survey it's in. Edit
NAMES, not the file it writes, to change a name.
"""
import collections
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

# names the files don't give well
NAMES = {
    'GB': 'GB Cave', 'Goughs': "Gough's Cave", 'GoughsOld': "Gough's Old Cave", 'Reservoir': 'Reservoir Hole',
    'Coxs': "Cox's Cave", 'ReadsGrotto': "Read's Grotto", 'TyningsGS': "Tyning's Great Swallet",
    'TyningsBarrow': "Tyning's Barrows Swallet", 'Grebe_Swallet': 'Grebe Swallet', 'LongHole': 'Long Hole',
    'LongwoodValleySink': 'Longwood Valley Sink', 'Longwood': 'Longwood Swallet', 'Charterhouse': 'Charterhouse Cave',
    'UpperFlood': 'Upper Flood Swallet', 'Sayes': 'Sayes Hole', 'Palmers': "Palmer's Cave", 'Pigs': 'Pigs Hole',
}


def words(name):
    name = name.replace('_', ' ')
    return re.sub(r'(?<=[a-z])(?=[A-Z0-9])|(?<=[A-Z])(?=[A-Z][a-z])', ' ', name).strip()


def titles():
    """{survey id: title} from each cave's Therion files."""
    out = {}
    for d in os.listdir(ROOT):
        p = os.path.join(ROOT, d)
        if not os.path.isdir(p) or d.startswith('.'):
            continue
        for f in os.listdir(p):
            if f.endswith('.th'):
                for line in open(os.path.join(p, f), encoding='utf-8', errors='replace'):
                    m = re.match(r'\s*survey\s+(\S+).*?-title\s+"([^"]+)"', line)
                    if m:
                        out.setdefault(m.group(1), re.split(r'<br>', m.group(2))[0].strip())
                        break
    return out


def main():
    from caveviewer.formats import read_3d
    legs, stations = read_3d(os.path.join(ROOT, 'build', 'catchment', 'cave.3d'))
    t = titles()
    ents = [n for n, p, f in stations if f & 4 and n.count('.') >= 1]
    by = collections.defaultdict(list)
    for n in ents:
        by[n.split('.')[1]].append(n)
    out = {}
    for cave, ns in sorted(by.items()):
        name = NAMES.get(cave) or t.get(cave) or words(cave)
        if len(ns) == 1:
            out[ns[0]] = name
            continue
        parts = [n.split('.')[2] if n.count('.') >= 3 else n.split('.')[-1] for n in ns]
        for k, (n, part) in enumerate(zip(ns, parts)):
            tell = words(part) if parts.count(part) == 1 and not part.isdigit() else str(k + 1)
            out[n] = f'{name} ({tell})'
    json.dump({'_comment': 'Made by tools/entrances.py: the catchment page\'s entrances, by station. Edit NAMES there, not this file.',
               'entrances': out}, open(os.path.join(ROOT, 'catchment-names.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    print(f'catchment-names.json: {len(out)} entrances in {len(by)} caves')


if __name__ == '__main__':
    main()
