from __future__ import annotations

import streamlit as st

from ..ai.engine import AIEngine
from ..ai.prompts import system_intent, max_tokens_for_length
from ..config.state import AppState
from ..data.storage import LocalJSONStore


def render(state: AppState) -> None:
    st.markdown("## 🛠️ Enablement Interventions")
    st.caption("Generate the smallest helpful artefact first. Training is suggested only when simpler support won’t work.")

    store = LocalJSONStore(state.storage_dir)
    prior = store.read("enablement_interventions") or {}

    st.markdown("### Describe the need")
    with st.form("interventions_form"):
        capability = st.text_input("Target capability", value=prior.get("capability", ""), placeholder="e.g., stakeholder alignment, structured interviewing")
        scenario = st.text_area("Real work scenario", value=prior.get("scenario", ""), placeholder="What is the person trying to do? With whom? Under what constraints?")
        constraints = st.text_area("Constraints / risks", value=prior.get("constraints", ""), placeholder="Time, policy, compliance, decision risk, customer impact, etc.")
        preferred = st.selectbox(
            "Preferred intervention type",
            options=["Auto (AI chooses smallest helpful)", "Job aid", "Checklist", "Conversation guide", "Short explainer", "Coaching prompts", "Workshop outline"],
            index=int(prior.get("preferred_idx", 0)),
        )
        submitted = st.form_submit_button("Generate intervention", use_container_width=True)

    if submitted:
        payload = {"capability": capability, "scenario": scenario, "constraints": constraints, "preferred_idx": ["Auto (AI chooses smallest helpful)", "Job aid", "Checklist", "Conversation guide", "Short explainer", "Coaching prompts", "Workshop outline"].index(preferred)}
        store.write("enablement_interventions", payload)

        user = f"""Target capability: {capability}
Scenario: {scenario}
Constraints/risks: {constraints}
Preferred type: {preferred}

Rules:
- Recommend the smallest intervention that will likely help immediately.
- If you suggest training/workshop, explain why simpler supports are insufficient.
Output:
1) Recommendation (type + why)
2) The generated artefact content, ready to copy/paste
3) A 30-second 'how to use this' instruction
4) A lightweight signal to track whether it helped (no long surveys)."""

        engine = AIEngine(providers={})
        result = engine.generate(
            provider=state.ai.provider,
            model=state.ai.model,
            system=system_intent(state.ai.tone),
            user=user,
            temperature=state.ai.temperature,
            max_tokens=max_tokens_for_length(state.ai.response_length),
        )

        st.markdown("### Intervention")
        st.write(result.text)
