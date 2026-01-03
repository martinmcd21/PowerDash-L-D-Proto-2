from __future__ import annotations

import streamlit as st

from ..config.state import AppState
from ..ui.components import tile_button
from ..ui.tiles import TILES


def render(state: AppState) -> None:
    st.markdown("### What do people need to do better at work — right now?")
    st.caption("Choose a tile to define capabilities, capture signals, generate interventions, and summarise impact.")

    # Tiles: 2 columns for clean enterprise layout
    cols = st.columns(2, gap="large")

    def go(page_key: str):
        st.session_state["active_page"] = page_key

    for idx, tile in enumerate(TILES):
        with cols[idx % 2]:
            tile_button(tile, on_click=lambda k=tile.key: go(k), key_suffix=f"_{idx}")
