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
    origin_area: str = Field(..., description="It can be a country, a city, etc.")
    author: str
    source: Literal["youtube", "book", "picture", "instagram", "blogpost"] = Field(..., description="Please add the source used to find the recipe")
    ingredients: list[Ingredient]
    instructions: list[str]
    notes: Optional[str]


# Define a function to handle user input validation safely
def validate_recipe_input(input_data):
    try:
        # Attempt to create a UserInput model instance from user input data
        recipe_input = BasicRecipe(**input_data)
        print(f"✅ Valid recipe input created:")
        print(f"{recipe_input.model_dump_json(indent=2)}")
        return recipe_input
    except ValidationError as e:
        # Capture and display validation errors in a readable format
        print(f"❌ Validation error occurred:")
        for error in e.errors():
            print(f"  - {error['loc'][0]}: {error['msg']}")
        return None