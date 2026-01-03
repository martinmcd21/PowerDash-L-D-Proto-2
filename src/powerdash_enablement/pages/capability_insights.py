from __future__ import annotations

import streamlit as st

from ..ai.engine import AIEngine
from ..ai.prompts import system_intent, max_tokens_for_length
from ..config.state import AppState
from ..data.storage import LocalJSONStore


def render(state: AppState) -> None:
    st.markdown("## 📈 Capability Insights")
    st.caption("Plain-English insight summaries and next actions. No vanity metrics.")

    store = LocalJSONStore(state.storage_dir)

    cap = store.read("capability_architecture") or {}
    signals = store.read("performance_signals") or {}
    interventions = store.read("enablement_interventions") or {}
    inflow = store.read("inflow_support") or {}

    st.markdown("### Inputs used (lightweight)")
    with st.expander("View collected inputs", expanded=False):
        st.json({
            "capability_architecture": cap,
            "performance_signals": signals,
            "enablement_interventions": interventions,
            "inflow_support": inflow,
        })

    if not any([cap, signals, interventions, inflow]):
        st.info("No inputs yet. Use the other tiles first, then come back here for summaries.")
        return

    if st.button("Generate insight summary", use_container_width=True):
        user = f"""Using the following lightweight inputs, generate:
1) Capability health snapshot (qualitative, inferred)
2) Confidence vs competence gaps (hypotheses, not certainties)
3) Which interventions appear to have helped (based on signals available)
4) 3–6 recommended next actions (smallest useful next steps)
5) What to monitor next week (lightweight signals)

Inputs:
Capability architecture: {cap}
Performance signals: {signals}
Generated interventions: {interventions}
In-flow support usage: {inflow}

Constraints:
- Avoid completions/hours trained.
- Avoid heavy survey framing.
- Keep it enterprise-safe and actionable."""

        engine = AIEngine(providers={})
        result = engine.generate(
            provider=state.ai.provider,
            model=state.ai.model,
            system=system_intent(state.ai.tone),
            user=user,
            temperature=state.ai.temperature,
            max_tokens=max_tokens_for_length(state.ai.response_length),
        )

        st.markdown("### Insights")
        st.write(result.text)
