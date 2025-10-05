from fastapi import FastAPI, BackgroundTasks
from .space_saving import SpaceSavingCounter
from .models import LogEntry, AnalyticsResponse

app = FastAPI(
    title="LogFlow Sketcher",
    description="Educational implementation of real-time log analytics using streaming algorithms. Demonstrates 'Applied Rigor' by bringing theoretical computer science to practical engineering challenges.",
    version="1.0.0",
    docs_url="/"
)

# Initialize streaming algorithms with educational capacities
endpoint_counter = SpaceSavingCounter(capacity=50)   # Track top 50 endpoints
error_counter = SpaceSavingCounter(capacity=20)      # Track top 20 error types

def _process_log_entry(log_entry: LogEntry):
    """
    Background processing using Space-Saving algorithm.
    
    This simulates real-world log processing pipelines where efficiency
    and constant memory usage are critical at scale.
    """
    endpoint_counter.add(log_entry.endpoint)
    if log_entry.status_code >= 400:
        error_counter.add(f"{log_entry.status_code}")

@app.post("/log", response_model=dict)
async def ingest_log(log_entry: LogEntry, background_tasks: BackgroundTasks):
    """
    Ingest a log entry for real-time analysis.
    
    Simulates production log ingestion endpoints used in observability
    platforms and API monitoring systems.
    """
    background_tasks.add_task(_process_log_entry, log_entry)
    return {
        "status": "success", 
        "message": "Log processed by streaming algorithm",
        "philosophy": "learning → applying rigorous CS theory"
    }

@app.get("/analytics/top-endpoints", response_model=AnalyticsResponse)
async def get_top_endpoints(k: int = 10):
    """
    Get most frequently accessed endpoints.
    
    Uses Space-Saving algorithm to provide approximate top-K results
    with guaranteed memory efficiency - essential for high-throughput systems.
    """
    top_endpoints = endpoint_counter.get_top_k(k)
    return AnalyticsResponse(
        data=top_endpoints,
        algorithm="Space-Saving Counter",
        capacity=endpoint_counter.capacity,
        current_items=len(endpoint_counter.counters)
    )

@app.get("/analytics/top-errors", response_model=AnalyticsResponse)
async def get_top_errors(k: int = 10):
    """
    Get most frequent error codes.
    
    Demonstrates how streaming algorithms enable real-time alerting
    and monitoring without expensive storage or processing.
    """
    top_errors = error_counter.get_top_k(k)
    return AnalyticsResponse(
        data=top_errors,
        algorithm="Space-Saving Counter", 
        capacity=error_counter.capacity,
        current_items=len(error_counter.counters)
    )

@app.get("/algorithms/space-saving")
async def algorithm_info():
    """
    Educational endpoint explaining the Space-Saving algorithm.
    
    Shows how theoretical computer science enables practical solutions
    to real-world data streaming challenges.
    """
    return {
        "algorithm": "Space-Saving",
        "purpose": "Find frequent items in data streams with limited memory",
        "use_cases": [
            "Real-time API monitoring",
            "Network traffic analysis", 
            "Error rate detection",
            "Trend identification in high-volume data"
        ],
        "trade_offs": {
            "advantage": "Constant memory usage, real-time processing",
            "limitation": "Approximate counts, not exact frequencies"
        },
        "educational_value": "Bridges theory (streaming algorithms) and practice (observability systems)"
    }
