import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/workflow-handoff"

class PackageTests(unittest.TestCase):
    def test_names_versions_and_license_agree(self):
        plugin = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
        market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        text = (SKILL / "SKILL.md").read_text()
        self.assertEqual(plugin["name"], SKILL.name)
        self.assertIn("name: " + plugin["name"], text.split("---")[1])
        self.assertIn('version: "' + plugin["version"] + '"', text.split("---")[1])
        self.assertEqual(market["plugins"][0]["name"], plugin["name"])
        self.assertTrue((ROOT / market["plugins"][0]["source"]).is_dir())
        self.assertEqual((ROOT / "LICENSE").read_bytes(), (SKILL / "LICENSE").read_bytes())

    def test_local_reference_targets_ship_inside_package(self):
        for document in SKILL.rglob("*.md"):
            for target in re.findall(r"\]\(([^)]+)\)", document.read_text()):
                if "://" in target or target.startswith("#"):
                    continue
                path = (document.parent / target.split("#")[0]).resolve()
                self.assertTrue(path.is_relative_to(SKILL.resolve()), (document, target))
                self.assertTrue(path.is_file(), (document, target))

if __name__ == "__main__":
    unittest.main()
