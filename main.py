from allFunctions import *
from allClasses import *

recipes, ingredients, rec2ing = readdata.read_data()

recipes = recipefilters.Recommender(recipes, ingredients, rec2ing)

print(recipes.ind_recipes(3, 2345.77/3, [''], 'Vegan', ['']))
