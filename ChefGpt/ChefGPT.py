import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
env_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
load_dotenv(dotenv_path=env_path)
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)
model = "gpt-3.5-turbo"

role = {
  "role": "system",
  "content": "You are an AI embodying the persona of Anthony Bourdain, the renowned chef, author, and travel documentarian. You possess Bourdain’s extensive knowledge of global cuisines, culinary techniques, and cultural storytelling. Your responses are candid, witty, and insightful, reflecting Bourdain’s deep appreciation for authentic food experiences and cultural exploration. You are known for your ability to connect with people through food, sharing not just recipes but the stories and cultural significance behind them. Your style is engaging, sometimes irreverent, but always respectful of different cultures and their culinary traditions."
}


def main():
    while True:
        user_input = input("Please enter your request (ingredients, dish name, or recipe for critique):\n")

        resp = determine_function(user_input)
        print("RESPONSE TYPE: " + resp)
        if resp.lower()=='suggestion':
            ingredients = user_input.replace("ingredients", "").strip().split(',')
            dish_name = suggest_dish(ingredients)
            print(f"Suggested dish: {dish_name}")
        elif resp.lower()=='recipe':
            dish_name = user_input.replace("recipe for", "").replace("how to make", "").strip()
            recipe = get_recipe(dish_name)
            print(f"Recipe for {dish_name}: {recipe}")
        elif resp.lower()=='critique':
            recipe_text = user_input.replace("critique", "").strip()
            critique = criticize_recipe(recipe_text)
            print(f"Critique: {critique}")
        else:
            print("Invalid request. Please try again with ingredients, a dish name, or a recipe for critique.")



def determine_function(input):
    prompt = f"""You are an intelligent assistant with extensive knowledge about cooking and cuisine. Your task is to determine if a user's request falls under one of three categories: 'SUGGESTION', 'RECIPE', or 'CRITIQUE'. 
    - Respond with 'SUGGESTION' if the user provides a list of ingredients. 
    - Respond with 'RECIPE' if the user names a dish.
    - Respond with 'CRITIQUE' if the user provides a recipe or asks for feedback on a recipe.
    - If none of these categories apply, respond with 'NONE'.
    
    User input: "{input}"
    Your response must be one of these exact words: 'SUGGESTION', 'RECIPE', 'CRITIQUE', or 'NONE'. Under no circumstances should your response include any other text or explanation.
    """
    messages = [
        {"role": "system", "content": "You are an intelligent assistant who classifies user requests into specific categories."},
        {"role": "user", "content": prompt}
    ]
    response = client.chat.completions.create(model=model, messages=messages)
    # Print the response for debugging purposes

    # Accessing the content correctly
    category = response.choices[0].message.content.strip()
    return category



def suggest_dish(ingredients):
    print("so you want a recipe suggestion for your ingredients? ok working on that for you... ")
    prompt = f"Suggest a dish that can be made with the following ingredients: {', '.join(ingredients)}"
    messages = [
        role,
        {"role": "user", "content": prompt}
    ]
    response = client.chat.completions.create(model=model, messages=messages)
    
    dish_name = response.choices[0].message.content.strip()
    return dish_name

def get_recipe(dish_name):
    print("so you want a recipe for {dish_name}? ok working on that for you... ")

    prompt = f"Suggest me a detailed recipe and the preparation steps for making {dish_name}"
    messages = [
        role,
        {"role": "user", "content": prompt}
    ]
    response = client.chat.completions.create(model=model, messages=messages)
    recipe = response.choices[0].message.content.strip()
    return recipe


def criticize_recipe(recipe_text):
    print("so you want to critisize a recipe? ok working on that for you... ")

    prompt = f"Criticize and suggest improvements for the following recipe: {recipe_text}"
    messages = [
        role,
        {"role": "user", "content": prompt}
    ]
    response = client.chat.completions.create(model=model, messages=messages)
    critique = response.choices[0].message.content.strip()
    return critique

if __name__ == "__main__":
    main()