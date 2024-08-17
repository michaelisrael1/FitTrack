import os
from dataclasses import dataclass
import json
from essential import *


class Calories:
    CALORIES_PER_DAY: float = None

    def __init__(self, calories: float):
        """
        Initialize a Calories object.

        :param calories: The number of calories
        """
        self.calories = calories


@dataclass
class Food:
    date: str
    data: dict
    no_date: dict

    def __init__(self, date: str, name: str, calories: float, protein: float, fat: float, carbs: float):
        """
        Initialize a Food object.

        :param date: The date of the food log
        :param name: The name of the food
        :param calories: The number of calories in the food
        :param protein: The amount of protein in the food
        :param fat: The amount of fat in the food
        :param carbs: The amount of carbohydrates in the food
        """
        self.date = date
        self.data = {date: [
            {'name': name, "calories": calories, 'protein': protein, 'fat': fat, 'carbs': carbs}
        ]}
        self.no_date = {'name': name, "calories": calories, 'protein': protein, 'fat': fat, 'carbs': carbs}

    def write_food(self) -> None:
        """
        Write the food data to the JSON file.
        """
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
    TOTAL_FILE: str = "food_data.json"
    GOAL_FILE: str = "demographics.json"

    def __init__(self, name: str, date: str = 'None', filename: str = 'None'):
        """
        Initialize a Totals object.

        :param name: The name of the nutrient or goal
        :param date: The date for which to get the total (default is 'None')
        :param filename: The type of total to get (e.g., 'goal' or 'total') (default is 'None')
        """
        self.name = name
        self.date = date
        self.type = filename

    def get_sum(self) -> float:
        """
        Get the sum of the specified nutrient or goal.

        :return: The sum of the specified nutrient or goal
        """
        if self.type == 'goal':
            total = get_goal(self.name, self.GOAL_FILE)
        elif self.type == 'total':
            total = get_sum(self.name, self.date, self.TOTAL_FILE)

        return total
