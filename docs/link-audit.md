# Seed link audit

Checked: **2026-10-31**. This audit accounts for every URL extracted from the original README seed list.

## Summary

- Total seed URLs: **286**
- `alias`: **26**
- `excluded`: **4**
- `included`: **145**
- `included-as-source`: **41**
- `replaced`: **42**
- `unavailable`: **25**
- `unverified`: **3**

Status meanings:

- `included`: the seed URL is the canonical primary link for a catalog entry.
- `included-as-source`: the seed URL is retained as a source/repository link.
- `alias`: the seed URL is an old slug, alternate front door, or alias of a canonical entry.
- `redirected`: GitHub redirects the seed repository to a canonical repository that is cataloged.
- `replaced`: the seed URL was unavailable or non-canonical, and a verified replacement/continuation is cataloged.
- `unavailable`: the URL returned 404 or the repository/page was not found; no live recommendation is implied.
- `unverified`: the fetch failed or availability was uncertain; the entry is not rendered as a live recommendation.
- `excluded`: malformed badge/image markup or unrelated decoration, not a Factorio resource.

A failed fetch is not always proof of permanent disappearance. Where the evidence was only a transient HTTP error, the note says so.

## Audit table

| # | Seed URL | Status | Catalog entry | Note |
| ---: | --- | --- | --- | --- |
| 1 | <https://github.com/FCTostin-team/awesome-factorio-tool/blob/main/image/awesome-factorio.png)](https://github.com/FCTostin-team/awesome-factorio-tool/pulls)> | `excluded` | — | Malformed Markdown badge/image fragment from the old README, not a Factorio resource. |
| 2 | <https://github.com/adops-tool/awesome-lead-generation/blob/main/image/line-svg-3D444D-alg.svg"> | `excluded` | — | Unrelated decorative SVG/badge fragment from the old README, not a Factorio resource. |
| 3 | <https://awesome.re/badge.svg)](https://awesome.re)> | `excluded` | — | Malformed awesome-list badge fragment from the old README, not a Factorio resource. |
| 4 | <https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/FCTostin-team/awesome-factorio-tool/pulls)> | `excluded` | — | Malformed PRs-welcome badge fragment from the old README, not a Factorio resource. |
| 5 | <https://www.factorio.com/> | `included` | [Factorio official website](../README.md#factorio-home) | Seed URL is the canonical primary link for the catalog entry. |
| 6 | <https://www.factorio.com/blog/> | `included` | [Factorio blog / Friday Facts](../README.md#factorio-blog) | Seed URL is the canonical primary link for the catalog entry. |
| 7 | <https://wiki.factorio.com/> | `included` | [Factorio wiki](../README.md#factorio-wiki) | Seed URL is the canonical primary link for the catalog entry. |
| 8 | <https://wiki.factorio.com/Tutorial:Combinator_tutorial> | `included` | [Wiki: Combinator tutorial](../README.md#wiki-combinator) | Seed URL is the canonical primary link for the catalog entry. |
| 9 | <https://wiki.factorio.com/Tutorial:Circuit_network_cookbook> | `included` | [Wiki: Circuit network cookbook](../README.md#wiki-circuit-cookbook) | Seed URL is the canonical primary link for the catalog entry. |
| 10 | <https://wiki.factorio.com/Tutorial:Train_signals> | `included` | [Wiki: Train signals](../README.md#wiki-train-signals) | Seed URL is the canonical primary link for the catalog entry. |
| 11 | <https://wiki.factorio.com/Console> | `included` | [Wiki: Console](../README.md#wiki-console) | Seed URL is the canonical primary link for the catalog entry. |
| 12 | <https://wiki.factorio.com/Keyboard_bindings> | `alias` | [Wiki: Controls](../README.md#wiki-controls) | Seed URL is retained as an alias, old slug, or alternate front door for the canonical catalog entry. |
| 13 | <https://mods.factorio.com/> | `included` | [Factorio Mod Portal](../README.md#factorio-mod-portal) | Seed URL is the canonical primary link for the catalog entry. |
| 14 | <https://forums.factorio.com/> | `included` | [Factorio forums](../README.md#factorio-forums) | Seed URL is the canonical primary link for the catalog entry. |
| 15 | <https://lua-api.factorio.com/> | `alias` | [Factorio Lua API documentation](../README.md#factorio-lua-api) | Seed URL is retained as an alias, old slug, or alternate front door for the canonical catalog entry. |
| 16 | <https://github.com/wube> | `included` | [Wube Software on GitHub](../README.md#wube-github) | Seed URL is the canonical primary link for the catalog entry. |
| 17 | <https://github.com/wube/factorio-data> | `included` | [wube/factorio-data](../README.md#factorio-data) | Seed URL is the canonical primary link for the catalog entry. |
| 18 | <https://github.com/wube/factorio-lualib> | `replaced` | [Wube Software on GitHub](../README.md#wube-github) | The old factorio-lualib repository is not present in the Wube organization; the organization page is cataloged instead. |
| 19 | <https://github.com/FCTostin-team> | `included` | [FCTostin-team on GitHub](../README.md#fctostin-team) | Seed URL is the canonical primary link for the catalog entry. |
| 20 | <https://fctostin-team.github.io/blueprint-text_formatter/> | `included` | [FCT Blueprint Text Formatter](../README.md#fct-text-formatter) | Seed URL is the canonical primary link for the catalog entry. |
| 21 | <https://github.com/FCTostin-team/blueprint-text_formatter> | `included-as-source` | [FCT Blueprint Text Formatter](../README.md#fct-text-formatter) | Seed URL is retained as the source/repository link for the catalog entry. |
| 22 | <https://fctostin-team.github.io/fonts-online_rich_text/> | `included` | [FCT Fonts / Rich Text Generator](../README.md#fct-fonts-rich-text) | Seed URL is the canonical primary link for the catalog entry. |
| 23 | <https://github.com/FCTostin-team/fonts-online_rich_text> | `included-as-source` | [FCT Fonts / Rich Text Generator](../README.md#fct-fonts-rich-text) | Seed URL is retained as the source/repository link for the catalog entry. |
| 24 | <https://fctostin-team.github.io/solar-accumulator-calculator/> | `included` | [FCT Solar / Accumulator Calculator](../README.md#fct-solar-calculator) | Seed URL is the canonical primary link for the catalog entry. |
| 25 | <https://github.com/FCTostin-team/solar-accumulator-calculator> | `included-as-source` | [FCT Solar / Accumulator Calculator](../README.md#fct-solar-calculator) | Seed URL is retained as the source/repository link for the catalog entry. |
| 26 | <https://fctostin-team.github.io/market-code_generator/> | `included` | [FCT Market Code Generator](../README.md#fct-market-generator) | Seed URL is the canonical primary link for the catalog entry. |
| 27 | <https://github.com/FCTostin-team/market-code_generator> | `included-as-source` | [FCT Market Code Generator](../README.md#fct-market-generator) | Seed URL is retained as the source/repository link for the catalog entry. |
| 28 | <https://fctostin-team.github.io/linked-belt/> | `included` | [FCT Linked-Belt Command Generator](../README.md#fct-linked-belt) | Seed URL is the canonical primary link for the catalog entry. |
| 29 | <https://github.com/FCTostin-team/linked-belt> | `included-as-source` | [FCT Linked-Belt Command Generator](../README.md#fct-linked-belt) | Seed URL is retained as the source/repository link for the catalog entry. |
| 30 | <https://fctostin-team.github.io/progress-bar_display-panel/> | `included` | [FCT Progress Bar Display Panel](../README.md#fct-progress-bar) | Seed URL is the canonical primary link for the catalog entry. |
| 31 | <https://github.com/FCTostin-team/progress-bar_display-panel> | `included-as-source` | [FCT Progress Bar Display Panel](../README.md#fct-progress-bar) | Seed URL is retained as the source/repository link for the catalog entry. |
| 32 | <https://github.com/FCTostin-team/Factorio-Achievement-Unlocker> | `included` | [FCT Achievement Unlocker](../README.md#fct-achievement-unlocker) | Seed URL is the canonical primary link for the catalog entry. |
| 33 | <https://github.com/FCTostin-team/Factorio-server-admin-Devkit> | `included` | [FCT Factorio Server Admin Devkit](../README.md#fct-admin-devkit) | Seed URL is the canonical primary link for the catalog entry. |
| 34 | <https://fctostin-team.github.io/blueprint-code_compression/> | `included` | [FCT Blueprint Compression](../README.md#fct-blueprint-compression) | Seed URL is the canonical primary link for the catalog entry. |
| 35 | <https://github.com/FCTostin-team/blueprint-code_compression> | `included-as-source` | [FCT Blueprint Compression](../README.md#fct-blueprint-compression) | Seed URL is retained as the source/repository link for the catalog entry. |
| 36 | <https://fctostin-team.github.io/blueprints-book-rich_text/> | `included` | [FCT Blueprint Book Rich Text](../README.md#fct-book-rich-text) | Seed URL is the canonical primary link for the catalog entry. |
| 37 | <https://github.com/FCTostin-team/blueprints-book-rich_text> | `included-as-source` | [FCT Blueprint Book Rich Text](../README.md#fct-book-rich-text) | Seed URL is retained as the source/repository link for the catalog entry. |
| 38 | <https://fctostin-team.github.io/blueprints-decoder_encoder/> | `included` | [FCT Blueprint Decoder / Encoder](../README.md#fct-blueprint-decoder) | Seed URL is the canonical primary link for the catalog entry. |
| 39 | <https://github.com/FCTostin-team/blueprints-decoder_encoder> | `included-as-source` | [FCT Blueprint Decoder / Encoder](../README.md#fct-blueprint-decoder) | Seed URL is retained as the source/repository link for the catalog entry. |
| 40 | <https://www.autotorio.com/> | `included` | [Autotorio](../README.md#autotorio) | Seed URL is the canonical primary link for the catalog entry. |
| 41 | <https://www.autotorio.com/github> | `alias` | [Autotorio](../README.md#autotorio) | Seed URL is retained as an alias, old slug, or alternate front door for the canonical catalog entry. |
| 42 | <https://www.autotorio.com/blueprint> | `alias` | [Autotorio](../README.md#autotorio) | Seed URL is retained as an alias, old slug, or alternate front door for the canonical catalog entry. |
| 43 | <https://www.autotorio.com/outpost> | `alias` | [Autotorio](../README.md#autotorio) | Seed URL is retained as an alias, old slug, or alternate front door for the canonical catalog entry. |
| 44 | <https://www.autotorio.com/oil> | `alias` | [Autotorio](../README.md#autotorio) | Seed URL is retained as an alias, old slug, or alternate front door for the canonical catalog entry. |
| 45 | <https://github.com/FlameSla/autotorio> | `replaced` | [Autotorio](../README.md#autotorio) | Original seed repository returned 404; the canonical Autotorio source is demipixel/autotorio. |
| 46 | <https://factoriocheatsheet.com/> | `included` | [Factorio Cheat Sheet](../README.md#factorio-cheatsheet) | Seed URL is the canonical primary link for the catalog entry. |
| 47 | <https://factoriocheatsheet.com/#Useful%20Quality-of-Life%20mods_Small%20gameplay%20additions> | `alias` | [Factorio Cheat Sheet](../README.md#factorio-cheatsheet) | Seed URL is retained as an alias, old slug, or alternate front door for the canonical catalog entry. |
| 48 | <https://factoriocheatsheet.com/#links> | `alias` | [Factorio Cheat Sheet](../README.md#factorio-cheatsheet) | Seed URL is retained as an alias, old slug, or alternate front door for the canonical catalog entry. |
| 49 | <https://dddgamer.github.io/factorio-cheat-sheet/> | `alias` | [Factorio Cheat Sheet](../README.md#factorio-cheatsheet) | Seed URL is retained as an alias, old slug, or alternate front door for the canonical catalog entry. |
| 50 | <https://github.com/deniszholob/factorio-cheat-sheet> | `included-as-source` | [Factorio Cheat Sheet](../README.md#factorio-cheatsheet) | Seed URL is retained as the source/repository link for the catalog entry. |
| 51 | <https://factoriolab.github.io/> | `included` | [FactorioLab](../README.md#factoriolab) | Seed URL is the canonical primary link for the catalog entry. |
| 52 | <https://github.com/factoriolab/factoriolab> | `included-as-source` | [FactorioLab](../README.md#factoriolab) | Seed URL is retained as the source/repository link for the catalog entry. |
| 53 | <https://kirkmcdonald.github.io/> | `alias` | [Kirk McDonald's Factorio Calculator](../README.md#kirk-mcdonald-calculator) | Seed URL is retained as an alias, old slug, or alternate front door for the canonical catalog entry. |
| 54 | <https://kirkmcdonald.github.io/calc.html> | `included` | [Kirk McDonald's Factorio Calculator](../README.md#kirk-mcdonald-calculator) | Seed URL is the canonical primary link for the catalog entry. |
| 55 | <https://github.com/KirkMcDonald/kirkmcdonald.github.io> | `included-as-source` | [Kirk McDonald's Factorio Calculator](../README.md#kirk-mcdonald-calculator) | Seed URL is retained as the source/repository link for the catalog entry. |
| 56 | <https://github.com/shpaass/yafc-ce> | `alias` | [YAFC: Community Edition](../README.md#yafc-ce) | Seed URL is retained as an alias, old slug, or alternate front door for the canonical catalog entry. |
| 57 | <https://github.com/Dorus/yafc-ce> | `alias` | [YAFC: Community Edition](../README.md#yafc-ce) | Seed URL is retained as an alias, old slug, or alternate front door for the canonical catalog entry. |
| 58 | <https://github.com/ShadowTheAge/yafc> | `included` | [YAFC (original)](../README.md#yafc-original) | Seed URL is the canonical primary link for the catalog entry. |
| 59 | <https://github.com/DanielKote/Foreman2> | `included` | [Foreman2](../README.md#foreman2) | Seed URL is the canonical primary link for the catalog entry. |
| 60 | <https://github.com/Nicksaurus/foreman> | `replaced` | [Foreman2](../README.md#foreman2) | Original Foreman repository returned 404; Foreman2 is cataloged as the visual planning successor. |
| 61 | <https://doomeer.com/factorio/> | `included` | [Doomeer's Factorio Planner](../README.md#doomeer-planner) | Seed URL is the canonical primary link for the catalog entry. |
| 62 | <https://github.com/doomeer/factorio> | `included-as-source` | [Doomeer's Factorio Planner](../README.md#doomeer-planner) | Seed URL is retained as the source/repository link for the catalog entry. |
| 63 | <https://factoriocalculator.blog/> | `included` | [factoriocalculator.blog](../README.md#factoriocalculator-blog) | Seed URL is the canonical primary link for the catalog entry. |
| 64 | <https://calculatorio.com/> | `unverified` | [Calculatorio](https://calculatorio.com/) (not rendered) | Fetch returned HTTP 500; availability is uncertain and the entry is not rendered as a live recommendation. |
| 65 | <https://factoriocalc.com/> | `unverified` | [factoriocalc.com](https://factoriocalc.com/) (not rendered) | Fetch failed generically; availability is uncertain and the entry is not rendered as a live recommendation. |
| 66 | <https://factorio.rotol.me/> | `unverified` | [factorio.rotol.me](https://factorio.rotol.me/) (not rendered) | Fetch returned HTTP 500; availability is uncertain and the entry is not rendered as a live recommendation. |
| 67 | <https://burnysc2.github.io/Factorio/Tools/TrainAcceleration/> | `replaced` | [Factorio Train Station Blueprint Creator](../README.md#train-station-creator) | GitHub Pages URL returned 404; the related BurnySc2 train-station blueprint repository is cataloged instead. |
| 68 | <https://codepen.io/Tickthokk/full/NBbKPZ/> | `included` | [Tickthokk's Ratio Calculator](../README.md#tickthokk-ratio-calculator) | Seed URL is the canonical primary link for the catalog entry. |
| 69 | <https://github.com/R-O-C-K-E-T/Factorio-SAT> | `included` | [Factorio-SAT](../README.md#factorio-sat) | Seed URL is the canonical primary link for the catalog entry. |
| 70 | <https://github.com/Aidiakapi/factorio_sat> | `replaced` | [Factorio-SAT](../README.md#factorio-sat) | Original seed repository returned 404; R-O-C-K-E-T/Factorio-SAT is cataloged as the verified SAT-solver project. |
| 71 | <https://github.com/awkwardly-attentive/factorio-sat> | `replaced` | [Factorio-SAT](../README.md#factorio-sat) | Original seed repository returned 404; R-O-C-K-E-T/Factorio-SAT is cataloged as the verified SAT-solver project. |
| 72 | <https://github.com/iTitus/factorio-recipes> | `included` | [iTitus factorio-recipes](../README.md#factorio-recipes) | Seed URL is the canonical primary link for the catalog entry. |
| 73 | <https://factorioprints.com/> | `included` | [FactorioPrints](../README.md#factorioprints) | Seed URL is the canonical primary link for the catalog entry. |
| 74 | <https://github.com/FactorioBlueprints/factorio-prints> | `included-as-source` | [FactorioPrints](../README.md#factorioprints) | Seed URL is retained as the source/repository link for the catalog entry. |
| 75 | <https://www.factorio.school/> | `included` | [Factorio School](../README.md#factorio-school) | Seed URL is the canonical primary link for the catalog entry. |
| 76 | <https://factoriobin.com/> | `included` | [FactorioBin](../README.md#factoriobin) | Seed URL is the canonical primary link for the catalog entry. |
| 77 | <https://www.factoriocodex.com/> | `included` | [FactorioCodex](../README.md#factoriocodex) | Seed URL is the canonical primary link for the catalog entry. |
| 78 | <https://factorioblueprints.tech/> | `included` | [factorioblueprints.tech](../README.md#factorioblueprints-tech) | Seed URL is the canonical primary link for the catalog entry. |
| 79 | <https://supercheese.github.io/Factorio-Blueprints/> | `unavailable` | [Supercheese Factorio-Blueprints](https://supercheese.github.io/Factorio-Blueprints/) (not rendered) | GitHub Pages site returned 404; retained as unavailable. |
| 80 | <https://github.com/Supercheese/Factorio-Blueprints> | `unavailable` | [Supercheese Factorio-Blueprints](https://supercheese.github.io/Factorio-Blueprints/) (not rendered) | GitHub repository and GitHub Pages site were unavailable; retained as an unavailable historical entry. |
| 81 | <https://github.com/raynquist/balancer> | `included` | [raynquist/balancer](../README.md#balancer-book) | Seed URL is the canonical primary link for the catalog entry. |
| 82 | <https://github.com/MaxiumeGaming/Factorio> | `included` | [MaxiumeGaming/Factorio](../README.md#maxiume-factorio) | Seed URL is the canonical primary link for the catalog entry. |
| 83 | <https://fbe.teoxoy.com/> | `included` | [Factorio Blueprint Editor (teoxoy, unmaintained)](../README.md#fbe-teoxoy) | Seed URL is the canonical primary link for the catalog entry. |
| 84 | <https://github.com/teoxoy/factorio-blueprint-editor> | `included-as-source` | [Factorio Blueprint Editor (teoxoy, unmaintained)](../README.md#fbe-teoxoy) | Seed URL is retained as the source/repository link for the catalog entry. |
| 85 | <https://christoph-frick.github.io/factorio-blueprint-tools/> | `included` | [Christoph Frick's Blueprint Tools](../README.md#christoph-blueprint-tools) | Seed URL is the canonical primary link for the catalog entry. |
| 86 | <https://github.com/christoph-frick/factorio-blueprint-tools> | `included-as-source` | [Christoph Frick's Blueprint Tools](../README.md#christoph-blueprint-tools) | Seed URL is retained as the source/repository link for the catalog entry. |
| 87 | <https://piebro.github.io/factorio-blueprint-visualizer/> | `included` | [piebro Blueprint Visualizer](../README.md#piebro-visualizer) | Seed URL is the canonical primary link for the catalog entry. |
| 88 | <https://github.com/piebro/factorio-blueprint-visualizer> | `included-as-source` | [piebro Blueprint Visualizer](../README.md#piebro-visualizer) | Seed URL is retained as the source/repository link for the catalog entry. |
| 89 | <https://github.com/redruin1/factorio-draftsman> | `included` | [factorio-draftsman](../README.md#factorio-draftsman) | Seed URL is the canonical primary link for the catalog entry. |
| 90 | <https://github.com/demodude4u/Factorio-FBSR> | `included` | [Factorio-FBSR](../README.md#factorio-fbsr) | Seed URL is the canonical primary link for the catalog entry. |
| 91 | <https://github.com/JensForstmann/factorio-blueprint-tools> | `included` | [JensForstmann/factorio-blueprint-tools](../README.md#jensforstmann-blueprint-tools) | Seed URL is the canonical primary link for the catalog entry. |
| 92 | <https://github.com/felixlinker/factorio-blueprint> | `unavailable` | — | GitHub API returned 404. No verified successor was identified; use factorio-draftsman or demipixel/factorio-blueprint for current blueprint libraries. |
| 93 | <https://github.com/LvanderRee/factorio-blueprint> | `unavailable` | — | GitHub API returned 404. No verified successor was identified; use factorio-draftsman or demipixel/factorio-blueprint for current blueprint libraries. |
| 94 | <https://github.com/ChangeTheGame/factorio-blueprint> | `unavailable` | — | GitHub API returned 404. No verified successor was identified; use factorio-draftsman or demipixel/factorio-blueprint for current blueprint libraries. |
| 95 | <https://github.com/Jason-Clement/Factorio-Blueprint-Tool> | `included` | [Factorio-Blueprint-Tool](../README.md#jason-clement-blueprint-tool) | Seed URL is the canonical primary link for the catalog entry. |
| 96 | <https://github.com/35mt/factorio-blueprint-generator-java> | `included` | [factorio-blueprint-generator-java](../README.md#35mt-blueprint-generator) | Seed URL is the canonical primary link for the catalog entry. |
| 97 | <https://github.com/RisingThumb/Factorio-Blueprint-String-Converter> | `unavailable` | — | GitHub API returned 404. No verified successor was identified; use the FCT decoder/encoder or typed blueprint libraries. |
| 98 | <https://github.com/Deskbot/Factorio-Blueprint-Reader> | `unavailable` | — | GitHub API returned 404. No verified successor was identified; use the FCT decoder/encoder or typed blueprint libraries. |
| 99 | <https://github.com/sparr/factorio-blueprint-align> | `replaced` | [Blueprint Aligner](../README.md#blueprint-aligner) | Original seed repository returned 404; emlun/factorio-blueprint-aligner is cataloged as a verified blueprint alignment mod. |
| 100 | <https://github.com/Redcrafter/verilog2factorio> | `included-as-source` | [Verilog2Factorio](../README.md#verilog2factorio) | Seed URL is retained as the source/repository link for the catalog entry. |
| 101 | <https://charredutensil.github.io/cnide/> | `included` | [Cnide - Circuit Network IDE](../README.md#cnide) | Seed URL is the canonical primary link for the catalog entry. |
| 102 | <https://github.com/charredUtensil/cnide> | `included-as-source` | [Cnide - Circuit Network IDE](../README.md#cnide) | Seed URL is retained as the source/repository link for the catalog entry. |
| 103 | <https://miditorio.com/> | `included` | [Miditorio](../README.md#miditorio) | Seed URL is the canonical primary link for the catalog entry. |
| 104 | <https://github.com/hermann-p/miditorio> | `replaced` | [Miditorio](../README.md#miditorio) | Original seed repository returned 404; mgabor3141/miditorio and miditorio.com are cataloged as the verified MIDI tool. |
| 105 | <https://github.com/ConcurrentSquared/Factorio-MIDI-to-Combinator> | `unavailable` | — | GitHub API returned 404. No verified successor was identified; use Miditorio or FactorioComposer for MIDI-to-blueprint work. |
| 106 | <https://github.com/velachev/factorio-midi> | `unavailable` | — | GitHub API returned 404. No verified successor was identified; use Miditorio or FactorioComposer for MIDI-to-blueprint work. |
| 107 | <https://github.com/Quintenps/Factorio-Image-Converter> | `unavailable` | — | GitHub API returned 404. No verified successor was identified; use the Nico Kandut pixel-art/solar-art generators or Artorio. |
| 108 | <https://github.com/Arrowin/Factorio-Image-to-Blueprint> | `unavailable` | — | GitHub API returned 404. No verified successor was identified; use the Nico Kandut pixel-art/solar-art generators or Artorio. |
| 109 | <https://mods.factorio.com/mod/helmod> | `included` | [Helmod](../README.md#helmod) | Seed URL is the canonical primary link for the catalog entry. |
| 110 | <https://github.com/Helfima/helmod> | `included-as-source` | [Helmod](../README.md#helmod) | Seed URL is retained as the source/repository link for the catalog entry. |
| 111 | <https://mods.factorio.com/mod/factoryplanner> | `included` | [Factory Planner](../README.md#factory-planner) | Seed URL is the canonical primary link for the catalog entry. |
| 112 | <https://github.com/Therenas/factoryplanner> | `replaced` | [Factory Planner](../README.md#factory-planner) | Original seed repository URL returned 404; the canonical source is ClaudeMetz/FactoryPlanner and the portal page is cataloged. |
| 113 | <https://mods.factorio.com/mod/RateCalculator> | `included` | [Rate Calculator](../README.md#rate-calculator) | Seed URL is the canonical primary link for the catalog entry. |
| 114 | <https://codeberg.org/raiguard/RateCalculator> | `included-as-source` | [Rate Calculator](../README.md#rate-calculator) | Seed URL is retained as the source/repository link for the catalog entry. |
| 115 | <https://github.com/raiguard/RateCalculator> | `alias` | [Rate Calculator](../README.md#rate-calculator) | Seed URL is retained as an alias, old slug, or alternate front door for the canonical catalog entry. |
| 116 | <https://mods.factorio.com/mod/MaxRateCalculator> | `included` | [Max Rate Calculator](../README.md#max-rate-calculator) | Seed URL is the canonical primary link for the catalog entry. |
| 117 | <https://mods.factorio.com/mod/FNEI> | `included` | [FNEI](../README.md#fnei) | Seed URL is the canonical primary link for the catalog entry. |
| 118 | <https://github.com/npo6ka/FNEI> | `included-as-source` | [FNEI](../README.md#fnei) | Seed URL is retained as the source/repository link for the catalog entry. |
| 119 | <https://mods.factorio.com/mod/RecipeBook> | `included` | [Recipe Book](../README.md#recipe-book) | Seed URL is the canonical primary link for the catalog entry. |
| 120 | <https://codeberg.org/raiguard/RecipeBook> | `alias` | [Recipe Book](../README.md#recipe-book) | Seed URL is retained as an alias, old slug, or alternate front door for the canonical catalog entry. |
| 121 | <https://mods.factorio.com/mod/what-is-it-really-used-for> | `included` | [What is it really used for?](../README.md#what-is-it-really-used-for) | Seed URL is the canonical primary link for the catalog entry. |
| 122 | <https://mods.factorio.com/mod/Bottleneck> | `included` | [Bottleneck](../README.md#bottleneck) | Seed URL is the canonical primary link for the catalog entry. |
| 123 | <https://github.com/troelsbjerre/Bottleneck> | `included-as-source` | [Bottleneck](../README.md#bottleneck) | Seed URL is retained as the source/repository link for the catalog entry. |
| 124 | <https://mods.factorio.com/mod/BottleneckLite> | `included` | [Bottleneck Lite](../README.md#bottleneck-lite) | Seed URL is the canonical primary link for the catalog entry. |
| 125 | <https://github.com/raiguard/BottleneckLite> | `alias` | [Bottleneck Lite](../README.md#bottleneck-lite) | Seed URL is retained as an alias, old slug, or alternate front door for the canonical catalog entry. |
| 126 | <https://mods.factorio.com/mod/even-distribution> | `included` | [Even Distribution](../README.md#even-distribution) | Seed URL is the canonical primary link for the catalog entry. |
| 127 | <https://github.com/321freddy/even-distribution> | `included-as-source` | [Even Distribution](../README.md#even-distribution) | Seed URL is retained as the source/repository link for the catalog entry. |
| 128 | <https://mods.factorio.com/mod/Squeak%20Through> | `included` | [Squeak Through (original)](../README.md#squeak-through-original) | Seed URL is the canonical primary link for the catalog entry. |
| 129 | <https://github.com/NommyB/Squeak-Through> | `replaced` | [Squeak Through (original)](../README.md#squeak-through-original) | Original seed repository returned 404; the original Squeak Through mod is cataloged as legacy, with Squeak Through 2 as the current alternative. |
| 130 | <https://mods.factorio.com/mod/far-reach> | `included` | [Far Reach](../README.md#far-reach) | Seed URL is the canonical primary link for the catalog entry. |
| 131 | <https://mods.factorio.com/mod/long-reach> | `included` | [Long Reach](../README.md#long-reach) | Seed URL is the canonical primary link for the catalog entry. |
| 132 | <https://mods.factorio.com/mod/afraid-of-the-dark> | `included` | [Bright Universe](../README.md#bright-universe) | Seed URL is the canonical primary link for the catalog entry. |
| 133 | <https://mods.factorio.com/mod/LightedPolesPlus> | `included` | [Lighted Electric Poles +](../README.md#lighted-poles-plus) | Seed URL is the canonical primary link for the catalog entry. |
| 134 | <https://mods.factorio.com/mod/Inbuilt-Lighting> | `unavailable` | — | Mod Portal page returned 404. No canonical replacement was verified; consider Bright Universe or Lighted Electric Poles + depending on game version. |
| 135 | <https://mods.factorio.com/mod/Todo-List> | `included` | [Todo List](../README.md#todo-list) | Seed URL is the canonical primary link for the catalog entry. |
| 136 | <https://github.com/JonasJurczok/Todo-List> | `replaced` | [Todo List](../README.md#todo-list) | Original mixed-case seed repository URL returned 404; JonasJurczok/factorio-todo-list is the verified source. |
| 137 | <https://mods.factorio.com/mod/TaskList> | `included` | [Task List](../README.md#task-list) | Seed URL is the canonical primary link for the catalog entry. |
| 138 | <https://mods.factorio.com/mod/ModuleInserter> | `included` | [Module Inserter](../README.md#module-inserter) | Seed URL is the canonical primary link for the catalog entry. |
| 139 | <https://mods.factorio.com/mod/ModuleInserterSimplified> | `included` | [Module Inserter Simplified](../README.md#module-inserter-simplified) | Seed URL is the canonical primary link for the catalog entry. |
| 140 | <https://mods.factorio.com/mod/YARM> | `included` | [YARM - Resource Monitor](../README.md#yarm) | Seed URL is the canonical primary link for the catalog entry. |
| 141 | <https://github.com/narc0tiq/YARM> | `included-as-source` | [YARM - Resource Monitor](../README.md#yarm) | Seed URL is retained as the source/repository link for the catalog entry. |
| 142 | <https://mods.factorio.com/mod/AutoDeconstruct> | `included` | [Auto Deconstruct](../README.md#auto-deconstruct) | Seed URL is the canonical primary link for the catalog entry. |
| 143 | <https://github.com/mindmix/AutoDeconstruct> | `replaced` | [Auto Deconstruct](../README.md#auto-deconstruct) | Original seed repository URL returned 404; softmix/AutoDeconstruct is the verified source. |
| 144 | <https://mods.factorio.com/mod/nanobots> | `replaced` | [Nanobots](../README.md#nanobots) | Lowercase slug returned 404; canonical portal slug is Nanobots. |
| 145 | <https://github.com/Nexela/Nanobots> | `included-as-source` | [Nanobots](../README.md#nanobots) | Seed URL is retained as the source/repository link for the catalog entry. |
| 146 | <https://mods.factorio.com/mod/upgrade-builder-and-planner> | `unavailable` | — | Mod Portal page returned 404. No canonical replacement was verified; use vanilla upgrade planners or Upgrade Planner-related mods after checking current portal metadata. |
| 147 | <https://mods.factorio.com/mod/VehicleSnap> | `included` | [VehicleSnap](../README.md#vehicle-snap) | Seed URL is the canonical primary link for the catalog entry. |
| 148 | <https://github.com/Zaflis/VehicleSnap> | `replaced` | [VehicleSnap](../README.md#vehicle-snap) | Original seed repository URL returned 404; the VehicleSnap mod portal page is cataloged. |
| 149 | <https://mods.factorio.com/mod/PavementDriveAssistContinued> | `included` | [Pavement Drive Assist Continued](../README.md#pavement-drive-assist) | Seed URL is the canonical primary link for the catalog entry. |
| 150 | <https://mods.factorio.com/mod/EvoGUI> | `included` | [EvoGUI](../README.md#evogui) | Seed URL is the canonical primary link for the catalog entry. |
| 151 | <https://mods.factorio.com/mod/StatsGui> | `included` | [Stats GUI](../README.md#stats-gui) | Seed URL is the canonical primary link for the catalog entry. |
| 152 | <https://mods.factorio.com/mod/Milestones> | `included` | [Milestones](../README.md#milestones) | Seed URL is the canonical primary link for the catalog entry. |
| 153 | <https://github.com/Wiwiweb/Milestones> | `replaced` | [Milestones](../README.md#milestones) | Original seed repository URL returned 404; Wiwiweb/FactorioMilestones is the verified source. |
| 154 | <https://mods.factorio.com/mod/QuickItemSearch> | `included` | [Quick Item Search](../README.md#quick-item-search) | Seed URL is the canonical primary link for the catalog entry. |
| 155 | <https://github.com/raiguard/QuickItemSearch> | `included-as-source` | [Quick Item Search](../README.md#quick-item-search) | Seed URL is retained as the source/repository link for the catalog entry. |
| 156 | <https://mods.factorio.com/mod/CursorEnhancements> | `included` | [Cursor Enhancements](../README.md#cursor-enhancements) | Seed URL is the canonical primary link for the catalog entry. |
| 157 | <https://github.com/raiguard/CursorEnhancements> | `alias` | [Cursor Enhancements](../README.md#cursor-enhancements) | Seed URL is retained as an alias, old slug, or alternate front door for the canonical catalog entry. |
| 158 | <https://mods.factorio.com/mod/Tapeline> | `included` | [Tapeline](../README.md#tapeline) | Seed URL is the canonical primary link for the catalog entry. |
| 159 | <https://github.com/raiguard/Tapeline> | `alias` | [Tapeline](../README.md#tapeline) | Seed URL is retained as an alias, old slug, or alternate front door for the canonical catalog entry. |
| 160 | <https://mods.factorio.com/mod/PipeVisualizer> | `included` | [Pipe Visualizer](../README.md#pipe-visualizer) | Seed URL is the canonical primary link for the catalog entry. |
| 161 | <https://github.com/raiguard/PipeVisualizer> | `included-as-source` | [Pipe Visualizer](../README.md#pipe-visualizer) | Seed URL is retained as the source/repository link for the catalog entry. |
| 162 | <https://mods.factorio.com/mod/BeltVisualizer> | `replaced` | [Belt Visualizer](../README.md#belt-visualizer) | Old slug returned 404; canonical portal slug is belt-visualizer. |
| 163 | <https://github.com/sanqui/factorio-belt-visualizer> | `replaced` | [Belt Visualizer](../README.md#belt-visualizer) | Original seed repository URL returned 404; CodeGreen0386/belt-visualizer is the verified source. |
| 164 | <https://mods.factorio.com/mod/SpidertronEnhancements> | `included` | [Spidertron Enhancements](../README.md#spidertron-enhancements) | Seed URL is the canonical primary link for the catalog entry. |
| 165 | <https://github.com/tburrows13/SpidertronEnhancements> | `included-as-source` | [Spidertron Enhancements](../README.md#spidertron-enhancements) | Seed URL is retained as the source/repository link for the catalog entry. |
| 166 | <https://mods.factorio.com/mod/Constructron-Continued> | `included` | [Spidertron Automation (Constructron Continued)](../README.md#constructron) | Seed URL is the canonical primary link for the catalog entry. |
| 167 | <https://mods.factorio.com/mod/Blueprint-Sandboxes> | `replaced` | [Blueprint Sandboxes](../README.md#blueprint-sandboxes) | Old mixed-case slug returned 404; canonical portal slug is blueprint-sandboxes. |
| 168 | <https://github.com/GlassBricks/Blueprint-Sandboxes> | `replaced` | [Blueprint Sandboxes](../README.md#blueprint-sandboxes) | Original seed repository URL returned 404; cameronleger/blueprint-sandboxes is the verified source. |
| 169 | <https://mods.factorio.com/mod/editor-extensions> | `included` | [Editor Extensions](../README.md#editor-extensions) | Seed URL is the canonical primary link for the catalog entry. |
| 170 | <https://github.com/raiguard/EditorExtensions> | `alias` | [Editor Extensions](../README.md#editor-extensions) | Seed URL is retained as an alias, old slug, or alternate front door for the canonical catalog entry. |
| 171 | <https://mods.factorio.com/mod/creative-mod> | `included` | [Creative Mod](../README.md#creative-mod) | Seed URL is the canonical primary link for the catalog entry. |
| 172 | <https://mods.factorio.com/mod/rso-mod> | `included` | [Resource Spawner Overhaul](../README.md#rso) | Seed URL is the canonical primary link for the catalog entry. |
| 173 | <https://mods.factorio.com/mod/FARL> | `included` | [FARL - Fully Automated Rail Layer](../README.md#farl) | Seed URL is the canonical primary link for the catalog entry. |
| 174 | <https://github.com/Choumiko/FARL> | `included-as-source` | [FARL - Fully Automated Rail Layer](../README.md#farl) | Seed URL is retained as the source/repository link for the catalog entry. |
| 175 | <https://mods.factorio.com/mod/LogisticTrainNetwork> | `included` | [LTN - Logistic Train Network](../README.md#ltn) | Seed URL is the canonical primary link for the catalog entry. |
| 176 | <https://github.com/Yousei9/Logistic-Train-Network> | `alias` | [LTN - Logistic Train Network](../README.md#ltn) | Seed URL is retained as an alias, old slug, or alternate front door for the canonical catalog entry. |
| 177 | <https://mods.factorio.com/mod/ProjectCybersyn> | `replaced` | [Project Cybersyn](../README.md#cybersyn) | Uppercase slug returned 404; canonical portal slug is cybersyn. |
| 178 | <https://github.com/mamoniot/project-cybersyn> | `included-as-source` | [Project Cybersyn](../README.md#cybersyn) | Seed URL is retained as the source/repository link for the catalog entry. |
| 179 | <https://mods.factorio.com/mod/fill4me> | `unavailable` | — | Mod Portal page returned 404. No canonical replacement was verified; use Waterfill or Dectorio landscaping after checking current portal metadata. |
| 180 | <https://mods.factorio.com/mod/tree_collision> | `included` | [Tree Collision](../README.md#tree-collision) | Seed URL is the canonical primary link for the catalog entry. |
| 181 | <https://mods.factorio.com/mod/CleanedConcrete> | `included` | [Cleaned Concrete](../README.md#cleaned-concrete) | Seed URL is the canonical primary link for the catalog entry. |
| 182 | <https://mods.factorio.com/mod/dectorio> | `included` | [Dectorio](../README.md#dectorio) | Seed URL is the canonical primary link for the catalog entry. |
| 183 | <https://github.com/jpanther/Dectorio> | `included-as-source` | [Dectorio](../README.md#dectorio) | Seed URL is retained as the source/repository link for the catalog entry. |
| 184 | <https://mods.factorio.com/mod/textplates> | `included` | [Text Plates](../README.md#text-plates) | Seed URL is the canonical primary link for the catalog entry. |
| 185 | <https://mods.factorio.com/mod/alien-biomes> | `included` | [Alien Biomes](../README.md#alien-biomes) | Seed URL is the canonical primary link for the catalog entry. |
| 186 | <https://mods.factorio.com/mod/DiscoScience> | `included` | [Disco Science](../README.md#disco-science) | Seed URL is the canonical primary link for the catalog entry. |
| 187 | <https://github.com/danielv123/disco-science> | `replaced` | [Disco Science](../README.md#disco-science) | Original seed repository URL returned 404; danielbrauer/DiscoScience is the verified source. |
| 188 | <https://mods.factorio.com/mod/bullet-trails> | `included` | [Bullet Trails](../README.md#bullet-trails) | Seed URL is the canonical primary link for the catalog entry. |
| 189 | <https://mods.factorio.com/mod/grappling-gun> | `included` | [Grappling Gun](../README.md#grappling-gun) | Seed URL is the canonical primary link for the catalog entry. |
| 190 | <https://mods.factorio.com/mod/jetpack> | `included` | [Jetpack](../README.md#jetpack) | Seed URL is the canonical primary link for the catalog entry. |
| 191 | <https://mods.factorio.com/mod/Waterfill_v17> | `included` | [Waterfill](../README.md#waterfill) | Seed URL is the canonical primary link for the catalog entry. |
| 192 | <https://mods.factorio.com/mod/warehousing> | `replaced` | [Warehousing](../README.md#warehousing) | Lowercase slug returned 404; canonical portal slug is Warehousing. |
| 193 | <https://github.com/Warehousing/Warehousing> | `included-as-source` | [Warehousing](../README.md#warehousing) | Seed URL is retained as the source/repository link for the catalog entry. |
| 194 | <https://mods.factorio.com/mod/miniloader> | `included` | [Miniloader](../README.md#miniloader) | Seed URL is the canonical primary link for the catalog entry. |
| 195 | <https://github.com/Therax/miniloader> | `replaced` | [Miniloader](../README.md#miniloader) | Original seed repository URL returned 404; mspielberg/factorio-miniloader is the verified source. |
| 196 | <https://mods.factorio.com/mod/aai-containers> | `included` | [AAI Containers & Warehouses](../README.md#aai-containers) | Seed URL is the canonical primary link for the catalog entry. |
| 197 | <https://mods.factorio.com/mod/aai-vehicles-miner> | `included` | [AAI Vehicles: Miner](../README.md#aai-vehicles-miner) | Seed URL is the canonical primary link for the catalog entry. |
| 198 | <https://mods.factorio.com/mod/nixie-tubes> | `included` | [Nixie Tubes](../README.md#nixie-tubes) | Seed URL is the canonical primary link for the catalog entry. |
| 199 | <https://github.com/justarandomgeek/factorio-nixie-tubes> | `replaced` | [Nixie Tubes](../README.md#nixie-tubes) | Original seed repository URL returned 404; justarandomgeek/nixie-tubes is the verified source. |
| 200 | <https://mods.factorio.com/mod/pushbutton> | `included` | [Pushbutton](../README.md#pushbutton) | Seed URL is the canonical primary link for the catalog entry. |
| 201 | <https://github.com/justarandomgeek/factorio-pushbutton> | `included-as-source` | [Pushbutton](../README.md#pushbutton) | Seed URL is retained as the source/repository link for the catalog entry. |
| 202 | <https://github.com/justarandomgeek/factorio-computer> | `included` | [factorio-computer](../README.md#factorio-computer) | Seed URL is the canonical primary link for the catalog entry. |
| 203 | <https://mods.factorio.com/mod/Krastorio2> | `included` | [Krastorio 2](../README.md#krastorio2) | Seed URL is the canonical primary link for the catalog entry. |
| 204 | <https://github.com/raiguard/Krastorio2> | `alias` | [Krastorio 2](../README.md#krastorio2) | Seed URL is retained as an alias, old slug, or alternate front door for the canonical catalog entry. |
| 205 | <https://mods.factorio.com/mod/space-exploration> | `included` | [Space Exploration](../README.md#space-exploration) | Seed URL is the canonical primary link for the catalog entry. |
| 206 | <https://mods.factorio.com/mod/IndustrialRevolution3> | `included` | [Industrial Revolution 3](../README.md#industrial-revolution3) | Seed URL is the canonical primary link for the catalog entry. |
| 207 | <https://mods.factorio.com/mod/SeaBlock> | `included` | [Sea Block (original)](../README.md#seablock-original) | Seed URL is the canonical primary link for the catalog entry. |
| 208 | <https://github.com/KiwiHawk/SeaBlock> | `alias` | [Sea Block (original)](../README.md#seablock-original) | Seed URL is retained as an alias, old slug, or alternate front door for the canonical catalog entry. |
| 209 | <https://mods.factorio.com/mod/Nullius> | `replaced` | [Nullius](../README.md#nullius) | Uppercase slug returned 404; canonical portal slug is nullius. |
| 210 | <https://github.com/anachrony/nullius> | `replaced` | [Nullius](../README.md#nullius) | Original seed repository URL returned 404; GregorSamsanite/nullius is the verified source. |
| 211 | <https://mods.factorio.com/mod/pycoalprocessing> | `included` | [Pyanodons Coal Processing](../README.md#py-coal-processing) | Seed URL is the canonical primary link for the catalog entry. |
| 212 | <https://github.com/Pyrodactyl-Vulpine/pycoalprocessing> | `replaced` | [Pyanodons Coal Processing](../README.md#py-coal-processing) | Original seed repository URL returned 404; pyanodon/pycoalprocessing is the verified source. |
| 213 | <https://mods.factorio.com/mod/bobsmods> | `replaced` | [Bob's Mods](../README.md#bobs-mods) | There is no single bobsmods portal slug; Bob's mods are a family of individual components. |
| 214 | <https://github.com/Bobingabout/bobsmods> | `replaced` | [Bob's Mods](../README.md#bobs-mods) | Original seed repository URL returned 404; modded-factorio/bobsmods is the verified current source organization. |
| 215 | <https://mods.factorio.com/mod/angelsrefining> | `included` | [Angel's Refining](../README.md#angels-refining) | Seed URL is the canonical primary link for the catalog entry. |
| 216 | <https://github.com/Arch666Angel/mods> | `included-as-source` | [Angel's Refining](../README.md#angels-refining) | Seed URL is retained as the source/repository link for the catalog entry. |
| 217 | <https://mods.factorio.com/mod/Ultracube> | `included` | [Ultracube: Age of Cube](../README.md#ultracube) | Seed URL is the canonical primary link for the catalog entry. |
| 218 | <https://github.com/grandseiken/ultracube> | `replaced` | [Ultracube: Age of Cube](../README.md#ultracube) | Original seed repository URL returned 404; grandseiken/factorio-ultracube is the verified source. |
| 219 | <https://mods.factorio.com/mod/Warptorio2> | `replaced` | [Warptorio2](../README.md#warptorio2) | Uppercase slug returned 404; canonical original continuation slug is warptorio2. |
| 220 | <https://mods.factorio.com/mod/Exotic-Industries> | `replaced` | [Exotic Industries](../README.md#exotic-industries) | Mixed-case slug returned 404; canonical portal slug is exotic-industries. |
| 221 | <https://github.com/PreLeyZero/Exotic-Industries> | `included-as-source` | [Exotic Industries](../README.md#exotic-industries) | Seed URL is retained as the source/repository link for the catalog entry. |
| 222 | <https://mods.factorio.com/mod/LunarLandings> | `included` | [Lunar Landings](../README.md#lunar-landings) | Seed URL is the canonical primary link for the catalog entry. |
| 223 | <https://github.com/tburrows13/LunarLandings> | `included-as-source` | [Lunar Landings](../README.md#lunar-landings) | Seed URL is retained as the source/repository link for the catalog entry. |
| 224 | <https://mods.factorio.com/mod/FreightForwarding> | `included` | [Freight Forwarding](../README.md#freight-forwarding) | Seed URL is the canonical primary link for the catalog entry. |
| 225 | <https://github.com/tburrows13/FreightForwarding> | `included-as-source` | [Freight Forwarding](../README.md#freight-forwarding) | Seed URL is retained as the source/repository link for the catalog entry. |
| 226 | <https://github.com/factoriotools/factorio-docker> | `included` | [factoriotools/factorio-docker](../README.md#factorio-docker) | Seed URL is the canonical primary link for the catalog entry. |
| 227 | <https://github.com/zopanix/docker-factorio-server> | `unavailable` | — | GitHub API returned 404. No verified successor was identified; use factoriotools/factorio-docker or aconti90/factorio-headless. |
| 228 | <https://github.com/rfvgyhn/factorio-docker> | `replaced` | [factoriotools/factorio-docker](../README.md#factorio-docker) | Original seed repository URL returned 404; factoriotools/factorio-docker is cataloged as the current community Docker image. |
| 229 | <https://github.com/clusterio/clusterio> | `included` | [Clusterio](../README.md#clusterio) | Seed URL is the canonical primary link for the catalog entry. |
| 230 | <https://github.com/OpenFactorioServerManager/factorio-server-manager> | `included` | [Open Factorio Server Manager](../README.md#ofsm) | Seed URL is the canonical primary link for the catalog entry. |
| 231 | <https://github.com/Roang-zero1/Factorio-Server-Manager> | `replaced` | [Open Factorio Server Manager](../README.md#ofsm) | Original seed repository URL returned 404; OpenFactorioServerManager/factorio-server-manager is the verified continuation. |
| 232 | <https://github.com/Bisa/factorio-init> | `included` | [factorio-init](../README.md#factorio-init) | Seed URL is the canonical primary link for the catalog entry. |
| 233 | <https://linuxgsm.com/servers/fctrserver/> | `included` | [LinuxGSM Factorio server](../README.md#linuxgsm-factorio) | Seed URL is the canonical primary link for the catalog entry. |
| 234 | <https://github.com/GameServerManagers/LinuxGSM> | `included-as-source` | [LinuxGSM Factorio server](../README.md#linuxgsm-factorio) | Seed URL is retained as the source/repository link for the catalog entry. |
| 235 | <https://github.com/majormjr/factorio-rcon-py> | `unavailable` | — | GitHub API returned 404. No verified successor was identified; use mark9064/factorio-rcon-py or factorio-rcon-api. |
| 236 | <https://github.com/narfman0/factorio-rcon> | `unavailable` | — | GitHub API returned 404. No verified successor was identified; use gtaylor/factorio-rcon, FactorioSharp.Rcon, or factorio-rcon-api. |
| 237 | <https://github.com/gtaylor/factorio-rcon> | `included` | [gtaylor/factorio-rcon](../README.md#gtaylor-rcon) | Seed URL is the canonical primary link for the catalog entry. |
| 238 | <https://github.com/PrefectHQ/factorio-rcon> | `unavailable` | — | GitHub API returned 404. No verified successor was identified; use gtaylor/factorio-rcon, FactorioSharp.Rcon, or factorio-rcon-api. |
| 239 | <https://github.com/DistilledP/Factorio-Discord-Bot> | `unavailable` | — | GitHub API returned 404. No verified successor was identified; use FactoCord, FactorioChatBot, ChatWire, or D-Wire. |
| 240 | <https://github.com/tofuman0/factorio-discord-bridge> | `unavailable` | — | GitHub API returned 404. No verified successor was identified; use FactoCord, FactorioChatBot, ChatWire, or D-Wire. |
| 241 | <https://github.com/efokschaner/terraform-provider-factorio> | `included` | [terraform-provider-factorio](../README.md#terraform-factorio-provider) | Seed URL is the canonical primary link for the catalog entry. |
| 242 | <https://factorio.zone/> | `included` | [Factorio Zone](../README.md#factorio-zone) | Seed URL is the canonical primary link for the catalog entry. |
| 243 | <https://redmew.com/> | `alias` | [RedMew](../README.md#redmew) | Site fetch returned HTTP 500 during verification; the RedMew source repository is cataloged as the durable primary link. |
| 244 | <https://github.com/Factorio-RedMew/RedMew> | `replaced` | [RedMew](../README.md#redmew) | Original seed repository URL returned 404; Refactorio/RedMew is the verified source. |
| 245 | <https://getcomfy.eu/> | `alias` | [ComfyFactorio](../README.md#comfy) | Seed URL is retained as an alias, old slug, or alternate front door for the canonical catalog entry. |
| 246 | <https://github.com/ComfyFactorio/ComfyFactorio> | `replaced` | [ComfyFactorio](../README.md#comfy) | Original seed organization/repository URL returned 404; M3wM3w/ComfyFactorio is the verified source. |
| 247 | <https://github.com/AwF-Team/AwF-Scenario> | `unavailable` | [AwF Scenario](https://github.com/AwF-Team/AwF-Scenario) (not rendered) | Seed URL is the canonical primary link for the catalog entry. |
| 248 | <https://github.com/FactorioMMO/FactorioMMO> | `replaced` | [FactorioMMO scenarios](../README.md#factoriommo) | Original seed repository URL returned 404; factoriommo/factoriommoscenarios preserves the historical scenario lineage. |
| 249 | <https://github.com/FishBus/FishBus> | `unavailable` | [FishBus](https://github.com/FishBus/FishBus) (not rendered) | Seed URL is the canonical primary link for the catalog entry. |
| 250 | <https://github.com/ExplosiveGaming/scenario> | `alias` | [ExpCluster](../README.md#expcluster) | Seed URL is retained as an alias, old slug, or alternate front door for the canonical catalog entry. |
| 251 | <https://github.com/Oarcinae/FactorioScenarioMultiplayerSpawn> | `included` | [Oarc's Multiplayer Spawn](../README.md#oarc-spawn) | Seed URL is the canonical primary link for the catalog entry. |
| 252 | <https://github.com/justarandomgeek/vscode-factoriomod-debug> | `included` | [Factorio Mod Tool Kit (FMTK)](../README.md#fmtk) | Seed URL is the canonical primary link for the catalog entry. |
| 253 | <https://github.com/Roang-zero1/FMTK> | `replaced` | [Factorio Mod Tool Kit (FMTK)](../README.md#fmtk) | Original seed repository URL returned 404; justarandomgeek/vscode-factoriomod-debug is the canonical Factorio Mod Tool Kit. |
| 254 | <https://github.com/JanSharp/FactorioSumnekoLuaPlugin> | `included` | [FactorioSumnekoLuaPlugin](../README.md#sumneko-plugin) | Seed URL is the canonical primary link for the catalog entry. |
| 255 | <https://github.com/GlassBricks/typed-factorio> | `included` | [typed-factorio](../README.md#typed-factorio) | Seed URL is the canonical primary link for the catalog entry. |
| 256 | <https://github.com/PennyJim/factorio-type-kit> | `replaced` | [factorio-type-kit](../README.md#factorio-type-kit) | Original seed repository URL returned 404; cdaringe/factorio-type-kit is archived and retained as historical. |
| 257 | <https://github.com/Afforess/Factorio-Stdlib> | `included` | [Factorio-Stdlib](../README.md#factorio-stdlib) | Seed URL is the canonical primary link for the catalog entry. |
| 258 | <https://codeberg.org/raiguard/flib> | `alias` | [Factorio Library (flib)](../README.md#flib) | Seed URL is retained as an alias, old slug, or alternate front door for the canonical catalog entry. |
| 259 | <https://github.com/raiguard/flib> | `replaced` | [Factorio Library (flib)](../README.md#flib) | GitHub repository is an archived migration notice; flib source and issue tracking are on Codeberg. |
| 260 | <https://mods.factorio.com/mod/flib> | `included` | [Factorio Library (flib)](../README.md#flib) | Seed URL is the canonical primary link for the catalog entry. |
| 261 | <https://github.com/demodude4u/Java-Factorio-Data-Wrapper> | `included` | [Java-Factorio-Data-Wrapper](../README.md#java-data-wrapper) | Seed URL is the canonical primary link for the catalog entry. |
| 262 | <https://github.com/fgardt/factorio-mod-portal-client> | `replaced` | [factorio-mod-portal-client](../README.md#mod-portal-client-php) | Original seed repository URL returned 404; BluePsyduck/factorio-mod-portal-client is the verified PHP portal client. |
| 263 | <https://github.com/nickolasbradham/Factorio-Mod-Downloader> | `included` | [Factorio-Mod-Downloader](../README.md#nickolasbradham-mod-downloader) | Seed URL is the canonical primary link for the catalog entry. |
| 264 | <https://github.com/Modo-lv/Factorio-Mod-Portal-Downloader> | `unavailable` | [Factorio-Mod-Portal-Downloader](https://github.com/Modo-lv/Factorio-Mod-Portal-Downloader) (not rendered) | Seed URL is the canonical primary link for the catalog entry. |
| 265 | <https://github.com/MitchRooney/FactorioModManager> | `unavailable` | [FactorioModManager](https://github.com/MitchRooney/FactorioModManager) (not rendered) | Seed URL is the canonical primary link for the catalog entry. |
| 266 | <https://re146.dev/factorio/mods/en> | `included` | [re146 Factorio mods mirror](../README.md#re146-mods) | Seed URL is the canonical primary link for the catalog entry. |
| 267 | <https://github.com/re146/factorio-mods-portal> | `unavailable` | [factorio-mods-portal](https://github.com/re146/factorio-mods-portal) (not rendered) | Seed URL is the canonical primary link for the catalog entry. |
| 268 | <https://github.com/factoriolab/factoriolab-export> | `included` | [factoriolab-export](../README.md#factoriolab-export) | Seed URL is the canonical primary link for the catalog entry. |
| 269 | <https://github.com/factoriolab/factorio-lab-tools> | `included` | [factorio-lab-tools](../README.md#factorio-lab-tools) | Seed URL is the canonical primary link for the catalog entry. |
| 270 | <https://factoriomaps.com/> | `alias` | [FactorioMaps (L0laapk3)](../README.md#factoriomaps-mod) | Seed URL is retained as an alias, old slug, or alternate front door for the canonical catalog entry. |
| 271 | <https://github.com/FactorioMaps/FactorioMaps> | `replaced` | [FactorioMaps (L0laapk3)](../README.md#factoriomaps-mod) | Original seed repository URL returned 404; L0laapk3/FactorioMaps is the verified source. |
| 272 | <https://github.com/nickolasbradham/Factorio-Screenshot-Stitcher> | `included` | [Factorio-Screenshot-Stitcher](../README.md#screenshot-stitcher) | Seed URL is the canonical primary link for the catalog entry. |
| 273 | <https://github.com/eisenefaust/factorio_tricks_iceberg> | `included-as-source` | [Factorio Tricks Iceberg](../README.md#factorio-tricks-iceberg) | Seed URL is retained as the source/repository link for the catalog entry. |
| 274 | <https://alt-f4.blog/> | `included` | [Alt-F4](../README.md#alt-f4) | Seed URL is the canonical primary link for the catalog entry. |
| 275 | <https://github.com/AlternativeFFFF/Alt-F4> | `included-as-source` | [Alt-F4](../README.md#alt-f4) | Seed URL is retained as the source/repository link for the catalog entry. |
| 276 | <https://www.speedrun.com/factorio> | `included` | [Speedrun.com Factorio](../README.md#speedrun-factorio) | Seed URL is the canonical primary link for the catalog entry. |
| 277 | <https://www.reddit.com/r/factorio/> | `included` | [r/factorio](../README.md#reddit-factorio) | Seed URL is the canonical primary link for the catalog entry. |
| 278 | <https://www.reddit.com/r/factorio/wiki/index> | `included` | [r/factorio wiki](../README.md#reddit-wiki) | Seed URL is the canonical primary link for the catalog entry. |
| 279 | <https://www.reddit.com/r/FactorioBlueprints/> | `included` | [r/FactorioBlueprints](../README.md#reddit-blueprints) | Seed URL is the canonical primary link for the catalog entry. |
| 280 | <https://www.reddit.com/r/technicalfactorio/> | `included` | [r/technicalfactorio](../README.md#reddit-technical) | Seed URL is the canonical primary link for the catalog entry. |
| 281 | <https://steamcommunity.com/sharedfiles/filedetails/?id=862972621> | `included` | [Xterminator: Everything To Do With Smelting](../README.md#steam-smelting-guide) | Seed URL is the canonical primary link for the catalog entry. |
| 282 | <https://discord.gg/factorio> | `included` | [Official Factorio Discord](../README.md#official-discord) | Seed URL is the canonical primary link for the catalog entry. |
| 283 | <https://github.com/topics/factorio> | `included` | [GitHub topic: factorio](../README.md#github-topic-factorio) | Seed URL is the canonical primary link for the catalog entry. |
| 284 | <https://github.com/topics/factorio-mod> | `included` | [GitHub topic: factorio-mod](../README.md#github-topic-factorio-mod) | Seed URL is the canonical primary link for the catalog entry. |
| 285 | <https://github.com/topics/factorio-blueprints> | `included` | [GitHub topic: factorio-blueprints](../README.md#github-topic-factorio-blueprints) | Seed URL is the canonical primary link for the catalog entry. |
| 286 | <https://github.com/topics/factorio-tool> | `included` | [GitHub topic: factorio-tool](../README.md#github-topic-factorio-tool) | Seed URL is the canonical primary link for the catalog entry. |
