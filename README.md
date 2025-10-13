# PlannificationDuManger
Each sunday, there is this dreadful feeling of having to prepare the menu for the whole week. And then, make a grocery list out of it. So Dreadful. So I decided to automatize this process with Generative AI! 


## 1. Defining the Recipe model with Pydantic

To preserve the data integrity of the recipe when I use it either with a LLM or through sending API request, I created pydantic data model for the recipe. You can find it in the file `src/recipe_scheme.py`. It's a basic pydantic model that you can easily modify! 


# TODO

* [x] Create pydantic models for the recipes
* [ ] Create a local MongoDB database
* [ ] Write a FastAPI .py script to communicate with the database
* [ ] Make call API with the Pydantic schema
* [ ] Create a .py script that calls an LLM to get the recipes from different data source
* [ ] Create a dashboard to display the recipes