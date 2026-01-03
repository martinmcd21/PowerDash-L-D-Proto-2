from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass
class AIRequest:
    system: str
    user: str
    temperature: float
    max_output_tokens: int | None = None


class AIProvider(Protocol):
    name: str

    def generate(self, req: AIRequest) -> str:
        ...
