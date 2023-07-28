import random
import numpy as np


class Recommender:

    def __int__(self, df_recipes, df_ing, df_rec2ing):
        self.recipes = df_recipes
        self.ing = df_ing
        self.rec2ing = df_rec2ing

    def allergy_filter(self, allergies):

        if len(allergies) >= 1 and allergies[0] != '':

            alg = [i + '*' for i in allergies]

            # get all ingredients whose name matches the allergies; merge it with rec2ing to get a list of recipeIDs
            dfi = self.ing[self.ing.IngredientName.str.lower().str.contains('|'.join(alg), na=False, regex=True)]
            rec2ingID_list = list(self.rec2ing.merge(dfi, on='IngredientID')['RecipeID'])

            # get all recipes whose title matches the allergies
            recList = list(
                self.recipes[self.recipes.Title.str.lower().str.contains('|'.join(alg), na=False, regex=True)][
                    'RecipeID'])
            recList.append(rec2ingID_list)
            dfr = self.recipes[~self.recipes.RecipeID.isin(recList)]
        else:
            dfr = self.recipes

        return dfr

    # Filter the inputted df using the isVegan attribute based on user input

    def vegan_filter(self, vegan, dfr):

        if vegan == 'Vegan':
            df = dfr[dfr.isVegan == '1']
        elif vegan == "Strictly not vegan":
            df = dfr[dfr.isVegan == '0']
        else:
            df = dfr

        return df

    # Exactly the same as allergy_filter. Only this time we return the df elemtns containing the search_term

    def search_filter(self, search_term, df):

        if len(search_term) >= 1 and search_term[0] != '':

            srch = [i + '*' for i in search_term]

            # get all ingredients whose name matches the allergies; merge it with rec2ing to get a list of recipeIDs
            dfi = self.ing[self.ing.IngredientName.str.lower().str.contains('|'.join(srch), na=False, regex=True)]
            rec2ingID_list = list(self.rec2ing.merge(dfi, on='IngredientID')['RecipeID'])

            # get all recipes whose title matches the allergies
            recList = list(df[df.Title.str.lower().str.contains('|'.join(srch), na=False, regex=True)]['RecipeID'])
            recList.append(rec2ingID_list)
            dfr = df[df.RecipeID.isin(recList)]
        else:
            dfr = df

        return dfr

    # Filters based on calculated nutritional facts adding a +/- 10% buffer

    def cal_filter(self, cal, protein, fat, df):
        return df[(df.Calories >= 0.9 * cal) & (df.Calories <= 1.1 * cal) & (df.Protein >= 0.9 * protein) & (
                    df.Protein >= 0.9 * protein)
                  & (df.Fats >= 0.9 * fat) & (df.Fats >= 0.9 * fat)]

    # Incorporates the above functions to return a list of recipe IDs for individual recipe search

    def ind_recipes(self, x, cals, protein, fat, search_term, vegan, allergies):

        df = self.cal_filter(cals, protein, fat,
                             self.search_filter(search_term,
                                                self.vegan_filter(vegan,
                                                                  self.allergy_filter(allergies))))

        df = df[df.No_of_reviews >= 10]
        df['score'] = (df.Average_rating * np.log10(df.No_of_reviews)) - (x * df.Prep_time / 60)
        df.sort_values('score', ascending=False, inplace=True)

        ind_list = list(df['RecipeID'].iloc[0:14])
        filtered_list = random.sample(ind_list, k=5)

        return filtered_list

    # Uses the above functions (not ind_recipes) to return a list of lists
    # Each child list corresponds to the meals (so 4 child lists for 4 meals/day)
    # Each element in the child list corresponds to the recipe options user can select from (3/5 options per child list - defined by k)

    def meal_plan(self, x, cals, protein, fat, vegan, allergies, meals):

        df = self.cal_filter(cals, protein, fat,
                             self.vegan_filter(vegan,
                                               self.allergy_filter(allergies)))

        df = df[df.No_of_reviews >= 10]
        df['score'] = (df.Average_rating * np.log10(df.No_of_reviews)) - (x * df.Prep_time / 60)
        df.sort_values('score', ascending=False, inplace=True)

        ind_list = list(df['RecipeID'].iloc[0:5 * meals])
        filtered_list = [random.sample(ind_list, k=3) for i in range(0, meals)]

        return filtered_list
