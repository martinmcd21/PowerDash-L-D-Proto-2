from __future__ import annotations

import os
from typing import Optional

from openai import OpenAI

from .base import AIProvider, AIRequest


class OpenAIProvider:
    """OpenAI provider wrapper.

    Notes:
    - Uses the new OpenAI Python SDK.
    - Model IDs are configurable; you can map your catalog in config/config.yaml.
    - This is intentionally thin to keep a clean separation between UI and AI logic.
    """

    name = "openai"

    def __init__(self, api_key: Optional[str] = None):
        api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is not set.")
        self.client = OpenAI(api_key=api_key)

    def generate(self, req: AIRequest, *, model: str) -> str:
        # Using Responses API style. If your org uses a different endpoint, swap here.
        resp = self.client.responses.create(
            model=model,
            temperature=req.temperature,
            input=[
                {"role": "system", "content": req.system},
                {"role": "user", "content": req.user},
            ],
            max_output_tokens=req.max_output_tokens,
        )
        # The SDK returns structured output; .output_text is the convenience accessor.
        return resp.output_text
