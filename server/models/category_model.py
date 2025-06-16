from enum import Enum


class Category(str, Enum):
    Entertainment = "Entertainment"
    Bills = "Bills"
    DiningOut = "Dining Out"
    PersonalCare = "Personal Care"
    General = "General"
