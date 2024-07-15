from demographics import *


def input_demographics():
    name = input("What is your name? ").strip()
    age = input("What is your age? ").strip()
    sex = input("What is your sex?(M/F): ").lower().strip()
    weight = input("What is your weight?(lb): ").strip()
    goal_weight = input("What is your goal weight?(lb): ").strip()

    return name, age, sex, weight, goal_weight


def get_goals(profile):
    print("""
    1. Gain weight
    2. Lose weight
    3. Maintain weight
    """)
    weight = profile['weight']
    maintain = weight * 15
    pounds = float(0)
    goal = input("What is your goal? ").strip()
    while goal not in ['g', 'l', 'm']:
        goal = input("What is your goal? ").strip()

    if goal == 'g':
        pounds = input("How many pounds do you want to gain a week?(0-2): ").strip()
        calories_per_day = maintain + (((float(pounds)) / 2) * 1000)

    elif goal == 'l':
        pounds = input("How many pounds do you want to lose a week?(0-2): ").strip()
        calories_per_day = maintain - (((float(pounds)) / 2) * 1000)

    elif goal == 'm':
        calories_per_day = maintain

    protein_goal = weight * 0.36
    carbs_goal = calories_per_day * 0.55
    fat_goal = calories_per_day * .25

    return goal, calories_per_day, pounds, protein_goal, carbs_goal, fat_goal
