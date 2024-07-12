import json
class Person:
    def __init__(self, name, age, sex, weight, goal_weight):
        self.demographics = {
            'name': name,
            'age': int(age),
            'sex': sex,
            'weight': float(weight),
            'goal_weight': float(goal_weight)
        }

    def write_demographics(self):
        with open("demographics.json", "w") as f:
            json.dump(self.demographics, f)
        return f'Your profile has been saved!'

class Goals(Person):
    def __init__(self, goal_type, calories_per_day):
        self.goals = {
            'goal_type': goal_type,
            'calories_per_day': float(calories_per_day)
        }

    def write_goals(self):
        with open("demographics.json", "r") as f:
            goals = json.load(f)
        goals.update(self.goals)
        with open("demographics.json", "w") as f:
            json.dump(goals, f)

        return f'Your goals have been saved!'








