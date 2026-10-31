#!/usr/bin/env python3
"""Offline validation for the Awesome Factorio catalog and generated documents."""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build  # noqa: E402

DATA = ROOT / "data"
REQUIRED = {"id", "name", "url", "description", "category", "kind", "status", "verification"}
KINDS = set(build.KIND_LABELS)
STATUSES = set(build.STATUS_LABELS)
VERIFICATIONS = set(build.VERIFICATION_LABELS)
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
NON_ENGLISH_SCRIPT_RE = re.compile(r"[\u0400-\u04FF\u0590-\u05FF\u0600-\u06FF\u3040-\u30FF\u4E00-\u9FFF\uAC00-\uD7AF]")


def norm_url(url: str) -> str:
    return re.sub(r"^https?://(www\.)?", "", unquote(url.strip()).rstrip("/")).lower()


def is_http_url(url: str) -> bool:
    p = urlparse(url)
    return p.scheme in {"http", "https"} and bool(p.netloc)


def markdown_anchors(text: str) -> set[str]:
    anchors = set(re.findall(r'<a id="([^"]+)"></a>', text))
    for heading in re.findall(r"^#{1,6}\s+(.+)$", text, flags=re.M):
        anchor = heading.strip().lower()
        anchor = re.sub(r"[^\w\s-]", "", anchor)
        anchor = re.sub(r"\s+", "-", anchor)
        anchors.add(anchor)
    return anchors


def main() -> int:
    errors: list[str] = []
    resources = json.loads((DATA / "resources.json").read_text(encoding="utf-8"))
    categories = json.loads((DATA / "categories.json").read_text(encoding="utf-8"))
    seeds = json.loads((DATA / "seed-urls.json").read_text(encoding="utf-8"))
    audit = json.loads((DATA / "seed-audit.json").read_text(encoding="utf-8"))
    cat_ids = {c["id"] for c in categories}
    ids: set[str] = set()
    primary_urls: dict[str, str] = {}
    alias_urls: dict[str, str] = {}

    if len(categories) != len(cat_ids):
        errors.append("Duplicate category ids")
    for r in resources:
        rid = r.get("id", "<missing>")
        missing = REQUIRED - set(r)
        if missing:
            errors.append(f"{rid}: missing fields {sorted(missing)}")
        if not ID_RE.match(rid):
            errors.append(f"{rid}: invalid id format")
        if rid in ids:
            errors.append(f"{rid}: duplicate id")
        ids.add(rid)
        if r.get("category") not in cat_ids:
            errors.append(f"{rid}: unknown category {r.get('category')}")
        if r.get("kind") not in KINDS:
            errors.append(f"{rid}: unknown kind {r.get('kind')}")
        if r.get("status") not in STATUSES:
            errors.append(f"{rid}: unknown status {r.get('status')}")
        if r.get("verification") not in VERIFICATIONS:
            errors.append(f"{rid}: unknown verification {r.get('verification')}")
        if not is_http_url(r.get("url", "")):
            errors.append(f"{rid}: invalid primary URL")
        if r.get("source") and not is_http_url(r["source"]):
            errors.append(f"{rid}: invalid source URL")
        desc = r.get("description", "")
        if len(desc) < 40:
            errors.append(f"{rid}: description too short")
        if NON_ENGLISH_SCRIPT_RE.search(desc) or NON_ENGLISH_SCRIPT_RE.search(r.get("name", "")):
            errors.append(f"{rid}: non-English script in name/description")
        n = norm_url(r.get("url", ""))
        if n in primary_urls:
            errors.append(f"{rid}: duplicate primary URL with {primary_urls[n]}")
        primary_urls[n] = rid
        for a in r.get("aliases", []):
            if not is_http_url(a):
                errors.append(f"{rid}: invalid alias URL {a}")
            na = norm_url(a)
            if na in primary_urls and primary_urls[na] != rid:
                errors.append(f"{rid}: alias collides with primary URL of {primary_urls[na]}")
            if na in alias_urls and alias_urls[na] != rid:
                errors.append(f"{rid}: alias shared with {alias_urls[na]}")
            alias_urls[na] = rid
        if r.get("status") in build.HIDDEN_STATUSES and r.get("compatibility"):
            errors.append(f"{rid}: hidden unavailable/unverified entry should not carry compatibility recommendation")

    # Seed audit coverage
    if len(seeds) != 286:
        errors.append(f"Expected 286 seed URLs, found {len(seeds)}")
    if len(audit) != len(seeds):
        errors.append(f"Audit row count {len(audit)} != seed count {len(seeds)}")
    if [row["url"] for row in audit] != seeds:
        errors.append("Audit rows do not match seed URL order/content exactly")
    audit_statuses = {"included", "included-as-source", "alias", "redirected", "replaced", "unavailable", "unverified", "excluded"}
    for row in audit:
        if row["status"] not in audit_statuses:
            errors.append(f"Invalid audit status {row['status']} for {row['url']}")
        rid = row.get("resource_id")
        if rid and rid not in ids:
            errors.append(f"Audit references unknown resource {rid}")
        if row["status"] in {"included", "included-as-source", "alias", "redirected", "replaced", "unverified"} and not rid:
            errors.append(f"Audit status {row['status']} lacks resource_id: {row['url']}")
        if not row.get("note"):
            errors.append(f"Audit row lacks note: {row['url']}")

    # Generated files must match deterministic build
    expected_readme = build.build_readme(resources, categories)
    expected_audit = build.build_audit(resources, audit)
    expected_compat = build.build_compatibility(resources)
    for path, expected in [
        (ROOT / "README.md", expected_readme),
        (ROOT / "docs/link-audit.md", expected_audit),
        (ROOT / "docs/compatibility.md", expected_compat),
    ]:
        if not path.exists() or path.read_text(encoding="utf-8") != expected:
            errors.append(f"{path.relative_to(ROOT)} is not up to date; run scripts/build.py")

    # Local markdown links and anchors
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    anchors = markdown_anchors(readme)
    for target in re.findall(r"\]\(([^)]+)\)", readme):
        if target.startswith("#"):
            if target[1:] not in anchors:
                errors.append(f"README missing anchor {target}")
        elif not target.startswith(("http://", "https://", "mailto:")):
            path = ROOT / target.split("#")[0]
            if not path.exists():
                errors.append(f"README local link missing: {target}")
    for doc in [ROOT / "docs/link-audit.md", ROOT / "docs/compatibility.md"]:
        text = doc.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)]+)\)", text):
            if target.startswith("../README.md#"):
                if target.split("#", 1)[1] not in anchors:
                    errors.append(f"{doc.name} missing README anchor {target}")
            elif not target.startswith(("http://", "https://", "mailto:", "<")):
                path = (doc.parent / target.split("#")[0]).resolve()
                if not path.exists():
                    errors.append(f"{doc.name} local link missing: {target}")

    # Hidden statuses must not be rendered as recommendations
    visible = build.visible_resources(resources)
    for r in visible:
        if r["status"] in build.HIDDEN_STATUSES:
            errors.append(f"Hidden status rendered: {r['id']}")

    if errors:
        print("Validation failed:")
        for e in errors:
            print(f"- {e}")
        return 1
    counts = Counter(r["category"] for r in visible)
    print(f"OK: {len(resources)} cataloged resources, {len(visible)} rendered entries, {len(audit)} audited seed URLs.")
    print("Categories: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
