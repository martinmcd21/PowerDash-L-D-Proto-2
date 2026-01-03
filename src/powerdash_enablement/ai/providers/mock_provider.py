from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from .base import AIProvider, AIRequest


class MockProvider:
    name = "mock"

    def generate(self, req: AIRequest) -> str:
        # Deterministic-ish placeholder that makes dev/testing easier.
        stamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
        return (
            "⚙️ *Mock AI response (offline)*\n\n"
            f"**Timestamp:** {stamp}\n\n"
            "This is placeholder logic. Wire in a real provider to generate production outputs.\n\n"
            "---\n"
            "**System intent (summary):**\n"
            f"{req.system[:500]}{'…' if len(req.system) > 500 else ''}\n\n"
            "**User input (echo):**\n"
            f"{req.user[:1200]}{'…' if len(req.user) > 1200 else ''}"
        )
