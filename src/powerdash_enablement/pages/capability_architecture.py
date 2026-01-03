from __future__ import annotations

import streamlit as st

from ..ai.engine import AIEngine
from ..ai.prompts import system_intent, max_tokens_for_length
from ..config.state import AppState
from ..data.storage import LocalJSONStore


def render(state: AppState) -> None:
    st.markdown("## 🧩 Capability Architecture")
    st.caption("Define what “good” looks like — in observable behaviours and real work contexts.")

    store = LocalJSONStore(state.storage_dir)
    prior = store.read("capability_architecture") or {}

    with st.form("capability_form"):
        role = st.text_input("Role", value=prior.get("role", ""), placeholder="e.g., Regional TA Partner, HRBP, Team Leader")
        context = st.text_area("Business context", value=prior.get("context", ""), placeholder="What environment are they operating in? Constraints? Stakeholders?")
        outcomes = st.text_area("Priority outcomes", value=prior.get("outcomes", ""), placeholder="What must improve? What outcomes matter most?")
        constraints = st.text_area("Risk / regulatory constraints", value=prior.get("constraints", ""), placeholder="Any compliance, safety, data, or policy constraints?")
        submitted = st.form_submit_button("Generate capability architecture", use_container_width=True)

    if submitted:
        payload = {"role": role, "context": context, "outcomes": outcomes, "constraints": constraints}
        store.write("capability_architecture", payload)

        user = f"""Role: {role}
Business context: {context}
Priority outcomes: {outcomes}
Risk/regulatory constraints: {constraints}

Generate:
1) A capability map (5–9 capabilities max, grouped if helpful)
2) Observable behaviours for each capability
3) Real work contexts where the capability is applied (scenarios/tasks)
4) Success indicators (lightweight, practical)
Keep it relevant, clear, and respectful of practitioner experience."""

        engine = AIEngine(providers={})
        result = engine.generate(
            provider=state.ai.provider,
            model=state.ai.model,
            system=system_intent(state.ai.tone),
            user=user,
            temperature=state.ai.temperature,
            max_tokens=max_tokens_for_length(state.ai.response_length),
        )

        st.markdown("### Output")
        st.write(result.text)
