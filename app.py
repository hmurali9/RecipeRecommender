from flask import Flask, render_template, request, redirect, url_for

from allFunctions import *
from allClasses import *

app = Flask(__name__)

# Read data - filepath hardcoded
recipes, ingredients, rec2ing = readdata.read_data()
recipe = recipefilters.Recommender(recipes, ingredients, rec2ing)


@app.route('/', methods=['GET', 'POST'])
def get_info():
    return render_template('homepage.html')


@app.route('/results', methods=['POST'])
def results():
    age = int(request.form['age'])
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    activity = ActivityClass.ActivityOptions(request.form['activity'])
    gender = GenderClass.GenderOptions(request.form['gender'])
    mealtype = MealTypeClass.MealTypeOptions(request.form['mealtype'])
    preptime = PrepTimeClass.PrepTimeOptions(request.form['preptime'])
    allergies = request.form['allergies']
    searchterm = request.form['searchterm']
    vegan = VeganClass.VeganOptions(request.form['vegan'])
    meals = int(request.form['servings'])

    cals = BMR_func.BMR_calc(age, height, weight, float(activity.value), gender.value)

    if mealtype.value == "Individual Recipe":
        recipe_ids = recipe.ind_recipes(int(preptime.value), cals/meals, searchterm, vegan.value, allergies)
    else:
        recipe_ids = recipe.meal_plan(int(preptime.value), cals, vegan.value, allergies, meals)

    return render_template('results.html', entry=recipe_ids)


if __name__ == '__main__':
    app.run(debug=True)
