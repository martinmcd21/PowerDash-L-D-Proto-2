from __future__ import annotations

import streamlit as st


POWERDASH_CSS = """
<style>
/* Layout */
.pd-header {
  display:flex;
  align-items:center;
  justify-content:space-between;
  padding: 14px 16px;
  border-radius: 14px;
  background: #F5F7FB;
  border: 1px solid rgba(15, 23, 42, 0.08);
  margin-bottom: 14px;
}
.pd-header .title {
  font-size: 18px;
  font-weight: 700;
  color: #0B1220;
  letter-spacing: 0.2px;
}
.pd-header .subtitle {
  font-size: 12px;
  color: rgba(11, 18, 32, 0.7);
  margin-top: 2px;
}
.pd-pill {
  display:inline-flex;
  align-items:center;
  gap: 8px;
  padding: 6px 10px;
  border-radius: 999px;
  border: 1px solid rgba(15, 23, 42, 0.10);
  background: white;
  font-size: 12px;
  color: rgba(11, 18, 32, 0.85);
}
.pd-dot {
  width: 8px;
  height: 8px;
  border-radius: 999px;
  background: #22C55E; /* green */
  display:inline-block;
}
.pd-dot.off {
  background: #EF4444; /* red */
}

/* Tile cards */
.pd-tile {
  border-radius: 18px;
  padding: 18px 16px;
  background: #1F5BFF;  /* BLUE background */
  color: #FFFFFF;       /* WHITE text */
  border: 1px solid rgba(255,255,255,0.15);
  box-shadow: 0 8px 18px rgba(31, 91, 255, 0.12);
  transition: transform 120ms ease, box-shadow 120ms ease;
  min-height: 122px;
}
.pd-tile:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 24px rgba(31, 91, 255, 0.18);
}
.pd-tile .pd-tile-title {
  font-size: 16px;
  font-weight: 800;
  line-height: 1.15;
  margin-bottom: 8px;
}
.pd-tile .pd-tile-desc {
  font-size: 13px;
  opacity: 0.92;
  line-height: 1.35;
}
.pd-tile .pd-tile-meta {
  margin-top: 12px;
  font-size: 12px;
  opacity: 0.9;
  display:flex;
  align-items:center;
  justify-content:space-between;
}

/* Streamlit element spacing */
div.block-container { padding-top: 1.1rem; }
section[data-testid="stSidebar"] > div { padding-top: 0.8rem; }

/* Make buttons fill tile card area visually */
.pd-tile-btn button {
  width: 100%;
  height: 100%;
  border-radius: 18px !important;
  padding: 0 !important;
  border: none !important;
  background: transparent !important;
}
.pd-tile-btn button:hover { background: transparent !important; }
</style>
"""


def inject_style() -> None:
    st.markdown(POWERDASH_CSS, unsafe_allow_html=True)
