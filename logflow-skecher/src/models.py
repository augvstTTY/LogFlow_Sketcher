from pydantic import BaseModel

class LogEntry(BaseModel):
    """Model for log entry data - represents real-world API log structure."""
    message: str
    endpoint: str
    status_code: int

class AnalyticsResponse(BaseModel):
    """Standard response format for analytics endpoints."""
    data: list
    algorithm: str
    capacity: int
    current_items: int
