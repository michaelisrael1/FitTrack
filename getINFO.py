import json
from PyQt6.QtWidgets import *
from gui import *


def input_demographics():
    """Takes demographic input from user and returns it in proper order for class"""
    name = input("What is your name? ").strip()
    age = input("What is your age? ").strip()
    sex = input("What is your sex?(M/F): ").lower().strip()
    weight = input("What is your weight?(lb): ").strip()
    goal_weight = input("What is your goal weight?(lb): ").strip()

    return name, age, sex, weight, goal_weight


def get_goals(goal, pounds_week=0):
    """Finds the daily intake needs to reach the goal provided, and returns the numbers for input into a class"""
    weight = get_weight()
    maintain = weight * 15

    if goal == 'g':
        calories_per_day = maintain + (((float(pounds_week)) / 2) * 1000)

    elif goal == 'l':
        calories_per_day = maintain - (((float(pounds_week)) / 2) * 1000)

    elif goal == 'm':
        calories_per_day = maintain

    protein_goal = weight * 0.36
    carbs_goal = calories_per_day * 0.55
    fat_goal = calories_per_day * .25

    return goal, calories_per_day, pounds_week, protein_goal, carbs_goal, fat_goal, weight


def update_weight():
    new_weight = {}
    done = False
    while not done:
        try:
            new_weight['weight'] = float(input('Please enter your updated weight: '))
            done = True
        except ValueError:
            print('Error only enter numbers ')
    return get_goals(new_weight)


def extract_info():
    info = []
    with open("demographics.json", 'r') as f:
        data = json.load(f)
        data = list(data.values())
    return data


def get_weight():
    with open('demographics.json', 'r') as f:
        data = json.load(f)
        weight = data['weight']
    return weight
