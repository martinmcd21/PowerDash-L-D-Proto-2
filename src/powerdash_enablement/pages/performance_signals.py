from __future__ import annotations

import streamlit as st

from ..ai.engine import AIEngine
from ..ai.prompts import system_intent, max_tokens_for_length
from ..config.state import AppState
from ..data.storage import LocalJSONStore


def render(state: AppState) -> None:
    st.markdown("## 📡 Performance Signals")
    st.caption("Understand reality using lightweight prompts and reflections — no heavy surveys.")

    store = LocalJSONStore(state.storage_dir)
    prior = store.read("performance_signals") or {}

    st.markdown("### Capture signals")
    with st.form("signals_form"):
        self_reflection = st.text_area(
            "Self-reflection (short prompts + notes)",
            value=prior.get("self_reflection", ""),
            placeholder="What felt hard this week? Where did work slow down? What would you do differently?",
        )
        manager_obs = st.text_area(
            "Manager observation (notes)",
            value=prior.get("manager_obs", ""),
            placeholder="What did you see? What decisions were strong/weak? Where did support get used?",
        )
        confidence = st.slider("Confidence check-in", min_value=1, max_value=5, value=int(prior.get("confidence", 3)))
        reflections = st.text_area(
            "Free-text reflections (optional)",
            value=prior.get("reflections", ""),
            placeholder="Paste snippets from retros, calls, chat messages (no sensitive data).",
        )
        submitted = st.form_submit_button("Synthesize signals", use_container_width=True)

    if submitted:
        payload = {
            "self_reflection": self_reflection,
            "manager_obs": manager_obs,
            "confidence": confidence,
            "reflections": reflections,
        }
        store.write("performance_signals", payload)

        user = f"""Inputs:
- Self-reflection: {self_reflection}
- Manager observation: {manager_obs}
- Confidence check-in (1–5): {confidence}
- Free-text reflections: {reflections}

Tasks:
1) Synthesize weak signals into a few clear themes
2) Identify friction points (where work breaks down or slows)
3) Highlight repeating patterns and likely causes (be cautious, don't overclaim)
4) Suggest 3–6 next-step hypotheses to test using lightweight checks
Keep it practical and non-judgmental."""

        engine = AIEngine(providers={})
        result = engine.generate(
            provider=state.ai.provider,
            model=state.ai.model,
            system=system_intent(state.ai.tone),
            user=user,
            temperature=state.ai.temperature,
            max_tokens=max_tokens_for_length(state.ai.response_length),
        )

        st.markdown("### Patterns & friction")
        st.write(result.text)
