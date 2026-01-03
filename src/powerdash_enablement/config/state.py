from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Optional


ResponseLength = Literal["short", "medium", "long"]
Tone = Literal["practical", "coaching", "analytical"]


@dataclass
class AIControls:
    provider: str
    model: str
    temperature: float
    response_length: ResponseLength
    tone: Tone


@dataclass
class AppState:
    suite_name: str
    connection_ok: bool
    connection_label: str
    ai: AIControls
    storage_dir: str
