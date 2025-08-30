from enum import Enum


class SubscriptionRecurrence(str, Enum):
    Monthly = "Monthly"
    Yearly = "Yearly"
