from enum import Enum


class SubscriptionStatus(str, Enum):
    Active = "Active"
    Inactive = "Inactive"
