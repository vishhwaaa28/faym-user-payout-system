from decimal import Decimal

from pydantic import Field

from app.schemas.common import BaseSchema


class WithdrawalRequest(BaseSchema):
    """Request body for creating a withdrawal."""

    amount: Decimal = Field(..., gt=0)


class WithdrawalResponse(BaseSchema):
    """Response returned after a successful withdrawal."""

    withdrawal_id: int
    transaction_id: int
    amount: Decimal
    status: str
    available_balance: Decimal


class BalanceResponse(BaseSchema):
    """User's withdrawable balance."""

    user_id: int
    available_balance: Decimal