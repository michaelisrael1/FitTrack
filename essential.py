import json
from typing import Any, Dict, List, Union


def data_at_date(date: str, file: str) -> Union[Dict[str, Any], Dict]:
    """
    Reads file and extracts if value exists at key, the value is returned.

    :param date: The date to look for in the file
    :param file: The file to read from
    :return: The data at the specified date or an empty dictionary if not found
    """
    with open(file, 'r') as f:
        data = json.load(f)
    if date in data:
        return data[date]
    else:
        return {}


def food_log_data(date: str) -> List[str]:
    """
    Get the food log data for a specific date.

    :param date: The date to get the food log data for
    :return: A list of formatted strings containing food log data
    """
    with open('food_data.json', 'r') as f:
        data = json.load(f)
    food_list = data[date]

    formatted_list = []
    for i, food in enumerate(food_list, start=1):
        formatted_string = f"{i}. {food['name']} - Calories: {food['calories']}, Protein: {food['protein']}, Fat: {food['fat']}, Carbs: {food['carbs']}"
        formatted_list.append(formatted_string)

    return formatted_list


def get_sum(name: str, date: str, file: str) -> float:
    """
    Gets sum of numbers stored in json.

    :param name: The name of the nutrient to sum
    :param date: The date to get the data for
    :param file: The file to read from
    :return: The sum of the specified nutrient
    """
    food = data_at_date(date, file)
    total = sum(i[name] for i in food)
    return total


def get_goal(name: str, file: str) -> Dict[str, Any]:
    """
    Gets daily goals from the file.

    :param name: The name of the goal to get
    :param file: The file to read from
    :return: The goal data
    """
    goal = data_at_date(name, file)
    return goal


def get_remaining(goal: float, current: float) -> float:
    """
    Calculate the remaining amount to reach the goal.

    :param goal: The goal amount
    :param current: The current amount
    :return: The remaining amount to reach the goal
    """
    if goal - current <= 0:
        remaining = 0
    else:
        remaining = goal - current
    return remaining
