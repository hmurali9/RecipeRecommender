from flask import Flask, render_template, request

from allFunctions import *
from allClasses import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def get_info():
    result = None
    if request.method == 'POST':
        age = int(request.form['age'])
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        activity = ActivityClass.ActivityOptions(request.form['activity'])
        gender = GenderClass.GenderOptions(request.form['gender'])
        result = BMR_func.BMR_calc(age, height, weight, float(activity.value), gender.value)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run()
