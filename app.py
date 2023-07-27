from flask import Flask, render_template, request

# import sys
# sys.path.append('allFunctions')
# sys.path.append('allClasses')

from allFunctions.BMR_func import BMR_calc
from allClasses.ActivityClass import ActivityOptions
from allClasses.GenderClass import GenderOptions

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def get_info():
    result = None
    if request.method == 'POST':
        age = int(request.form['age'])
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        activity = ActivityOptions(request.form['activity'])
        gender = GenderOptions(request.form['gender'])
        result = BMR_calc(age, height, weight, float(activity.value), gender.value)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run()
