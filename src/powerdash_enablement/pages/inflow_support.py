from __future__ import annotations

import streamlit as st

from ..ai.engine import AIEngine
from ..ai.prompts import system_intent, max_tokens_for_length
from ..config.state import AppState
from ..data.storage import LocalJSONStore


def render(state: AppState) -> None:
    st.markdown("## ⚡ In-Flow Support")
    st.caption("A lightweight support layer for real work — not a course catalogue.")

    store = LocalJSONStore(state.storage_dir)
    prior = store.read("inflow_support") or {}

    st.markdown("### Context")
    with st.form("inflow_form"):
        task = st.text_input("What are you about to do?", value=prior.get("task", ""), placeholder="e.g., run a stakeholder meeting, make a hiring decision")
        context = st.text_area("Context (short)", value=prior.get("context", ""), placeholder="Key constraints, stakeholders, risks, time pressure")
        mode = st.radio("Support mode", options=["Pre-task nudge", "Decision co-pilot", "Post-action reflection"], index=int(prior.get("mode_idx", 0)), horizontal=True)
        submitted = st.form_submit_button("Generate in-flow support", use_container_width=True)

    if submitted:
        payload = {"task": task, "context": context, "mode_idx": ["Pre-task nudge", "Decision co-pilot", "Post-action reflection"].index(mode)}
        store.write("inflow_support", payload)

        user = f"""Task: {task}
Context: {context}
Mode: {mode}

Generate:
- If Pre-task: 5–8 concise prompts/checks to reduce risk and increase quality.
- If Co-pilot: a short decision framework + clarifying questions + next step suggestion.
- If Post-action: reflection prompts that drive learning without judgment.
Keep it quick, relevant, and usable in under 2 minutes."""

        engine = AIEngine(providers={})
        result = engine.generate(
            provider=state.ai.provider,
            model=state.ai.model,
            system=system_intent(state.ai.tone),
            user=user,
            temperature=state.ai.temperature,
            max_tokens=max_tokens_for_length(state.ai.response_length),
        )

        st.markdown("### Support layer")
        st.write(result.text)
