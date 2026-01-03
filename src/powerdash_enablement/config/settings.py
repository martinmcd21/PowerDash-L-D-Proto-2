from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml


@dataclass(frozen=True)
class ModelOption:
    id: str
    label: str
    provider: str


@dataclass(frozen=True)
class AIDefaults:
    temperature: float
    response_length: str
    tone: str


@dataclass(frozen=True)
class AppConfig:
    suite_name: str
    org_name: str
    storage_dir: str


@dataclass(frozen=True)
class AIConfig:
    default_provider: str
    default_model: str
    models: List[ModelOption]
    defaults: AIDefaults


@dataclass(frozen=True)
class Settings:
    app: AppConfig
    ai: AIConfig


def load_settings(config_path: str | Path) -> Settings:
    path = Path(config_path)
    data: Dict[str, Any] = yaml.safe_load(path.read_text(encoding="utf-8"))

    app = data.get("app", {})
    ai = data.get("ai", {})

    models = [
        ModelOption(
            id=m["id"],
            label=m.get("label", m["id"]),
            provider=m.get("provider", ai.get("default_provider", "mock")),
        )
        for m in ai.get("models", [])
    ]

    defaults = ai.get("defaults", {})
    return Settings(
        app=AppConfig(
            suite_name=app.get("suite_name", "PowerDash Enablement"),
            org_name=app.get("org_name", "PowerDash HR"),
            storage_dir=app.get("storage_dir", ".data"),
        ),
        ai=AIConfig(
            default_provider=ai.get("default_provider", "mock"),
            default_model=ai.get("default_model", "mock"),
            models=models if models else [ModelOption(id="mock", label="Mock (offline)", provider="mock")],
            defaults=AIDefaults(
                temperature=float(defaults.get("temperature", 0.2)),
                response_length=str(defaults.get("response_length", "medium")),
                tone=str(defaults.get("tone", "practical")),
            ),
        ),
    )
