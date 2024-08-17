import json


def data_at_date(date, file):
    """Reads file and extracts if value exists at key, the value is returned"""
    with open(file, 'r') as f:
        data = json.load(f)
    if date in data:
        return data[date]
    else:
        return {}


def food_log_data(date):
    with open('food_data.json', 'r') as f:
        data = json.load(f)
    food_list = data[date]

    formatted_list = []
    for i, food in enumerate(food_list, start=1):
        formatted_string = f"{i}. {food['name']} - Calories: {food['calories']}, Protein: {food['protein']}, Fat: {food['fat']}, Carbs: {food['carbs']}"
        formatted_list.append(formatted_string)

    return formatted_list


def get_sum(name, date, file):
    """Gets sum of numbers stored in json"""
    food = data_at_date(date, file)
    total = sum(i[name] for i in food)
    return total


def get_goal(name, file):
    """Gets daily goals from"""
    goal = data_at_date(name, file)
    return goal


def get_remaining(goal, current):
    if goal - current <= 0:
        remaining = 0
    else:
        remaining = goal - current
    return remaining
