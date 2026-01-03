from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict

from ..config.state import AppState

RenderFn = Callable[[AppState], None]


@dataclass(frozen=True)
class PageDef:
    key: str
    title: str
    render: RenderFn


def get_pages() -> Dict[str, PageDef]:
    from .home import render as render_home
    from .capability_architecture import render as render_capability
    from .performance_signals import render as render_signals
    from .enablement_interventions import render as render_interventions
    from .inflow_support import render as render_inflow
    from .capability_insights import render as render_insights

    pages = [
        PageDef("home", "Home", render_home),
        PageDef("capability_architecture", "Capability Architecture", render_capability),
        PageDef("performance_signals", "Performance Signals", render_signals),
        PageDef("enablement_interventions", "Enablement Interventions", render_interventions),
        PageDef("inflow_support", "In-Flow Support", render_inflow),
        PageDef("capability_insights", "Capability Insights", render_insights),
    ]
    return {p.key: p for p in pages}
