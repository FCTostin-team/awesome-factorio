#!/usr/bin/env python3
"""Deterministically generate README.md and audit/compatibility docs from data/*.json."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CHECKED = "2026-10-31"

KIND_LABELS = {
    "website": "website",
    "tool": "tool",
    "mod": "mod",
    "repository": "repository",
    "reference": "reference",
    "community": "community",
    "api": "API",
    "library": "library",
    "service": "service",
    "creator": "creator",
    "discovery": "discovery",
}
STATUS_LABELS = {
    "listed": "listed",
    "historical": "historical",
    "legacy": "legacy",
    "archived": "archived",
    "experimental": "experimental",
    "unmaintained": "unmaintained",
    "unavailable": "unavailable",
    "unverified": "unverified",
}
VERIFICATION_LABELS = {
    "page": "web page",
    "github": "GitHub API/README",
    "portal": "Mod Portal page",
    "portal-batch": "Mod Portal batch API",
    "wiki": "MediaWiki API",
    "search": "search result",
}
HIDDEN_STATUSES = {"unavailable", "unverified"}


def load_json(name: str):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def visible_resources(resources):
    return [r for r in resources if r.get("status", "listed") not in HIDDEN_STATUSES]


def entry_lines(r: dict) -> list[str]:
    meta = [f"`{KIND_LABELS.get(r['kind'], r['kind'])}`"]
    if r.get("language"):
        meta.append(f"`{r['language']}`")
    status = r.get("status", "listed")
    if status != "listed":
        meta.append(f"`{STATUS_LABELS.get(status, status)}`")
    if r.get("compatibility"):
        meta.append(f"`{r['compatibility']}`")
    meta.append(f"`checked: {VERIFICATION_LABELS.get(r['verification'], r['verification'])}`")
    links = []
    if r.get("source") and r["source"].rstrip("/") != r["url"].rstrip("/"):
        links.append(f"[source]({r['source']})")
    tail = " · ".join(meta)
    if links:
        tail += " · " + " · ".join(links)
    return [
        f'<a id="{r["id"]}"></a>',
        f"- **[{r['name']}]({r['url']})** — {r['description']}",
        f"  {tail}",
        "",
    ]


def build_readme(resources, categories) -> str:
    visible = visible_resources(resources)
    by_cat = {c["id"]: [] for c in categories}
    for r in visible:
        by_cat[r["category"]].append(r)
    counts = Counter(r["category"] for r in visible)
    lines = [
        '<p align="center">',
        '  <img src="image/awesome-factorio.png" alt="Awesome Factorio" width="640">',
        "</p>",
        "",
        "<h1 align=\"center\">Awesome Factorio</h1>",
        "",
        '<p align="center">',
        f'  <a href="LICENSE"><img alt="License: Apache-2.0" src="https://img.shields.io/badge/license-Apache--2.0-blue.svg"></a>',
        f'  <img alt="Curated resources" src="https://img.shields.io/badge/resources-{len(visible)}-brightgreen.svg">',
        f'  <img alt="Last checked" src="https://img.shields.io/badge/last%20checked-{CHECKED}-orange.svg">',
        "</p>",
        "",
        "> A curated, English-language map of useful Factorio websites, tools, mods, repositories, servers, modding utilities, and communities.",
        "",
        f"This list catalogs **{len(resources)} resources** and renders **{len(visible)} recommended or clearly labeled historical entries**. "
        f"It was expanded from a 286-URL seed list through web research, GitHub discovery, Mod Portal checks, and repository README review. "
        f"It is broad, but it is **not a claim that every Factorio resource on the internet has been found**. Broken or unavailable seed links are preserved in the [link audit](docs/link-audit.md) instead of being presented as live recommendations.",
        "",
        "## How to read this list",
        "",
        "- **Primary links** point to the canonical project page, mod portal page, live tool, or repository.",
        "- **Source links** point to source code when the primary link is a live site or mod portal page.",
        f"- **`checked:`** records the verification method used on {CHECKED}. It does not mean the tool was exhaustively tested.",
        "- **Compatibility tags** are included only when project documentation or portal metadata supplied evidence. A broad portal range is not a guarantee that every feature works with Space Age, quality, or other overhauls.",
        "- **`legacy`** usually means the project stops at Factorio 1.1 or an older major version. **`historical`** means it is useful for context but not necessarily maintained. **`experimental`** means the project itself warns about stability.",
        "- **Space Age ≠ Factorio 2.x.** Some mods support the 2.x engine but not the expansion; some support the expansion only through add-ons; some portal ranges conflict with prose. Read the compatibility note before starting a long run.",
        "- **Modpacks are not interchangeable.** Krastorio 2, Space Exploration, Nullius, Pyanodons, Sea Block, Ultracube, and similar overhauls often require dedicated mod lists.",
        "",
        "## Quick start",
        "",
        "| Goal | Start with |",
        "| --- | --- |",
        "| Install or update the game | [Factorio downloads](#factorio-download), [Space Age](#factorio-space-age), [version history](#wiki-version-history) |",
        "| Learn ratios and mechanics | [Factorio Cheat Sheet](#factorio-cheatsheet), [FactorioLab](#factoriolab), [Kirk McDonald calculator](#kirk-mcdonald-calculator) |",
        "| Plan a modded factory in-game | [Factory Planner](#factory-planner), [Helmod](#helmod), [Rate Calculator](#rate-calculator) |",
        "| Find recipes and bottlenecks | [FNEI](#fnei), [What is it really used for?](#what-is-it-really-used-for), [Assembly Analyst](#assembly-analyst), [Bottleneck Lite](#bottleneck-lite) |",
        "| Share or edit blueprints | [FactorioPrints](#factorioprints), [FactorioBin](#factoriobin), [FactoryGameFan FBE](#fbe-factorygamefan), [FCT decoder/encoder](#fct-blueprint-decoder) |",
        "| Build circuits or displays | [Circuit cookbook](#wiki-circuit-cookbook), [Verilog2Factorio](#verilog2factorio), [Cnide](#cnide), [Nixie Tubes](#nixie-tubes) |",
        "| Test designs safely | [Blueprint Sandboxes](#blueprint-sandboxes), [Editor Extensions](#editor-extensions), [Creative Mod](#creative-mod) |",
        "| Run a server | [Factorio downloads/headless](#factorio-download), [factorio-docker](#factorio-docker), [LinuxGSM](#linuxgsm-factorio), [Clusterio](#clusterio) |",
        "| Make a mod | [Modding wiki](#wiki-modding), [Lua API](#factorio-lua-api), [FMTK](#fmtk), [flib](#flib), [Untitled GUI Guide](#untitled-gui-guide) |",
        "| Choose an overhaul | [Overhauls](#overhauls-and-challenge-modpacks), [compatibility guide](docs/compatibility.md) |",
        "",
        "## Contents",
        "",
    ]
    for c in categories:
        anchor = c["title"].lower().replace(",", "").replace(" ", "-")
        lines.append(f"- [{c['title']}](#{anchor}) ({counts[c['id']]})")
    lines += [
        "- [Link audit](docs/link-audit.md)",
        "- [Compatibility guide](docs/compatibility.md)",
        "- [Research methodology](docs/research-methodology.md)",
        "- [Contributing](CONTRIBUTING.md)",
        "",
    ]
    for c in categories:
        lines += [f"## {c['title']}", "", c["description"], ""]
        for r in by_cat[c["id"]]:
            lines += entry_lines(r)
    lines += [
        "## Audit, methodology, and maintenance",
        "",
        f"- [Complete seed-link audit](docs/link-audit.md): all {len(load_json('seed-urls.json'))} original URLs, including redirects, aliases, unavailable links, and excluded badge fragments.",
        "- [Compatibility guide](docs/compatibility.md): evidence-based compatibility notes and known conflicts.",
        "- [Research methodology](docs/research-methodology.md): discovery sources, verification methods, and scope limits.",
        "- [Contributing](CONTRIBUTING.md): how to add or correct entries without turning the list into an uncurated link dump.",
        "",
        "## License",
        "",
        "The list and repository documentation are licensed under [Apache-2.0](LICENSE). Linked projects retain their own licenses; check each project before redistributing code, assets, or modpacks.",
        "",
    ]
    return "\n".join(lines)


def build_audit(resources, audit) -> str:
    by_id = {r["id"]: r for r in resources}
    counts = Counter(row["status"] for row in audit)
    lines = [
        "# Seed link audit",
        "",
        f"Checked: **{CHECKED}**. This audit accounts for every URL extracted from the original README seed list.",
        "",
        "## Summary",
        "",
        f"- Total seed URLs: **{len(audit)}**",
    ]
    for status, count in sorted(counts.items()):
        lines.append(f"- `{status}`: **{count}**")
    lines += [
        "",
        "Status meanings:",
        "",
        "- `included`: the seed URL is the canonical primary link for a catalog entry.",
        "- `included-as-source`: the seed URL is retained as a source/repository link.",
        "- `alias`: the seed URL is an old slug, alternate front door, or alias of a canonical entry.",
        "- `redirected`: GitHub redirects the seed repository to a canonical repository that is cataloged.",
        "- `replaced`: the seed URL was unavailable or non-canonical, and a verified replacement/continuation is cataloged.",
        "- `unavailable`: the URL returned 404 or the repository/page was not found; no live recommendation is implied.",
        "- `unverified`: the fetch failed or availability was uncertain; the entry is not rendered as a live recommendation.",
        "- `excluded`: malformed badge/image markup or unrelated decoration, not a Factorio resource.",
        "",
        "A failed fetch is not always proof of permanent disappearance. Where the evidence was only a transient HTTP error, the note says so.",
        "",
        "## Audit table",
        "",
        "| # | Seed URL | Status | Catalog entry | Note |",
        "| ---: | --- | --- | --- | --- |",
    ]
    for i, row in enumerate(audit, 1):
        rid = row.get("resource_id")
        if rid:
            resource = by_id[rid]
            if resource.get("status", "listed") in HIDDEN_STATUSES:
                entry = f"[{resource['name']}]({resource['url']}) (not rendered)"
            else:
                entry = f"[{resource['name']}](../README.md#{rid})"
        else:
            entry = "—"
        url = row["url"].replace("|", "%7C")
        note = row["note"].replace("|", "\\|")
        lines.append(f"| {i} | <{url}> | `{row['status']}` | {entry} | {note} |")
    lines.append("")
    return "\n".join(lines)


def build_compatibility(resources) -> str:
    rows = [r for r in resources if r.get("compatibility")]
    lines = [
        "# Compatibility guide",
        "",
        f"Checked: **{CHECKED}**. This guide collects compatibility statements that had explicit evidence in project documentation, mod portal pages, or live tool output.",
        "",
        "## Rules used by this list",
        "",
        "1. **Factorio 2.x engine support is not the same as Space Age support.** A mod may load on 2.0/2.1 while breaking expansion progression.",
        "2. **Portal version ranges are metadata, not a full test matrix.** They can include old releases and can conflict with the author's prose.",
        "3. **Recent commits do not prove compatibility.** A repository can be pushed recently while still targeting 1.1 or an experimental branch.",
        "4. **Batch Mod Portal checks do not identify every member's exact range.** Entries checked only by batch API are labeled as such and should be rechecked individually before installation.",
        "5. **Overhauls often conflict.** Do not combine major overhauls unless the authors explicitly document compatibility.",
        "",
        "## Known important distinctions",
        "",
        "- **Krastorio 2**: portal metadata lists 2.1, but the project says Space Age progression is broken without an add-on such as Krastorio 2 Spaced Out.",
        "- **Space Exploration**: portal metadata lists 2.1, but the project describes 0.7.x as targeting Factorio 2.0 and labels the mod experimental/alpha.",
        "- **Ultracube**: portal range says 1.1-2.1, but prose says Factorio 2.0 only and incompatible with Space Age/Quality.",
        "- **Sea Block**: original `SeaBlock` stops at 1.1; `SeaBlockPack` is the current 2.x lineage.",
        "- **Warptorio**: original `warptorio2` stops at 1.1; `warptorio-space-age` is a separate community continuation.",
        "- **Exotic Industries**: original `exotic-industries` is 1.1-only; `exotic-space-industries` is a separate 2.x fork/rewrite.",
        "- **Recipe Book**: explicitly 2.0 only and will not update to 2.1.",
        "- **Quick Item Search / Pipe Visualizer**: explicitly 1.1 only because their core features are now built into the game.",
        "- **Project Cybersyn**: portal metadata lists 2.1, but the project says 2.1 support is experimental.",
        "- **Cargo Ships**: 2.1 splits oil rigs and floating electric poles into separate mods and requires a 2.0 migration step for old saves.",
        "",
        "## Compatibility table",
        "",
        "| Resource | Kind | Status | Compatibility evidence |",
        "| --- | --- | --- | --- |",
    ]
    for r in rows:
        status = r.get("status", "listed")
        lines.append(f"| [{r['name']}](../README.md#{r['id']}) | {r['kind']} | {status} | {r['compatibility']} |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    resources = load_json("resources.json")
    categories = load_json("categories.json")
    audit = load_json("seed-audit.json")
    (ROOT / "README.md").write_text(build_readme(resources, categories), encoding="utf-8")
    (ROOT / "docs").mkdir(exist_ok=True)
    (ROOT / "docs/link-audit.md").write_text(build_audit(resources, audit), encoding="utf-8")
    (ROOT / "docs/compatibility.md").write_text(build_compatibility(resources), encoding="utf-8")
    print(f"Generated README.md, docs/link-audit.md, docs/compatibility.md from {len(resources)} resources.")


if __name__ == "__main__":
    main()
