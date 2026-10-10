import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ContextLayerTests(unittest.TestCase):
    def test_context_validator_passes(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "validate_context.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_faraday_has_no_downstream_execution_authority(self):
        data = json.loads((ROOT / "registry" / "ecosystem.json").read_text())
        faraday = next(s for s in data["systems"] if s["id"] == "faraday")
        self.assertFalse(faraday["authority"]["may_execute_downstream"])
        self.assertFalse(faraday["authority"]["may_authorize"])

    def test_authorization_is_epistemically_distinct(self):
        data = json.loads((ROOT / "registry" / "epistemic.json").read_text())
        kinds = {k["id"] for k in data["epistemic_kinds"]}
        self.assertIn("decision", kinds)
        self.assertIn("authorization", kinds)
        rules = "\n".join(data["rules"]).lower()
        self.assertIn("authorization cannot be inferred", rules)


if __name__ == "__main__":
    unittest.main()
