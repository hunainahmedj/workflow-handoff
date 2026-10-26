import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("installer", ROOT / "scripts/install_skill.py")
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)

class InstallTests(unittest.TestCase):
    def test_copy_and_protect_existing(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / "skills/workflow-handoff"
            installer.install(dest)
            for source in (ROOT / "skills/workflow-handoff").rglob("*"):
                if source.is_file() and "__pycache__" not in source.parts:
                    self.assertEqual(source.read_bytes(), (dest / source.relative_to(ROOT / "skills/workflow-handoff")).read_bytes())
            (dest / "SKILL.md").write_text("local customisation")
            with self.assertRaises(FileExistsError):
                installer.install(dest)
            self.assertEqual((dest / "SKILL.md").read_text(), "local customisation")

    def test_refuses_recursive_destination(self):
        destination = ROOT / "skills/workflow-handoff/nested-install"
        with self.assertRaises(ValueError):
            installer.install(destination)
        self.assertFalse(destination.exists())

    def test_refuses_dangling_symlink(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / "workflow-handoff"
            dest.symlink_to(Path(tmp) / "missing", target_is_directory=True)
            with self.assertRaises(FileExistsError):
                installer.install(dest)
            self.assertTrue(dest.is_symlink())

if __name__ == "__main__":
    unittest.main()
