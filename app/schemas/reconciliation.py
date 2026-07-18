from app.schemas.common import BaseSchema


class ReconciliationRequest(BaseSchema):
    """Approve or reject a sale."""

    approved: bool


class ReconciliationResponse(BaseSchema):
    sale_id: int
    status: str
    action: str