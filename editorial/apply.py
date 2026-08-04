"""editorial/ed_*.py dosyalarını content/ altına JSON olarak yazar.

    python -m editorial.apply
"""

from __future__ import annotations

import importlib
import sys
from pathlib import Path

from pipeline.compose import save_edition

HERE = Path(__file__).resolve().parent


def main() -> int:
    modules = sorted(p.stem for p in HERE.glob("ed_*.py"))
    if not modules:
        print("editorial/ altında ed_*.py yok.", file=sys.stderr)
        return 1

    failed = 0
    for name in modules:
        module = importlib.import_module(f"editorial.{name}")
        try:
            save_edition(module.DATE, module.INTRO, module.DRAFTS)
        except Exception as exc:
            failed += 1
            print(f"  HATA {name}: {type(exc).__name__}: {exc}")

    print(f"\n{len(modules) - failed}/{len(modules)} sayı yazıldı.")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
