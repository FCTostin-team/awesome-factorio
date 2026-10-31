import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.resources = json.loads((ROOT / "data/resources.json").read_text(encoding="utf-8"))
        cls.audit = json.loads((ROOT / "data/seed-audit.json").read_text(encoding="utf-8"))
        cls.seeds = json.loads((ROOT / "data/seed-urls.json").read_text(encoding="utf-8"))

    def test_resource_ids_unique(self):
        ids = [r["id"] for r in self.resources]
        self.assertEqual(len(ids), len(set(ids)))

    def test_seed_audit_complete(self):
        self.assertEqual(len(self.seeds), 286)
        self.assertEqual([r["url"] for r in self.audit], self.seeds)

    def test_no_duplicate_primary_urls(self):
        urls = [r["url"].rstrip("/").lower() for r in self.resources]
        self.assertEqual(len(urls), len(set(urls)))

    def test_validator_passes(self):
        proc = subprocess.run([sys.executable, str(ROOT / "scripts/validate.py")], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)

    def test_build_is_deterministic(self):
        before = (ROOT / "README.md").read_text(encoding="utf-8")
        subprocess.run([sys.executable, str(ROOT / "scripts/build.py")], cwd=ROOT, check=True, capture_output=True, text=True)
        after = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
