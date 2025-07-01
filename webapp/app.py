from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
import os

app = FastAPI()

# Mount static files (CSS, icons) using absolute path
static_dir = os.path.join(os.path.dirname(__file__), 'static')
app.mount('/static', StaticFiles(directory=static_dir), name='static')

# Jinja2 environment
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
env = Environment(
    loader=FileSystemLoader(template_dir),
    autoescape=select_autoescape(['html', 'xml'])
)

# Load all JSON files from ../sections/
def load_resume_data():
    data = {}
    sections_dir = os.path.join(os.path.dirname(__file__), '../sections')
    for fname in os.listdir(sections_dir):
        if fname.endswith('.json'):
            with open(os.path.join(sections_dir, fname), 'r') as f:
                data[fname.replace('.json', '')] = json.load(f)
    return data

@app.get('/', response_class=HTMLResponse)
async def homepage(request: Request):
    resume_data = load_resume_data()
    template = env.get_template('index.html')
    # Expose state and logic in the template context
    return template.render(request=request, resume=resume_data, state=resume_data)

@app.get('/state', response_class=JSONResponse)
async def state():
    # Expose all loaded JSON data as JSON
    return load_resume_data()

# Example: serve a JSON file directly for inspection
@app.get('/state/{section}', response_class=FileResponse)
async def state_section(section: str):
    path = os.path.join(os.path.dirname(__file__), '../sections', f'{section}.json')
    if os.path.exists(path):
        return FileResponse(path)
    return JSONResponse({'error': 'Section not found'}, status_code=404)

# Comments and state exposure are present throughout for transparency. 