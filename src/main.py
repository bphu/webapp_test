from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import random
import json
from pathlib import Path

# Load configuration
config_path = Path(__file__).parent.parent / "config" / "config.json"
with open(config_path, 'r') as f:
    config_data = json.load(f)

# Extract mount configuration (first item has api_base_url and other settings)
config_dict = config_data[0] if isinstance(config_data, list) else config_data

app = FastAPI()

# Mount the config directory to serve static files using relative path from config
config_dir = Path(__file__).parent.parent / "config"
app.mount("/config", StaticFiles(directory=str(config_dir)), name="config")


@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the HTML page"""
    html_file = Path(__file__).parent / "index.html"
    return html_file.read_text()


class EchoRequest(BaseModel):
    message: str


class EchoResponse(BaseModel):
    message: str
    random_number: int


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


@app.post("/echo")
async def echo(request: EchoRequest) -> EchoResponse:
    """Echo endpoint that returns the message with a random number"""
    return EchoResponse(
        message=request.message,
        random_number=random.randint(1, 1000)
    )
