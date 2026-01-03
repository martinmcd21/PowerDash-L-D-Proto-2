# PowerDash Enablement Suite (Capability Enablement & L&D)

This is **not** a traditional LMS.

PowerDash Enablement is a *Capability Enablement Platform* built around:
- **Capabilities + real work contexts** first (not courses)
- Learning as **one** intervention alongside job aids, nudges, guidance, and reflection
- Adult learning principles baked in (relevance, autonomy, respect for experience)
- **Lightweight impact signals** and pattern inference (not heavy surveys or completion vanity metrics)

Everything in the UI is designed to answer:

> **“What do people need to do better at work, right now — and how can AI help?”**

---

## What’s Included (MVP Scaffold)

Tiles (in order):
1. **Capability Architecture** – define what “good” looks like
2. **Performance Signals** – capture weak signals (reflection + observation prompts)
3. **Enablement Interventions** – generate the smallest helpful artefact first
4. **In-Flow Support** – lightweight prompts and decision support while working
5. **Capability Insights** – plain-English summaries + what to do next

MVP focus:
- Capability definition engine
- Signal collection
- Intervention generator
- Insight summaries
- Clean navigation between tiles

Avoided intentionally:
- Full LMS features
- User management complexity
- Over-engineered analytics

---

## Tech Stack

- Python
- Streamlit
- Modular, production-ready structure with clear separation of:
  - UI
  - AI logic
  - Data handling
  - Configuration

---

## Run Locally

### 1) Create and activate a virtual env
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
```

### 3) Configure models (and optionally API key)
Copy/edit the default config:
```bash
cp config/config.example.yaml config/config.yaml
```

If using OpenAI:
- set `OPENAI_API_KEY` in your environment

### 4) Run
```bash
streamlit run app.py
```

---

## How to Extend / Add Tiles

Each tile is a module in:
- `src/powerdash_enablement/pages/`

To add a tile:
1. Create `src/powerdash_enablement/pages/your_tile.py` with a `render(app_state)` function
2. Register it in `src/powerdash_enablement/pages/registry.py`
3. Add a tile definition in `src/powerdash_enablement/ui/tiles.py`

---

## Notes on Branding / UI

This scaffold includes a PowerDash-style layout:
- Always-visible left sidebar
- Top header with suite name + connection status
- Clickable **blue tiles with white text**
- Rounded corners, consistent spacing, clean enterprise-safe language

You can further tune CSS in:
- `src/powerdash_enablement/ui/style.py`

---

## Repo Layout

```
powerdash_enablement_suite/
  app.py
  config/
    config.example.yaml
    config.yaml                # (ignored in git)
  src/
    powerdash_enablement/
      ai/
      config/
      data/
      pages/
      ui/
  .streamlit/
    config.toml
  requirements.txt
  .gitignore
```

---

## Disclaimer

This repo is a **commercial-grade scaffold**: navigation, layout, config, and placeholder AI flows are implemented.
Replace the mock AI provider with a real provider and refine prompts + persistence for production.
