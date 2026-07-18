from typing import Generator

from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import SessionLocal

from app.repositories.sale_repository import SaleRepository
from app.repositories.payout_repository import PayoutRepository
from app.repositories.withdrawal_repository import WithdrawalRepository
from app.repositories.payment_transaction_repository import (
    PaymentTransactionRepository,
)

from app.services.advance_service import AdvancePayoutService
from app.services.reconciliation_service import ReconciliationService
from app.services.withdrawal_service import WithdrawalService


def get_db() -> Generator[Session, None, None]:
    """
    Provide a database session per request.
    """
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# -----------------------
# Repository Dependencies
# -----------------------

def get_sale_repository(
    db: Session = Depends(get_db),
) -> SaleRepository:
    return SaleRepository(db)


def get_payout_repository(
    db: Session = Depends(get_db),
) -> PayoutRepository:
    return PayoutRepository(db)


def get_withdrawal_repository(
    db: Session = Depends(get_db),
) -> WithdrawalRepository:
    return WithdrawalRepository(db)


def get_payment_transaction_repository(
    db: Session = Depends(get_db),
) -> PaymentTransactionRepository:
    return PaymentTransactionRepository(db)


# -----------------------
# Service Dependencies
# -----------------------

def get_advance_service(
    sale_repo: SaleRepository = Depends(get_sale_repository),
    payout_repo: PayoutRepository = Depends(get_payout_repository),
) -> AdvancePayoutService:
    return AdvancePayoutService(
        sale_repo,
        payout_repo,
    )


def get_reconciliation_service(
    sale_repo: SaleRepository = Depends(get_sale_repository),
    payout_repo: PayoutRepository = Depends(get_payout_repository),
) -> ReconciliationService:
    return ReconciliationService(
        sale_repo,
        payout_repo,
    )


def get_withdrawal_service(
    payout_repo: PayoutRepository = Depends(get_payout_repository),
    withdrawal_repo: WithdrawalRepository = Depends(
        get_withdrawal_repository
    ),
    payment_repo: PaymentTransactionRepository = Depends(
        get_payment_transaction_repository
    ),
) -> WithdrawalService:
    return WithdrawalService(
        payout_repo,
        withdrawal_repo,
        payment_repo,
    )