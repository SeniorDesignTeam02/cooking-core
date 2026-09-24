from typing import Literal
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Cooking Core API",
    version="0.1.0",
    description="Core backend API for the cooking assistant.",
)

class PingResponse(BaseModel):
    status: Literal["ok"] = "ok"

@app.get("/ping", tags=["Health"])
def ping() -> PingResponse:
    return PingResponse()
