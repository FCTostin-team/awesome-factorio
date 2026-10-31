# Compatibility guide

Checked: **2026-10-31**. This guide collects compatibility statements that had explicit evidence in project documentation, mod portal pages, or live tool output.

## Rules used by this list

1. **Factorio 2.x engine support is not the same as Space Age support.** A mod may load on 2.0/2.1 while breaking expansion progression.
2. **Portal version ranges are metadata, not a full test matrix.** They can include old releases and can conflict with the author's prose.
3. **Recent commits do not prove compatibility.** A repository can be pushed recently while still targeting 1.1 or an experimental branch.
4. **Batch Mod Portal checks do not identify every member's exact range.** Entries checked only by batch API are labeled as such and should be rechecked individually before installation.
5. **Overhauls often conflict.** Do not combine major overhauls unless the authors explicitly document compatibility.

## Known important distinctions

- **Krastorio 2**: portal metadata lists 2.1, but the project says Space Age progression is broken without an add-on such as Krastorio 2 Spaced Out.
- **Space Exploration**: portal metadata lists 2.1, but the project describes 0.7.x as targeting Factorio 2.0 and labels the mod experimental/alpha.
- **Ultracube**: portal range says 1.1-2.1, but prose says Factorio 2.0 only and incompatible with Space Age/Quality.
- **Sea Block**: original `SeaBlock` stops at 1.1; `SeaBlockPack` is the current 2.x lineage.
- **Warptorio**: original `warptorio2` stops at 1.1; `warptorio-space-age` is a separate community continuation.
- **Exotic Industries**: original `exotic-industries` is 1.1-only; `exotic-space-industries` is a separate 2.x fork/rewrite.
- **Recipe Book**: explicitly 2.0 only and will not update to 2.1.
- **Quick Item Search / Pipe Visualizer**: explicitly 1.1 only because their core features are now built into the game.
- **Project Cybersyn**: portal metadata lists 2.1, but the project says 2.1 support is experimental.
- **Cargo Ships**: 2.1 splits oil rigs and floating electric poles into separate mods and requires a 2.0 migration step for old saves.

## Compatibility table

