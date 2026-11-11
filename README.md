# The Cheddar Catchment

A copy of the Cave Registry Data Archive's **CheddarCatchment** Therion and
Survex surveys of the caves of the Cheddar catchment on Mendip, with its
history, and a 3D view of them all together.

**The source of truth is the SVN repository:
<https://www.cave-registry.org.uk/svn/CheddarCatchment/>.** That's where
the Cheddar surveys are developed and where changes go. This repository
is a copy of it, for building the 3D view; don't make survey changes here.
The surveys' credits and licences are as their own files give them.

## See it

**<https://cavesurveying.github.io/gb.mendips.cheddar-catchment/>**: the catchment's landing page, as the Swildons survey's
homepage is: the whole catchment in 3D (<https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/>), a page for each of the
bigger caves, every survey by length, and the files to download.

Each bigger cave's page, Upper Flood's for example
(<https://cavesurveying.github.io/gb.mendips.cheddar-catchment/upper-flood/>), has its figures, its 3D view
(`upper-flood/3d/`: the survey beneath the LiDAR ground and aerial imagery,
with the drawn survey as a 2D plan, passage walls from the drawings and
routes through the cave), the plan to print as a PDF, and its models and
data: Survex `.3d`, Therion `.lox`, the plan as SVG, KML for Google Earth,
and Therion's survey, cave and continuation lists. The 3D views work
offline once opened, and in AR on an iPhone or iPad.

`#at=` opens the catchment's 3D view on one cave: a survey's name in
`CheddarCatchment.th` (`3d/#at=UpperFlood`) or an entrance's (`3d/#at=Goughs%202`).

## The caves

By surveyed length (Therion's figures, including duplicate legs but not surface ones).
**Bold** caves have a page of their own. *Drawn*: there are Therion drawings
(`.th2`) for it, which give the passage walls in 3D (and the 2D plan on its own
page). *Splays*: the survey has splay shots, shown faintly in 3D.

| Cave | Length | Depth | Its own page | In the catchment 3D | Drawn | Splays | Data |
|---|--:|--:|---|---|:-:|:-:|---|
| **Charterhouse Cave** | 5,218 m | 228 m | [page](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/charterhouse/) | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=Charterhouse) | ✓ | ✓ | [`Charterhouse/`](Charterhouse/) |
| **Upper Flood Swallet** | 4,725 m | 138 m | [page](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/upper-flood/) | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=UpperFlood) | ✓ | ✓ | [`UpperFlood/`](UpperFlood/) |
| **Gough's Cave** | 3,440 m | 116 m | [page](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/goughs/) | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=Goughs) | ✓ | ✓ | [`Goughs/`](Goughs/) |
| **GB Cave** | 2,533 m | 138 m | [page](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/gb/) | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=GB) | ✓ | ✓ | [`GB/`](GB/) |
| **Reservoir Hole** | 2,236 m | 131 m | [page](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/reservoir/) | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=Reservoir) | ✓ | ✓ | [`Reservoir/`](Reservoir/) |
| **Longwood Valley Sink** | 1,731 m | 130 m | [page](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/longwood-valley-sink/) | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=LongwoodValleySink) | ✓ | ✓ | [`LongwoodValleySink/`](LongwoodValleySink/) |
| **Longwood Swallet** | 1,444 m | 177 m | [page](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/longwood/) | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=Longwood) | ✓ |  | [`Longwood/`](Longwood/) |
| Tyning's Barrows Swallet | 1,094 m | 130 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=TyningsBarrow) | ✓ |  | [`TyningsBarrow/`](TyningsBarrow/) |
| **Wigmore Swallet** | 961 m | 100 m | [page](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/wigmore/) | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=Wigmore) |  |  | [`Wigmore/`](Wigmore/) |
| Buddles Wood (Chewton Mendip) | 731 m | 35 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=Buddles) | ✓ | ✓ | [`ChewtonMendip/`](ChewtonMendip/) |
| **Bone Hole** | 438 m | 37 m | [page](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/bone-hole/) | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=BoneHole) | ✓ | ✓ | [`BoneHole/`](BoneHole/) |
| Long Hole | 315 m | 31 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=LongHole) | ✓ | ✓ | [`LongHole/`](LongHole/) |
| Attborough Swallet | 307 m | 41 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=Attborough) |  |  | [`Attborough/`](Attborough/) |
| Waterwheel Swallet | 301 m | 64 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=Waterwheel) |  |  | [`Waterwheel/`](Waterwheel/) |
| Grebe Swallet | 296 m | 53 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=Grebe_Swallet) | ✓ | ✓ | [`Grebe/`](Grebe/) |
| Great Oones Hole | 257 m | 37 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=GreatOones) | ✓ | ✓ | [`GreatOones/`](GreatOones/) |
| Rhino Rift | 253 m | 147 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=RRift) | ✓ |  | [`RRift/`](RRift/) |
| Charterhouse Warren Farm Swallet | 209 m | 49 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=CharterhouseWarren) | ✓ | ✓ | [`CharterhouseWarren/`](CharterhouseWarren/) |
| Spider Hole | 179 m | 102 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=SpiderHole) | ✓ | ✓ | [`Spider/`](Spider/) |
| Gough's Old Cave | 154 m | 27 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=GoughsOld) | ✓ | ✓ | [`GoughsOld/`](GoughsOld/) |
| Cox's Cave | 149 m | 5 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=Coxs) | ✓ | ✓ | [`Coxs/`](Coxs/) |
| Box Cave | 132 m | 27 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=BoxCave) | ✓ |  | [`BoxCave/`](BoxCave/) |
| Whitebeam area (Whitebeam, Swine Hole, Brock) | 109 m | 16 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=WhitebeamArea) | ✓ | ✓ | [`WhitebeamArea/`](WhitebeamArea/) |
| Stainsby's Shaft | 105 m | 32 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=Blackmoor) |  |  | [`Blackmoor/`](Blackmoor/) |
| Dave Mitchell's Dig | 102 m | 75 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=DaveMitchellsDig) | ✓ | ✓ | [`DaveMitchellsDig/`](DaveMitchellsDig/) |
| Chelms Combe | 101 m | 25 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=ChelmsCombe) | ✓ | ✓ | [`ChelmsCombe/`](ChelmsCombe/) |
| Canyon Cave | 88 m | 17 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=CanyonCave) | ✓ | ✓ | [`CanyonCave/`](CanyonCave/) |
| Bowery Corner | 85 m | 7 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=BoweryCorner) | ✓ | ✓ | [`BoweryCorner/`](BoweryCorner/) |
| Tynings Great Swallet | 78 m | 37 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=TyningsGS) | ✓ | ✓ | [`TyningsGS/`](TyningsGS/) |
| Cooper's Hole | 68 m | 11 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=Coopers) | ✓ | ✓ | [`Coopers/`](Coopers/) |
| White Spot Cave | 60 m | 33 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=WhiteSpot) | ✓ | ✓ | [`WhiteSpot/`](WhiteSpot/) |
| Box | 56 m | 21 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=Box) |  |  | [`Box/`](Box/) |
| Sayes Hole | 46 m | 5 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=Sayes) | ✓ | ✓ | [`SayesHole/`](SayesHole/) |
| Palmer's Cave | 37 m | 10 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=Palmers) | ✓ | ✓ | [`Palmers/`](Palmers/) |
| Read's Grotto | 35 m | 6 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=ReadsGrotto) | ✓ | ✓ | [`ReadsGrotto/`](ReadsGrotto/) |
| Totty Pot | 34 m | 8 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=Totty) |  |  | [`Totty/`](Totty/) |
| Pig's Hole | 32 m | 12 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=Pigs) | ✓ | ✓ | [`Pigs/`](Pigs/) |
| Sun Hole | 25 m | 11 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=SunHole) | ✓ | ✓ | [`SunHole/`](SunHole/) |
| Toothache Pot | 20 m | 20 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=Toothache) |  |  | [`Toothache/`](Toothache/) |
| Pride Evans | 19 m | 6 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=PrideEvans) | ✓ | ✓ | [`PrideEvans/`](PrideEvans/) |
| Reynolds' Cave | 17 m | 11 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=Reynolds) | ✓ | ✓ | [`Reynolds/`](Reynolds/) |
| Blackrock Rift | 14 m | 7 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=BlackrockRift) | ✓ | ✓ | [`BlackrockRift/`](BlackrockRift/) |
| Bridged Rift Cave | 11 m | 3 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=BridgedRiftCave) | ✓ | ✓ | [`BridgedRiftCave/`](BridgedRiftCave/) |
| Timber Pot | 8 m | 8 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=Timber) |  |  | [`Timber/`](Timber/) |
| Champion's Cave | 7 m | 3 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=Champions) | ✓ | ✓ | [`Champions/`](Champions/) |
| Yew Cleft Hole | 6 m | 2 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=YewCleftHole) | ✓ | ✓ | [`YewCleftHole/`](YewCleftHole/) |
| Bake Hole | 5 m | 1 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=BakeHole) | ✓ | ✓ | [`BakeHole/`](BakeHole/) |
| Sparry Fissure | 4 m | 1 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=SparryFissure) | ✓ | ✓ | [`SparryFissure/`](SparryFissure/) |
| Hangover Pot | 4 m | 4 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=Hangover) |  |  | [`Hangover/`](Hangover/) |
| Pride Evans Attic | 3 m | 0 m |  | [show](https://cavesurveying.github.io/gb.mendips.cheddar-catchment/3d/#at=PrideEvansAttic) | ✓ | ✓ | [`PrideEvansAttic/`](PrideEvansAttic/) |

Entrances with no survey beneath them yet, shown in the catchment view only:
All Eights, Batts Combe Quarry Pot, Bed Stead, Black Rock Quarry, Chedder 1 Feeder, Chedder 2 Rising, Chelms Combe Quarry Cave, Chelms Combe Shelter, Falling Scree, His Lordship, Home Close, Honey Hole, Long Wrangle, Nods Pot, Paveys Cave, Pinetree, Pittards Crawl, Reynolds Rift, Scalloped Hole, Second Tier, Snablets Dig, Soldiers Hole, Sows Hole, Suger Loaf Rock, Tor Hole, Tynings Gate Ochre 1, Tynings Gate Ochre 2, Tynings Gate Ochre 3, Vurley, Wallflower, Whopper.

## What's here

| | |
|---|---|
| The cave folders (`GB/`, `Goughs/`, `UpperFlood/`, …) and `CheddarCatchment.th` | The SVN data as it is, every revision from r1 (2011) to r503 (October 2026), each commit with its author, date and an `SVN-Revision:` trailer. |
| `caves.json` | The 3D views: the whole catchment (everything in `CheddarCatchment.th` together) at the site's root, and each bigger cave's own page in its folder. |

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
Actions builds the views and publishes them to GitHub Pages on every push
to main (`.github/workflows/build.yml`), each cave in a job of its own at
the same time, keeping the LiDAR in its cache between runs.

## Bringing across new SVN revisions

The history came from SVN with `git svn`. With a `git svn` clone of
<https://www.cave-registry.org.uk/svn/CheddarCatchment>, fetch the new
revisions and apply them here the same way, keeping each one's author,
date and `SVN-Revision:` trailer.
