from typing import List

from pydantic import BaseModel


class ProductSchema(BaseModel):
    name: str
    description: str
    price: float
    ingredients: List[str]
    skin_type: List[str]


class SkincareQuestionnaire(BaseModel):
    skin_type: str
    concerns: List[str]
    age_group: str
    budget: float
    preferred_ingredients: List[str] = []
    avoid_ingredients: List[str] = []
