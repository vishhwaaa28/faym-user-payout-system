from pydantic import BaseModel, ConfigDict


class MessageResponse(BaseModel):
    """Generic success/error message."""

    message: str


class HealthResponse(BaseModel):
    """Health check response."""

    status: str


class ErrorResponse(BaseModel):
    """Generic API error."""

    detail: str


class BaseSchema(BaseModel):
    """Base schema configuration."""

    model_config = ConfigDict(from_attributes=True)