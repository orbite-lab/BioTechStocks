# -*- coding: utf-8 -*-
"""Validate every config against scripts/lib/config_schema.json.

Usage:
  py scripts/ops/validate_schema.py           # validate all, exit 1 on error
  py scripts/ops/validate_schema.py TICKER    # validate single ticker

Requires: jsonschema (pip install jsonschema)
"""
import json, sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator
except ImportError:
    print("Missing dependency: pip install jsonschema")
    sys.exit(2)

ROOT = Path(__file__).resolve().parent.parent.parent
CONFIGS = ROOT / "configs"
SCHEMA = ROOT / "scripts" / "lib" / "config_schema.json"


def main():
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)

    argv = sys.argv[1:]
    if argv:
        tickers = argv
    else:
        manifest = json.loads((CONFIGS / "manifest.json").read_text())
        tickers = manifest

    total_errors = 0
    for tk in sorted(tickers):
        path = CONFIGS / f"{tk}.json"
        if not path.exists():
            print(f"[MISS] {tk}: not found")
            total_errors += 1
            continue
        try:
            cfg = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            print(f"[JSON] {tk}: {e}")
            total_errors += 1
            continue
        errors = list(validator.iter_errors(cfg))
        if errors:
            print(f"[FAIL] {tk} ({len(errors)} errors):")
            for err in errors[:10]:
                path_str = "/".join(str(p) for p in err.absolute_path) or "<root>"
                print(f"  {path_str}: {err.message}")
            if len(errors) > 10:
                print(f"  ... +{len(errors)-10} more")
            total_errors += len(errors)
        # else silent

    print(f"\nValidated {len(tickers)} configs, {total_errors} total errors")
    sys.exit(1 if total_errors else 0)


if __name__ == "__main__":
    main()
