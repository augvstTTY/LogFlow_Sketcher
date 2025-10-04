from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import time
from .space_saving import SpaceSavingCounter

app = FastAPI(title="LogFlow Sketcher", version="1.0.0")

# Initialize our streaming algorithms
endpoint_counter = SpaceSavingCounter(capacity=50)
error_counter = SpaceSavingCounter(capacity=20)

class LogEntry(BaseModel):
    message: str
    endpoint: str
    status_code: int

def process_log_entry(log_entry: LogEntry):
    """Background task to process log entry."""
    endpoint_counter.add(log_entry.endpoint)
    if log_entry.status_code >= 400:
        error_counter.add(f"{log_entry.status_code}")

@app.post("/log")
async def ingest_log(log_entry: LogEntry, background_tasks: BackgroundTasks):
    """Endpoint to receive log entries."""
    background_tasks.add_task(process_log_entry, log_entry)
    return {"status": "success", "message": "Log processed"}

@app.get("/analytics/top-endpoints")
async def get_top_endpoints(k: int = 10):
    top_endpoints = endpoint_counter.get_top_k(k)
    return {"top_endpoints": top_endpoints}

@app.get("/analytics/top-errors")
async def get_top_errors(k: int = 10):
    top_errors = error_counter.get_top_k(k)
    return {"top_errors": top_errors}

@app.get("/")
async def root():
    return {"message": "LogFlow Sketcher - Real-time log analytics"}
