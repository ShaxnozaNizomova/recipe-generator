import streamlit as st
from recipe_fetcher import get_recipes, get_recipe_details

# Correct Text Colors for Readability
st.markdown(
    """
    <style>
        /* Background */
        .stApp {
            background-color: #F5DEB3; /* Warm wheat */
        }

        /* Headings */
        h1, h2, h3 {
            color: #4A2C2A; /* Dark brown */
            font-family: 'Poppins', sans-serif;
        }

        /* General Text */
        p, span, div {
            color: #5C4033 !important; /* Medium brown */
            font-size: 16px;
        }

        /* Input Box */
        .stTextInput>div>div>input {
            border: 2px solid #D2691E; /* Warm orange */
            border-radius: 10px;
            padding: 10px;
            font-size: 16px;
            background-color: white;
            color: #4A2C2A; /* Dark brown */
        }

        /* Buttons */
        .stButton>button {
            background-color: #D2691E; /* Warm orange */
            color: white;
            border-radius: 10px;
            font-size: 16px;
            padding: 12px;
            transition: 0.3s;
            font-weight: bold;
        }

        .stButton>button:hover {
            background-color: #A0522D; /* Darker brown */
        }

        /* Recipe Cards */
        .recipe-container {
            background-color: #FAE5D3; /* Light beige */
            padding: 20px;
            border-radius: 12px;
            box-shadow: 2px 2px 15px rgba(0, 0, 0, 0.15);
            margin-bottom: 20px;
        }

        .recipe-title {
            font-size: 22px;
            color: #4A2C2A; /* Dark brown */
            font-weight: bold;
        }

        .recipe-info {
            font-size: 18px;
            color: #5C4033; /* Medium brown */
        }

        .recipe-link {
            font-size: 16px;
            font-weight: bold;
            color: #D2691E; /* Orange */
            text-decoration: none;
        }

        .recipe-link:hover {
            text-decoration: underline;
        }
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    st.title("🍽️ AI Recipe Generator")

    ingredients = st.text_input("Enter ingredients (comma-separated):")

    if st.button("Find Recipes"):
        recipes = get_recipes(ingredients)

        if recipes:
            for recipe in recipes:
                recipe_id = recipe['id']
                details = get_recipe_details(recipe_id)

                st.markdown('<div class="recipe-container">', unsafe_allow_html=True)
                st.markdown(f'<h2 class="recipe-title">{recipe["title"]}</h2>', unsafe_allow_html=True)
                st.image(recipe['image'], width=350)
                st.markdown(f'<p class="recipe-info"><strong>Calories:</strong> {details["calories"]} kcal</p>', unsafe_allow_html=True)

                st.write("### Ingredients:")
                for item in details["ingredients"]:
                    st.write(f"- {item}")

                st.write("### Instructions:")
                st.write(details["instructions"])

                st.markdown(
                    f'<a class="recipe-link" href="{details["source_url"]}" target="_blank">📖 Full Recipe Here</a>',
                    unsafe_allow_html=True
                )
                st.markdown('</div>', unsafe_allow_html=True)

        else:
            st.error("No recipes found. Try different ingredients!")

if __name__ == "__main__":
    main()
