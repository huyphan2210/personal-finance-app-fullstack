from enum import Enum


class SubscriptionPaidStage(str, Enum):
    DueSoon = "DueSoon"
    Paid = "Paid"
    Unpaid = "Unpaid"
    Upcoming = "Upcoming"
    
