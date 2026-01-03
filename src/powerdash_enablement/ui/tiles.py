from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Tile:
    key: str
    icon: str
    title: str
    desc: str


TILES: list[Tile] = [
    Tile(
        key="capability_architecture",
        icon="🧩",
        title="Capability Architecture",
        desc="Define what “good” looks like: capability map, behaviours, work contexts, indicators.",
    ),
    Tile(
        key="performance_signals",
        icon="📡",
        title="Performance Signals",
        desc="Capture weak signals: reflection, manager observations, confidence check-ins, patterns.",
    ),
    Tile(
        key="enablement_interventions",
        icon="🛠️",
        title="Enablement Interventions",
        desc="Generate the smallest helpful support first: job aids, checklists, guides, prompts.",
    ),
    Tile(
        key="inflow_support",
        icon="⚡",
        title="In-Flow Support",
        desc="Support while working: contextual prompts, pre-task nudges, post-action reflection.",
    ),
    Tile(
        key="capability_insights",
        icon="📈",
        title="Capability Insights",
        desc="See what’s improving and what to do next: health, gaps, effective interventions.",
    ),
]
