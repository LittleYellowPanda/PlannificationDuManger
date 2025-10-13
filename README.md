# PlannificationDuManger
Each sunday, there is this dreadful feeling of having to prepare the menu for the whole week. And then, make a grocery list out of it. So Dreadful. So I decided to automatize this process with Generative AI! 


## 1. Defining the Recipe model with Pydantic

To preserve the data integrity of the recipe when I will use it either with a LLM or through sending API request, I created pydantic data model for the recipe. You can find it in the file `config.recipe_model.json`. 
