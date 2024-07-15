import json

def add_food():
    """Takes food input from user and returns it in proper order for class"""
    name = input("Input the name of the food: ")
    calories = int(input("Input the calorie of the food: "))
    protein = int(input("Input the protein of the food: "))
    fat = int(input("Input the fat of the food: "))
    carbs = int(input("Input the carbs of the food: "))

    return name, calories, protein, fat, carbs


def data_at_date(date, file):
    """Reads file and extracts if value exists at key, the value is returned"""
    with open(file, 'r') as f:
        data = json.load(f)
    if date in data:
        return data[date]
    else:
        return {}


def get_sum(name, date, file):
    """Gets sum of numbers stored in json"""
    food = data_at_date(date, file)
    total = sum(i[name] for i in food)
    return total


def get_goal(name, file):
    """Gets daily goals from"""
    goal = data_at_date(name, file)
    return goal