| Resource | Kind | Status | Compatibility evidence |
| --- | --- | --- | --- |
| [FactorioLab](../README.md#factoriolab) | tool | listed | Factorio 2.x / Space Age dataset selected in live app |
| [Kirk McDonald's Factorio Calculator](../README.md#kirk-mcdonald-calculator) | tool | listed | Base-game 2.0 dataset observed; Space Age support not verified |
| [s-fabian's Factorio Calculator](../README.md#s-fabian-calculator) | tool | listed | Space Age 2.1.20 normal quality per project changelog |
| [factoriocalculator.app](../README.md#factoriocalculator-app) | tool | listed | Space Age / quality / planets advertised by live app |
| [anthfgreco's Factorio Calculator](../README.md#anthfgreco-calculator) | tool | listed | Factorio 2.1.14 / Space Age per README |
| [Jordan Schnur's Factorio Calculator](../README.md#jordan-schnur-calculator) | tool | listed | Factorio 2.0 / Space Age per project description |
| [0sdknum Factorio Live Planner](../README.md#factorio-live-planner) | tool | listed | Base and Space Age recipes advertised by live app |
| [FactorioTools](../README.md#factorio-tools) | tool | listed | Dataset 2.0.77 observed; rates approximate |
| [FactorioFactoryFactory](../README.md#factorio-factory-factory) | tool | listed | Space Age / Space Exploration / vanilla 2.0 per project docs |
| [FactorioQualityOptimizer](../README.md#quality-optimizer) | tool | listed | Space Age quality focus |
| [Factorio Quality Benchmarker](../README.md#quality-benchmarker) | tool | listed | Space Age quality focus |
| [Factorio Blueprint Editor (FactoryGameFan)](../README.md#fbe-factorygamefan) | tool | listed | Factorio 2.0 / Space Age; some features still planned |
| [Christoph Frick's Blueprint Tools](../README.md#christoph-blueprint-tools) | tool | listed | Entity update helpers documented for 1.1; 2.x unchecked |
| [Blueprint Aligner](../README.md#blueprint-aligner) | mod | listed | Factorio 1.1-2.0 per portal release metadata |
| [Nixie Tubes](../README.md#nixie-tubes) | mod | listed | Factorio 0.14-2.1 per portal release metadata |
| [Pushbutton](../README.md#pushbutton) | mod | listed | Factorio 0.14-2.1 per portal release metadata |
| [Helmod](../README.md#helmod) | mod | listed | Factorio 0.14-2.1 per portal release metadata |
| [Factory Planner](../README.md#factory-planner) | mod | listed | Factorio 0.17-2.1; Space Age supported per project docs |
| [Rate Calculator](../README.md#rate-calculator) | mod | listed | Factorio 1.1-2.1 per portal release metadata |
| [Max Rate Calculator](../README.md#max-rate-calculator) | mod | listed | Factorio 0.15-2.0; Space Age yes, quality no per portal description |
| [FNEI](../README.md#fnei) | mod | listed | Factorio 0.15-2.1 per portal release metadata |
| [Recipe Book](../README.md#recipe-book) | mod | legacy | Factorio 2.0 only; not 2.1 per portal description |
| [What is it really used for?](../README.md#what-is-it-really-used-for) | mod | listed | Factorio 0.15-2.1 per portal release metadata |
| [Bottleneck](../README.md#bottleneck) | mod | listed | Factorio 0.13-2.0 per portal release metadata |
| [Bottleneck Lite](../README.md#bottleneck-lite) | mod | listed | Factorio 1.1-2.1 per portal release metadata |
| [Assembly Analyst](../README.md#assembly-analyst) | mod | listed | Factorio 0.18-2.1 per portal release metadata |
| [Even Distribution](../README.md#even-distribution) | mod | listed | Factorio 0.15-2.1 per portal release metadata |
| [Squeak Through 2](../README.md#squeak-through-2) | mod | listed | Factorio 1.1-2.1 per portal release metadata |
| [Squeak Through (original)](../README.md#squeak-through-original) | mod | legacy | Factorio 0.13-1.1 only |
| [Far Reach](../README.md#far-reach) | mod | listed | Factorio 0.16-2.1 per portal release metadata |
| [Long Reach](../README.md#long-reach) | mod | legacy | Factorio 0.13-0.18 only |
| [Bright Universe](../README.md#bright-universe) | mod | listed | Factorio 2.0-2.1 per portal release metadata |
| [Lighted Electric Poles +](../README.md#lighted-poles-plus) | mod | legacy | Factorio 0.15-1.1 only |
| [Todo List](../README.md#todo-list) | mod | listed | Factorio 0.16-2.1 per portal release metadata |
| [Task List](../README.md#task-list) | mod | listed | Factorio 1.1-2.1 per portal release metadata |
| [Module Inserter](../README.md#module-inserter) | mod | legacy | Factorio 0.15-1.1 only |
| [Module Inserter Simplified](../README.md#module-inserter-simplified) | mod | listed | 2.1 release visible in batch check; exact range not individually recorded |
| [YARM - Resource Monitor](../README.md#yarm) | mod | listed | Factorio 0.14-2.0 per portal release metadata |
| [Resource Monitor](../README.md#resource-monitor) | mod | listed | Factorio 1.1-2.1 per portal release metadata |
| [Auto Deconstruct](../README.md#auto-deconstruct) | mod | listed | Factorio 0.13-2.1 per portal release metadata |
| [Nanobots](../README.md#nanobots) | mod | legacy | Factorio 0.15-1.1 only |
| [VehicleSnap](../README.md#vehicle-snap) | mod | listed | Factorio 0.15-2.1 per portal release metadata |
| [Pavement Drive Assist Continued](../README.md#pavement-drive-assist) | mod | listed | Factorio 1.1-2.0 per portal release metadata |
| [EvoGUI](../README.md#evogui) | mod | legacy | Factorio 0.14-1.1 only; deprecated |
| [Stats GUI](../README.md#stats-gui) | mod | listed | Factorio 1.1-2.1 per portal release metadata |
| [Milestones](../README.md#milestones) | mod | listed | Factorio 1.1-2.1 per portal release metadata |
| [Quick Item Search](../README.md#quick-item-search) | mod | legacy | Factorio 0.17-1.1 only; superseded by built-in features |
| [Cursor Enhancements](../README.md#cursor-enhancements) | mod | listed | Factorio 1.0-2.1 per portal release metadata |
| [Tapeline](../README.md#tapeline) | mod | listed | Factorio 0.17-2.1 per portal release metadata |
| [Pipe Visualizer](../README.md#pipe-visualizer) | mod | legacy | Factorio 1.1 only; superseded by built-in features |
| [Belt Visualizer](../README.md#belt-visualizer) | mod | listed | Factorio 1.1-2.1 per portal release metadata; lane splitters limited |
| [Spidertron Enhancements](../README.md#spidertron-enhancements) | mod | listed | Factorio 1.0-2.1 per portal release metadata |
| [Spidertron Patrols](../README.md#spidertron-patrols) | mod | listed | Factorio 1.1-2.1 per portal release metadata |
| [Spidertron Automation (Constructron Continued)](../README.md#constructron) | mod | listed | Factorio 1.1-2.1 per portal release metadata |
| [Shortcuts](../README.md#shortcuts-ick) | mod | listed | Factorio 0.18-2.1 per portal release metadata |
| [Quality of Life research](../README.md#qol-research) | mod | listed | Factorio 0.15-2.1 per portal release metadata |
| [Attach Notes](../README.md#attach-notes) | mod | legacy | Factorio 0.16-1.1 only |
| [Change Map Settings](../README.md#change-map-settings) | mod | legacy | Factorio 0.15-1.1 only |
| [Tree Collision](../README.md#tree-collision) | mod | listed | Factorio 0.13-2.0 per portal release metadata |
| [Cleaned Concrete](../README.md#cleaned-concrete) | mod | listed | 2.1 release visible in batch check; exact range not individually recorded |
| [Waterfill](../README.md#waterfill) | mod | listed | 2.1 release visible in batch check; exact range not individually recorded |
| [Grappling Gun](../README.md#grappling-gun) | mod | listed | Factorio 0.17-2.1 per portal release metadata |
| [Jetpack](../README.md#jetpack) | mod | listed | Factorio 0.18-2.1 per portal release metadata |
| [LTN - Logistic Train Network](../README.md#ltn) | mod | listed | Factorio 1.1-2.1 per portal release metadata |
| [Project Cybersyn](../README.md#cybersyn) | mod | listed | Factorio 1.1-2.1 listed; 2.1 experimental per project docs |
| [Cargo Ships](../README.md#cargo-ships) | mod | listed | Factorio 0.16-2.1 per portal release metadata; 2.1 split mods and migration caveats |
| [AAI Programmable Vehicles](../README.md#aai-programmable-vehicles) | mod | listed | Factorio 0.14-2.1 per portal release metadata; alpha status per project docs |
| [AAI Vehicles: Miner](../README.md#aai-vehicles-miner) | mod | listed | Factorio 0.14-2.1 per portal release metadata |
| [Mining Drones Remastered](../README.md#mining-drones-remastered) | mod | listed | Factorio 1.1-2.1 per portal release metadata |
| [Warehousing](../README.md#warehousing) | mod | listed | Factorio 0.14-2.1 per portal release metadata |
| [AAI Containers & Warehouses](../README.md#aai-containers) | mod | listed | Factorio 1.0-2.1 per portal release metadata |
| [Miniloader](../README.md#miniloader) | mod | legacy | Factorio 0.15-1.1 only |
| [FARL - Fully Automated Rail Layer](../README.md#farl) | mod | legacy | Factorio 0.14-1.1 only |
| [Disco Science](../README.md#disco-science) | mod | listed | 2.1 release visible in batch check; exact range not individually recorded |
| [Resource Spawner Overhaul](../README.md#rso) | mod | listed | Factorio 0.14-2.1 per portal release metadata |
| [Dectorio](../README.md#dectorio) | mod | listed | Factorio 0.15-2.0 per portal release metadata |
| [Text Plates](../README.md#text-plates) | mod | listed | Factorio 0.14-2.1 per portal release metadata |
| [Alien Biomes](../README.md#alien-biomes) | mod | listed | Factorio 0.14-2.1 per portal release metadata; Space Age affects Nauvis only |
| [Bullet Trails](../README.md#bullet-trails) | mod | listed | Factorio 0.14-2.1 per portal release metadata |
| [Tile Painter](../README.md#tile-painter) | mod | listed | Factorio 1.1-2.1 per portal release metadata |
| [Moshine](../README.md#moshine) | mod | listed | Space Age planet mod |
| [Krastorio 2](../README.md#krastorio2) | mod | listed | Factorio 0.18-2.1 listed; Space Age requires add-on per project docs |
| [Krastorio 2 Spaced Out](../README.md#krastorio2-spaced-out) | mod | listed | Factorio 2.0-2.1 / Space Age; 2.1 preferred per project docs |
| [Space Exploration](../README.md#space-exploration) | mod | experimental | Factorio 0.17-2.1 listed; 0.7.x targets 2.0; experimental per project docs |
| [Industrial Revolution 3](../README.md#industrial-revolution3) | mod | legacy | Factorio 1.1 only |
| [Sea Block Pack - Official](../README.md#seablock-pack) | mod | listed | Factorio 2.0-2.1 per portal release metadata |
| [Sea Block (original)](../README.md#seablock-original) | mod | legacy | Factorio 0.14-1.1 only |
| [Nullius](../README.md#nullius) | mod | listed | Factorio 1.1-2.1 per portal release metadata |
| [Pyanodons Modpack](../README.md#pyanodons) | mod | listed | Factorio 2.0-2.1; partial Space Age support per portal description |
| [Pyanodons Coal Processing](../README.md#py-coal-processing) | mod | listed | Factorio 1.1-2.1 per portal release metadata |
| [Bob's Metals, Chemicals and Intermediates](../README.md#bob-plates) | mod | listed | Factorio 0.13-2.1 per portal release metadata |
| [Angel's Refining](../README.md#angels-refining) | mod | listed | Factorio 0.14-2.1 per portal release metadata |
| [Angel's Petrochemical Processing](../README.md#angels-petrochem) | mod | listed | Factorio 0.14-2.1 per portal release metadata |
| [Angel's Smelting](../README.md#angels-smelting) | mod | listed | Factorio 0.14-2.1 per portal release metadata |
| [Ultracube: Age of Cube](../README.md#ultracube) | mod | listed | Portal range 1.1-2.1 conflicts with prose: 2.0 only, no Space Age/Quality |
| [Warptorio2](../README.md#warptorio2) | mod | legacy | Factorio 0.17-1.1 only |
| [Warptorio: Space Age](../README.md#warptorio-space-age) | mod | listed | Factorio 2.0-2.1 / Space Age per portal release metadata |
| [Exotic Industries](../README.md#exotic-industries) | mod | legacy | Factorio 1.1 only |
| [Exotic Space Industries](../README.md#exotic-space-industries) | mod | listed | Factorio 2.0-2.1 / Space Age per portal release metadata |
| [Lunar Landings](../README.md#lunar-landings) | mod | listed | Factorio 1.1-2.0; not Space Age compatible per portal description |
| [Freight Forwarding](../README.md#freight-forwarding) | mod | legacy | Factorio 1.1 only |
| [Blueprint Sandboxes](../README.md#blueprint-sandboxes) | mod | listed | Factorio 1.1-2.1 per portal release metadata |
| [Editor Extensions](../README.md#editor-extensions) | mod | listed | Factorio 1.1-2.1 per portal release metadata |
| [Creative Mod](../README.md#creative-mod) | mod | listed | Factorio 0.17-2.1 per portal release metadata |
| [Factorio Library (flib)](../README.md#flib) | library | listed | Factorio 0.18-2.1 per portal release metadata |
