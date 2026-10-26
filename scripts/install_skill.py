#!/usr/bin/env python3
"""Copy the portable skill without replacing an existing installation."""
import argparse
from pathlib import Path
import shutil


def install(destination):
    source = Path(__file__).resolve().parents[1] / "skills" / "workflow-handoff"
    destination = Path(destination).expanduser()
    if destination.exists() or destination.is_symlink():
        raise FileExistsError(f"Refusing to overwrite {destination}; preserve local changes before updating.")
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    return destination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", choices=("codex", "claude"), required=True)
    parser.add_argument("--destination", type=Path, help="Override the complete skill directory path")
    args = parser.parse_args()
    root = ".agents" if args.target == "codex" else ".claude"
    dest = args.destination or Path.home() / root / "skills" / "workflow-handoff"
    try:
        installed = install(dest)
    except OSError as exc:
        parser.exit(1, str(exc) + "\n")
    print(f"Installed workflow-handoff at {installed}")
    print("Open a new host session if the skill is not discovered immediately.")


if __name__ == "__main__":
    main()
