import pandas as pd

def read_data():
    df_recipes = pd.read_csv("./data/Recipes.csv")
    df_ing = pd.read_csv("./data/Ingredients.csv")
    df_rec2ing = pd.read_csv("./data/Rec2Ing.csv")

    return df_recipes, df_ing, df_rec2ing
