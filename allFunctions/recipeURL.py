def urlCreation(recipe_ids, df):
    df = df[df.RecipeID.isin(recipe_ids)]

    df['URL'] = 'https://www.allrecipes.com/recipe/' + df.RecipeID.map(str) + "/" + df['Title'].str.replace(r"[(',)]", "", regex=True).str.replace(r" ", "-", regex=True).map(str)

    return df
