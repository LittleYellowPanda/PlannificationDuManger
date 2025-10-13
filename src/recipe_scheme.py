"""
Data format in pydantic.
Author: YellowPanda

"""

from pydantic import BaseModel, ValidationError, EmailStr
from pydantic import Field
from typing import Optional, Literal
from datetime import date
import json

# Pydantic model for validating user input
class UserInput(BaseModel):
    name: str
    email: EmailStr
    query: str

# Pydantic model for validating ingredient input
class Ingredient(BaseModel):
    name: str
    quantity: int
    unit: str
    note: Optional[str]
    

# Pydantic model for validating recipe input
class BasicRecipe(BaseModel):
    recipe_name: str
    total_preparation_time: int
    origin_area: str
    author: str
    source: Literal["youtube", "book", "picture", "instagram", "blogpost"]
    ingredients: list[Ingredient]
    instructions: list[str]
    notes: Optional[str]



