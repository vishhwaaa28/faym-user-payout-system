from enum import Enum


class SaleStatus(str, Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"


class PayoutType(str, Enum):
    ADVANCE = "ADVANCE"
    FINAL = "FINAL"
    ADJUSTMENT = "ADJUSTMENT"
    RECOVERY = "RECOVERY"


class PayoutStatus(str, Enum):
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


class WithdrawalStatus(str, Enum):
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"


class TransactionStatus(str, Enum):
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    REJECTED = "REJECTED"
    CANCELLED = "CANCELLED"