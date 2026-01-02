"""FastAPI entrypoint for exchanging workflow ids for ChatKit client secrets."""

from __future__ import annotations

import json
import os
import uuid
from typing import Any, Mapping

import httpx
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# ... (all your imports and setup)

@app.get("/")
async def root() -> Mapping[str, str]:
    return {"status": "ok"}

@app.get("/health")
async def health() -> Mapping[str, str]:
    return {"status": "ok"}

@app.post("/api/create-session")
async def create_session(request: Request) -> JSONResponse:
    """Exchange a workflow id for a ChatKit client secret."""
    # ... all your real code here

# ... (all your helper functions)
