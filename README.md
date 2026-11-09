# The Cheddar Catchment

The Cave Registry Data Archive's
[CheddarCatchment](http://www.cave-registry.org.uk/svn/CheddarCatchment/)
dataset: the Therion and Survex surveys of the caves of the Cheddar
catchment on Mendip, with every revision of its history (503 so far,
from 2008), and the 3D views made from them.

**Private for now.** The data is under several licences, and some caves'
files state none: see [Licences](#licences) before anything is shared or
published.

## What's here

| | |
|---|---|
| The cave folders (`GB/`, `Goughs/`, `UpperFlood/`, …) | The surveys, as they are in SVN. `CheddarCatchment.th` puts them all together. |
| `caves.json` | What's built: the whole catchment on one page, and five caves on their own pages. |
| `catchment-names.json` | The catchment page's entrance names (made by `tools/entrances.py`). |
| `LICENCES.md` | What each cave's files say about its licence, made by `tools/licences.py`. |
| `lidar/` | The Environment Agency LiDAR, fetched once and kept (OGL v3). |

## The 3D views

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python -m caveviewer build caves.json --out site/
python -m http.server -d site     # then open http://localhost:8000
```

It needs Therion, Survex (`cavern`) and Chrome as well (see
[cave-viewer](https://github.com/CaveSurveying/cave-viewer)). It makes:

- **The whole catchment** (`site/catchment/`): everything in
  `CheddarCatchment.th` beneath the ground at once, with every entrance
  named, so a cave that's only an entrance or a few legs is on the map
  with the rest.
- **GB Cave, Charterhouse Cave, Upper Flood Swallet, Reservoir Hole and
  Gough's Cave**, each with routes, passage walls and its drawn survey as
  a 2D plan.
- A landing page listing them, with each one's credit and licence.

To give another cave a page of its own, add it to `caves.json` like the
five there. GitHub Actions builds it all when run by hand (Actions tab,
*Build the 3D views*, Run workflow); the site is attached to the run,
not published.

## Licences

`LICENCES.md` lists, cave by cave, what the files say: their
`copyright` lines, any licence file, the title boxes' credits and who
surveyed them. In short:

- Most caves' files say **Creative Commons BY-NC-SA**, usually without a
  version or a named rights holder.
- **Upper Flood Swallet** has a `Licence.txt` (CC BY-NC-SA 2.0 UK), but
  some of its files say GNU GPL, and its older data is copyright the
  Mendip Caving Group (1996).
- **Many caves state no licence at all**, GB Cave among them.
- Several caves include older surveys (Crickmay's in GB, W. I. Stanton's
  1952 survey in Gough's, Cave Diving Group sump data) whose terms are
  not in the files.

Questions still open before publishing: which licence and version
applies to each cave, how each wants to be credited, whether the older
surveys are covered, and what Upper Flood's GPL statements mean. The
person to ask first is Andrew Atkinson, who keeps the dataset; then
UBSS, the Mendip Caving Group, Ben Cooper (Upper Flood), Graham Mullan
(Gough's, Reservoir) and the Cave Diving Group.

## SVN

The history came from SVN with `git svn` (`git svn clone
https://www.cave-registry.org.uk/svn/CheddarCatchment`), each commit
keeping its author and date, with an `SVN-Revision:` trailer. New SVN
revisions can be brought across the same way. This repository is meant
to become the main copy; until everyone works here, check SVN for newer
revisions before relying on it.
