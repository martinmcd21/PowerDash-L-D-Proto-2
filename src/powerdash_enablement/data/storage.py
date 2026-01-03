from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Optional


class LocalJSONStore:
    """Lightweight local persistence for MVP.

    Stores per-tile JSON payloads under a single directory.
    This keeps the app stateless-friendly while still allowing quick iteration.
    """

    def __init__(self, root_dir: str):
        self.root = Path(root_dir)
        self.root.mkdir(parents=True, exist_ok=True)

    def _path(self, key: str) -> Path:
        safe = "".join([c for c in key if c.isalnum() or c in ("-", "_")]).strip()
        return self.root / f"{safe}.json"

    def read(self, key: str) -> Optional[Dict[str, Any]]:
        p = self._path(key)
        if not p.exists():
            return None
        return json.loads(p.read_text(encoding="utf-8"))

    def write(self, key: str, payload: Dict[str, Any]) -> None:
        p = self._path(key)
        p.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
