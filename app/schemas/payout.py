from decimal import Decimal

from app.schemas.common import BaseSchema


class AdvancePayoutResponse(BaseSchema):
    processed: int
    skipped: int


class PayoutResponse(BaseSchema):
    id: int
    sale_id: int
    amount: Decimal
    payout_type: str
    status: str