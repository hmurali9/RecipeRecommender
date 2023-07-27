def BMR_calc(age, height, weight, activity, gender):
    if gender=="Male":
        BMR = 66.5 + (13.75*weight) + (5.003*height) - (6.75*age)
    else:
        BMR = 655.1 + (9.563*weight) + (1.85*height) - (4.676*age)

    return round(activity*BMR, 2)
