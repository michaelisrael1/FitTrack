from dataclasses import dataclass

class Calories:
    CALORIES_PER_DAY = None
    def __init__(self, calories):
        self.calories = calories

@dataclass
class Food:
    def __init__(self, name, calories, protein, fat, carbs):
        self.data = {
            'name': name,
            'calories': calories,
            'protein': protein,
            'fat': fat,
            'carbs': carbs
        }

