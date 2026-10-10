import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]

class FaradayValidationTests(unittest.TestCase):
    def test_validator_passes_repository(self):
        result = subprocess.run([sys.executable, str(ROOT / "scripts" / "validate.py")], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("OK: validated", result.stdout)

    def test_registry_ids_are_unique(self):
        data = json.loads((ROOT / "registry" / "records.json").read_text())
        ids = [r["id"] for r in data["records"]]
        self.assertEqual(len(ids), len(set(ids)))

    def test_speculative_alignment_claims_are_not_marked_supported(self):
        data = json.loads((ROOT / "registry" / "records.json").read_text())
        status = {r["id"]: r["status"] for r in data["records"]}
        self.assertEqual(status["C-003"], "SPECULATIVE")
        self.assertEqual(status["C-004"], "SPECULATIVE")

if __name__ == "__main__":
    unittest.main()
