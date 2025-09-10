from enum import Enum


class SubscriptionPaidStatus(str, Enum):
    DueSoon = "DueSoon"
    Paid = "Paid"
    Unpaid = "Unpaid"
    Upcoming = "Upcoming"
    
