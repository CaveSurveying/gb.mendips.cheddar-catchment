# The Cheddar Catchment

A copy of the Cave Registry Data Archive's **CheddarCatchment** Therion and
Survex surveys of the caves of the Cheddar catchment on Mendip, with its
history, and a 3D view of them all together.

**The source of truth is the SVN repository:
<https://www.cave-registry.org.uk/svn/CheddarCatchment/>.** That's where
the Cheddar surveys are developed and where changes go. This repository
is a copy of it, for building the 3D view; don't make survey changes here.
The surveys' credits and licences are as their own files give them.

## What's here

| | |
|---|---|
| The cave folders (`GB/`, `Goughs/`, `UpperFlood/`, …) and `CheddarCatchment.th` | The SVN data as it is, every revision from r1 (2011) to r503 (October 2026), each commit with its author, date and an `SVN-Revision:` trailer. |
| `caves.json` | The 3D view: everything in `CheddarCatchment.th` together, beneath the Environment Agency's LiDAR ground, with every entrance named. |

## The 3D view

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python -m caveviewer build caves.json --out site/
python -m http.server -d site     # then open http://localhost:8000
```

It needs Therion, Survex (`cavern`) and Chrome as well (see
[cave-viewer](https://github.com/CaveSurveying/cave-viewer)). The LiDAR
isn't kept in the repository: the build fetches it from the Environment
Agency the first time and keeps it in `lidar/` (ignored by git). GitHub
Actions builds the view and publishes it to GitHub Pages
(`.github/workflows/build.yml`, run by hand), keeping the LiDAR in its
cache between runs.

## Bringing across new SVN revisions

The history came from SVN with `git svn`. With a `git svn` clone of
<https://www.cave-registry.org.uk/svn/CheddarCatchment>, fetch the new
revisions and apply them here the same way, keeping each one's author,
date and `SVN-Revision:` trailer.
