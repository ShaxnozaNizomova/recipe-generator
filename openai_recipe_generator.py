import cohere
import os
from dotenv import load_dotenv

load_dotenv()
cohere_api_key = os.getenv("COHERE_API_KEY")
co = cohere.Client(cohere_api_key)

def generate_recipe_with_cohere(ingredients):
    prompt = f"""
    You are a professional chef. Create a unique recipe using the following ingredients: {ingredients}.
    Provide:
    - A recipe title
    - Approximate calories
    - A list of ingredients
    - Step-by-step instructions
    Make it easy to understand and practical to cook at home.
    """

    response = co.generate(
        model="command",  # Best Cohere model for generation
        prompt=prompt,
        max_tokens=500,
        temperature=0.7
    )

    return response.generations[0].text.strip()
