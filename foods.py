import os
from dataclasses import dataclass
import json
from essential import *


class Calories:
    CALORIES_PER_DAY = None

    def __init__(self, calories):
        self.calories = calories


@dataclass
class Food:
    def __init__(self, date, name, calories, protein, fat, carbs):
        self.date = date
        self.data = {date: [
            {'name': name, "calories": calories, 'protein': protein, 'fat': fat, 'carbs': carbs}
        ]}
        self.no_date = {'name': name, "calories": calories, 'protein': protein, 'fat': fat, 'carbs': carbs}

    def write_food(self):
        if "food_data.json" not in os.listdir():
            with open("food_data.json", 'w') as f:
                json.dump(self.data, f, indent=4)
        else:
            with open("food_data.json", 'r') as f:
                data = json.load(f)
            if self.date in data:
                data[self.date].append(self.no_date)
                with open("food_data.json", 'w') as f:
                    json.dump(data, f, indent=4)
            else:
                data[self.date] = [self.no_date]
                with open("food_data.json", 'w') as f:
                    json.dump(data, f, indent=4)


class Totals:
    TOTAL_FILE = "food_data.json"
    GOAL_FILE = "demographics.json"

    def __init__(self, name, date='None', type='None'):
        self.name = name
        self.date = date
        self.type = type

    def get_sum(self):
        if self.type == 'goal':
            total = get_goal(self.name, self.GOAL_FILE)
        elif self.type == 'total':
            total = get_sum(self.name, self.date, self.TOTAL_FILE)

        return total
