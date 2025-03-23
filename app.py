import streamlit as st
from spoonacular_recipe_fetcher import fetch_recipes, fetch_recipe_details

def main():
    st.set_page_config(page_title="Recipe Generator", layout="wide")

    # Load custom CSS
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Title
    title_text = "Recipe Generator"
    animated_title = "".join(f"<span>{char}</span>" for char in title_text)
    st.markdown(f"<h1 class='animated-title'>{animated_title}</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Find the best recipes based on your preferences!</p>", unsafe_allow_html=True)

    # Sidebar for filters
    with st.sidebar:
        st.header("Filter Your Search")
        query = st.text_input("Enter an ingredient:")
        diet = st.selectbox("Diet Preference:", ["None", "Vegetarian", "Vegan", "Gluten-Free"])
        meal_type = st.selectbox("Meal Type:", ["None", "Breakfast", "Lunch", "Dinner"])
        calories = st.slider("Max Calories:", 50, 1000, 500)

    if st.button("Find Recipes"):
        # Check if query is empty or contains only spaces
        if not query.strip():
            st.warning("Please enter at least one ingredient.")
        else:
            # Proceed to fetch recipes if query is valid
            recipes = fetch_recipes(query, diet, meal_type, calories)

            if recipes:
                st.markdown("<h2>Recipes Found:</h2>", unsafe_allow_html=True)
                for recipe in recipes:
                    details = fetch_recipe_details(recipe["id"])
                    ingredients_list = "".join(f"<li>{ing}</li>" for ing in details["ingredients"])

                    st.markdown(f"""
                        <div class='recipe-card'>
                            <img src='{details["image"]}' class='recipe-img'>
                            <h3>{details["title"]}</h3>
                            <p><b>Calories:</b> {details["calories"]} kcal</p>
                            <p><b>Ingredients:</b></p>
                            <ul>{ingredients_list}</ul>
                            <p><b>Instructions:</b></p>
                            <p>{details["instructions"]}</p>
                        </div>
                    """, unsafe_allow_html=True)
            else:
                st.warning("No recipes found. Try different filters.")

if __name__ == "__main__":
    main()
