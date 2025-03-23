import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
API_KEY = os.getenv("SPOONACULAR_API_KEY")
SEARCH_URL = "https://api.spoonacular.com/recipes/complexSearch"
DETAILS_URL = "https://api.spoonacular.com/recipes/{id}/information"

# Function to fetch recipes
def fetch_recipes(ingredients, diet, meal_type, calories):
    params = {
        "includeIngredients": ingredients,  # Use this instead of "query"
        "diet": diet if diet.lower() != "none" else "",
        "type": meal_type if meal_type.lower() != "none" else "",
        "maxCalories": calories,
        "apiKey": API_KEY,
        "number": 10
    }
    response = requests.get(SEARCH_URL, params=params)
    if response.status_code == 200:
        return response.json().get("results", [])
    return []


# Function to fetch recipe details (ingredients + instructions)
def fetch_recipe_details(recipe_id):
    response = requests.get(DETAILS_URL.format(id=recipe_id), params={"apiKey": API_KEY})
    if response.status_code == 200:
        details = response.json()
        
        # Extract key details
        ingredients = [ing["original"] for ing in details.get("extendedIngredients", [])]
        instructions = details.get("instructions", "No instructions available.")
        
        # Extract calories
        nutrients = details.get("nutrition", {}).get("nutrients", [])
        calories = next((n["amount"] for n in nutrients if n["name"] == "Calories"), "N/A")
        
        return {
            "title": details.get("title"),
            "image": details.get("image"),
            "ingredients": ingredients,
            "instructions": instructions,
            "calories": calories
        }
    return {}

# Testing API
if __name__ == "__main__":
    test_recipes = fetch_recipes("chicken", "None", "Dinner", 500)
    if test_recipes:
        test_details = fetch_recipe_details(test_recipes[0]["id"])
        print(test_details)
    else:
        print("No recipes found.")
