from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import random
import json
from pathlib import Path

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
