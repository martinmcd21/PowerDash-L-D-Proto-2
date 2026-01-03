from __future__ import annotations

import streamlit as st

from .tiles import Tile


def tile_button(tile: Tile, *, on_click, key_suffix: str = "") -> None:
    # Use a real Streamlit button for accessibility and consistent event handling,
    # then render the card visuals via HTML inside the button container.
    with st.container():
        col = st.columns([1])[0]
        with col:
            clicked = st.button(" ", key=f"tile_btn_{tile.key}{key_suffix}", on_click=on_click, use_container_width=True)
            # Render the card *over* the button area. Streamlit won't allow button content HTML,
            # so we render immediately after and rely on spacing to appear like one tile.
            st.markdown(
                f"""
<div class="pd-tile" style="margin-top:-62px;">
  <div class="pd-tile-title">{tile.icon} {tile.title}</div>
  <div class="pd-tile-desc">{tile.desc}</div>
  <div class="pd-tile-meta">
    <span>Open</span>
    <span>→</span>
  </div>
</div>
""",
                unsafe_allow_html=True,
            )
            # Spacer to avoid overlap with next elements
            st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
