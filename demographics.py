import json
from getINFO import *


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

    def update_weight(self, new_weight):
        self.demographics['weight'] = new_weight

    @property
    def display_person_info(self):
        return self.demographics['name'], self.demographics['age'], self.demographics['sex'], self.demographics[
            'weight'], self.demographics['goal_weight']


def find_weight():
    with open('demographics.json', 'r') as f:
        data = f.read()
        parse_data = json.loads(data)
    weight = parse_data['weight']
    goal_weight = parse_data['goal_weight']

    return weight, goal_weight


class Goals:
    def __init__(self, goal_type, calories_per_day, pounds, protein_goal, carbs_goal, fat_goal):
        self.goals = {
            'goal_type': goal_type,
            'calories_per_day': float(calories_per_day),
            'pounds': float(pounds),
            'protein_goal': float(protein_goal),
            'carbs_goal': float(carbs_goal),
            'fat_goal': float(fat_goal)
        }

    def write_goals(self):
        with open("demographics.json", "r") as f:
            goals = json.load(f)
        goals.update(self.goals)
        with open("demographics.json", "w") as f:
            json.dump(goals, f)

        return f'Your goals have been saved!'

    def update_goals(self, goal_type):
        if goal_type == 'maintain':
            goals = get_goals('maintain')
        else:
            goals = get_goals(goal_type, self.goals['pounds'])

        self.goals['goal_type'] = goals[0]
        self.goals['calories_per_day'] = goals[1]
        self.goals['pounds'] = goals[2]
        self.goals['protein_goal'] = goals[3]
        self.goals['carbs_goal'] = goals[4]
        self.goals['fat_goal'] = goals[5]
        self.write_goals()

    @property
    def display_goals_info(self):
        return self.goals['goal_type'], self.goals['calories_per_day'], self.goals['pounds'], self.goals[
            'protein_goal'], self.goals['fat_goal'], self.goals['carbs_goal']
