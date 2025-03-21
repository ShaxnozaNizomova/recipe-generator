import requests
import re
from api_config import SPOONACULAR_API_KEY

def get_recipes(ingredients):
    """Fetch recipes based on user ingredients."""
    url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&number=3&apiKey={SPOONACULAR_API_KEY}"
    response = requests.get(url)
    
    return response.json() if response.status_code == 200 else []

def get_recipe_details(recipe_id):
    """Fetch recipe details: calories, used & missing ingredients, and clean instructions."""
    url = f"https://api.spoonacular.com/recipes/{recipe_id}/information?includeNutrition=true&apiKey={SPOONACULAR_API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Get calories
        calories = "N/A"
        nutrients = data.get("nutrition", {}).get("nutrients", [])
        for nutrient in nutrients:
            if nutrient["name"] == "Calories":
                calories = f"{nutrient['amount']} kcal"
        
        # Get ingredients (used + missing)
        ingredients = [ingredient["original"] for ingredient in data.get("extendedIngredients", [])]
        
        # Clean HTML tags from instructions
        raw_instructions = data.get("instructions", "No instructions available.")
        instructions = re.sub(r'<.*?>', '', raw_instructions)  # Remove HTML tags
        
        return {
            "calories": calories,
            "ingredients": ingredients,
            "instructions": instructions,
            "source_url": data.get("sourceUrl", "#")
        }
    
    return None
