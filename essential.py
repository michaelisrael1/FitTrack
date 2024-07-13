import json
from datetime import date


def add_food():
    name = input("Input the name of the food: ")
    calories = int(input("Input the calorie of the food: "))
    protein = int(input("Input the protein of the food: "))
    fat = int(input("Input the fat of the food: "))
    carbs = int(input("Input the carbs of the food: "))

    return name, calories, protein, fat, carbs

def get_date(date):
    with open("food_data.json", 'r') as f:
        data = json.load(f)
    if date in data:
        print(data[date])
        return []

# def get_sum(name, date):
#     food = get_date(name,date)
#     total = sum(i[name] for i in food)
#     return total

