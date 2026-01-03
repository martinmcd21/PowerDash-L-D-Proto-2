from __future__ import annotations

import streamlit as st

from src.powerdash_enablement.ai.engine import AIEngine
from src.powerdash_enablement.config.settings import load_settings
from src.powerdash_enablement.config.state import AIControls, AppState
from src.powerdash_enablement.pages.registry import get_pages
from src.powerdash_enablement.ui.layout import render_header, connection_status
from src.powerdash_enablement.ui.style import inject_style


def init_session_state(default_page: str = "home") -> None:
    if "active_page" not in st.session_state:
        st.session_state["active_page"] = default_page


def sidebar_controls(settings) -> AIControls:
    st.sidebar.markdown("### Navigation")
    pages = get_pages()
    page_titles = {k: v.title for k, v in pages.items() if k != "home"}
    nav_options = ["home"] + [k for k in page_titles.keys()]
    nav_labels = ["Home"] + [page_titles[k] for k in page_titles.keys()]

    # Sidebar navigation (always visible)
    current = st.session_state.get("active_page", "home")
    selected_label = st.sidebar.radio(
        "Go to",
        options=nav_labels,
        index=max(0, nav_labels.index("Home") if current == "home" else nav_labels.index(page_titles.get(current, "Home"))),
        label_visibility="collapsed",
    )
    selected_key = nav_options[nav_labels.index(selected_label)]
    st.session_state["active_page"] = selected_key

    st.sidebar.markdown("---")
    st.sidebar.markdown("### AI Controls")

    model_labels = [m.label for m in settings.ai.models]
    model_by_label = {m.label: m for m in settings.ai.models}

    # Defaults
    default_model = next((m for m in settings.ai.models if m.id == settings.ai.default_model), settings.ai.models[0])
    default_label = default_model.label

    chosen_label = st.sidebar.selectbox("Model", options=model_labels, index=model_labels.index(default_label))
    chosen = model_by_label[chosen_label]

    temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=float(settings.ai.defaults.temperature), step=0.05)
    response_length = st.sidebar.selectbox("Response length", options=["short", "medium", "long"], index=["short", "medium", "long"].index(settings.ai.defaults.response_length))
    tone = st.sidebar.selectbox("Tone", options=["practical", "coaching", "analytical"], index=["practical", "coaching", "analytical"].index(settings.ai.defaults.tone))

    return AIControls(
        provider=chosen.provider,
        model=chosen.id,
        temperature=float(temperature),
        response_length=response_length,  # type: ignore
        tone=tone,  # type: ignore
    )


def main() -> None:
    st.set_page_config(page_title="PowerDash Enablement", layout="wide")
    inject_style()

    settings = load_settings("config/config.yaml")
    init_session_state(default_page="home")

    ai_controls = sidebar_controls(settings)
    ok, label = connection_status(ai_controls.provider)

    state = AppState(
        suite_name=settings.app.suite_name,
        connection_ok=ok,
        connection_label=label,
        ai=ai_controls,
        storage_dir=settings.app.storage_dir,
    )

    render_header(state)

    pages = get_pages()
    active_key = st.session_state.get("active_page", "home")
    page = pages.get(active_key, pages["home"])
    page.render(state)


if __name__ == "__main__":
    main()
