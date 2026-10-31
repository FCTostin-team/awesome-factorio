# Research methodology

Last updated: **2026-10-31**.

## Goal

Build a broad, English-language, curated map of useful Factorio resources: official sites, references, calculators, blueprint tools, mods, server operations, modding utilities, communities, and creators. The list is intentionally curated rather than an unfiltered dump of every search result.

## Inputs

- Original seed README: **286 extracted URLs**.
- Seed GitHub inventory: **137 repository URLs**.
- Seed Mod Portal inventory: **74 mod slugs**.
- GitHub discovery corpus: **689 repository records**, narrowed to **428 candidates** before manual curation.
- Selected repository README review: **209 selected repositories**, **200 READMEs downloaded**.
- Final catalog: **404 resources**, with **394 rendered entries**. Unavailable/unverified entries are retained for audit but not rendered as recommendations.

## Discovery methods

1. **Seed extraction and normalization.** URLs were extracted from the original README, separated into GitHub repositories, Mod Portal slugs, official/wiki links, tools, communities, and malformed badge fragments.
2. **GitHub API checks.** Seed repositories were checked for existence, redirects, archived status, language, homepage, and description. Missing repositories were not replaced by name alone; unrelated projects with similar names were rejected.
3. **GitHub topic/search discovery.** Topic feeds and search queries surfaced additional tools, mods, libraries, server managers, and data pipelines. Candidates were filtered for relevance, usefulness, and evidence of actual Factorio scope.
4. **Mod Portal checks.** Individual portal pages were used where possible to capture exact release metadata and compatibility prose. Batch API checks were used only as weaker evidence and are labeled `portal-batch`.
5. **Web page verification.** Live tools, official pages, community sites, and documentation pages were fetched where network access allowed. Fetch failures are recorded as failures, not automatically as permanent disappearance.
6. **Wiki API verification.** Key official wiki pages and redirects were checked through the MediaWiki API. Missing pages such as `Data_lifecycle` and `Community` were not invented.
7. **README and documentation review.** Repository READMEs and project docs were used to distinguish current tools, historical projects, experimental frameworks, and migration notices.

## Verification labels

- `web page`: the primary page was fetched successfully.
- `GitHub API/README`: repository metadata and/or README was checked through GitHub.
- `Mod Portal page`: an individual mod portal page was checked.
- `Mod Portal batch API`: the mod appeared in a batch check, but exact individual release metadata was not fully recorded.
- `MediaWiki API`: page existence or redirect behavior was checked through the wiki API.
- `search result`: the resource was identified through search results but not fully fetched or tested.

A verification label is **not** a full functional test. It does not guarantee that every feature works with the current game, Space Age, quality, or a particular modpack.

## Compatibility policy

- Prefer explicit project documentation over inferred compatibility.
- Distinguish Factorio 1.1, 2.0, 2.1, Space Age, quality, and experimental support.
- Do not infer compatibility from recent commits, broad portal ranges, or batch counts.
- Preserve conflicts when portal metadata and project prose disagree, as with Ultracube.
- Label legacy, historical, archived, experimental, and unmaintained projects clearly.

## Scope limits

This list is broad but not exhaustive. It does not claim to contain every Factorio website, mod, repository, Discord server, video, or blueprint collection. Some resources are historical, some are experimental, and some seed links are unavailable. The audit preserves those outcomes instead of hiding them.

Network access in the research environment was restricted. GitHub and package hosts were reachable from the shell; other sites were checked through web fetch/search tools. Some sites returned transient HTTP 500 or generic fetch failures; those are recorded as uncertain rather than permanently dead.

## Reproducibility

The public source of truth is:

- `data/resources.json` — curated resource records.
- `data/categories.json` — section order and descriptions.
- `data/seed-urls.json` — original 286 seed URLs.
- `data/seed-audit.json` — disposition of every seed URL.
- `data/audit-overrides.json` — manual audit decisions for malformed or unavailable seeds.

Generated files:

- `README.md`
- `docs/link-audit.md`
- `docs/compatibility.md`

Run:

```bash
python scripts/build.py
python scripts/validate.py
```

The validator checks schema, duplicates, English descriptions, seed coverage, generated-file consistency, local links, and anchors. It does not perform live network checks by default.
