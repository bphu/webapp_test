from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import random
from pathlib import Path

app = FastAPI()

# Mount the config directory to serve static files
app.mount("/config", StaticFiles(directory="config"), name="config")


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
