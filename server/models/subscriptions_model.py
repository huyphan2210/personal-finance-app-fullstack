from datetime import datetime
from enums.subscriptions.subscription_recurrence_enum import SubscriptionRecurrence
from enums.subscriptions.subscription_status_enum import SubscriptionStatus
from models.base_model import BaseModel


class RecurringBillsSummary(BaseModel):
    paidAmount: float
    totalUpcomingAmount: float
    dueSoonAmount: float


class Subscription(BaseModel):
    avatarUrl: str
    user: str
    dueDate: datetime
    amount: float
    recurrence: SubscriptionRecurrence
    status: SubscriptionStatus

class SubscriptionsContent(BaseModel):
    subscriptions: list[Subscription]
    numberOfPages: int
    currentPage: int