import json
from pathlib import Path
from typing import Any


class AlertStore:
    def __init__(self, path: str | None = None) -> None:
        self.path = Path(path or "alerts.json")
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            self.path.write_text("[]", encoding="utf-8")

    def load(self) -> list[dict[str, Any]]:
        return json.loads(self.path.read_text(encoding="utf-8"))

    def append(self, item: dict[str, Any]) -> None:
        records = self.load()
        records.append(item)
        self.path.write_text(json.dumps(records, indent=2), encoding="utf-8")
