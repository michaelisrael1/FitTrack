import json
from PyQt6.QtWidgets import *
from gui import *


def get_goals(goal: str, pounds_week: float = 0) -> tuple:
    """
    Finds the daily intake needs to reach the goal provided, and returns the numbers for input into a class.

    :param goal: The type of goal (e.g., maintain, gain, lose)
    :param pounds_week: The weight goal in pounds per week
    :return: A tuple containing goal type, daily calorie intake, weight goal, protein goal, carbohydrate goal, fat goal, and current weight
    """
    weight = get_weight()
    maintain = weight * 15

    if goal == 'gain':
        calories_per_day = maintain + (((float(pounds_week)) / 2) * 1000)

    elif goal == 'lose':
        calories_per_day = maintain - (((float(pounds_week)) / 2) * 1000)

    elif goal == 'maintain':
        calories_per_day = maintain

    protein_goal = weight * 0.36
    carbs_goal = calories_per_day * 0.55
    fat_goal = calories_per_day * .25

    return goal, calories_per_day, pounds_week, protein_goal, carbs_goal, fat_goal, weight


def extract_info() -> list:
    """
    Extract information from the demographics JSON file.

    :return: A list of demographic information
    """
    info = []
    with open("demographics.json", 'r') as f:
        data = json.load(f)
        data = list(data.values())
    return data


def get_weight() -> float:
    """
    Get the current weight from the demographics JSON file.

    :return: The current weight
    """
    with open('demographics.json', 'r') as f:
        data = json.load(f)
        weight = data['weight']
    return weight
