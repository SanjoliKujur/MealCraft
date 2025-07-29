import pandas as pd
import tensorflow as tf
from collections import Counter

# Load and process recipes
def load_recipes():
    df = pd.read_csv("recipes.csv")
    df['ingredients_list'] = df['ingredients'].apply(lambda x: [i.strip().lower() for i in x.split(',')])
    return df

# Match recipes with ML scoring
def match_recipes(user_input, df):
    user_ingredients = [i.strip().lower() for i in user_input.split(',') if i.strip()]
    matches = []
    
    for _, row in df.iterrows():
        recipe_ingredients = set(row['ingredients_list'])
        user_set = set(user_ingredients)
        common = user_set.intersection(recipe_ingredients)
        
        if common:
            score = len(common) / len(recipe_ingredients) * 100
            matches.append({
                'name': row['name'],
                'instructions': row['instructions'],
                'match_score': round(score, 1),
                'common_ingredients': list(common),
                'missing_ingredients': list(recipe_ingredients - user_set)
            })
    
    return sorted(matches, key=lambda x: x['match_score'], reverse=True)[:8]

df = load_recipes()