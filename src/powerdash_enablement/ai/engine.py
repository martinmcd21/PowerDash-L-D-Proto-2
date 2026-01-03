from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Dict, Optional

from .providers.base import AIRequest
from .providers.mock_provider import MockProvider


@dataclass
class AIResult:
    text: str
    provider: str
    model: str


class AIEngine:
    def __init__(self, providers: Dict[str, object]):
        self.providers = providers

    def generate(self, *, provider: str, model: str, system: str, user: str, temperature: float, max_tokens: Optional[int] = None) -> AIResult:
        req = AIRequest(system=system, user=user, temperature=temperature, max_output_tokens=max_tokens)

        if provider == "mock" or model == "mock":
            text = MockProvider().generate(req)
            return AIResult(text=text, provider="mock", model="mock")

        if provider == "openai":
            from .providers.openai_provider import OpenAIProvider

            p = self.providers.get("openai")
            if p is None:
                p = OpenAIProvider(api_key=os.getenv("OPENAI_API_KEY"))
                self.providers["openai"] = p
            text = p.generate(req, model=model)
            return AIResult(text=text, provider="openai", model=model)

        raise ValueError(f"Unknown provider: {provider}")
