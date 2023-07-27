from flask import Flask, render_template, request
from enum import Enum

app = Flask(__name__)

def BMR_calc(age, height, weight, activity, gender):
    if gender=="Male":
        BMR = 66.5 + (13.75*weight) + (5.003*height) - (6.75*age)
    else:
        BMR = 655.1 + (9.563*weight) + (1.85*height) - (4.676*age)

    activity_dict = {'Sedentary':1.2,
                    'Lightly active': 1.375,
                    'Moderatly active': 1.55,
                    'Very active': 1.725,
                    'Extra active': 1.9}

    return round(activity_dict[activity]*BMR, 2)

class ActivityOptions(Enum):
    Option1 = 'Sedentary'
    Option2 = 'Lightly active'
    Option3 = 'Moderatly active'
    Option4 = 'Very active'
    Option5 = 'Extra active'

class GenderOptions(Enum):
    Option1 = 'Male'
    Option2 = 'Female'
    Option3 = 'Rather not say'

@app.route('/', methods=['GET', 'POST'])
def get_info():
    result = None
    if request.method == 'POST':
        age = int(request.form['age'])
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        activity = ActivityOptions(request.form['activity'])
        gender = GenderOptions(request.form['gender'])
        result = BMR_calc(age, height, weight, activity.value, gender.value)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run()
