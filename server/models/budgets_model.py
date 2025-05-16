from models.base_model import BaseModel
from models.category_model import Category


class Budget(BaseModel):
    maximum: float
    category: Category
