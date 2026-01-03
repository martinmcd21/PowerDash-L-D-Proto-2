from __future__ import annotations

import os
import streamlit as st

from ..config.state import AppState


def render_header(state: AppState) -> None:
    dot_class = "" if state.connection_ok else "off"
    st.markdown(
        f"""
<div class="pd-header">
  <div>
    <div class="title">{state.suite_name}</div>
    <div class="subtitle">Capability-first enablement • enterprise-safe • AI-assisted</div>
  </div>
  <div class="pd-pill">
    <span class="pd-dot {dot_class}"></span>
    <span>{state.connection_label}</span>
  </div>
</div>
""",
        unsafe_allow_html=True,
    )


def connection_status(provider: str) -> tuple[bool, str]:
    if provider == "openai":
        ok = bool(os.getenv("OPENAI_API_KEY"))
        return ok, ("Connected" if ok else "Not connected (set OPENAI_API_KEY)")
    return True, "Ready (mock mode)"
