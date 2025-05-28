from models.base_model import BaseModel


class RecurringBillsSummary(BaseModel):
    paidAmount: float
    totalUpcomingAmount: float
    dueSoonAmount: float
