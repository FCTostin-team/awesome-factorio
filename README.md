[![awesome-adops-site](https://github.com/FCTostin-team/awesome-factorio/blob/main/image/awesome-factorio.png)](https://github.com/FCTostin-team/awesome-factorio/pulls)

[![animated-line](https://github.com/readme-SVG/animated-line/blob/main/STORAGE/line-svg-D35A05.svg)](https://github.com/readme-SVG/animated-line) <!-- -SVG-Line- -->

<p align="center">
  <a href="https://awesome.re"><img alt="Awesome" src="https://awesome.re/badge.svg"></a>
  <a href="https://github.com/FCTostin-team/awesome-factorio/pulls"><img alt="PRs Welcome" src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square"></a>
  <a href="LICENSE"><img alt="License: Apache-2.0" src="https://img.shields.io/badge/license-Apache--2.0-blue.svg"></a>
  <img alt="Curated resources" src="https://img.shields.io/badge/resources-394-brightgreen.svg">
</p>

> A curated, English-language map of useful Factorio websites, tools, mods, repositories, servers, modding utilities, and communities.

This list catalogs **404 resources** and renders **394 recommended or clearly labeled historical entries**. It was expanded from a 286-URL seed list through web research, GitHub discovery, Mod Portal checks, and repository README review. It is broad, but it is **not a claim that every Factorio resource on the internet has been found**. Broken or unavailable seed links are preserved in the [link audit](docs/link-audit.md) instead of being presented as live recommendations.

## How to read this list

- **Primary links** point to the canonical project page, mod portal page, live tool, or repository.
- **Source links** point to source code when the primary link is a live site or mod portal page.
- **`checked:`** records the verification method used on 2026-10-31. It does not mean the tool was exhaustively tested.
- **Compatibility tags** are included only when project documentation or portal metadata supplied evidence. A broad portal range is not a guarantee that every feature works with Space Age, quality, or other overhauls.
- **`legacy`** usually means the project stops at Factorio 1.1 or an older major version. **`historical`** means it is useful for context but not necessarily maintained. **`experimental`** means the project itself warns about stability.
- **Space Age ≠ Factorio 2.x.** Some mods support the 2.x engine but not the expansion; some support the expansion only through add-ons; some portal ranges conflict with prose. Read the compatibility note before starting a long run.
- **Modpacks are not interchangeable.** Krastorio 2, Space Exploration, Nullius, Pyanodons, Sea Block, Ultracube, and similar overhauls often require dedicated mod lists.

## Quick start

| Goal | Start with |
| --- | --- |
| Install or update the game | [Factorio downloads](#factorio-download), [Space Age](#factorio-space-age), [version history](#wiki-version-history) |
| Learn ratios and mechanics | [Factorio Cheat Sheet](#factorio-cheatsheet), [FactorioLab](#factoriolab), [Kirk McDonald calculator](#kirk-mcdonald-calculator) |
| Plan a modded factory in-game | [Factory Planner](#factory-planner), [Helmod](#helmod), [Rate Calculator](#rate-calculator) |
| Find recipes and bottlenecks | [FNEI](#fnei), [What is it really used for?](#what-is-it-really-used-for), [Assembly Analyst](#assembly-analyst), [Bottleneck Lite](#bottleneck-lite) |
| Share or edit blueprints | [FactorioPrints](#factorioprints), [FactorioBin](#factoriobin), [FactoryGameFan FBE](#fbe-factorygamefan), [FCT decoder/encoder](#fct-blueprint-decoder) |
| Build circuits or displays | [Circuit cookbook](#wiki-circuit-cookbook), [Verilog2Factorio](#verilog2factorio), [Cnide](#cnide), [Nixie Tubes](#nixie-tubes) |
| Test designs safely | [Blueprint Sandboxes](#blueprint-sandboxes), [Editor Extensions](#editor-extensions), [Creative Mod](#creative-mod) |
| Run a server | [Factorio downloads/headless](#factorio-download), [factorio-docker](#factorio-docker), [LinuxGSM](#linuxgsm-factorio), [Clusterio](#clusterio) |
| Make a mod | [Modding wiki](#wiki-modding), [Lua API](#factorio-lua-api), [FMTK](#fmtk), [flib](#flib), [Untitled GUI Guide](#untitled-gui-guide) |
| Choose an overhaul | [Overhauls](#overhauls-and-challenge-modpacks), [compatibility guide](docs/compatibility.md) |

## Contents

- [Official resources](#official-resources) (13)
- [Reference, tutorials, and guides](#reference-tutorials-and-guides) (32)
- [Calculators and production planners](#calculators-and-production-planners) (30)
- [Blueprint sites, editors, and libraries](#blueprint-sites-editors-and-libraries) (42)
- [Circuit network programming and simulation](#circuit-network-programming-and-simulation) (12)
- [Art, music, maps, and visualization](#art-music-maps-and-visualization) (20)
- [Quality-of-life and information mods](#quality-of-life-and-information-mods) (53)
- [Logistics, trains, storage, and production mods](#logistics-trains-storage-and-production-mods) (15)
- [World, decoration, combat, and power mods](#world-decoration-combat-and-power-mods) (18)
- [Overhauls and challenge modpacks](#overhauls-and-challenge-modpacks) (24)
- [Sandbox, testing, and editor tools](#sandbox-testing-and-editor-tools) (7)
- [Multiplayer, servers, and operations](#multiplayer-servers-and-operations) (59)
- [Modding frameworks, data tooling, and developer utilities](#modding-frameworks-data-tooling-and-developer-utilities) (35)
- [Communities, discovery, and creators](#communities-discovery-and-creators) (34)
- [Link audit](docs/link-audit.md)
- [Compatibility guide](docs/compatibility.md)
- [Research methodology](docs/research-methodology.md)
- [Contributing](CONTRIBUTING.md)

## Official resources

Start here for authoritative downloads, expansion information, development news, wiki documentation, mod distribution, and API references.

<a id="factorio-home"></a>
- **[Factorio official website](https://www.factorio.com/)** — The canonical home for Factorio: game overview, news, purchase links, expansion information, and pointers to the wiki, forums, mod portal, and API documentation.
  `website` · `checked: web page`

<a id="factorio-download"></a>
- **[Factorio downloads and demo](https://www.factorio.com/download)** — Official stable, experimental, and headless server downloads plus the free demo. On 2026-10-31 the stable/experimental/headless build was 2.1.24 and the demo was 2.1.23; always use this page rather than third-party mirrors for current installers.
  `website` · `checked: web page`

<a id="factorio-space-age"></a>
- **[Factorio: Space Age](https://www.factorio.com/space-age)** — Official expansion page describing the new planets, space platforms, quality, elevated rails, and other Space Age content. Use it to distinguish expansion features from base-game 2.x features when choosing mods and calculators.
  `website` · `checked: web page`

<a id="factorio-blog"></a>
- **[Factorio blog / Friday Facts](https://www.factorio.com/blog/)** — Wube's development blog and Friday Facts archive. Primary source for engine changes, modding API changes, release announcements, and design rationale; FFF-449 announced the 2.1 stable release on 2026-10-23.
  `website` · `checked: web page`

<a id="factorio-forums"></a>
- **[Factorio forums](https://forums.factorio.com/)** — Official discussion forums for support, bug reports, mod releases, multiplayer, and community projects. Many older mods still use forum threads as their canonical documentation and issue tracker.
  `community` · `checked: web page`

<a id="factorio-wiki"></a>
- **[Factorio wiki](https://wiki.factorio.com/)** — Community-maintained official wiki covering mechanics, items, tutorials, modding, and version history. Page existence for key tutorials and reference pages was checked through the MediaWiki API on 2026-10-31.
  `reference` · `checked: MediaWiki API`

<a id="factorio-mod-portal"></a>
- **[Factorio Mod Portal](https://mods.factorio.com/)** — Official mod distribution platform with versioned releases, dependency metadata, changelogs, discussions, and download counts. Prefer the portal page over old forum download links when checking a mod's supported Factorio versions.
  `website` · `checked: web page`

<a id="factorio-lua-api"></a>
- **[Factorio Lua API documentation](https://lua-api.factorio.com/latest/)** — Official machine-readable and human-readable runtime modding API documentation. The latest docs track the current game; use versioned API docs when targeting older Factorio releases.
  `reference` · `checked: web page`

<a id="factorio-steam"></a>
- **[Factorio on Steam](https://store.steampowered.com/app/427520/Factorio/)** — Steam store page for Factorio, including the base game, Space Age expansion, news, reviews, and community hub. Useful for platform-specific purchase and update questions.
  `website` · `checked: search result`

<a id="factorio-api-releases"></a>
- **[Factorio release API](https://factorio.com/api/latest-releases)** — Small official JSON endpoint listing the latest stable, experimental, and headless release versions. Handy for server automation and update checks without scraping the download page.
  `API` · `checked: web page`

<a id="factorio-mod-portal-api"></a>
- **[Mod Portal API documentation](https://wiki.factorio.com/Mod_portal_API)** — Official wiki documentation for the Mod Portal HTTP API, including mod metadata, release listings, pagination, and download authentication. Useful for building mod managers, mirrors, and update checkers.
  `reference` · `checked: MediaWiki API`

<a id="factorio-data"></a>
- **[wube/factorio-data](https://github.com/wube/factorio-data)** — Official repository tracking changes to Factorio's Lua prototype definitions between releases. Invaluable for mod authors who need to diff base-game data stages, recipes, technologies, and entity prototypes across versions.
  `repository` · `Lua` · `checked: GitHub API/README`

<a id="wube-github"></a>
- **[Wube Software on GitHub](https://github.com/wube)** — Official Wube Software GitHub organization. Hosts factorio-data, graphics tools, and other public repositories; note that the old factorio-lualib repository is not currently present.
  `repository` · `checked: GitHub API/README`

## Reference, tutorials, and guides

Mechanics references, tutorials, cheat sheets, and community guides. Older guides are labeled when their game-version relevance is limited.

<a id="wiki-combinator"></a>
- **[Wiki: Combinator tutorial](https://wiki.factorio.com/Tutorial:Combinator_tutorial)** — Step-by-step introduction to arithmetic, decider, and constant combinators, including signal wiring and common patterns. A good starting point before reading the circuit cookbook or compiler projects.
  `reference` · `checked: MediaWiki API`

<a id="wiki-circuit-cookbook"></a>
- **[Wiki: Circuit network cookbook](https://wiki.factorio.com/Tutorial:Circuit_network_cookbook)** — Collection of practical circuit recipes such as counters, memory cells, clocks, and condition logic. Useful both for hand-building circuits and for understanding what circuit compilers generate.
  `reference` · `checked: MediaWiki API`

<a id="wiki-train-signals"></a>
- **[Wiki: Train signals](https://wiki.factorio.com/Tutorial:Train_signals)** — Official tutorial on rail blocks, chain signals, intersections, and deadlock avoidance. Still the best first reference for vanilla rail signaling before adding LTN or Cybersyn.
  `reference` · `checked: MediaWiki API`

<a id="wiki-console"></a>
- **[Wiki: Console](https://wiki.factorio.com/Console)** — Reference for the Lua console, command syntax, permissions, and commonly used administrative commands. Important reading before running generated commands from blueprint or server tools.
  `reference` · `checked: MediaWiki API`

<a id="wiki-controls"></a>
- **[Wiki: Controls](https://wiki.factorio.com/Controls)** — Official keyboard and mouse control reference. The old Keyboard_bindings URL redirects here; use this page for current default bindings and customization notes.
  `reference` · `checked: MediaWiki API`

<a id="wiki-blueprint-string"></a>
- **[Wiki: Blueprint string format](https://wiki.factorio.com/Blueprint_string_format)** — Technical description of the base64/zlib/JSON blueprint exchange format. Essential for writing decoders, generators, editors, and migration tools.
  `reference` · `checked: MediaWiki API`

<a id="wiki-command-line"></a>
- **[Wiki: Command line parameters](https://wiki.factorio.com/Command_line_parameters)** — Official reference for headless server and client command-line options, including save loading, mod directories, server settings, and RCON-related startup flags.
  `reference` · `checked: MediaWiki API`

<a id="wiki-multiplayer"></a>
- **[Wiki: Multiplayer](https://wiki.factorio.com/Multiplayer)** — Official multiplayer overview covering joining games, server browsing, latency, and headless server basics. Pair with the server-operations section for deployment tooling.
  `reference` · `checked: MediaWiki API`

<a id="wiki-application-directory"></a>
- **[Wiki: Application directory](https://wiki.factorio.com/Application_directory)** — Explains where Factorio stores saves, mods, logs, configuration, and user data on Windows, macOS, and Linux. Needed when installing mods manually or debugging server deployments.
  `reference` · `checked: MediaWiki API`

<a id="wiki-quality"></a>
- **[Wiki: Quality](https://wiki.factorio.com/Quality)** — Official reference for the Space Age quality mechanic, quality tiers, recycling, and module interactions. Check this before assuming a calculator or mod supports quality.
  `reference` · `checked: MediaWiki API`

<a id="wiki-space-age"></a>
- **[Wiki: Space Age](https://wiki.factorio.com/Space_Age)** — Official expansion reference covering planets, space platforms, quality, elevated rails, and new recipes. Useful for separating base 2.x content from expansion-only content.
  `reference` · `checked: MediaWiki API`

<a id="wiki-version-history"></a>
- **[Wiki: Version history](https://wiki.factorio.com/Version_history)** — Chronological changelog of Factorio releases. Use it to confirm when a mechanic or API changed instead of relying on old tutorials or forum posts.
  `reference` · `checked: MediaWiki API`

<a id="wiki-replay"></a>
- **[Wiki: Replay system](https://wiki.factorio.com/Replay_system)** — Documentation for Factorio's replay recording and playback system. Relevant to timelapse tools, debugging, and recovering footage from saves.
  `reference` · `checked: MediaWiki API`

<a id="wiki-modding"></a>
- **[Wiki: Modding](https://wiki.factorio.com/Modding)** — Official modding portal page with installation instructions, data-stage overview, and links to API documentation and tutorials. The old Installing_Mods URL redirects into this page.
  `reference` · `checked: MediaWiki API`

<a id="wiki-mod-structure"></a>
- **[Wiki: Mod structure](https://wiki.factorio.com/Tutorial:Mod_structure)** — Explains the required info.json, data.lua, control.lua, locale, graphics, and migration layout of a Factorio mod. Read before using templates or transpilers.
  `reference` · `checked: MediaWiki API`

<a id="wiki-mod-settings"></a>
- **[Wiki: Mod settings](https://wiki.factorio.com/Tutorial:Mod_settings)** — Tutorial for startup, map, and per-player mod settings, including data-stage definitions and runtime access. Useful for both mod authors and players editing mod-settings.dat.
  `reference` · `checked: MediaWiki API`

<a id="wiki-localisation"></a>
- **[Wiki: Localisation](https://wiki.factorio.com/Tutorial:Localisation)** — Official guide to locale files, rich text, plurals, and parameterized strings. Pair with factorio-mods-localization for community translation workflows.
  `reference` · `checked: MediaWiki API`

<a id="wiki-gangsir"></a>
- **[Gangsir's modding tutorial](https://wiki.factorio.com/Tutorial:Gangsir%27s_modding_tutorial)** — Long-running community modding tutorial hosted on the official wiki. Covers practical Lua examples and common mod patterns, though readers should cross-check API details against the current Lua API docs.
  `reference` · `checked: MediaWiki API`

<a id="factorio-cheatsheet"></a>
- **[Factorio Cheat Sheet](https://factoriocheatsheet.com/)** — Dense visual reference for ratios, balancers, science, modules, nuclear power, trains, and Space Age content. The site explicitly uses 2.0.7 data and marks Space Age sections, so treat it as a 2.0-era reference rather than a live 2.1 database.
  `reference` · `checked: web page` · [source](https://github.com/deniszholob/factorio-cheat-sheet)

<a id="factorio-tricks-iceberg"></a>
- **[Factorio Tricks Iceberg](https://eisenefaust.github.io/factorio_tricks_iceberg/)** — Community collection of speedrun tricks, obscure mechanics, and optimization notes. Useful for advanced players and tool authors who need to understand edge-case behavior.
  `reference` · `checked: GitHub API/README` · [source](https://github.com/eisenefaust/factorio_tricks_iceberg)

<a id="untitled-gui-guide"></a>
- **[Untitled GUI Guide](https://github.com/ClaudeMetz/UntitledGuiGuide)** — Practical Factorio GUI tutorial with runnable examples for styles, elements, events, and common interface patterns. One of the best complements to the official Lua API docs for mod authors.
  `reference` · `Lua` · `checked: GitHub API/README`

<a id="factorio-mod-scripts"></a>
- **[FactorioModScripts](https://github.com/StephenBarnes/FactorioModScripts)** — Collection of small Lua scripts and console snippets for inspecting and manipulating a running game. Useful for debugging, experimentation, and learning the runtime API.
  `repository` · `Python` · `checked: GitHub API/README`

<a id="steam-smelting-guide"></a>
- **[Xterminator: Everything To Do With Smelting](https://steamcommunity.com/sharedfiles/filedetails/?id=862972621)** — Classic Steam guide covering belt-based and bot-based smelting designs, ratios, and furnace setups. Historical but still useful for understanding smelting layout principles; verify exact ratios against current game data.
  `reference` · `historical` · `checked: web page`

<a id="reddit-wiki"></a>
- **[r/factorio wiki](https://www.reddit.com/r/factorio/wiki/index)** — Community-maintained index of FAQs, guides, mod recommendations, and technical resources. A good discovery layer, but individual guides may be older than the current game.
  `reference` · `checked: search result`

<a id="pyanodons-early-guide"></a>
- **[Pyanodons early-game guide](https://docs.google.com/document/d/1KfoEFVTMYV0LAUR7M1yXrR8QV8_mW01YpW6X1IvP-z8/edit)** — Community guide linked from the official Pyanodons Coal Processing page for surviving the first hundred hours. Useful because pY's byproduct-heavy early game differs sharply from vanilla intuition.
  `reference` · `checked: web page`

<a id="pyanodons-ups-guide"></a>
- **[Pyanodons installation and UPS guide](https://docs.google.com/document/d/1T3c9Eo3Dhx_-DCmr268s4j9NMUZWb4GDj6zm_90xnAc/edit)** — Community installation and performance guide linked from the pY mod page. Covers mod setup and UPS optimization for one of Factorio's largest modpacks.
  `reference` · `checked: web page`

<a id="nullius-faq"></a>
- **[Nullius FAQ](https://mods.factorio.com/mod/nullius/faq)** — Official FAQ tab for Nullius covering installation, compatibility, and common progression questions. Read before combining Nullius with other overhauls or quality-of-life mods.
  `reference` · `checked: web page`

<a id="space-exploration-wiki"></a>
- **[Space Exploration wiki](https://spaceexploration.miraheze.org/)** — Community wiki for Space Exploration mechanics, science packs, planets, logistics, and progression. Linked as the official homepage from the mod portal page.
  `reference` · `checked: web page`

<a id="kirk-mcdonald-calc-docs"></a>
- **[Kirk McDonald calculator documentation](https://kirkmcdonald.github.io/posts/calculation.html)** — Explains the matrix-based production calculation model behind the classic Factorio calculator. Useful for understanding how recipe solvers handle byproducts and cycles.
  `reference` · `checked: search result`

<a id="writeup-factorio-rce"></a>
- **[Factorio save-file RCE writeup](https://github.com/valentin-metz/writeup_factorio)** — Security writeup of a remote-code-execution issue involving modified Factorio save files. Important reading for server operators and modders about trusting untrusted saves.
  `reference` · `Python` · `checked: GitHub API/README`

<a id="awesomefactorio-yrfle"></a>
- **[AwesomeFactorio (yrfle)](https://awesomefactorio.yrfle.com/)** — Community guide/project asking how to build an awesome factory at very high science throughput. Useful as a niche megabase reference; verify current maintenance.
  `reference` · `TypeScript` · `checked: GitHub API/README` · [source](https://github.com/canadianbeaver/awesomefactorio)

<a id="introduction-to-factorio"></a>
- **[Introduction to Factorio](http://tanganke.github.io/introduction-to-factorio/)** — Introductory book-style guide to Factorio. Useful for new players who prefer a structured text walkthrough; check version relevance.
  `reference` · `checked: GitHub API/README` · [source](https://github.com/tanganke/introduction-to-factorio)

## Calculators and production planners

Web, desktop, and in-game-adjacent tools for ratios, production chains, quality loops, power, balancers, and layout optimization.

<a id="factoriolab"></a>
- **[FactorioLab](https://factoriolab.github.io/)** — Browser-based production calculator for Factorio and other factory games, with recipe trees, machine/module/beacon selection, and shareable URLs. The live app redirected to a 2.x Space Age dataset on 2026-10-31; the open-source data pipeline is also listed in the modding section.
  `tool` · `TypeScript` · `Factorio 2.x / Space Age dataset selected in live app` · `checked: web page` · [source](https://github.com/factoriolab/factoriolab)

<a id="kirk-mcdonald-calculator"></a>
- **[Kirk McDonald's Factorio Calculator](https://kirkmcdonald.github.io/calc.html)** — Classic matrix-based production calculator with a clean recipe table and dependency graph. The live base-game dataset identified itself as 2.0; do not assume Space Age or quality support from the calculator's age or popularity.
  `tool` · `JavaScript` · `Base-game 2.0 dataset observed; Space Age support not verified` · `checked: web page` · [source](https://github.com/KirkMcDonald/kirkmcdonald.github.io)

<a id="yafc-ce"></a>
- **[YAFC: Community Edition](https://github.com/Yafc-CE/yafc-ce)** — Desktop production planner and analyzer that loads your actual Factorio installation and mod set, making it one of the strongest choices for heavily modded games. Supports complex recipe graphs, byproducts, and detailed machine/module configuration.
  `tool` · `C#` · `checked: GitHub API/README`

<a id="yafc-original"></a>
- **[YAFC (original)](https://github.com/ShadowTheAge/yafc)** — Original YAFC repository by ShadowTheAge. Kept for historical reference and upstream context; new users should normally prefer the actively redirected Community Edition above.
  `repository` · `C#` · `historical` · `checked: GitHub API/README`

<a id="foreman2"></a>
- **[Foreman2](https://github.com/DanielKote/Foreman2)** — Visual flowchart-style production planner for Factorio. Lets you build recipe nodes, connect production lines, and inspect machine counts in a graph rather than a flat table.
  `tool` · `C#` · `checked: GitHub API/README`

<a id="doomeer-planner"></a>
- **[Doomeer's Factorio Planner](https://doomeer.com/factorio/)** — Long-running web planner for production chains and ratios. Useful as a lightweight alternative to larger calculators, but check the selected game dataset before using it for Space Age recipes.
  `tool` · `OCaml` · `checked: web page` · [source](https://github.com/doomeer/factorio)

<a id="s-fabian-calculator"></a>
- **[s-fabian's Factorio Calculator](https://just-a-server.de/factorio/)** — Web calculator whose changelog explicitly targets Space Age 2.1.20 normal quality as of 2026-10-20. A useful current-era alternative when you want a browser planner with recent expansion data.
  `tool` · `JavaScript` · `Space Age 2.1.20 normal quality per project changelog` · `checked: web page` · [source](https://github.com/s-fabian/factorio-calculator)

<a id="factoriocalculator-app"></a>
- **[factoriocalculator.app](https://factoriocalculator.app/)** — Browser production planner advertising Space Age, quality, planets, modules, beacons, and shareable state. Useful for quick expansion-aware planning without installing a desktop tool.
  `tool` · `Space Age / quality / planets advertised by live app` · `checked: web page`

<a id="anthfgreco-calculator"></a>
- **[anthfgreco's Factorio Calculator](https://github.com/anthfgreco/factorio-calculator)** — TypeScript production calculator with Space Age, quality, and planet-aware planning. The README targets Factorio 2.1.14, so it is a recent expansion-focused option rather than a legacy 1.1 calculator.
  `tool` · `TypeScript` · `Factorio 2.1.14 / Space Age per README` · `checked: GitHub API/README`

<a id="jordan-schnur-calculator"></a>
- **[Jordan Schnur's Factorio Calculator](https://jordanschnur.com/factorio-calculator/)** — Table-first Factorio 2.0 / Space Age production-rate calculator forked from Kirk McDonald's calculator, with a flow graph view. Good if you like the classic calculator model but want expansion-era data.
  `tool` · `JavaScript` · `Factorio 2.0 / Space Age per project description` · `checked: GitHub API/README` · [source](https://github.com/jordan-schnur/factorio-calculator)

<a id="factorio-live-planner"></a>
- **[0sdknum Factorio Live Planner](https://0sdknum.github.io/factorio-live-planner/)** — Stateless browser planner advertising 659 official recipes, interactive dependency maps, throughput analysis, shareable URLs, and connected-machine blueprint export. Useful when you want to move from a recipe plan to a rough layout.
  `tool` · `TypeScript` · `Base and Space Age recipes advertised by live app` · `checked: web page` · [source](https://github.com/0sdknum/factorio-live-planner)

<a id="metatorio"></a>
- **[Metatorio](https://github.com/cyx2015s/metatorio-calc)** — Rust-based Factorio calculator project. Interesting for users who want a native or self-hosted planner and for developers studying alternative solver implementations.
  `tool` · `Rust` · `checked: GitHub API/README`

<a id="pyops"></a>
- **[PyOps](https://apocdev.github.io/pyops/)** — Local browser-based planner focused on Pyanodons, with support for cycles, byproducts, spoilage, fluid temperatures, and other modpacks. Also includes in-game ops assistance; especially useful where vanilla-oriented calculators struggle with pY's recipe graph.
  `tool` · `TypeScript` · `checked: web page` · [source](https://github.com/apocdev/pyops)

<a id="factorio-tools"></a>
- **[FactorioTools](https://malte9799.github.io/FactorioTools/)** — Client-side blueprint viewer and rate calculator that renders blueprints with game sprites and computes production rates. The live dataset showed 2.0.77; rates are theoretical and machine/inserter simulation is approximate.
  `tool` · `TypeScript` · `Dataset 2.0.77 observed; rates approximate` · `checked: web page` · [source](https://github.com/malte9799/FactorioTools)

<a id="factorio-factory-factory"></a>
- **[FactorioFactoryFactory](https://github.com/Barthuijgen/FactorioFactoryFactory)** — Converts FactorioLab CSV production plans into Factorio blueprints, supporting Space Age, Space Exploration, and vanilla 2.0. Does not solve cyclic recipes or generate mining layouts, so treat it as a layout assistant rather than a full factory generator.
  `tool` · `Space Age / Space Exploration / vanilla 2.0 per project docs` · `checked: web page`

<a id="factorio-recipes"></a>
- **[iTitus factorio-recipes](https://github.com/iTitus/factorio-recipes)** — Java tool that parses Factorio recipes and generates ratio graphs. Useful for data exploration and for understanding recipe dependencies outside the game.
  `tool` · `Java` · `checked: GitHub API/README`

<a id="factorio-nuclear-power"></a>
- **[Factorio Nuclear Power Calculator](https://factorio-nuclear-power-plant.netlify.app/)** — Small web calculator for planning Factorio nuclear power plants. Helps estimate reactor, heat exchanger, turbine, and water relationships without building a full production graph.
  `tool` · `TypeScript` · `checked: GitHub API/README` · [source](https://github.com/fangyi-zhou/factorio-nuclear-power)

<a id="machine-ratio-calc"></a>
- **[Factorio Machine Ratio Calculator](https://deniszholob.github.io/factorio-machine-ratio-calc/)** — Focused machine-ratio calculator from the Factorio Cheat Sheet author. Useful for quick assembler/furnace ratio checks when a full production planner is overkill.
  `tool` · `TypeScript` · `checked: GitHub API/README` · [source](https://github.com/deniszholob/factorio-machine-ratio-calc)

<a id="fct-solar-calculator"></a>
- **[FCT Solar / Accumulator Calculator](https://fctostin-team.github.io/solar-accumulator-calculator/)** — Browser calculator for solar panel to accumulator ratios, power output, and storage capacity, with live calculations and locale-aware formatting. Part of the FCT browser tool suite.
  `tool` · `Python` · `checked: web page` · [source](https://github.com/FCTostin-team/solar-accumulator-calculator)

<a id="quality-optimizer"></a>
- **[FactorioQualityOptimizer](https://github.com/scottmsul/FactorioQualityOptimizer)** — Python optimizer for production/quality module ratios when creating high-quality products in Space Age. Useful for comparing quality-loop strategies rather than hand-tuning module mixes.
  `tool` · `Python` · `Space Age quality focus` · `checked: GitHub API/README`

<a id="quality-benchmarker"></a>
- **[Factorio Quality Benchmarker](https://github.com/Max-Hawkins12/Factorio-quality-benchmarker)** — Python graph-optimization tool for discovering resource-efficient and high-throughput legendary item production systems in Space Age. More research-oriented than a typical ratio calculator.
  `tool` · `Python` · `Space Age quality focus` · `checked: GitHub API/README`

<a id="factorio-sat"></a>
- **[Factorio-SAT](https://github.com/R-O-C-K-E-T/Factorio-SAT)** — Applies SAT solvers to Factorio layout and design problems, including belt balancers and other constraint-heavy blueprint generation tasks. A strong example of formal methods applied to factory design.
  `tool` · `Python` · `checked: GitHub API/README`

<a id="factorio-simulation"></a>
- **[FactorioSimulation](https://github.com/d4rkc0d3r/FactorioSimulation)** — C++ simulation tools for Factorio, most notably belt balancer analysis. Useful for testing throughput and deadlock behavior of balancer designs without building them in-game.
  `tool` · `C++` · `checked: GitHub API/README`

<a id="verifactory"></a>
- **[VeriFactory](https://github.com/alegnani/verifactory)** — Rust verifier for Factorio blueprints that checks logical properties automatically. Interesting for advanced users who want stronger guarantees about circuit or layout behavior than visual inspection provides.
  `tool` · `Rust` · `checked: GitHub API/README`

<a id="train-station-creator"></a>
- **[Factorio Train Station Blueprint Creator](https://github.com/BurnySc2/Factorio-Train-Station-Blueprint-Creator)** — TypeScript tool for generating train station blueprints. The older GitHub Pages TrainAcceleration URL returned 404, so use the repository as the canonical entry point and check current release instructions.
  `tool` · `TypeScript` · `checked: GitHub API/README`

<a id="tickthokk-ratio-calculator"></a>
- **[Tickthokk's Ratio Calculator](https://codepen.io/Tickthokk/full/NBbKPZ/)** — Older CodePen-based ratio calculator preserved from the seed list. Useful as a historical reference, but prefer maintained calculators for current game data.
  `tool` · `historical` · `checked: search result`

<a id="factoriocalculator-blog"></a>
- **[factoriocalculator.blog](https://factoriocalculator.blog/)** — Factorio calculator site preserved from the seed list. Verify the current dataset and maintenance status before relying on it for Space Age or quality calculations.
  `tool` · `checked: search result`

<a id="ekimekim-factoriocalc"></a>
- **[ekimekim/factoriocalc](https://github.com/ekimekim/factoriocalc)** — Python production-facility ratio calculator. Useful as a scriptable or historical alternative to browser planners.
  `tool` · `Python` · `checked: GitHub API/README`

<a id="production-flow"></a>
- **[production-flow](https://github.com/windfisch/production-flow)** — C++ graph-based production-flow optimizer for Factorio-like recipe graphs. Useful for research and custom planner experiments.
  `tool` · `C++` · `checked: GitHub API/README`

<a id="beltproblemgecco"></a>
- **[FactorioBeltProblemGECCO](https://github.com/drkenreid/FactorioBeltProblemGECCO)** — Research interface for optimizing Factorio belt layouts, associated with a GECCO paper. Useful for evolutionary-layout experiments rather than everyday play.
  `tool` · `Python` · `checked: GitHub API/README`

## Blueprint sites, editors, and libraries

Blueprint sharing sites, browser editors, string codecs, generators, and in-game blueprint utilities.

<a id="factorioprints"></a>
- **[FactorioPrints](https://factorioprints.com/)** — Long-running community blueprint sharing site with categories, search, and comments. The open-source frontend/backend lives in FactorioBlueprints/factorio-prints; check blueprint descriptions for game-version assumptions.
  `website` · `TypeScript` · `checked: web page` · [source](https://github.com/FactorioBlueprints/factorio-prints)

<a id="factoriocodex"></a>
- **[FactorioCodex](https://www.factoriocodex.com/)** — Blueprint sharing and discovery site with searchable designs and version tags. Useful for finding community layouts, but always inspect the blueprint's stated game version and mod dependencies before importing.
  `website` · `checked: web page`

<a id="factoriobin"></a>
- **[FactorioBin](https://factoriobin.com/)** — Simple blueprint-string pastebin for sharing single blueprints or books. Widely used in forum posts, Discord, and mod documentation because it requires no account for basic sharing.
  `website` · `checked: web page`

<a id="factorio-school"></a>
- **[Factorio School](https://www.factorio.school/)** — Blueprint sharing site that is an alias/alternate front door for FactorioPrints-style community designs. Retained because the seed list included it; prefer the canonical site when linking publicly.
  `website` · `checked: web page`

<a id="factorioblueprints-tech"></a>
- **[factorioblueprints.tech](https://factorioblueprints.tech/)** — Blueprint sharing and management project with a TypeScript monorepo backend. Useful as another community design source and as an open-source example of a blueprint site.
  `website` · `TypeScript` · `checked: web page` · [source](https://github.com/barthuijgen/factorio-sites)

<a id="fbe-factorygamefan"></a>
- **[Factorio Blueprint Editor (FactoryGameFan)](https://fbe.factorygamefan.com/)** — Actively maintained browser blueprint editor with Factorio 2.0 and Space Age support. This is a separate project from the unmaintained teoxoy editor; full rails/trains/mod support is still planned, so verify complex blueprints in-game.
  `tool` · `TypeScript` · `Factorio 2.0 / Space Age; some features still planned` · `checked: web page` · [source](https://github.com/FactoryGameFan/factorio-blueprint-editor)

<a id="fbe-teoxoy"></a>
- **[Factorio Blueprint Editor (teoxoy, unmaintained)](https://fbe.teoxoy.com/)** — Original feature-rich browser blueprint editor. The repository is explicitly unmaintained and the live app errored during verification; use the FactoryGameFan continuation for current work and keep this entry for historical reference.
  `tool` · `TypeScript` · `unmaintained` · `checked: web page` · [source](https://github.com/teoxoy/factorio-blueprint-editor)

<a id="christoph-blueprint-tools"></a>
- **[Christoph Frick's Blueprint Tools](https://christoph-frick.github.io/factorio-blueprint-tools/)** — Browser tools for tiling, splitting, mirroring, landfilling, and otherwise manipulating blueprint strings. Entity-update helpers explicitly target 1.1, so 2.x compatibility is not assumed.
  `tool` · `Clojure` · `Entity update helpers documented for 1.1; 2.x unchecked` · `checked: web page` · [source](https://github.com/christoph-frick/factorio-blueprint-tools)

<a id="piebro-visualizer"></a>
- **[piebro Blueprint Visualizer](https://piebro.github.io/factorio-blueprint-visualizer/)** — Interactive web demo and Python library for rendering Factorio blueprints as stylized visualizations. Useful for documentation, previews, and art-like renders of factory designs.
  `tool` · `JavaScript` · `checked: web page` · [source](https://github.com/piebro/factorio-blueprint-visualizer)

<a id="autotorio"></a>
- **[Autotorio](https://www.autotorio.com/)** — Web suite for generating Factorio blueprints, including outpost and oil layouts. The blueprint and oil generators were live on 2026-10-31, but oil output uses old straight-rail naming, so do not assume current 2.x rail compatibility.
  `tool` · `TypeScript` · `checked: web page` · [source](https://github.com/demipixel/autotorio)

<a id="factorio-draftsman"></a>
- **[factorio-draftsman](https://github.com/redruin1/factorio-draftsman)** — Well-tested Python library for creating, reading, and manipulating Factorio blueprint strings, including modded entities. One of the strongest foundations for custom blueprint generators and ETL pipelines.
  `library` · `Python` · `checked: GitHub API/README`

<a id="demipixel-factorio-blueprint"></a>
- **[demipixel/factorio-blueprint](https://github.com/demipixel/factorio-blueprint)** — TypeScript library for importing and exporting Factorio blueprint strings. Used by Autotorio and useful for Node-based blueprint tools.
  `library` · `TypeScript` · `checked: GitHub API/README`

<a id="jensforstmann-blueprint-tools"></a>
- **[JensForstmann/factorio-blueprint-tools](https://github.com/JensForstmann/factorio-blueprint-tools)** — Fully typed JavaScript/TypeScript library for encoding and decoding Factorio blueprint strings. Good fit for web apps and typed Node tooling.
  `library` · `TypeScript` · `checked: GitHub API/README`

<a id="pierre-dejoue-blueprints"></a>
- **[pierre-dejoue/factorio-blueprints](https://github.com/pierre-dejoue/factorio-blueprints)** — Python module and CLI for managing blueprint exchange strings. Useful for scripting blueprint transformations outside the game.
  `library` · `Python` · `checked: GitHub API/README`

<a id="factorio-fbsr"></a>
- **[Factorio-FBSR](https://github.com/demodude4u/Factorio-FBSR)** — Java Factorio Blueprint String Renderer. Useful for rendering blueprint strings to images in JVM-based tooling; the repository exists even though README fetch returned 404.
  `tool` · `Java` · `checked: GitHub API/README`

<a id="jason-clement-blueprint-tool"></a>
- **[Factorio-Blueprint-Tool](https://github.com/Jason-Clement/Factorio-Blueprint-Tool)** — C# tool for manipulating Factorio blueprints. Useful for .NET developers who want a native blueprint manipulation library or CLI.
  `tool` · `C#` · `checked: GitHub API/README`

<a id="35mt-blueprint-generator"></a>
- **[factorio-blueprint-generator-java](https://github.com/35mt/factorio-blueprint-generator-java)** — Open-source Java blueprint generator for Factorio. Another option for JVM-based procedural layout experiments.
  `tool` · `Java` · `checked: GitHub API/README`

<a id="factorio-blueprint-decoder"></a>
- **[factorio-blueprint-decoder](https://github.com/asheiduk/factorio-blueprint-decoder)** — Python tool that decodes Factorio's binary blueprint-storage.dat into JSON for backup, downgrading, or further manipulation. Important when the in-game blueprint library is not enough.
  `tool` · `Python` · `checked: GitHub API/README`

<a id="whitequark-data-codec"></a>
- **[factorio-data-codec](https://codeberg.org/whitequark/factorio-data-codec)** — Python codec for Factorio data formats, migrated from GitHub to Codeberg. Useful for low-level save/blueprint data experiments; the GitHub repository is archived.
  `library` · `Python` · `archived` · `checked: GitHub API/README`

<a id="blueprint-upgrader"></a>
- **[Factorio Blueprint Upgrader](https://alufers.github.io/factorio-blueprint-upgrader/)** — Browser tool for upgrading entity names in old blueprint strings. Helpful when migrating designs across Factorio versions or mod renames, but always test the result in a copy of your save.
  `tool` · `JavaScript` · `checked: GitHub API/README` · [source](https://github.com/alufers/factorio-blueprint-upgrader)

<a id="fct-blueprint-compression"></a>
- **[FCT Blueprint Compression](https://fctostin-team.github.io/blueprint-code_compression/)** — Browser tool that decodes a blueprint, strips defaults/empty fields, tries pako compression levels, and verifies the output. The site warns to back up blueprints and notes compatibility risks.
  `tool` · `JavaScript` · `checked: web page` · [source](https://github.com/FCTostin-team/blueprint-code_compression)

<a id="fct-blueprint-decoder"></a>
- **[FCT Blueprint Decoder / Encoder](https://fctostin-team.github.io/blueprints-decoder_encoder/)** — Client-side blueprint string decoder/encoder with a CodeMirror JSON editor, search/replace, history, and multilingual UI. Useful for inspecting or hand-editing blueprint JSON without sending data to a server.
  `tool` · `JavaScript` · `checked: web page` · [source](https://github.com/FCTostin-team/blueprints-decoder_encoder)

<a id="fct-book-rich-text"></a>
- **[FCT Blueprint Book Rich Text](https://fctostin-team.github.io/blueprints-book-rich_text/)** — Browser decoder/encoder focused on blueprint book metadata, icons, rich text, and search/replace. Distinct from the general decoder/encoder and useful when polishing shared blueprint books.
  `tool` · `JavaScript` · `checked: web page` · [source](https://github.com/FCTostin-team/blueprints-book-rich_text)

<a id="fct-text-formatter"></a>
- **[FCT Blueprint Text Formatter](https://fctostin-team.github.io/blueprint-text_formatter/)** — Browser text formatter that splits strings into fixed-size chunks for Factorio/Steam guide tables, with normal/tail modes and client-side processing. Useful for publishing blueprint documentation.
  `tool` · `Python` · `checked: web page` · [source](https://github.com/FCTostin-team/blueprint-text_formatter)

<a id="fct-fonts-rich-text"></a>
- **[FCT Fonts / Rich Text Generator](https://fctostin-team.github.io/fonts-online_rich_text/)** — Live-preview generator for Factorio [font] and [color] rich-text tags, with color picker, font selection, and clipboard export. Useful for blueprint book labels, signs, and guide formatting.
  `tool` · `Python` · `checked: web page` · [source](https://github.com/FCTostin-team/fonts-online_rich_text)

<a id="fct-progress-bar"></a>
- **[FCT Progress Bar Display Panel](https://fctostin-team.github.io/progress-bar_display-panel/)** — Blueprint builder for display-panel progress bars with gradient design, live JSON editing, item selection, font choice, and instant blueprint encoding. Useful for factory dashboards and status displays.
  `tool` · `JavaScript` · `checked: web page` · [source](https://github.com/FCTostin-team/progress-bar_display-panel)

<a id="fct-linked-belt"></a>
- **[FCT Linked-Belt Command Generator](https://fctostin-team.github.io/linked-belt/)** — Browser generator for Lua console commands that pair linked-belt entities by tag, with input/output/combined command modes. Useful for map makers and sandbox scenarios; console commands can disable achievements.
  `tool` · `Python` · `checked: web page` · [source](https://github.com/FCTostin-team/linked-belt)

<a id="fct-market-generator"></a>
- **[FCT Market Code Generator](https://fctostin-team.github.io/market-code_generator/)** — Generates Lua /c commands for in-game market entities with quality-aware pricing, discounts, bidirectional trade rows, and a searchable item catalog. Useful for scenario authors and multiplayer economies.
  `tool` · `JavaScript` · `checked: web page` · [source](https://github.com/FCTostin-team/market-code_generator)

<a id="buildasaurus-generator"></a>
- **[Factorio-Blueprint-Generator](https://github.com/Buildasaurus/Factorio-Blueprint-Generator)** — Python tool that automatically designs a blueprint from production requirements. Useful for procedural layout experiments and for studying how recipe graphs can become physical builds.
  `tool` · `Python` · `checked: GitHub API/README`

<a id="spaghetti-generator"></a>
- **[spaghetti_generator](https://github.com/hjpulkki/spaghetti_generator)** — Python tool for generating Factorio blueprints and automating part of the design phase. Repository metadata confirms the project even though README fetch returned 404.
  `tool` · `Python` · `checked: GitHub API/README`

<a id="pumpjack-blueprint"></a>
- **[FactorioPumpjackBlueprint](https://github.com/d4rkc0d3r/FactorioPumpjackBlueprint)** — C# CLI that automatically generates pumpjack outpost blueprints. Useful for oil-field layout experiments; check current entity names before using output in 2.x.
  `tool` · `C#` · `checked: GitHub API/README`

<a id="balancer-book"></a>
- **[raynquist/balancer](https://github.com/raynquist/balancer)** — Community balancer blueprint collection/repository. Useful as a reference for belt-balancer designs, but verify throughput claims with a simulator or in-game test.
  `repository` · `checked: GitHub API/README`

<a id="maxiume-factorio"></a>
- **[MaxiumeGaming/Factorio](https://github.com/MaxiumeGaming/Factorio)** — Community Factorio blueprint/resource repository associated with Maxiume's content. Useful for finding designs shared alongside videos; check game-version notes before importing.
  `repository` · `checked: GitHub API/README`

<a id="rundesballi-blueprints"></a>
- **[RundesBalli/factorio-blueprints](https://github.com/RundesBalli/factorio-blueprints)** — Personal collection of Factorio blueprints published as a repository. Useful for browsing reusable designs in a version-controlled format.
  `repository` · `checked: GitHub API/README`

<a id="deniszholob-blueprints"></a>
- **[deniszholob/factorio-blueprints](https://deniszholob.github.io/factorio-blueprints)** — Browsable personal blueprint collection from the Factorio Cheat Sheet author. Useful for quick reference designs and examples.
  `website` · `checked: GitHub API/README` · [source](https://github.com/deniszholob/factorio-blueprints)

<a id="blueprint-aligner"></a>
- **[Blueprint Aligner](https://mods.factorio.com/mod/blueprint-align)** — In-game mod for setting blueprint grid size and offsets by placing the blueprint in the world. Portal release metadata lists 1.1-2.0; useful for city-block and grid-based factories.
  `mod` · `Lua` · `Factorio 1.1-2.0 per portal release metadata` · `checked: Mod Portal page` · [source](https://github.com/emlun/factorio-blueprint-aligner)

<a id="staged-blueprint-planning"></a>
- **[Staged Blueprint Planning](https://github.com/GlassBricks/StagedBlueprintPlanning)** — Advanced blueprint-planning mod project for staging construction and upgrades. Useful for large factories where a single blueprint cannot be built all at once.
  `mod` · `TypeScript` · `checked: GitHub API/README`

<a id="factorio-blueprinter"></a>
- **[FactorioBlueprinter](https://github.com/Seancheey/FactorioBlueprinter)** — In-game mod that helps create crafting blueprints by selecting inputs and outputs. Useful for turning a production intent into a rough layout without leaving the game.
  `mod` · `Lua` · `checked: GitHub API/README`

<a id="belt-router"></a>
- **[FactorioBeltRouter](https://github.com/Seancheey/FactorioBeltRouter)** — In-game belt and pipe routing mod using A*/Dijkstra-style pathfinding. Useful for connecting buildings automatically, though complex factories still need human review.
  `mod` · `Lua` · `checked: GitHub API/README`

<a id="mining-patch-planner"></a>
- **[Mining Patch Planner](https://mods.factorio.com/mod/mining-patch-planner)** — In-game tool mod that designs mining drill layouts for resource patches. Useful for quickly covering ore patches with power poles, belts, and drills.
  `mod` · `Lua` · `checked: GitHub API/README` · [source](https://github.com/rimbas/mining-patch-planner)

<a id="factorio-builds"></a>
- **[Factorio Builds](https://factorio.tech)** — Community blueprint/build sharing project with a TypeScript frontend. Another discovery source for reusable designs; verify version and mod assumptions before importing.
  `website` · `TypeScript` · `checked: GitHub API/README` · [source](https://github.com/factorio-builds/factorio-builds-tech)

<a id="gaming-tools"></a>
- **[JensForstmann Gaming Tools](https://gaming-tools.jensforstmann.vercel.app)** — Multi-purpose web app for generating or transforming in-game content, including Factorio-related utilities. Useful companion to the author's typed blueprint library.
  `tool` · `TypeScript` · `checked: GitHub API/README` · [source](https://github.com/JensForstmann/gaming-tools)

## Circuit network programming and simulation

Compilers, IDEs, simulators, and display/control mods for building logic inside Factorio.

<a id="verilog2factorio"></a>
- **[Verilog2Factorio](https://redcrafter.github.io/verilog2factorio/)** — Compiles Verilog hardware descriptions into Factorio combinator blueprints, with a live editor/example and an 'Open in FBE' workflow. Useful for building CPUs, controllers, and other digital logic inside Factorio.
  `tool` · `TypeScript` · `checked: web page` · [source](https://github.com/Redcrafter/verilog2factorio)

<a id="cnide"></a>
- **[Cnide - Circuit Network IDE](https://charredutensil.github.io/cnide/)** — Browser IDE for Factorio circuit-network logic. Lets you write and test circuit programs before turning them into combinator builds.
  `tool` · `JavaScript` · `checked: web page` · [source](https://github.com/charredUtensil/cnide)

<a id="combinatorc"></a>
- **[CombinatorC](https://github.com/osimon8/CombinatorC)** — C-style programming language for practical Factorio circuits that compiles into combinator blueprints. Good for engineers who prefer imperative code over wiring diagrams.
  `tool` · `OCaml` · `checked: GitHub API/README`

<a id="factoriogen"></a>
- **[factoriogen](https://github.com/Jobarion/factoriogen)** — Java tool that generates Factorio combinators from code. Another compiler-style approach to circuit construction.
  `tool` · `Java` · `checked: GitHub API/README`

<a id="factompiler"></a>
- **[Factompiler](https://github.com/Snagnar/Factompiler)** — Compiled language for Factorio blueprints, with a live web presence verified during research. Useful for expressing circuit logic in a higher-level language.
  `tool` · `Python` · `checked: web page`

<a id="factorio-state-machine"></a>
- **[factorio-state-machine](https://github.com/aebabis/factorio-state-machine)** — JavaScript project for building state-machine style circuit logic in Factorio. Useful for sequential controllers and automation puzzles.
  `tool` · `JavaScript` · `checked: GitHub API/README`

<a id="factsim"></a>
- **[Factsim](https://github.com/Factsimguru/Factsim)** — Python simulator for Factorio circuit-network entities. Lets you test combinator designs outside the game before committing them to a blueprint.
  `tool` · `Python` · `checked: GitHub API/README`

<a id="factorio-computer"></a>
- **[factorio-computer](https://github.com/justarandomgeek/factorio-computer)** — C# project exploring computer-like circuit constructions in Factorio. Useful for advanced circuit builders and computer-architecture experiments.
  `tool` · `C#` · `checked: GitHub API/README`

<a id="combinatorgraph"></a>
- **[factorio-combinatorgraph](https://github.com/justarandomgeek/factorio-combinatorgraph)** — Tooling around combinator graphs and circuit analysis. Useful for understanding or transforming complex circuit networks.
  `tool` · `checked: GitHub API/README`

<a id="microcontroller-mod"></a>
- **[Microcontroller (FAL)](https://mods.factorio.com/mod/m-microcontroller)** — In-game mod that lets you program circuit-network logic using FAL, a Factorio Assembly Language. Useful for compact programmable controllers without hand-wiring every combinator.
  `mod` · `Lua` · `checked: GitHub API/README` · [source](https://github.com/ZwerOxotnik/m-microcontroller)

<a id="nixie-tubes"></a>
- **[Nixie Tubes](https://mods.factorio.com/mod/nixie-tubes)** — Adds numeric display tubes driven by circuit signals, with support for larger display panels. Portal release 2.1.0 lists Factorio 0.14-2.1; a classic way to make circuit state readable.
  `mod` · `Lua` · `Factorio 0.14-2.1 per portal release metadata` · `checked: Mod Portal page` · [source](https://github.com/justarandomgeek/nixie-tubes)

<a id="pushbutton"></a>
- **[Pushbutton](https://mods.factorio.com/mod/pushbutton)** — Constant-combinator-like button that emits a configured single-tick pulse when toggled. Portal release 2.1.0 lists Factorio 0.14-2.1; useful for manual circuit triggers and control panels.
  `mod` · `Lua` · `Factorio 0.14-2.1 per portal release metadata` · `checked: Mod Portal page` · [source](https://github.com/justarandomgeek/factorio-pushbutton)

## Art, music, maps, and visualization

Image-to-blueprint tools, MIDI music generators, map exporters, timelapse tools, and graphics resources.

<a id="solar-art"></a>
- **[Factorio Solar Art](https://nicokandut.github.io/factorio-solar-art/)** — Converts images into solar-farm blueprints that double as pixel art. The README warns about very large images and transparency edge-power issues, so test small designs first.
  `tool` · `TypeScript` · `checked: web page` · [source](https://github.com/NicoKandut/factorio-solar-art)

<a id="pixel-art-generator"></a>
- **[Factorio Pixel Art Generator](https://nicokandut.github.io/factorio-pixel-art-generator/)** — Image-to-blueprint pixel-art generator with palettes, modded concrete/color coding, comparison/halftoning, upload, and preview. Useful for decorative builds that still behave like real factory tiles.
  `tool` · `Svelte` · `checked: web page` · [source](https://github.com/NicoKandut/factorio-pixel-art-generator)

<a id="factorio-concrete"></a>
- **[factorio-concrete](https://killedkenny.github.io/factorio-concrete/)** — Browser tool for turning images into concrete/tile-based Factorio art. Useful for large ground murals and decorative base areas.
  `tool` · `JavaScript` · `checked: GitHub API/README` · [source](https://github.com/KilledKenny/factorio-concrete)

<a id="artorio"></a>
- **[Artorio](https://github.com/EFLFE/Artorio)** — C# image-to-Factorio-blueprint converter. Useful for desktop pixel-art workflows and batch conversion.
  `tool` · `C#` · `checked: GitHub API/README`

<a id="factorio-art"></a>
- **[factorio-art](https://github.com/ChildishGiant/factorio-art)** — Python CLI for generating pixel-art blueprints from images. Good for scripted or reproducible art builds.
  `tool` · `Python` · `checked: GitHub API/README`

<a id="textplate-gen"></a>
- **[FactorioTextPlateGen](https://github.com/Sv443/FactorioTextPlateGen)** — TypeScript CLI that generates blueprints from text using the Text Plates mod. Useful for signs, labels, and large typographic builds.
  `tool` · `TypeScript` · `checked: GitHub API/README`

<a id="miditorio"></a>
- **[Miditorio](https://miditorio.com/)** — Converts MIDI songs into Factorio blueprints, typically using programmable speakers or circuit-driven music builds. The web app and repository were verified during research.
  `tool` · `TypeScript` · `checked: web page` · [source](https://github.com/mgabor3141/miditorio)

<a id="factorio-composer"></a>
- **[FactorioComposer](https://github.com/khjxiaogu/FactorioComposer)** — MIDI-to-Factorio music blueprint generator. Useful for creating in-game music boxes and speaker arrangements from MIDI files.
  `tool` · `Java` · `checked: GitHub API/README`

<a id="midi-factorio"></a>
- **[Midi-Factorio](https://github.com/RedTopper/Midi-Factorio)** — Java MIDI-to-blueprint converter for Factorio music builds. Another option if you prefer a desktop Java workflow.
  `tool` · `Java` · `checked: GitHub API/README`

<a id="mapshot"></a>
- **[Mapshot](https://github.com/Palats/mapshot)** — Factorio mod/exporter that turns a save into a zoomable HTML map. Excellent for sharing base progress, documenting megabases, and inspecting large factories outside the game.
  `mod` · `Go` · `checked: GitHub API/README`

<a id="factoriomaps-mod"></a>
- **[FactorioMaps (L0laapk3)](https://github.com/L0laapk3/FactorioMaps)** — Mod for generating Google-Maps-style views of a Factorio base. The older factoriomaps.com site is historical; use the repository and mod portal for current instructions.
  `mod` · `Python` · `checked: GitHub API/README`

<a id="tlbe"></a>
- **[TLBE - Time Lapse Base Edition](https://github.com/veger/TLBE)** — In-game timelapse mod that records your base's growth over time. Useful for progression videos and long-term build documentation.
  `mod` · `Lua` · `checked: GitHub API/README`

<a id="replay-timelapse"></a>
- **[factorio-replay-timelapse](https://github.com/emlun/factorio-replay-timelapse)** — Creates timelapses from Factorio replay saves. Useful when you forgot to record video but still have the game's replay data.
  `mod` · `Lua` · `checked: GitHub API/README`

<a id="screenshot-stitcher"></a>
- **[Factorio-Screenshot-Stitcher](https://github.com/nickolasbradham/Factorio-Screenshot-Stitcher)** — Java tool that stitches Factorio screenshots together into larger maps. Useful for high-resolution base posters and documentation.
  `tool` · `Java` · `checked: GitHub API/README`

<a id="unused-renders"></a>
- **[unused-renders](https://github.com/malcolmriley/unused-renders)** — Collection of unused Blender renders made for Factorio mods. Useful for mod authors needing art assets or players interested in Factorio-style rendering.
  `repository` · `checked: GitHub API/README`

<a id="factorio-gfx-tools"></a>
- **[Factorio GFX Tools](https://github.com/wube/Factorio-GFX-tools)** — Official Wube repository storing tools used by the graphics department, with documentation. Useful for mod authors who want to match Factorio's sprite/render pipeline.
  `repository` · `checked: GitHub API/README`

<a id="factorio-lut-tool"></a>
- **[Factorio LUT Tool](https://github.com/wube/factorio-LUT-tool)** — Official Wube lookup-table tool related to Factorio graphics/color processing. Useful for advanced sprite and lighting work.
  `repository` · `checked: GitHub API/README`

<a id="maptorio"></a>
- **[Maptorio](https://github.com/avigad/maptorio)** — Go program that generates Leaflet.js-powered browsable maps from a Factorio save. Useful alternative to Mapshot for self-hosted map publishing.
  `tool` · `Go` · `checked: GitHub API/README`

<a id="giftorio"></a>
- **[Giftorio](https://giftor.io/)** — Rust-based Factorio tool/service discovered through GitHub research. Check the live site and repository for current scope before relying on it.
  `tool` · `Rust` · `checked: GitHub API/README` · [source](https://github.com/colinchilds/giftorio)

<a id="miditool"></a>
- **[miditool](https://github.com/ultrawipf/miditool)** — C MIDI processing tool that can inspect files or generate formats such as Factorio blueprints. Useful for low-level music-build workflows.
  `tool` · `C` · `checked: GitHub API/README`

## Quality-of-life and information mods

Planners, recipe browsers, status displays, task lists, cursor tools, reach tools, and other interface improvements.

<a id="helmod"></a>
- **[Helmod](https://mods.factorio.com/mod/helmod)** — In-game production planner that calculates ingredients, products, machines, modules, beacons, and power for arbitrary modded recipe sets. Portal release 2.3.6 lists Factorio 0.14-2.1 and supports sharing sheets in multiplayer.
  `mod` · `Lua` · `Factorio 0.14-2.1 per portal release metadata` · `checked: Mod Portal page` · [source](https://github.com/Helfima/helmod)

<a id="factory-planner"></a>
- **[Factory Planner](https://mods.factorio.com/mod/factoryplanner)** — In-game production planner with nested subfloors, matrix solving, mining productivity, and UI that adapts to Space Age. Portal release 2.1.21 lists Factorio 0.17-2.1; the project explicitly states full Factorio 2.0 / Space Age compatibility.
  `mod` · `Lua` · `Factorio 0.17-2.1; Space Age supported per project docs` · `checked: Mod Portal page` · [source](https://github.com/ClaudeMetz/FactoryPlanner)

<a id="rate-calculator"></a>
- **[Rate Calculator](https://mods.factorio.com/mod/RateCalculator)** — Select machines in-game to calculate maximum production and consumption rates, including module and beacon effects. Portal release 3.4.2 lists Factorio 1.1-2.1; source has migrated from GitHub to Codeberg.
  `mod` · `Lua` · `Factorio 1.1-2.1 per portal release metadata` · `checked: Mod Portal page` · [source](https://codeberg.org/raiguard/RateCalculator)

<a id="max-rate-calculator"></a>
- **[Max Rate Calculator](https://mods.factorio.com/mod/MaxRateCalculator)** — Selection-tool rate calculator for assemblers, plants, and other machines. Portal release 200.0.53 lists Factorio 0.15-2.0 and explicitly says Space Age is supported but quality is not; idle recyclers can report zero.
  `mod` · `Lua` · `Factorio 0.15-2.0; Space Age yes, quality no per portal description` · `checked: Mod Portal page` · [source](https://github.com/JeffSpindler/Factorio-Mods)

<a id="fnei"></a>
- **[FNEI](https://mods.factorio.com/mod/FNEI)** — Recipe browser that shows how to craft an item/fluid and where it is used, including machines and unlocking technologies. Portal release 0.4.7 lists Factorio 0.15-2.1.
  `mod` · `Lua` · `Factorio 0.15-2.1 per portal release metadata` · `checked: Mod Portal page` · [source](https://github.com/npo6ka/FNEI)

<a id="recipe-book"></a>
- **[Recipe Book](https://mods.factorio.com/mod/RecipeBook)** — Searchable in-game encyclopedia of recipes, items, fluids, entities, and technologies. Portal release 4.0.8 explicitly says '2.0 ONLY' and will not update to 2.1; use FNEI or What Is It Really Used For on newer games.
  `mod` · `Lua` · `legacy` · `Factorio 2.0 only; not 2.1 per portal description` · `checked: Mod Portal page` · [source](https://codeberg.org/raiguard/RecipeBook)

<a id="what-is-it-really-used-for"></a>
- **[What is it really used for?](https://mods.factorio.com/mod/what-is-it-really-used-for)** — Recipe/usage explorer forked from the original 'What is it used for?' and updated for newer Factorio versions. Portal release 1.9.0 lists Factorio 0.15-2.1.
  `mod` · `Lua` · `Factorio 0.15-2.1 per portal release metadata` · `checked: Mod Portal page` · [source](https://github.com/Coppermine-factorio/what-is-it-really-used-for)

<a id="bottleneck"></a>
- **[Bottleneck](https://mods.factorio.com/mod/Bottleneck)** — Adds status lights to assemblers so you can see whether they are starved, blocked, or running. Portal release 0.12.1 lists Factorio 0.13-2.0; for 2.1 consider Bottleneck Lite or Assembly Analyst.
  `mod` · `Lua` · `Factorio 0.13-2.0 per portal release metadata` · `checked: Mod Portal page` · [source](https://github.com/troelsbjerre/Bottleneck)

<a id="bottleneck-lite"></a>
- **[Bottleneck Lite](https://mods.factorio.com/mod/BottleneckLite)** — Lightweight status-light mod for spotting production bottlenecks. Portal release 1.4.1 lists Factorio 1.1-2.1; source has migrated from GitHub to Codeberg.
  `mod` · `Lua` · `Factorio 1.1-2.1 per portal release metadata` · `checked: Mod Portal page` · [source](https://codeberg.org/raiguard/BottleneckLite)

<a id="assembly-analyst"></a>
- **[Assembly Analyst](https://mods.factorio.com/mod/assemblyanalyst)** — Select factory areas to analyze what machines spend time on: active, output full, input empty, low power, or disabled. Portal release 2.1.5 lists Factorio 0.18-2.1; intended for temporary local analysis because zones cost UPS.
  `mod` · `Lua` · `Factorio 0.18-2.1 per portal release metadata` · `checked: Mod Portal page` · [source](https://github.com/ClaudeMetz/AssemblyAnalyst)

<a id="even-distribution"></a>
- **[Even Distribution](https://mods.factorio.com/mod/even-distribution)** — Improves Ctrl+click-drag item distribution and adds inventory cleanup/balancing with fuel/ammo limits. Portal release 2.1.0 lists Factorio 0.15-2.1.
  `mod` · `Lua` · `Factorio 0.15-2.1 per portal release metadata` · `checked: Mod Portal page` · [source](https://github.com/321freddy/even-distribution)

<a id="squeak-through-2"></a>
- **[Squeak Through 2](https://mods.factorio.com/mod/squeak-through-2)** — Highly configurable rewrite of Squeak Through that lets you walk between tightly packed entities and optionally remove collision for selected entities. Portal release 0.2.1 lists Factorio 1.1-2.1.
  `mod` · `Lua` · `Factorio 1.1-2.1 per portal release metadata` · `checked: Mod Portal page` · [source](https://github.com/CodeGreen0386/squeak-through-2)

<a id="squeak-through-original"></a>
- **[Squeak Through (original)](https://mods.factorio.com/mod/Squeak%20Through)** — Original collision-reduction mod that lets you walk between adjacent solar panels, pipes, chests, and other entities. Portal release 1.8.2 stops at Factorio 1.1; use Squeak Through 2 for newer games.
  `mod` · `Lua` · `legacy` · `Factorio 0.13-1.1 only` · `checked: Mod Portal page` · [source](https://github.com/Suprcheese/Squeak-Through)

<a id="far-reach"></a>
- **[Far Reach](https://mods.factorio.com/mod/far-reach)** — Lets you build, interact, mine, and drop items across the visible screen with customizable distances. Portal release 2.1.0 lists Factorio 0.16-2.1 and positions itself as a maintained alternative to Long Reach.
  `mod` · `Factorio 0.16-2.1 per portal release metadata` · `checked: Mod Portal page`

<a id="long-reach"></a>
- **[Long Reach](https://mods.factorio.com/mod/long-reach)** — Older reach-distance mod that lets you build and open chests anywhere visible. Portal release 0.0.14 stops at Factorio 0.18; prefer Far Reach for current games.
  `mod` · `Lua` · `legacy` · `Factorio 0.13-0.18 only` · `checked: Mod Portal page` · [source](https://github.com/Geend/long-reach)

<a id="bright-universe"></a>
- **[Bright Universe](https://mods.factorio.com/mod/afraid-of-the-dark)** — Brightens the player's surroundings without changing planetary day/night cycles or solar power production. Portal release 3.0.0 lists Factorio 2.0-2.1; the old afraid-of-the-dark slug now resolves to this mod.
  `mod` · `Lua` · `Factorio 2.0-2.1 per portal release metadata` · `checked: Mod Portal page` · [source](https://github.com/RedRafe/afraid-of-the-dark)

<a id="lighted-poles-plus"></a>
- **[Lighted Electric Poles +](https://mods.factorio.com/mod/LightedPolesPlus)** — Automatically creates lighted variants of electric poles, including modded poles, with light radius and energy use scaling by wire distance. Portal release 1.10.1 stops at Factorio 1.1.
  `mod` · `Lua` · `legacy` · `Factorio 0.15-1.1 only` · `checked: Mod Portal page` · [source](https://github.com/0ptera/Lighted-Poles-Plus)

<a id="todo-list"></a>
- **[Todo List](https://mods.factorio.com/mod/Todo-List)** — Distributed multiplayer todo list with tasks, subtasks, assignment, and priorities. Portal release 19.15.3 lists Factorio 0.16-2.1.
  `mod` · `Lua` · `Factorio 0.16-2.1 per portal release metadata` · `checked: Mod Portal page` · [source](https://github.com/JonasJurczok/factorio-todo-list)

<a id="task-list"></a>
- **[Task List](https://mods.factorio.com/mod/TaskList)** — Simple unobtrusive task manager with nested subtasks and multiplayer collaboration. Portal release 0.6.0 lists Factorio 1.1-2.1; source is on Codeberg.
  `mod` · `Lua` · `Factorio 1.1-2.1 per portal release metadata` · `checked: Mod Portal page` · [source](https://codeberg.org/raiguard/TaskList)

<a id="module-inserter"></a>
- **[Module Inserter](https://mods.factorio.com/mod/ModuleInserter)** — Bulk-inserts modules into machines using configurable rules. Portal release 5.2.5 stops at Factorio 1.1; for newer games consider Module Inserter Simplified.
  `mod` · `Lua` · `legacy` · `Factorio 0.15-1.1 only` · `checked: Mod Portal page` · [source](https://github.com/Choumiko/ModuleInserter)

<a id="module-inserter-simplified"></a>
- **[Module Inserter Simplified](https://mods.factorio.com/mod/ModuleInserterSimplified)** — Simplified bulk module insertion mod with visible Factorio 2.1 releases in the portal batch check. Check the portal page for exact release metadata before installing.
  `mod` · `2.1 release visible in batch check; exact range not individually recorded` · `checked: Mod Portal batch API`

<a id="yarm"></a>
- **[YARM - Resource Monitor](https://mods.factorio.com/mod/YARM)** — Classic mining-site monitor showing remaining resources and estimated depletion. Portal release 1.0.5 lists Factorio 0.14-2.0; the project itself recommends Resource Monitor as a newer alternative.
  `mod` · `Lua` · `Factorio 0.14-2.0 per portal release metadata` · `checked: Mod Portal page` · [source](https://github.com/narc0tiq/YARM)

<a id="resource-monitor"></a>
- **[Resource Monitor](https://mods.factorio.com/mod/dqol-resource-monitor)** — Modern mining-site monitor with automatic scanning/tracking, map tags, multi-surface support, and YARM import. Portal release 1.7.3 lists Factorio 1.1-2.1 and is designed with Space Exploration and Space Age in mind.
  `mod` · `Lua` · `Factorio 1.1-2.1 per portal release metadata` · `checked: Mod Portal page` · [source](https://github.com/devdot/dqol-resource-monitor)

<a id="auto-deconstruct"></a>
- **[Auto Deconstruct](https://mods.factorio.com/mod/AutoDeconstruct)** — Automatically marks exhausted mining drills for deconstruction so bots return them and their modules to base. Portal release 1.1.2 lists Factorio 0.13-2.1.
  `mod` · `Lua` · `Factorio 0.13-2.1 per portal release metadata` · `checked: Mod Portal page` · [source](https://github.com/softmix/AutoDeconstruct)

<a id="nanobots"></a>
- **[Nanobots](https://mods.factorio.com/mod/Nanobots)** — Early-game ghost construction and logistics automation before conventional robotics. Portal release 3.2.19 stops at Factorio 1.1; the lowercase nanobots slug is invalid.
  `mod` · `Lua` · `legacy` · `Factorio 0.15-1.1 only` · `checked: Mod Portal page` · [source](https://github.com/Nexela/Nanobots)

<a id="vehicle-snap"></a>
- **[VehicleSnap](https://mods.factorio.com/mod/VehicleSnap)** — Snaps vehicle orientation to common angles while driving, making paved roads and rail-like vehicle lanes easier to follow. Portal release 2.0.4 lists Factorio 0.15-2.1.
  `mod` · `Factorio 0.15-2.1 per portal release metadata` · `checked: Mod Portal page`

<a id="pavement-drive-assist"></a>
- **[Pavement Drive Assist Continued](https://mods.factorio.com/mod/PavementDriveAssistContinued)** — Driver assistance that follows paved roads, adds cruise control, speed-limit signs, road sensors, and automated crossing logic. Portal release 5.0.0 lists Factorio 1.1-2.0.
  `mod` · `Lua` · `Factorio 1.1-2.0 per portal release metadata` · `checked: Mod Portal page` · [source](https://github.com/azaghal/Factorio-PavementDriveAssistContinued)

<a id="evogui"></a>
- **[EvoGUI](https://mods.factorio.com/mod/EvoGUI)** — Classic informational GUI for evolution, playtime, and other sensors. Portal release 0.4.601 stops at Factorio 1.1 and is deprecated; the author recommends Stats GUI.
  `mod` · `Lua` · `legacy` · `Factorio 0.14-1.1 only; deprecated` · `checked: Mod Portal page` · [source](https://github.com/narc0tiq/evoGUI)

<a id="stats-gui"></a>
- **[Stats GUI](https://mods.factorio.com/mod/StatsGui)** — Unobtrusive statistics display for research time, evolution, playtime, daytime, and custom mod sensors. Portal release 1.7.0 lists Factorio 1.1-2.1; source is on Codeberg.
  `mod` · `Lua` · `Factorio 1.1-2.1 per portal release metadata` · `checked: Mod Portal page` · [source](https://codeberg.org/raiguard/StatsGui)

<a id="milestones"></a>
- **[Milestones](https://mods.factorio.com/mod/Milestones)** — Tracks production and research milestones such as first rocket, science thresholds, and megabase-scale output. Portal release 1.5.2 lists Factorio 1.1-2.1.
  `mod` · `Lua` · `Factorio 1.1-2.1 per portal release metadata` · `checked: Mod Portal page` · [source](https://github.com/Wiwiweb/FactorioMilestones)

<a id="quick-item-search"></a>
- **[Quick Item Search](https://mods.factorio.com/mod/QuickItemSearch)** — Search inventory and connected logistic networks, set temporary requests, and trash unrequested items. Portal title explicitly says '1.1 ONLY' and will not update to 2.0 because core features are now built in.
  `mod` · `Lua` · `legacy` · `Factorio 0.17-1.1 only; superseded by built-in features` · `checked: Mod Portal page` · [source](https://github.com/raiguard/QuickItemSearch)

<a id="cursor-enhancements"></a>
- **[Cursor Enhancements](https://mods.factorio.com/mod/CursorEnhancements)** — Adds automatic ghost cursor, quick-craft, last-item recall, and subgroup scrolling. Portal release 2.3.1 lists Factorio 1.0-2.1; source has migrated to Codeberg.
  `mod` · `Lua` · `Factorio 1.0-2.1 per portal release metadata` · `checked: Mod Portal page` · [source](https://codeberg.org/raiguard/CursorEnhancements)

<a id="tapeline"></a>
- **[Tapeline](https://mods.factorio.com/mod/Tapeline)** — Draw temporary or persistent measurements, subgrids, and split layouts for precise factory planning. Portal release 3.1.1 lists Factorio 0.17-2.1; source is on Codeberg.
  `mod` · `Lua` · `Factorio 0.17-2.1 per portal release metadata` · `checked: Mod Portal page` · [source](https://codeberg.org/raiguard/Tapeline)

<a id="pipe-visualizer"></a>
- **[Pipe Visualizer](https://mods.factorio.com/mod/PipeVisualizer)** — Visualizes pipe-network layout and fluid contents with hotkeys and hover mode. Portal title explicitly says '1.1 ONLY' and will not update to 2.0 because the feature is built into the game.
  `mod` · `Lua` · `legacy` · `Factorio 1.1 only; superseded by built-in features` · `checked: Mod Portal page` · [source](https://github.com/raiguard/PipeVisualizer)

<a id="belt-visualizer"></a>
- **[Belt Visualizer](https://mods.factorio.com/mod/belt-visualizer)** — Highlights connected belt lines and cycles between lanes, including sideloading and modded belt connectables. Portal release 2.1.4 lists Factorio 1.1-2.1; lane-splitter support is still limited in 2.0+.
  `mod` · `Lua` · `Factorio 1.1-2.1 per portal release metadata; lane splitters limited` · `checked: Mod Portal page` · [source](https://github.com/CodeGreen0386/belt-visualizer)

<a id="spidertron-enhancements"></a>
- **[Spidertron Enhancements](https://mods.factorio.com/mod/SpidertronEnhancements)** — Quality-of-life improvements for spidertrons: enter vehicles without leaving, quick toggle, remote pathfinding, inventory sorting, remote pipette, and corpse inventory preservation. Portal release 1.11.0 lists Factorio 1.0-2.1.
  `mod` · `Lua` · `Factorio 1.0-2.1 per portal release metadata` · `checked: Mod Portal page` · [source](https://github.com/tburrows13/SpidertronEnhancements)

<a id="spidertron-patrols"></a>
- **[Spidertron Patrols](https://mods.factorio.com/mod/SpidertronPatrols)** — Adds waypoint patrols, docks that share spidertron inventory with inserters, and an earlier spiderling. Portal release 2.7.1 lists Factorio 1.1-2.1; requires Spidertron Enhancements.
  `mod` · `Lua` · `Factorio 1.1-2.1 per portal release metadata` · `checked: Mod Portal page` · [source](https://github.com/tburrows13/SpidertronPatrols)

<a id="constructron"></a>
- **[Spidertron Automation (Constructron Continued)](https://mods.factorio.com/mod/Constructron-Continued)** — Automates spidertrons for construction, deconstruction, repair, upgrades, logistics requests, and combat using real logistic-network items. Portal release 2.1.0 lists Factorio 1.1-2.1.
  `mod` · `Lua` · `Factorio 1.1-2.1 per portal release metadata` · `checked: Mod Portal page` · [source](https://github.com/ILLISIS/Constructron-continued)

<a id="factory-search"></a>
- **[Factory Search](https://mods.factorio.com/mod/FactorySearch)** — Searches your factory for machines, recipes, items, and other entities. Useful for locating production blocks in large or heavily modded bases.
  `mod` · `Lua` · `checked: GitHub API/README` · [source](https://github.com/tburrows13/FactorySearch)

<a id="shortcuts-ick"></a>
- **[Shortcuts](https://mods.factorio.com/mod/Shortcuts-ick)** — Adds configurable shortcuts for equipment toggles, logistics requests, artillery, environment deconstruction, vehicle/train controls, rail visualization, grid overlay, and more. Portal release 2.1.0 lists Factorio 0.18-2.1.
  `mod` · `Lua` · `Factorio 0.18-2.1 per portal release metadata` · `checked: Mod Portal page` · [source](https://github.com/ickputzdirwech/Shortcuts-ick)

<a id="qol-research"></a>
- **[Quality of Life research](https://mods.factorio.com/mod/qol_research)** — Adds configurable research or direct bonuses for inventory size, crafting speed, mining speed, movement speed, and reach. Portal release 3.4.4 lists Factorio 0.15-2.1.
  `mod` · `Lua` · `Factorio 0.15-2.1 per portal release metadata` · `checked: Mod Portal page` · [source](https://github.com/Aidiakapi/qol_research)

<a id="attach-notes"></a>
- **[Attach Notes](https://mods.factorio.com/mod/attach-notes)** — Attach notes to entities and combinators, plus signposts; notes can travel with blueprint strings when the mod is installed. Portal release 0.5.1 stops at Factorio 1.1.
  `mod` · `Lua` · `legacy` · `Factorio 0.16-1.1 only` · `checked: Mod Portal page` · [source](https://github.com/321freddy/attach-notes)

<a id="change-map-settings"></a>
- **[Change Map Settings](https://mods.factorio.com/mod/ChangeMapSettings)** — Lets you change map and map-generation settings after a game has started; generation changes apply only to new chunks. Portal release 5.0.1 stops at Factorio 1.1.
  `mod` · `Lua` · `legacy` · `Factorio 0.15-1.1 only` · `checked: Mod Portal page` · [source](https://github.com/Bilka2/ChangeMapSettings)

<a id="tree-collision"></a>
- **[Tree Collision](https://mods.factorio.com/mod/tree_collision)** — Shrinks tree collision boxes so you can traverse dense forests; biters also pass through more easily. Portal release 2.0.0 lists Factorio 0.13-2.0.
  `mod` · `Factorio 0.13-2.0 per portal release metadata` · `checked: Mod Portal page`

<a id="cleaned-concrete"></a>
- **[Cleaned Concrete](https://mods.factorio.com/mod/CleanedConcrete)** — Removes visual clutter from concrete and refined concrete for cleaner factory floors. A visible Factorio 2.1 release appeared in the portal batch check; verify exact release metadata on the portal page.
  `mod` · `2.1 release visible in batch check; exact range not individually recorded` · `checked: Mod Portal batch API`

<a id="waterfill"></a>
- **[Waterfill](https://mods.factorio.com/mod/Waterfill_v17)** — Adds landfill-like water placement for canals, moats, and terrain editing. A visible Factorio 2.1 release appeared in the portal batch check; verify exact release metadata on the portal page.
  `mod` · `2.1 release visible in batch check; exact range not individually recorded` · `checked: Mod Portal batch API`

<a id="grappling-gun"></a>
- **[Grappling Gun](https://mods.factorio.com/mod/grappling-gun)** — Fire a grapple to pull yourself across buildings, water, or back to a space station in Space Exploration. Portal release 0.5.0 lists Factorio 0.17-2.1.
  `mod` · `Factorio 0.17-2.1 per portal release metadata` · `checked: Mod Portal page`

<a id="jetpack"></a>
- **[Jetpack](https://mods.factorio.com/mod/jetpack)** — Adds fuel-consuming jetpack equipment for flying over buildings and water, with multiple tiers and Space Exploration integration. Portal release 0.5.1 lists Factorio 0.18-2.1.
  `mod` · `Factorio 0.18-2.1 per portal release metadata` · `checked: Mod Portal page`

<a id="quickbar-import-export"></a>
- **[Quickbar Import/Export](https://mods.factorio.com/mod/quickbarimportexport)** — Export and import quickbar layouts between saves. Useful when restarting maps or sharing standardized hotbar setups.
  `mod` · `Lua` · `checked: GitHub API/README` · [source](https://github.com/ClaudeMetz/QuickbarImportExport)

<a id="resource-marker"></a>
- **[Resource Marker](https://mods.factorio.com/mod/resourceMarker)** — Mod for marking resource patches on the map. Useful for exploration-heavy or train-focused games.
  `mod` · `Lua` · `checked: GitHub API/README` · [source](https://github.com/abaines/resource-marker)

<a id="gridlines"></a>
- **[Gridlines](https://mods.factorio.com/mod/gridlines)** — Customizable grid overlay for precise building layouts. Useful for city-block, rail-grid, and modular factory designs.
  `mod` · `TypeScript` · `checked: GitHub API/README` · [source](https://github.com/canisminor1990/factorio-gridlines)

<a id="colorblind-ultimate"></a>
- **[Colorblind Ultimate](https://mods.factorio.com/mod/colorblind_ultimate)** — Accessibility mod adding extensive colorblind options for Factorio. Useful for players who need stronger color differentiation than vanilla provides.
  `mod` · `Lua` · `checked: GitHub API/README` · [source](https://github.com/rycieos/factorio-colorblind-ultimate)

<a id="gun-turret-alerts"></a>
- **[Gun Turret Alerts](https://mods.factorio.com/mod/Gun_Turret_Alerts)** — Adds map alerts when gun turrets, vehicles, or artillery are low on ammo or out of ammo. Useful for defensive maintenance in large bases.
  `mod` · `Lua` · `checked: GitHub API/README` · [source](https://github.com/wyrrrd/gun_turret_alerts)

## Logistics, trains, storage, and production mods

Train dispatchers, vehicles, drones, loaders, warehouses, and logistics infrastructure.

<a id="ltn"></a>
- **[LTN - Logistic Train Network](https://mods.factorio.com/mod/LogisticTrainNetwork)** — Circuit-driven train logistics network that dispatches trains between provider and requester stations. Portal release 3.4.2 lists Factorio 1.1-2.1; the portal cites hgschmie/factorio-LogisticTrainNetwork while the older Yousei9 repository redirects to 0ptera.
  `mod` · `Lua` · `Factorio 1.1-2.1 per portal release metadata` · `checked: Mod Portal page` · [source](https://github.com/hgschmie/factorio-LogisticTrainNetwork)

<a id="cybersyn"></a>
- **[Project Cybersyn](https://mods.factorio.com/mod/cybersyn)** — Feature-rich train logistics network using cybernetic combinators, vanilla train limits, depots, and station thresholds. Portal release 2.1.3 lists Factorio 1.1-2.1, but the project explicitly says 2.1 support is still experimental.
  `mod` · `Lua` · `Factorio 1.1-2.1 listed; 2.1 experimental per project docs` · `checked: Mod Portal page` · [source](https://github.com/mamoniot/project-cybersyn)

<a id="cargo-ships"></a>
- **[Cargo Ships](https://mods.factorio.com/mod/cargo-ships)** — Adds waterways, ports, buoys, cargo ships, tankers, and boats that behave like waterborne trains. Portal release 2.1.8 lists Factorio 0.16-2.1; in 2.1 oil rigs and floating electric poles are separate mods and old saves need a 2.0 migration step.
  `mod` · `Lua` · `Factorio 0.16-2.1 per portal release metadata; 2.1 split mods and migration caveats` · `checked: Mod Portal page` · [source](https://github.com/robot256/cargo_ships)

<a id="aai-programmable-vehicles"></a>
- **[AAI Programmable Vehicles](https://mods.factorio.com/mod/aai-programmable-vehicles)** — Turns vehicles into RTS-style units controlled by remotes, circuit conditions, zones, and unit data. Portal release 0.9.2 lists Factorio 0.14-2.1; the project still describes itself as alpha.
  `mod` · `Factorio 0.14-2.1 per portal release metadata; alpha status per project docs` · `checked: Mod Portal page`

<a id="aai-vehicles-miner"></a>
- **[AAI Vehicles: Miner](https://mods.factorio.com/mod/aai-vehicles-miner)** — Mobile mining vehicles that harvest solid resources and trees, can burn collected wood, and can operate autonomously with AAI Programmable Vehicles. Portal release 0.8.0 lists Factorio 0.14-2.1.
  `mod` · `Factorio 0.14-2.1 per portal release metadata` · `checked: Mod Portal page`

<a id="mining-drones-remastered"></a>
- **[Mining Drones Remastered](https://mods.factorio.com/mod/Mining_Drones_Remastered)** — Configurable mining drones and depots with editable recipes, pollution, energy use, stack sizes, and broad mod compatibility. Portal release 2.3.0 lists Factorio 1.1-2.1 and documents Space Age/Quality behavior.
  `mod` · `Lua` · `Factorio 1.1-2.1 per portal release metadata` · `checked: Mod Portal page` · [source](https://github.com/AivanF/factorio-Mining-Drones-Remastered)

<a id="warehousing"></a>
- **[Warehousing](https://mods.factorio.com/mod/Warehousing)** — Adds 6x6 warehouses and 3x3 storehouses, including logistic variants and circuit connections. Portal release 1.1.0 lists Factorio 0.14-2.1; the lowercase warehousing slug is invalid.
  `mod` · `Lua` · `Factorio 0.14-2.1 per portal release metadata` · `checked: Mod Portal page` · [source](https://github.com/Warehousing/Warehousing)

<a id="aai-containers"></a>
- **[AAI Containers & Warehouses](https://mods.factorio.com/mod/aai-containers)** — Adds chest, strongbox, storehouse, and warehouse sizes with logistic and non-logistic variants and tintable masks. Portal release 0.4.0 lists Factorio 1.0-2.1.
  `mod` · `Factorio 1.0-2.1 per portal release metadata` · `checked: Mod Portal page`

<a id="miniloader"></a>
- **[Miniloader](https://mods.factorio.com/mod/miniloader)** — UPS-friendly 1x1 pseudo-loaders for chests and train wagons, implemented with hidden inserters rather than per-tick Lua. Portal release 1.15.7 stops at Factorio 1.1.
  `mod` · `Lua` · `legacy` · `Factorio 0.15-1.1 only` · `checked: Mod Portal page` · [source](https://github.com/mspielberg/factorio-miniloader)

<a id="loader-redux"></a>
- **[Loader Redux](https://mods.factorio.com/mod/LoaderRedux)** — Adds vanilla-style loaders with snapping and modded belt support. Check the portal page for current release metadata; useful when you want loader behavior without the hidden-inserter approach of Miniloader.
  `mod` · `Lua` · `checked: GitHub API/README` · [source](https://github.com/0ptera/Loader-Redux)

<a id="farl"></a>
- **[FARL - Fully Automated Rail Layer](https://mods.factorio.com/mod/FARL)** — Automated rail-laying train that places rails, signals, and stations while driving. Portal release 4.1.2 stops at Factorio 1.1.
  `mod` · `Lua` · `legacy` · `Factorio 0.14-1.1 only` · `checked: Mod Portal page` · [source](https://github.com/Choumiko/FARL)

<a id="disco-science"></a>
- **[Disco Science](https://mods.factorio.com/mod/DiscoScience)** — Makes labs cycle through colorful science-pack animations so research activity is visible at a glance. A visible Factorio 2.1 release appeared in the portal batch check; verify exact release metadata on the portal page.
  `mod` · `Lua` · `2.1 release visible in batch check; exact range not individually recorded` · `checked: Mod Portal batch API` · [source](https://github.com/danielbrauer/DiscoScience)

<a id="automatic-train-repair"></a>
- **[Automatic Train Repair](https://mods.factorio.com/mod/ick-automatic-train-repair)** — Stops destroyed trains and creates ghosts preserving filters, limits, fuel, and equipment where possible. Useful for biter-heavy rail networks.
  `mod` · `Lua` · `checked: GitHub API/README` · [source](https://github.com/ickputzdirwech/ick-automatic-train-repair)

<a id="ltn-tracker"></a>
- **[LTN Tracker](https://github.com/eduran84/ltn_tracker)** — Companion tracking tool/mod for Logistic Train Network. Useful for debugging LTN deliveries and station state; verify compatibility with your LTN version.
  `mod` · `Lua` · `checked: GitHub API/README`

<a id="se-ltn-glue"></a>
- **[SE-LTN Glue](https://mods.factorio.com/mod/se-ltn-glue)** — Connects LTN's cross-surface API with Space Exploration's space elevator so deliveries can move between surfaces. Useful for SE+LTN megabases.
  `mod` · `Lua` · `checked: GitHub API/README` · [source](https://github.com/harag-on-steam/se-ltn-glue)

## World, decoration, combat, and power mods

Terrain, biomes, decoration, visual effects, combat changes, and alternative power systems.

<a id="rso"></a>
- **[Resource Spawner Overhaul](https://mods.factorio.com/mod/rso-mod)** — Region-based resource spawning that makes patches sparser and richer farther from start, encouraging earlier train logistics. Portal release 7.1.4 lists Factorio 0.14-2.1; RSO does not appear in map preview and is not recommended for Pyanodons.
  `mod` · `Factorio 0.14-2.1 per portal release metadata` · `checked: Mod Portal page`

<a id="dectorio"></a>
- **[Dectorio](https://mods.factorio.com/mod/Dectorio)** — Large decoration pack with colored signals, walls, floors, painted concrete, landscaping, lamps, and configurable feature toggles. Portal release 0.13.1 lists Factorio 0.15-2.0; back up saves before disabling components.
  `mod` · `Lua` · `Factorio 0.15-2.0 per portal release metadata` · `checked: Mod Portal page` · [source](https://github.com/jpanther/dectorio)

<a id="text-plates"></a>
- **[Text Plates](https://mods.factorio.com/mod/textplates)** — Metal letters, numbers, arrows, and symbols for signs and labels, in iron/copper and small/large variants. Portal release 0.8.0 lists Factorio 0.14-2.1.
  `mod` · `Factorio 0.14-2.1 per portal release metadata` · `checked: Mod Portal page`

<a id="alien-biomes"></a>
- **[Alien Biomes](https://mods.factorio.com/mod/alien-biomes)** — Adds snow, volcanic, crater, dirt, sand, grass, shallow water, and new vegetation with planet climate controls. Portal release 0.8.0 lists Factorio 0.14-2.1; with Space Age only Nauvis is affected.
  `mod` · `Factorio 0.14-2.1 per portal release metadata; Space Age affects Nauvis only` · `checked: Mod Portal page`

<a id="bullet-trails"></a>
- **[Bullet Trails](https://mods.factorio.com/mod/bullet-trails)** — Adds visible trails to machine-gun-style bullets from turrets, personal weapons, and vehicles. Portal release 0.8.0 lists Factorio 0.14-2.1.
  `mod` · `Factorio 0.14-2.1 per portal release metadata` · `checked: Mod Portal page`

<a id="tile-painter"></a>
- **[Tile Painter](https://mods.factorio.com/mod/tile-painter)** — Paint or ghost tiles around selected entities or geometric shapes, with presets and import/export. Portal release 2.1.0 lists Factorio 1.1-2.1; large selections can cause lag spikes.
  `mod` · `Lua` · `Factorio 1.1-2.1 per portal release metadata` · `checked: Mod Portal page` · [source](https://github.com/Caleb-Wishart/tile-painter)

<a id="abandoned-ruins"></a>
- **[Abandoned Ruins](https://mods.factorio.com/mod/AbandonedRuins)** — Adds generated factory ruins to the map for exploration and salvage. Useful for players who want the world to feel previously industrialized.
  `mod` · `Lua` · `checked: GitHub API/README` · [source](https://github.com/Bilka2/AbandonedRuins)

<a id="rampant"></a>
- **[Rampant](https://mods.factorio.com/mod/Rampant)** — AI augmentation for biters using potential fields and more aggressive attack behavior. Check the portal page for current compatibility before adding it to a long-running save.
  `mod` · `Lua` · `checked: GitHub API/README` · [source](https://github.com/veden/Rampant)

<a id="total-automization"></a>
- **[Total Automization](https://mods.factorio.com/mod/Total_Automization)** — Adds RTS-style units and deployment machines from Klonan's experiments. Useful for players who want combat automation beyond vanilla spidertrons.
  `mod` · `Lua` · `checked: GitHub API/README` · [source](https://github.com/Klonan/Total_Automization)

<a id="factorissimo2"></a>
- **[Factorissimo2](https://mods.factorio.com/mod/Factorissimo2)** — Adds factory buildings that contain interior factory floors, letting you compact large production blocks. Check the portal page for the exact lineage and current compatibility; Factorissimo 3 is a separate continuation.
  `mod` · `Lua` · `checked: GitHub API/README` · [source](https://github.com/MagmaMcFry/Factorissimo2)

<a id="advanced-electric"></a>
- **[Advanced Electric](https://mods.factorio.com/mod/Advanced-Electric-Revamped-v16)** — Adds higher tiers of solar panels and accumulators to make power farms more space-efficient. Check the portal page for current release metadata before using in 2.x.
  `mod` · `Lua` · `checked: GitHub API/README` · [source](https://github.com/LsHallo/advanced-electric)

<a id="concentrated-solar"></a>
- **[Cheese's Concentrated Solar](https://mods.factorio.com/mod/ch-concentrated-solar)** — Adds concentrated solar power mechanics as an alternative to large photovoltaic fields. Useful for players who want a different power-layout challenge.
  `mod` · `Lua` · `checked: GitHub API/README` · [source](https://github.com/pettett/ch-concentrated-solar)

<a id="moshine"></a>
- **[Moshine](https://mods.factorio.com/mod/Moshine)** — Space Age planet mod adding a hot desert world rich in metals and computational science opportunities. Check dependencies and compatibility with other planet mods before starting a run.
  `mod` · `Lua` · `Space Age planet mod` · `checked: GitHub API/README` · [source](https://github.com/snouz/Moshine)

<a id="reskins-bobs"></a>
- **[Artisanal Reskins: Bob's Mods](https://mods.factorio.com/mod/reskins-bobs)** — High-resolution tier-colored reskins for Bob's mods and several related logistics mods. Useful when you want Bob's complexity with clearer visual tiering.
  `mod` · `Lua` · `checked: GitHub API/README` · [source](https://github.com/kirazy/reskins-bobs)

<a id="power-overload"></a>
- **[Power Overload](https://mods.factorio.com/mod/PowerOverload)** — Power-distribution overhaul that adds overload and grid-management challenges. Useful for players who want electricity to require more planning.
  `mod` · `Lua` · `checked: GitHub API/README` · [source](https://github.com/tburrows13/poweroverload)

<a id="fluidic-power"></a>
- **[Fluidic Power](https://mods.factorio.com/mod/FluidicPower)** — Simulates electricity as a fluid using Factorio's fluid system, making power generation and distribution more physical. Experimental and performance-sensitive.
  `mod` · `Lua` · `experimental` · `checked: GitHub API/README` · [source](https://github.com/heinwessels/factorio-fluidicpower)

<a id="portals"></a>
- **[Portals](https://mods.factorio.com/mod/Portals)** — Bilka's portal-gun mod with linked portals and combustible lemons. Useful for compact transport puzzles and playful base logistics.
  `mod` · `Lua` · `checked: GitHub API/README` · [source](https://github.com/Bilka2/Portals)

<a id="ruin-maker"></a>
- **[Ruin Maker](https://mods.factorio.com/mod/ruin-maker)** — Tool for generating ruin files for The Ruins Mod from in-game selections. Useful for players and scenario authors creating custom abandoned factories.
  `mod` · `Lua` · `checked: GitHub API/README` · [source](https://github.com/Bilka2/ruin-maker)

## Overhauls and challenge modpacks

Large total conversions and challenge packs. Compatibility notes are especially important here; many overhauls are mutually exclusive.

<a id="atomic-overhaul"></a>
- **[Atomic Overhaul](https://mods.factorio.com/mod/Atomic_Overhaul)** — Overhaul focused on nuclear technology and atomic-era progression. Check the portal page for current compatibility and dependency requirements.
  `mod` · `Lua` · `checked: GitHub API/README` · [source](https://github.com/Xman1109/Atomic_Overhaul)

<a id="5dims"></a>
- **[5Dim's Mods](https://mods.factorio.com/user/McGuten)** — Family of modular expansion mods covering modules, logistics, power, warfare, automation, and more. The seed slug bobsmods was invalid for Bob's mods; 5Dim's is a separate family and should be installed as individual components.
  `mod` · `Lua` · `checked: GitHub API/README` · [source](https://github.com/McGuten/Factorio5DimMods)

<a id="krastorio2"></a>
- **[Krastorio 2](https://mods.factorio.com/mod/Krastorio2)** — Moderate-complexity overhaul with new buildings, resources, tech cards, combat, equipment, and endgame technologies. Portal release 2.1.4 lists Factorio 0.18-2.1, but the project explicitly says Space Age progression is broken without an add-on such as Krastorio 2 Spaced Out.
  `mod` · `Lua` · `Factorio 0.18-2.1 listed; Space Age requires add-on per project docs` · `checked: Mod Portal page` · [source](https://codeberg.org/raiguard/Krastorio2)

<a id="krastorio2-spaced-out"></a>
- **[Krastorio 2 Spaced Out](https://mods.factorio.com/mod/Krastorio2-spaced-out)** — Space Age overhaul merging Krastorio 2 with planetary progression, data-based research, advanced tech cards, matter transmutation, and singularity science. Portal release 2.0.19 lists Factorio 2.0-2.1; the project says 2.1 is preferable and 2.0 will not receive fixes.
  `mod` · `Lua` · `Factorio 2.0-2.1 / Space Age; 2.1 preferred per project docs` · `checked: Mod Portal page` · [source](https://github.com/Polka37/Krastorio2-Spaced-Out)

<a id="space-exploration"></a>
- **[Space Exploration](https://mods.factorio.com/mod/space-exploration)** — Long-form space overhaul with orbital stations, spaceships, planets, moons, asteroid belts, and 29 science packs. Portal release 0.7.64 lists Factorio 0.17-2.1, but the project still labels itself experimental/alpha and says 0.7.x targets Factorio 2.0.
  `mod` · `experimental` · `Factorio 0.17-2.1 listed; 0.7.x targets 2.0; experimental per project docs` · `checked: Mod Portal page`

<a id="industrial-revolution3"></a>
- **[Industrial Revolution 3](https://mods.factorio.com/mod/IndustrialRevolution3)** — Material-progression overhaul with steam/burner early game, new materials, specialist furnaces, cryogenics, forestry, and hundreds of original sprites. Portal release 3.1.30 is Factorio 1.1 only.
  `mod` · `legacy` · `Factorio 1.1 only` · `checked: Mod Portal page`

<a id="seablock-pack"></a>
- **[Sea Block Pack - Official](https://mods.factorio.com/mod/SeaBlockPack)** — Current official Sea Block modpack lineage for starting on a small island and generating resources from water, algae, and sludge. Portal release 1.1.2 lists Factorio 2.0-2.1 and points to codeberg.org/wanne/SeaBlockPack; distinct from the original 1.1 SeaBlock mod.
  `mod` · `Factorio 2.0-2.1 per portal release metadata` · `checked: Mod Portal page` · [source](https://codeberg.org/wanne/SeaBlockPack)

<a id="seablock-original"></a>
- **[Sea Block (original)](https://mods.factorio.com/mod/SeaBlock)** — Original island-start overhaul with no ore patches, algae farms, and sludge filtering. Portal release 0.5.16 stops at Factorio 1.1; use Sea Block Pack for the current 2.x lineage.
  `mod` · `Lua` · `legacy` · `Factorio 0.14-1.1 only` · `checked: Mod Portal page` · [source](https://github.com/modded-factorio/SeaBlock)

<a id="nullius"></a>
- **[Nullius](https://mods.factorio.com/mod/nullius)** — Terraforming prequel where an android builds industry from air, seawater, and common minerals before seeding life. Portal release 2.1.3 lists Factorio 1.1-2.1; the lowercase slug is canonical.
  `mod` · `Lua` · `Factorio 1.1-2.1 per portal release metadata` · `checked: Mod Portal page` · [source](https://github.com/GregorSamsanite/nullius)

<a id="pyanodons"></a>
- **[Pyanodons Modpack](https://mods.factorio.com/mod/pymodpack)** — Official pY modpack bundling the extremely complex Pyanodon suite with thousands of recipes and very long playthroughs. Portal release 3.1.0 lists Factorio 2.0-2.1 and describes partial Space Age support; do not combine casually with other overhauls.
  `mod` · `Factorio 2.0-2.1; partial Space Age support per portal description` · `checked: Mod Portal page` · [source](https://github.com/pyanodon/pymodpack)

<a id="py-coal-processing"></a>
- **[Pyanodons Coal Processing](https://mods.factorio.com/mod/pycoalprocessing)** — Core pY mod that overhauls the burner phase with coal/oil chemistry, ash, tar, coke, and new resources. Portal release 3.1.8 lists Factorio 1.1-2.1; the project says it is not compatible with other major overhauls and does not recommend RSO.
  `mod` · `Lua` · `Factorio 1.1-2.1 per portal release metadata` · `checked: Mod Portal page` · [source](https://github.com/pyanodon/pycoalprocessing)

<a id="bobs-mods"></a>
- **[Bob's Mods](https://mods.factorio.com/user/Bobingabout)** — Classic modular overhaul family covering metals, chemicals, electronics, logistics, power, warfare, and more. There is no single bobsmods portal slug; install individual Bob's components. The current source organization is modded-factorio/bobsmods.
  `mod` · `Lua` · `checked: GitHub API/README` · [source](https://github.com/modded-factorio/bobsmods)

<a id="bob-plates"></a>
- **[Bob's Metals, Chemicals and Intermediates](https://mods.factorio.com/mod/bobplates)** — Core Bob's materials mod adding expanded metals, chemicals, and intermediates. Portal release 3.0.2 lists Factorio 0.13-2.1; often combined with Angel's mods for Bob-Angel playthroughs.
  `mod` · `Factorio 0.13-2.1 per portal release metadata` · `checked: Mod Portal page`

<a id="angels-refining"></a>
- **[Angel's Refining](https://mods.factorio.com/mod/angelsrefining)** — Replaces ore patches with compound ores that must be refined before smelting, with vanilla and Bob-Angel modes. Portal release 2.1.3 lists Factorio 0.14-2.1.
  `mod` · `Lua` · `Factorio 0.14-2.1 per portal release metadata` · `checked: Mod Portal page` · [source](https://github.com/Arch666Angel/mods)

<a id="angels-petrochem"></a>
- **[Angel's Petrochemical Processing](https://mods.factorio.com/mod/angelspetrochem)** — Overhauls oil and gas processing into a much larger chemical production web, with Bob's integration. Portal release 2.1.3 lists Factorio 0.14-2.1; requires Angel's Refining.
  `mod` · `Lua` · `Factorio 0.14-2.1 per portal release metadata` · `checked: Mod Portal page` · [source](https://github.com/Arch666Angel/mods)

<a id="angels-smelting"></a>
- **[Angel's Smelting](https://mods.factorio.com/mod/angelssmelting)** — Adds advanced metallurgy and alternative plate-production chains that trade space and energy for higher ore yield. Portal release 2.1.1 lists Factorio 0.14-2.1.
  `mod` · `Lua` · `Factorio 0.14-2.1 per portal release metadata` · `checked: Mod Portal page` · [source](https://github.com/Arch666Angel/mods)

<a id="ultracube"></a>
- **[Ultracube: Age of Cube](https://mods.factorio.com/mod/Ultracube)** — Logistics-puzzle overhaul built around a single non-craftable utility cube that must be routed through critical processes. Portal range says 1.1-2.1, but the description explicitly says Factorio 2.0 only and incompatible with Space Age/Quality; preserve that conflict when choosing a version.
  `mod` · `Lua` · `Portal range 1.1-2.1 conflicts with prose: 2.0 only, no Space Age/Quality` · `checked: Mod Portal page` · [source](https://github.com/grandseiken/factorio-ultracube)

<a id="warptorio2"></a>
- **[Warptorio2](https://mods.factorio.com/mod/warptorio2)** — Original canonical Warptorio continuation where your factory lives on a warping platform and must survive repeated relocations. Portal release 1.3.10 stops at Factorio 1.1; the uppercase Warptorio2 slug is invalid.
  `mod` · `Lua` · `legacy` · `Factorio 0.17-1.1 only` · `checked: Mod Portal page` · [source](https://github.com/PyroFire232/warptorio2)

<a id="warptorio-space-age"></a>
- **[Warptorio: Space Age](https://mods.factorio.com/mod/warptorio-space-age)** — Community continuation of Warptorio for Factorio 2.0/2.1 and Space Age, maintained separately from the original 1.1 Warptorio2. Portal release 0.4.7 lists Factorio 2.0-2.1.
  `mod` · `Lua` · `Factorio 2.0-2.1 / Space Age per portal release metadata` · `checked: Mod Portal page` · [source](https://github.com/VencaCZ/warptorio-space-age)

<a id="exotic-industries"></a>
- **[Exotic Industries](https://mods.factorio.com/mod/exotic-industries)** — Overhaul with new resources, large machines, and the alien world Gaia. Portal release 0.6.9 is Factorio 1.1 only; Exotic Space Industries is a separate 2.x fork, not a direct port.
  `mod` · `Lua` · `legacy` · `Factorio 1.1 only` · `checked: Mod Portal page` · [source](https://github.com/PreLeyZero/exotic-industries)

<a id="exotic-space-industries"></a>
- **[Exotic Space Industries](https://mods.factorio.com/mod/exotic-space-industries)** — Space Age fork/rewrite inspired by Exotic Industries, with Gaia as a planet, morphium, storms, freezing, and new progression. Portal release 3.2.0 lists Factorio 2.0-2.1 and is tagged as a Space Age mod.
  `mod` · `Factorio 2.0-2.1 / Space Age per portal release metadata` · `checked: Mod Portal page`

<a id="lunar-landings"></a>
- **[Lunar Landings](https://mods.factorio.com/mod/LunarLandings)** — Small overhaul expanding the factory to Nauvis' moon with reusable rockets, silicon, oxygen diffusers, telescopes, aluminium, and a quantum endgame. Portal release 1.1.8 lists Factorio 1.1-2.0 and explicitly says not yet compatible with Space Age.
  `mod` · `Lua` · `Factorio 1.1-2.0; not Space Age compatible per portal description` · `checked: Mod Portal page` · [source](https://github.com/tburrows13/LunarLandings)

<a id="freight-forwarding"></a>
- **[Freight Forwarding](https://mods.factorio.com/mod/FreightForwarding)** — Long-distance logistics overhaul using containerized cargo, trains, ships, islands, offshore oil, seabed dredging, and lava-pool titansteel. Portal release 1.9.0 is Factorio 1.1 only; a 2.0 update was described as in progress but not verified as released.
  `mod` · `Lua` · `legacy` · `Factorio 1.1 only` · `checked: Mod Portal page` · [source](https://github.com/tburrows13/FreightForwarding)

<a id="archipelago"></a>
- **[Archipelago](https://archipelago.gg)** — Multi-game randomizer framework with Factorio support, letting items and progression connect across different games. Useful for randomized co-op challenges; check the Factorio world/client documentation for current setup.
  `tool` · `Python` · `checked: GitHub API/README` · [source](https://github.com/ArchipelagoMW/Archipelago)

## Sandbox, testing, and editor tools

Creative/sandbox environments, editor extensions, mod test harnesses, coverage, and profiling tools.

<a id="blueprint-sandboxes"></a>
- **[Blueprint Sandboxes](https://mods.factorio.com/mod/blueprint-sandboxes)** — Temporary editor-lite lab environments for designing and testing blueprints without affecting your main save. Portal release 3.3.0 lists Factorio 1.1-2.1; the canonical slug is lowercase blueprint-sandboxes.
  `mod` · `Lua` · `Factorio 1.1-2.1 per portal release metadata` · `checked: Mod Portal page` · [source](https://github.com/cameronleger/blueprint-sandboxes)

<a id="editor-extensions"></a>
- **[Editor Extensions](https://mods.factorio.com/mod/editor-extensions)** — Extends the built-in map editor with extra tools for testing, cloning, and manipulating entities. Portal release 2.6.1 lists Factorio 1.1-2.1; source has migrated to Codeberg.
  `mod` · `Lua` · `Factorio 1.1-2.1 per portal release metadata` · `checked: Mod Portal page` · [source](https://codeberg.org/raiguard/EditorExtensions)

<a id="creative-mod"></a>
- **[Creative Mod](https://mods.factorio.com/mod/creative-mod)** — Creative-mode items and entities for unlimited resources, fluids, energy, and voiding, useful for testing and layout experiments. Portal release 2.2.1 lists Factorio 0.17-2.1.
  `mod` · `Lua` · `Factorio 0.17-2.1 per portal release metadata` · `checked: Mod Portal page` · [source](https://github.com/jodli/CreativeMod)

<a id="minimal-no-base"></a>
- **[Minimal No Base Mod](https://github.com/Bilka2/minimal-no-base-mod)** — Provides the minimal prototypes needed to load Factorio without the base mod. Useful for total-conversion experiments, engine testing, and modding research.
  `mod` · `Lua` · `checked: GitHub API/README`

<a id="faketorio"></a>
- **[Faketorio](https://github.com/JonasJurczok/faketorio)** — Runs automated tests for Factorio mods inside the game. Useful for mod authors who want regression tests beyond static Lua checks.
  `tool` · `Lua` · `checked: GitHub API/README`

<a id="factorio-coverage"></a>
- **[factorio-coverage](https://github.com/justarandomgeek/factorio-coverage)** — Coverage reporter for Factorio mods. Helps mod authors see which runtime code paths were exercised during tests or play sessions.
  `tool` · `checked: GitHub API/README`

<a id="factorio-profiler"></a>
- **[Factorio-Profiler](https://github.com/justarandomgeek/Factorio-Profiler)** — Profiling tool for Factorio mods and runtime behavior. Useful when diagnosing UPS problems or expensive mod callbacks.
  `tool` · `checked: GitHub API/README`

## Multiplayer, servers, and operations

Hosted services, Docker images, server managers, Clusterio, scenarios, RCON clients, monitoring, chat bridges, and deployment tooling.

<a id="factorio-zone"></a>
- **[Factorio Zone](https://factorio.zone/)** — Free/low-friction hosted Factorio server service with a web control panel. Useful for quick multiplayer sessions without managing a VPS; check current limits and save-export options before relying on it.
  `service` · `checked: web page`

<a id="linuxgsm-factorio"></a>
- **[LinuxGSM Factorio server](https://linuxgsm.com/servers/fctrserver/)** — LinuxGSM's Factorio dedicated-server management script, covering install, start/stop, update, backup, and monitor workflows. Good for self-hosters who want a conventional Linux game-server manager.
  `tool` · `Shell` · `checked: web page` · [source](https://github.com/GameServerManagers/LinuxGSM)

<a id="factorio-docker"></a>
- **[factoriotools/factorio-docker](https://github.com/factoriotools/factorio-docker)** — Widely used Docker image and compose examples for Factorio headless servers, with save/mod management and update workflows. The old rfvgyhn/factorio-docker seed URL is unavailable; this is the current community image.
  `tool` · `Shell` · `checked: GitHub API/README`

<a id="aconti-headless"></a>
- **[aconti90/factorio-headless](https://github.com/aconti90/factorio-headless)** — Docker headless server images with native amd64 and arm64 builds, automatically rebuilt for stable and experimental releases. Useful for ARM hosts and users who want multi-arch images without emulation.
  `tool` · `Shell` · `checked: GitHub API/README`

<a id="goofball-factorio"></a>
- **[goofball222/factorio](https://github.com/goofball222/factorio)** — Another long-running Factorio headless Docker container project. The seed URL goofball222/factorio-docker returned 404, but the renamed factorio repository exists.
  `tool` · `Shell` · `checked: GitHub API/README`

<a id="clusterio"></a>
- **[Clusterio](https://github.com/clusterio/clusterio)** — Framework for connecting multiple Factorio servers into a cluster, with cross-server communication, shared storage, and web management. The foundation for large public server networks and grid-world experiments.
  `tool` · `TypeScript` · `checked: GitHub API/README`

<a id="subspace-storage"></a>
- **[Clusterio Subspace Storage](https://github.com/clusterio/subspace_storage)** — Lua-side Clusterio plugin for shared cross-server storage. Useful when building multi-server economies or grid worlds where items must move between instances.
  `mod` · `Lua` · `checked: GitHub API/README`

<a id="ofsm"></a>
- **[Open Factorio Server Manager](https://github.com/OpenFactorioServerManager/factorio-server-manager)** — Go-based web manager for Factorio multiplayer servers, saves, mods, and console operations. The old Roang-zero1/Factorio-Server-Manager seed URL redirects here.
  `tool` · `Go` · `checked: GitHub API/README`

<a id="factorio-init"></a>
- **[factorio-init](https://github.com/Bisa/factorio-init)** — Classic init script for running Factorio as a managed Linux service. Useful for older or minimal self-hosted deployments.
  `tool` · `Shell` · `checked: GitHub API/README`

<a id="tricade-server-manager"></a>
- **[Tricade Factorio Server Manager](https://github.com/tricade/factorio-server-manager)** — Self-hosted Go server control with profiles, saves, mods, exact versions, checkpoints, and resource-aware factory maps. A newer option for operators who want more than a basic web console.
  `tool` · `Go` · `checked: GitHub API/README`

<a id="factorio-stack-manager"></a>
- **[factorio-stack-manager](https://github.com/BrennanWoodbury/factorio-stack-manager)** — Self-hosted manager for multiple Factorio dedicated servers on one host behind NAT, using DNS SRV records for per-subdomain routing. Useful for home labs and small communities.
  `tool` · `TypeScript` · `checked: GitHub API/README`

<a id="chatwire"></a>
- **[ChatWire](https://github.com/M45-Science/ChatWire)** — Go-based Factorio-to-Discord chat bridge and server manager used by M45 Science. Combines chat relay with operational controls for public servers.
  `tool` · `Go` · `checked: GitHub API/README`

<a id="m45-softmod"></a>
- **[M45 SoftMod](https://github.com/M45-Science/SoftMod)** — Scenario scripts used on M45 Science's Factorio servers, including administrative and community features. Useful reference for public-server softmod design.
  `mod` · `Lua` · `checked: GitHub API/README`

<a id="expcluster"></a>
- **[ExpCluster](https://github.com/explosivegaming/ExpCluster)** — Active Clusterio plugin collection for Explosive Gaming's weekly-reset vanilla+ servers. Release 7.0.2 includes Factorio 2.1 quick-bar fixes; the old ExplosiveGaming/scenario URL redirects here, but it is not a verified rename of AwF.
  `mod` · `Lua` · `checked: GitHub API/README`

<a id="redmew"></a>
- **[RedMew](https://github.com/Refactorio/RedMew)** — RedMew scenario code for public Factorio servers, with community game modes and administrative features. The old Factorio-RedMew/RedMew seed URL redirects here; redmew.com returned HTTP 500 during verification.
  `mod` · `Lua` · `checked: GitHub API/README`

<a id="comfy"></a>
- **[ComfyFactorio](https://github.com/M3wM3w/ComfyFactorio)** — Community scenario and server framework behind ComfyFactorio public games, with custom maps, roles, and moderation features. The old ComfyFactorio/ComfyFactorio organization URL is unavailable; getcomfy.eu remains the community front door.
  `mod` · `Lua` · `checked: GitHub API/README`

<a id="biter-battles"></a>
- **[Biter Battles](https://www.biterbattles.org)** — Competitive/co-op Factorio scenario where teams defend against shared biter waves while racing production goals. The open-source scenario lives in Factorio-Biter-Battles/Factorio-Biter-Battles.
  `mod` · `Lua` · `checked: web page` · [source](https://github.com/Factorio-Biter-Battles/Factorio-Biter-Battles)

<a id="oarc-spawn"></a>
- **[Oarc's Multiplayer Spawn](https://github.com/Oarcinae/FactorioScenarioMultiplayerSpawn)** — Scenario/mod that gives each player or team a unique starting spawn point. Useful for co-op servers where players should not all share one crash site.
  `mod` · `Lua` · `checked: GitHub API/README`

<a id="factoriommo"></a>
- **[FactorioMMO scenarios](https://github.com/factoriommo/factoriommoscenarios)** — Historical community scenario collection from FactorioMMO public events. The old FactorioMMO/FactorioMMO seed URL is unavailable; this repository preserves the scenario lineage.
  `mod` · `Lua` · `historical` · `checked: GitHub API/README`

<a id="factorio-rcon-api"></a>
- **[factorio-rcon-api](https://factorio-rcon-api.ayaka.io/apis/docs/v2)** — TypeScript wrapper exposing a Factorio headless server console through RESTful and gRPC APIs. Useful for building dashboards, bots, and automation around RCON without hand-rolling protocol details.
  `tool` · `TypeScript` · `checked: GitHub API/README` · [source](https://github.com/nekomeowww/factorio-rcon-api)

<a id="gtaylor-rcon"></a>
- **[gtaylor/factorio-rcon](https://github.com/gtaylor/factorio-rcon)** — Go RCON package that handles Factorio-specific protocol behavior. Useful for Go-based server tooling.
  `library` · `Go` · `checked: GitHub API/README`

<a id="mark9064-rcon"></a>
- **[mark9064/factorio-rcon-py](https://github.com/mark9064/factorio-rcon-py)** — Python RCON client for Factorio servers. Useful for scripts, bots, and lightweight automation.
  `library` · `Python` · `checked: GitHub API/README`

<a id="factoriosharp-rcon"></a>
- **[FactorioSharp.Rcon](https://github.com/FactorioSharp/FactorioSharp.Rcon)** — C# RCON client for Factorio targeting .NET Standard 2.1. Useful for Windows/.NET server tooling.
  `library` · `C#` · `checked: GitHub API/README`

<a id="cmdbuffer"></a>
- **[cmdbuffer](https://github.com/justarandomgeek/cmdbuffer)** — Factorio RCON large-command-buffer tool. Useful when console commands exceed normal RCON payload limits.
  `tool` · `checked: GitHub API/README`

<a id="graftorio2"></a>
- **[graftorio2](https://github.com/remijouannet/graftorio2)** — Factorio mod/exporter for Grafana dashboards, continuing the original graftorio idea. Useful for visualizing production, power, and UPS trends over time.
  `mod` · `Lua` · `checked: GitHub API/README`

<a id="rcon-prometheus"></a>
- **[factorio-rcon-prometheus-exporter](https://github.com/Sleavely/factorio-rcon-prometheus-exporter)** — Exports Factorio metrics through RCON without requiring an in-game mod. Useful for Prometheus/Grafana monitoring of headless servers.
  `tool` · `Lua` · `checked: GitHub API/README`

<a id="go-factorio-prometheus"></a>
- **[go-factorio-prometheus](https://github.com/DaanV2/go-factorio-prometheus)** — Go RCON-to-Prometheus exporter for Factorio server metrics. Another option for operators building monitoring stacks.
  `tool` · `Go` · `checked: GitHub API/README`

<a id="factorio-stats"></a>
- **[factorio-stats](https://github.com/janten/factorio-stats)** — Prometheus exporter for Factorio that does not require mods. Useful for lightweight server metrics collection.
  `tool` · `Lua` · `checked: GitHub API/README`

<a id="factorio-dissector"></a>
- **[Factorio Wireshark dissector](https://github.com/Hornwitser/factorio_dissector)** — Wireshark dissector for Factorio network traffic. Useful for protocol research, debugging multiplayer issues, and understanding client-server communication.
  `tool` · `Lua` · `checked: GitHub API/README`

<a id="factocord"></a>
- **[FactoCord](https://github.com/FactoKit/FactoCord)** — Go Discord bot for Factorio server chat relay and administration. A common choice for communities that want Discord integration.
  `tool` · `Go` · `checked: GitHub API/README`

<a id="factorio-chat-bot"></a>
- **[FactorioChatBot](https://github.com/AGuyNamedJens/FactorioChatBot)** — Node.js two-way chat bridge between Discord and Factorio. Useful for smaller communities that prefer a JavaScript bot.
  `tool` · `JavaScript` · `checked: GitHub API/README`

<a id="d-wire"></a>
- **[D-Wire](https://github.com/BanRevenant/D-Wire)** — Python Discord bot for managing Factorio servers from a Discord community, used on production servers. Combines chat and operational controls.
  `tool` · `Python` · `checked: GitHub API/README`

<a id="fct-admin-devkit"></a>
- **[FCT Factorio Server Admin Devkit](https://github.com/FCTostin-team/Factorio-server-admin-Devkit)** — Python administration toolkit with asynchronous RCON, log parsing, SQLite telemetry, UPS/production graphs, WebSocket updates, and Telegram/Slack control. Useful for operators building a custom management service.
  `tool` · `Python` · `checked: GitHub API/README`

<a id="terraform-factorio-provider"></a>
- **[terraform-provider-factorio](https://github.com/efokschaner/terraform-provider-factorio)** — Terraform provider for Factorio resources. Experimental infrastructure-as-code approach to server configuration; verify current maintenance before production use.
  `tool` · `Go` · `experimental` · `checked: GitHub API/README`

<a id="terraform-factorio-modules"></a>
- **[fkleon/terraform-factorio](https://github.com/fkleon/terraform-factorio)** — Terraform modules for provisioning a headless Factorio server in AWS. Useful for repeatable cloud deployments.
  `tool` · `HCL` · `checked: GitHub API/README`

<a id="factorio-spot-pricing"></a>
- **[factorio-spot-pricing](https://github.com/m-chandler/factorio-spot-pricing)** — Shell tooling for deploying Factorio to AWS using spot pricing. Useful for low-cost temporary servers, with the usual spot-interruption caveats.
  `tool` · `Shell` · `checked: GitHub API/README`

<a id="minecloud"></a>
- **[MineCloud](https://github.com/VeriorPies/MineCloud)** — AWS CDK project for low-cost on-demand multiplayer servers, including Factorio among supported games. Useful for Discord communities that want servers only when players are active.
  `tool` · `TypeScript` · `checked: GitHub API/README`

<a id="factorio-save-upgrader"></a>
- **[factorio-save-upgrader](https://joelpurra.com/projects/factorio-save-upgrader/)** — Tool for upgrading old Factorio saves through intermediate versions toward newer releases. Useful for map nostalgia and migration experiments; always work on copies.
  `tool` · `Shell` · `checked: GitHub API/README` · [source](https://github.com/joelpurra/factorio-save-upgrader)

<a id="mod-settings-converter"></a>
- **[ModSettingsConverter](https://github.com/MatrixDJ96/ModSettingsConverter)** — C# tool that converts Factorio's mod-settings.dat to JSON and back. Useful for server operators, modpack authors, and debugging settings migrations.
  `tool` · `C#` · `checked: GitHub API/README`

<a id="re146-mods"></a>
- **[re146 Factorio mods mirror](https://re146.dev/factorio/mods/en)** — Browsable mirror/index of Factorio mods and versions. Useful when the official portal is slow or when inspecting historical releases; always prefer the official portal for authoritative downloads.
  `website` · `checked: web page`

<a id="factorio-mod-downloader-vaibhav"></a>
- **[vaibhavvikas/factorio-mod-downloader](https://github.com/vaibhavvikas/factorio-mod-downloader)** — Standalone open-source mod downloader where you provide a mod URL. Useful for manual downloads and scripting, but respect mod licenses and official portal terms.
  `tool` · `TypeScript` · `checked: GitHub API/README`

<a id="nickolasbradham-mod-downloader"></a>
- **[Factorio-Mod-Downloader](https://github.com/nickolasbradham/Factorio-Mod-Downloader)** — Java tool for downloading Factorio mods. Useful for bulk/manual mod management workflows.
  `tool` · `Java` · `checked: GitHub API/README`

<a id="modmyfactory2"></a>
- **[ModMyFactory2](https://github.com/Artentus/ModMyFactory2)** — C# rewrite of the ModMyFactory Factorio mod manager. Check current release status before relying on it; useful for managing multiple modded instances.
  `tool` · `C#` · `checked: GitHub API/README`

<a id="cfan"></a>
- **[CFAN](https://github.com/trakos/CFAN)** — Cool Factorio Archive Network project for mod metadata/management. Historical or incomplete in places; verify current maintenance before use.
  `tool` · `C#` · `historical` · `checked: GitHub API/README`

<a id="glutenfree"></a>
- **[glutenfree](https://github.com/Quezler/glutenfree)** — PHP-based CLI for mods.factorio.com. Useful for scripted portal interactions and mod metadata workflows.
  `tool` · `Lua` · `checked: GitHub API/README`

<a id="factorio-dl"></a>
- **[factorio-dl](https://github.com/moviuro/factorio-dl)** — Shell downloader script for Factorio on UNIX-like systems. Useful for scripted installs; always verify you are downloading from official Wube endpoints.
  `tool` · `Shell` · `checked: GitHub API/README`

<a id="smartmodinserter"></a>
- **[SmartModInserter](https://github.com/narrowtux/smartmodinserter)** — Java mod manager for Factorio. Historical option for managing mod sets; verify current maintenance before use.
  `tool` · `Java` · `historical` · `checked: GitHub API/README`

<a id="factorio-greyroom"></a>
- **[factorio-greyroom](https://github.com/Hornwitser/factorio-greyroom)** — Headless TypeScript client for Factorio. Useful for protocol research, bots, and automated testing experiments.
  `tool` · `TypeScript` · `checked: GitHub API/README`

<a id="web-control"></a>
- **[3Ra Web_Control](https://gitlab.com/3RaGaming/Web_Control)** — All-in-one web GUI and server manager for Factorio. The GitHub repository is a sync mirror; canonical development moved to GitLab.
  `tool` · `JavaScript` · `checked: GitHub API/README` · [source](https://github.com/3ragaming/web_control)

<a id="armaani"></a>
- **[Armaani](https://armaani.narigon.dev/)** — PHP game-server manager with Factorio support. Useful for self-hosters managing multiple game servers from one panel.
  `tool` · `PHP` · `checked: GitHub API/README` · [source](https://github.com/tatupesonen/armaani)

<a id="sergen"></a>
- **[Sergen](https://github.com/tomhobson/sergen)** — C# Discord chat bot and Docker controller for creating game servers easily, including Factorio. Useful for Discord-driven on-demand servers.
  `tool` · `C#` · `checked: GitHub API/README`

<a id="games-on-k8s-factorio"></a>
- **[games-on-k8s/docker-factorio](https://github.com/games-on-k8s/docker-factorio)** — Docker image for Factorio dedicated servers in Kubernetes-oriented game-server setups. Useful for container orchestration users.
  `tool` · `Shell` · `checked: GitHub API/README`

<a id="carloe-docker-factorio"></a>
- **[carloe/docker-factorio](https://github.com/carloe/docker-factorio)** — Dockerfile-based Factorio game server image. Another self-hosting option; compare maintenance and update cadence before choosing.
  `tool` · `Dockerfile` · `checked: GitHub API/README`

<a id="dockette-factorio"></a>
- **[dockette/factorio](https://github.com/dockette/factorio)** — Dockerized Factorio game server from the Dockette collection. Useful for users already standardized on Dockette images.
  `tool` · `Dockerfile` · `checked: GitHub API/README`

<a id="factorio-aci-terraform"></a>
- **[factorio-aci-terraform](https://github.com/celaus/factorio-aci-terraform)** — Terraform configuration for running a Factorio server on Azure Container Instances. Useful for Azure users wanting container-based hosting.
  `tool` · `HCL` · `checked: GitHub API/README`

<a id="factorio-port-fixer"></a>
- **[factorio-port-fixer](https://github.com/zcube/factorio-port-fixer)** — Go utility for Factorio headless server port handling. Useful in container/NAT environments where advertised ports need correction.
  `tool` · `Go` · `checked: GitHub API/README`

<a id="factoirc"></a>
- **[factoirc](https://github.com/mickael9/factoirc)** — Bidirectional IRC bridge for Factorio. Useful for communities that still use IRC alongside or instead of Discord.
  `tool` · `Python` · `checked: GitHub API/README`

<a id="factorio-events-logger"></a>
- **[events-logger](https://github.com/darkmatterproductions/events-logger)** — Generates formatted event logs and JSON files from Factorio's Events API. Useful for server analytics, auditing, and external dashboards.
  `tool` · `Shell` · `checked: GitHub API/README`

<a id="admin-command-center"></a>
- **[Factorio Admin Command Center](https://mods.factorio.com/mod/factorio-admin-command-center)** — In-game administrative command center for console, editor, repair, and other admin functions. Useful for public-server staff; restrict permissions carefully.
  `mod` · `Lua` · `checked: GitHub API/README` · [source](https://github.com/factoriocenter/factorio-admin-command-center)

## Modding frameworks, data tooling, and developer utilities

API typings, Lua/Rust/TypeScript frameworks, data exporters, spritesheet tools, localization, packaging, and release automation.

<a id="fmtk"></a>
- **[Factorio Mod Tool Kit (FMTK)](https://github.com/justarandomgeek/vscode-factoriomod-debug)** — VS Code extension and debugger/toolkit for Factorio mod development, including launch configurations, debugging support, and modding workflow helpers. The old Roang-zero1/FMTK seed URL is unavailable; this is the canonical toolkit.
  `tool` · `TypeScript` · `checked: GitHub API/README`

<a id="sumneko-plugin"></a>
- **[FactorioSumnekoLuaPlugin](https://github.com/JanSharp/FactorioSumnekoLuaPlugin)** — Plugin for the Sumneko Lua language server that improves Factorio-specific syntax and IntelliSense. Useful when writing Lua mods with cross-mod type awareness.
  `tool` · `Lua` · `checked: GitHub API/README`

<a id="typed-factorio"></a>
- **[typed-factorio](https://github.com/GlassBricks/typed-factorio)** — Complete TypeScript definitions for the Factorio modding API, used with TypeScript-to-Factorio workflows. Strong choice for typed mod development and editor autocomplete.
  `library` · `TypeScript` · `checked: GitHub API/README`

<a id="factorio-types"></a>
- **[factorio-types](https://github.com/sguest/factorio-types)** — TypeScript declarations for the Factorio mod API. Another typed-API option for web/Node-style modding toolchains.
  `library` · `TypeScript` · `checked: GitHub API/README`

<a id="factorio-type-kit"></a>
- **[factorio-type-kit](https://github.com/cdaringe/factorio-type-kit)** — Archived TypeScript type kit for Factorio modding. The seed PennyJim/factorio-type-kit URL is unavailable; this repository is archived and should be treated as historical.
  `library` · `TypeScript` · `archived` · `checked: GitHub API/README`

<a id="factorio-stdlib"></a>
- **[Factorio-Stdlib](https://github.com/Afforess/Factorio-Stdlib)** — Long-running Lua standard library for Factorio mods, with utilities for areas, positions, events, entities, and GUI work. Many older mods depend on it.
  `library` · `Lua` · `checked: GitHub API/README`

<a id="flib"></a>
- **[Factorio Library (flib)](https://mods.factorio.com/mod/flib)** — High-quality common utilities for Factorio mod authors, including GUI, migration, and data helpers. Portal release 0.17.2 lists Factorio 0.18-2.1; source and issue tracking are on Codeberg.
  `library` · `Lua` · `Factorio 0.18-2.1 per portal release metadata` · `checked: Mod Portal page` · [source](https://codeberg.org/raiguard/flib)

<a id="aqua"></a>
- **[Aqua mod framework](https://github.com/acovaci/aqua-mod-framework)** — Rust-based framework aiming to bring static type checking and CLI project management to Factorio mods. The project explicitly says it is not ready for use, so treat it as experimental.
  `tool` · `Rust` · `experimental` · `checked: GitHub API/README`

<a id="factorio-rs"></a>
- **[factorio-rs](https://factorio-rs.dev/)** — Rust-to-Lua transpilation project for writing Factorio mods in Rust. Explicitly work in progress; useful for experiments and language-tooling research rather than production mods.
  `tool` · `Rust` · `experimental` · `checked: GitHub API/README` · [source](https://github.com/languint/factorio-rs)

<a id="factorio-rust-tools"></a>
- **[factorio-rust-tools](https://github.com/MForster/factorio-rust-tools)** — Rust library for exporting prototype definitions from Factorio. Useful for building calculators, data browsers, and modding tools in Rust.
  `library` · `Rust` · `checked: GitHub API/README`

<a id="factorio-lib-rs"></a>
- **[factorio-lib-rs](https://github.com/JohnTheCoolingFan/factorio-lib-rs)** — Rust collection of Factorio-related types and utilities. Useful for Rust tooling around saves, blueprints, prototypes, or server APIs.
  `library` · `Rust` · `checked: GitHub API/README`

<a id="flua-src-rs"></a>
- **[flua-src-rs](https://github.com/fgardt/flua-src-rs)** — Source and build logic for compiling Factorio's Lua variant for Rust. Useful when you need Factorio-compatible Lua behavior in native tooling.
  `library` · `Rust` · `checked: GitHub API/README`

<a id="java-data-wrapper"></a>
- **[Java-Factorio-Data-Wrapper](https://github.com/demodude4u/Java-Factorio-Data-Wrapper)** — Java tool for extracting game data from a Factorio installation. Useful for JVM-based calculators, recipe browsers, and data pipelines.
  `tool` · `Java` · `checked: GitHub API/README`

<a id="factoriolab-export"></a>
- **[factoriolab-export](https://github.com/factoriolab/factoriolab-export)** — Factorio mod that exports recipe data and icons into FactorioLab's data format. Essential for adding modpack support to FactorioLab.
  `mod` · `Lua` · `checked: GitHub API/README`

<a id="factorio-lab-tools"></a>
- **[factorio-lab-tools](https://github.com/factoriolab/factorio-lab-tools)** — C/Lua parser and tooling used to build FactorioLab base recipe datasets and icons. Useful for understanding or reproducing calculator data pipelines.
  `tool` · `C` · `checked: GitHub API/README`

<a id="factorio-scanner"></a>
- **[factorio-scanner](https://github.com/fgardt/factorio-scanner)** — Rust tools for rendering and working with blueprint strings, serializing prototype dumps, and related data tasks. Useful low-level infrastructure for blueprint and data tools.
  `library` · `Rust` · `checked: GitHub API/README`

<a id="factorio-spritter"></a>
- **[factorio-spritter](https://github.com/fgardt/factorio-spritter)** — Rust CLI for building Factorio mod spritesheets. Useful for mod authors automating graphics packaging.
  `tool` · `Rust` · `checked: GitHub API/README`

<a id="factorio-mod-template"></a>
- **[factorio-mod-template](https://github.com/fgardt/factorio-mod-template)** — Factorio mod template with automated changelog generation, packaging, and release workflows. Good starting point for new mods with CI.
  `tool` · `checked: GitHub API/README`

<a id="api-docs-diff"></a>
- **[factorio-api-docs-diff](https://github.com/fgardt/factorio-api-docs-diff)** — Rust tool that generates diffs from Factorio's machine-readable API docs. Useful for tracking runtime API changes between game versions.
  `tool` · `Rust` · `checked: GitHub API/README`

<a id="semantic-release-factorio"></a>
- **[semantic-release-factorio](https://github.com/fgardt/semantic-release-factorio)** — semantic-release plugin for publishing Factorio mods. Useful for automated versioning, changelogs, and portal releases from CI.
  `tool` · `TypeScript` · `checked: GitHub API/README`

<a id="mod-uploader-action"></a>
- **[Factorio-mod-uploader-action](https://github.com/TheBrutalX/Factorio-mod-uploader-action)** — GitHub Action that packages and uploads Factorio mods to the mod portal. Useful for release automation.
  `tool` · `TypeScript` · `checked: GitHub API/README`

<a id="pactorio"></a>
- **[pactorio](https://github.com/figsoda/pactorio)** — Rust mod packager for Factorio. Useful for reproducible mod zip creation and release pipelines.
  `tool` · `Rust` · `checked: GitHub API/README`

<a id="factorio-mods-localization"></a>
- **[factorio-mods-localization](https://github.com/dima74/factorio-mods-localization)** — Rust tooling that connects Factorio mods to Crowdin for community translation. Used by many popular mods to manage locale contributions.
  `tool` · `Rust` · `checked: GitHub API/README`

<a id="factorio-mod-luacheck"></a>
- **[factorio-mod-luacheck](https://github.com/Roang-zero1/factorio-mod-luacheck)** — Runs Factorio mod source through luacheck with Factorio-aware configuration. Useful for catching Lua mistakes in CI.
  `tool` · `Shell` · `checked: GitHub API/README`

<a id="example-mod"></a>
- **[factorio-example-mod](https://github.com/ZwerOxotnik/factorio-example-mod)** — Lightweight modular example mod demonstrating various features and compatibility patterns. Useful as a learning reference for runtime mod structure.
  `mod` · `Lua` · `checked: GitHub API/README`

<a id="mod-portal-client-php"></a>
- **[factorio-mod-portal-client](https://github.com/BluePsyduck/factorio-mod-portal-client)** — PHP client for the Factorio Mod Portal API. Useful for building PHP-based mod managers, mirrors, and metadata tools.
  `library` · `PHP` · `checked: GitHub API/README`

<a id="mod-explorer"></a>
- **[mod-explorer](https://mod.tools.bpbin.com)** — Web explorer for Factorio mod data and prototypes by fgardt. Useful for inspecting recipes, entities, and modded data without launching the game.
  `tool` · `checked: GitHub API/README` · [source](https://github.com/fgardt/mod-explorer)

<a id="raw-explorer"></a>
- **[raw-explorer](https://raw.tools.bpbin.com)** — Web explorer for raw Factorio prototype data. Useful for mod authors and calculator developers inspecting data-stage definitions.
  `tool` · `checked: GitHub API/README` · [source](https://github.com/fgardt/raw-explorer)

<a id="pocket-foundry"></a>
- **[Pocket Foundry](https://github.com/JulioFerrero/pocket-foundry)** — Android project for running the official Linux ARM64 Factorio build on a phone with an on-screen controller. Interesting for mobile experimentation; not an official Wube mobile release.
  `tool` · `Kotlin` · `checked: GitHub API/README`

<a id="fct-achievement-unlocker"></a>
- **[FCT Achievement Unlocker](https://github.com/FCTostin-team/Factorio-Achievement-Unlocker)** — Offline Python CLI that patches a separate copy of the Factorio executable so Steam achievements remain earnable with mods. Hash-checked and reversible, but current game compatibility was not validated; use only on a copy and understand the risk.
  `tool` · `Python` · `experimental` · `checked: GitHub API/README`

<a id="factorio-mep"></a>
- **[factorio-mep](https://github.com/timstableford/factorio-mep)** — JavaScript parser for Factorio map exchange strings. Useful for tooling that needs to inspect or generate map seeds/settings.
  `library` · `JavaScript` · `checked: GitHub API/README`

<a id="vscode-autocomplete"></a>
- **[vscode-factorio-lua-api-autocomplete](https://github.com/simonvizzini/vscode-factorio-lua-api-autocomplete)** — VS Code extension providing Factorio Lua API autocompletion. Useful lightweight editor support alongside or instead of heavier toolkits.
  `tool` · `TypeScript` · `checked: GitHub API/README`

<a id="factorioapiscraper"></a>
- **[factorioapiscraper](https://github.com/spiwn/factorioapiscraper)** — Python scraper that exports Factorio API documentation HTML to JSON for autocomplete extensions. Useful for editor-tooling pipelines.
  `tool` · `Python` · `checked: GitHub API/README`

<a id="treegraphgen"></a>
- **[factoriotreegraphgen](https://github.com/microeinstein/factoriotreegraphgen)** — Lua script that generates a technology dependency graph from Factorio game files. Useful for visualizing tech-tree structure and mod changes.
  `tool` · `Lua` · `checked: GitHub API/README`

<a id="wiki-scripts"></a>
- **[Factorio wiki scripts](https://github.com/Bilka2/wiki-scripts)** — Python scripts used on the official Factorio wiki. Useful for wiki maintainers and data-driven documentation tooling.
  `tool` · `Python` · `checked: GitHub API/README`

## Communities, discovery, and creators

Forums, Discords, subreddits, GitHub discovery feeds, speedrunning, community writing, and video creators.

<a id="official-discord"></a>
- **[Official Factorio Discord](https://discord.gg/factorio)** — Official community Discord linked from Factorio's ecosystem. Useful for real-time help, multiplayer coordination, and community announcements; invite links can expire, so use the official site if it fails.
  `community` · `checked: web page`

<a id="reddit-factorio"></a>
- **[r/factorio](https://www.reddit.com/r/factorio/)** — Main Factorio subreddit for builds, questions, mods, memes, and community discussion. Good discovery layer, but verify technical claims against primary sources.
  `community` · `checked: search result`

<a id="reddit-blueprints"></a>
- **[r/FactorioBlueprints](https://www.reddit.com/r/FactorioBlueprints/)** — Subreddit dedicated to sharing and requesting Factorio blueprints. Useful for finding designs, but check game version and mod dependencies before importing.
  `community` · `checked: search result`

<a id="reddit-technical"></a>
- **[r/technicalfactorio](https://www.reddit.com/r/technicalfactorio/)** — Technical Factorio community focused on UPS, megabases, mechanics, and optimization. Useful for advanced performance discussions and tool announcements.
  `community` · `checked: search result`

<a id="reddit-seablock"></a>
- **[r/Seablock](https://www.reddit.com/r/Seablock/)** — Community subreddit for Sea Block playthroughs and questions. Linked from the original Sea Block portal page; check whether advice applies to the original 1.1 mod or the current Sea Block Pack.
  `community` · `checked: web page`

<a id="reddit-pyanodons"></a>
- **[r/pyanodons](https://www.reddit.com/r/pyanodons/)** — Community subreddit for Pyanodon modpack discussion, progression help, and base showcases. Useful because pY's complexity makes generic Factorio advice unreliable.
  `community` · `checked: web page`

<a id="steam-discussions"></a>
- **[Factorio Steam Discussions](https://steamcommunity.com/app/427520/discussions/)** — Steam community discussions for Factorio. Useful for platform-specific issues and casual help, though the official forums are usually better for bugs and mod support.
  `community` · `checked: search result`

<a id="speedrun-factorio"></a>
- **[Speedrun.com Factorio](https://www.speedrun.com/factorio)** — Leaderboards, rules, and runs for Factorio speedrunning categories. Useful for competitive players and for finding optimized early-game routes.
  `community` · `checked: web page`

<a id="alt-f4"></a>
- **[Alt-F4](https://alt-f4.blog/)** — Community-written Alternative Factorio Friday Fan Facts, with mod spotlights, community stories, and technical articles. The source repository is AlternativeFFFF/Alt-F4; treat older posts as historical snapshots.
  `community` · `HTML` · `historical` · `checked: web page` · [source](https://github.com/AlternativeFFFF/Alt-F4)

<a id="github-topic-factorio"></a>
- **[GitHub topic: factorio](https://github.com/topics/factorio)** — GitHub's broad Factorio topic feed. Useful for discovering new tools, mods, calculators, and experiments, but requires manual curation because many repositories are unrelated or abandoned.
  `discovery` · `checked: web page`

<a id="github-topic-factorio-mod"></a>
- **[GitHub topic: factorio-mod](https://github.com/topics/factorio-mod)** — GitHub topic feed focused on Factorio mods. Useful for finding source code, forks, and continuations when portal pages lack repository links.
  `discovery` · `checked: web page`

<a id="github-topic-factorio-blueprint"></a>
- **[GitHub topic: factorio-blueprint](https://github.com/topics/factorio-blueprint)** — GitHub topic feed for blueprint tools, generators, editors, and libraries. Useful for discovering programmatic blueprint projects.
  `discovery` · `checked: web page`

<a id="github-topic-factorio-mods"></a>
- **[GitHub topic: factorio-mods](https://github.com/topics/factorio-mods)** — Another GitHub topic feed for Factorio mod collections and tooling. Overlaps with factorio-mod but sometimes surfaces different repositories.
  `discovery` · `checked: web page`

<a id="earendel-discord"></a>
- **[Earendel's Discord](https://discord.gg/GDvxHgXjkk)** — Community Discord linked from Earendel's mods, including Space Exploration, Alien Biomes, Jetpack, Text Plates, and AAI vehicles. Preferred support channel for several of those mods.
  `community` · `checked: web page`

<a id="pyanodons-discord"></a>
- **[Pyanodons Discord](https://discord.gg/SBHM3h5Utj)** — Community Discord linked from Pyanodons Coal Processing. Useful for pY-specific progression, compatibility, and bug questions.
  `community` · `checked: web page`

<a id="nullius-discord"></a>
- **[Nullius Discord](https://discord.gg/tZY2Rkte8Y)** — Community Discord linked from the Nullius portal page. Useful for terraforming progression, compatibility, and modpack questions.
  `community` · `checked: web page`

<a id="krastorio-discord"></a>
- **[Krastorio Discord](https://discord.gg/wCR2MVYqef)** — Krastorio community Discord referenced by Krastorio 2 Spaced Out for Space Age channel support. Useful for K2/K2SO compatibility questions.
  `community` · `checked: web page`

<a id="cybersyn-discord"></a>
- **[Project Cybersyn Discord](https://discord.gg/zmgUBu95HX)** — Preferred support channel for Project Cybersyn, especially experimental Factorio 2.1 issues. Linked from the mod portal page.
  `community` · `checked: web page`

<a id="xorimuth-discord"></a>
- **[Xorimuth's Discord](https://discord.gg/pkJc4v9nfT)** — Support Discord linked from Spidertron Enhancements, Spidertron Patrols, Lunar Landings, and Freight Forwarding. Useful for Xorimuth mod compatibility questions.
  `community` · `checked: web page`

<a id="codegreen-discord"></a>
- **[_CodeGreen's Discord](https://discord.gg/xNpBP6gzgK)** — Support Discord linked from Squeak Through 2 and Belt Visualizer. Useful for current _CodeGreen mod issues.
  `community` · `checked: web page`

<a id="constructron-discord"></a>
- **[Constructron Discord](https://discord.gg/m9TDSsH3u2)** — Support Discord linked from Spidertron Automation / Constructron Continued. Useful for job debugging and compatibility questions.
  `community` · `checked: web page`

<a id="helmod-discord"></a>
- **[Helmod Discord](https://discord.gg/mKEeAKb)** — Support Discord linked from Helmod. Useful for planner questions and mod-specific calculation issues.
  `community` · `checked: web page`

<a id="nilaus"></a>
- **[Nilaus](https://www.youtube.com/@Nilaus)** — YouTube creator known for Factorio base-building series, masterclass-style tutorials, and modded playthroughs. Useful for structured learning; check video dates for game-version relevance.
  `creator` · `checked: search result`

<a id="katherineofsky"></a>
- **[KatherineOfSky](https://www.youtube.com/@KatherineOfSky)** — YouTube creator with long-running Factorio tutorials, vanilla series, and modded playthroughs. Useful for beginner-to-intermediate explanations; older videos may predate 2.0.
  `creator` · `checked: search result`

<a id="michael-hendriks"></a>
- **[Michael Hendriks](https://www.youtube.com/@MichaelHendriks)** — YouTube creator focused on Factorio engineering challenges, circuit networks, and technical builds. Useful for advanced automation inspiration.
  `creator` · `checked: search result`

<a id="dosh"></a>
- **[DoshDoshington](https://www.youtube.com/@DoshDoshington)** — YouTube creator known for Factorio challenges, modded runs, and entertaining technical experiments. Useful for challenge ideas and mod showcases.
  `creator` · `checked: search result`

<a id="xterminator"></a>
- **[Xterminator](https://www.youtube.com/@Xterminator)** — Long-running Factorio mod spotlight creator. Many mod portal pages link to his spotlights; older videos may show outdated versions, so check the mod's current portal page.
  `creator` · `checked: web page`

<a id="jd-plays"></a>
- **[JD-Plays](https://www.youtube.com/@JDPlays)** — Factorio content creator with tutorials, megabase content, and community challenges. Useful for structured base-building ideas; verify game version in older videos.
  `creator` · `checked: search result`

<a id="nefrums"></a>
- **[Nefrums](https://www.youtube.com/@Nefrums)** — Factorio speedrunner and technical content creator. Useful for optimized routes, speedrun commentary, and high-efficiency early-game patterns.
  `creator` · `checked: search result`

<a id="trupen"></a>
- **[Trupen](https://www.youtube.com/@Trupen)** — Factorio content creator known for large-scale builds, challenges, and technical experiments. Useful for megabase inspiration.
  `creator` · `checked: search result`

<a id="maxiume"></a>
- **[Maxiume](https://www.youtube.com/@Maxiume)** — Factorio creator associated with blueprint collections and large-scale design content. The GitHub repository MaxiumeGaming/Factorio is listed separately in the blueprint section.
  `creator` · `checked: search result`

<a id="github-topic-factorio-blueprints"></a>
- **[GitHub topic: factorio-blueprints](https://github.com/topics/factorio-blueprints)** — GitHub topic feed for blueprint collections and sharing repositories. Useful for discovering community blueprint books and design archives.
  `discovery` · `checked: web page`

<a id="github-topic-factorio-tool"></a>
- **[GitHub topic: factorio-tool](https://github.com/topics/factorio-tool)** — GitHub topic feed for Factorio utilities and developer tools. Useful for finding calculators, editors, server tools, and modding experiments.
  `discovery` · `checked: web page`

<a id="fctostin-team"></a>
- **[FCTostin-team on GitHub](https://github.com/FCTostin-team)** — GitHub organization behind the FCT browser tool suite and this awesome list. Useful for finding related Factorio utilities, source repositories, and issue trackers.
  `community` · `checked: GitHub API/README`

## Audit, methodology, and maintenance

- [Complete seed-link audit](docs/link-audit.md): all 286 original URLs, including redirects, aliases, unavailable links, and excluded badge fragments.
- [Compatibility guide](docs/compatibility.md): evidence-based compatibility notes and known conflicts.
- [Research methodology](docs/research-methodology.md): discovery sources, verification methods, and scope limits.
- [Contributing](CONTRIBUTING.md): how to add or correct entries without turning the list into an uncurated link dump.

## License

The list and repository documentation are licensed under [Apache-2.0](LICENSE). Linked projects retain their own licenses; check each project before redistributing code, assets, or modpacks.
