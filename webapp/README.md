# Resume Web App

## Philosophy
- Terminal-style dark, dense, square edges, emergent over prescribed aesthetics.
- Expose state and inner workings. Verbosity over opacity.
- Explicit is better than implicit. Performance is design.
- Regiment functionalism. Engineered for human vision and perception.
- Flat, not hierarchical. Complex as needed, not minimal.
- Driven by objective reasoning and common sense. No infantilization.
- Timeless, unfashionable, ignores trends.

## Stack
- **Backend:** FastAPI (async, explicit, modern Python)
- **Frontend:** HTMX (dynamic, dense, interactive UI)
- **Templating:** Jinja2 (content from JSON)
- **Styling:** US Graphics CSS (terminal dark, square, dense)

## Directory Structure
- `static/` — CSS, JS, icons (US Graphics CSS included)
- `templates/` — Jinja2 HTML templates
- `state/` — Exposed app state, JSON
- `utils/` — JSON parsing, state exposure, helpers
- `app.py` — Main FastAPI app
- `requirements.txt` — Python dependencies

## How to Run
- **Recommended:** Use [uv](https://github.com/astral-sh/uv) for fast, modern Python environment and dependency management.

1. Create and activate a virtual environment:
   ```sh
   uv venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```sh
   uv pip install -r requirements.txt
   ```
3. Run the app:
   ```sh
   uvicorn app:app --reload
   ```
4. Visit: [http://localhost:8000](http://localhost:8000)

## Content
- All resume content is generated from JSON files or via Jinja2 templates.
- State and logic are exposed for user inspection.

---

**Design is performance. Complexity is not hidden. This is a tool for humans.** 