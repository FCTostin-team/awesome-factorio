# Contributing

Thank you for helping improve Awesome Factorio. The goal is a curated, English-language, evidence-based list, not an unfiltered link dump.

## What belongs here

Useful Factorio resources such as:

- Official sites, documentation, and APIs.
- Calculators, planners, blueprint tools, circuit tools, and art/music/map generators.
- Mods with clear utility, overhaul value, or developer relevance.
- Server hosting, management, monitoring, RCON, and deployment tools.
- Modding libraries, frameworks, data exporters, packaging, and testing tools.
- Communities, discovery feeds, and creators with durable Factorio content.

## What does not belong here

- Unrelated projects that merely mention Factorio.
- Name-only matches for missing repositories.
- Pure AI/blockchain/demo projects unless they provide a concrete Factorio utility.
- Broken links presented as live recommendations.
- Non-English descriptions. Resource names may remain in their original form, but descriptions must be English.
- Duplicate primary URLs, duplicate mods under old slugs, or mirrored repositories without a clear reason.

## How to add or update an entry

1. Edit `data/resources.json`.
2. Use a stable lowercase hyphenated `id`.
3. Provide:
   - `name`
   - `url` — canonical primary link
   - `description` — specific, English, and useful
   - `category` — one of `data/categories.json`
   - `kind` — website, tool, mod, repository, reference, community, API, library, service, creator, or discovery
   - `status` — listed, historical, legacy, archived, experimental, unmaintained, unavailable, or unverified
   - `verification` — page, github, portal, portal-batch, wiki, or search
4. Add optional fields when supported by evidence:
   - `source`
   - `language`
   - `compatibility`
   - `aliases`
5. If the entry replaces or aliases a seed URL, update `data/seed-audit.json` and, when needed, `data/audit-overrides.json`.
6. Regenerate and validate:

```bash
python scripts/build.py
python scripts/validate.py
```

## Description guidelines

Good descriptions explain:

- What the resource does.
- Who it is for.
- Important limitations, compatibility caveats, or migration notes.
- Why it is distinct from nearby alternatives.

Avoid vague praise such as "awesome tool" or "best mod" without specifics. Do not claim current compatibility unless the project page, portal metadata, or documentation supports it.

## Compatibility guidelines

- Factorio 2.x engine support is not the same as Space Age support.
- Portal ranges are metadata, not a full test matrix.
- Recent commits do not prove compatibility.
- Batch portal checks are weaker than individual page checks.
- Preserve conflicts when metadata and prose disagree.
- Label 1.1-only mods as `legacy` when they are not current for 2.x.

## Link audit guidelines

Every original seed URL must remain accounted for in `data/seed-audit.json`.

Use:

- `included` for canonical primary links.
- `included-as-source` for source/repository links.
- `alias` for old slugs or alternate front doors.
- `redirected` for GitHub redirects to a canonical repository.
- `replaced` for unavailable or non-canonical seeds with a verified replacement/continuation.
- `unavailable` for 404/not-found resources.
- `unverified` for transient fetch failures or uncertain availability.
- `excluded` for malformed badges or unrelated decoration.

Do not delete audit rows just because a link is broken. Explain the outcome and, when possible, point to a verified alternative.

## Pull request checklist

- [ ] The resource is relevant to Factorio.
- [ ] The description is English and specific.
- [ ] The primary URL is canonical and not duplicated.
- [ ] Compatibility claims have evidence.
- [ ] Legacy/experimental/unavailable status is labeled honestly.
- [ ] Seed audit coverage remains complete.
- [ ] `python scripts/build.py` and `python scripts/validate.py` pass.
