import json
from getINFO import *


class Person:
    def __init__(self, name: str, age: int, sex: str, weight: float, goal_weight: float):
        """
        Initialize a Person object with demographic information.

        :param name: Name of the person
        :param age: Age of the person
        :param sex: Sex of the person
        :param weight: Current weight of the person
        :param goal_weight: Goal weight of the person
        """
        self.demographics = {
            'name': name,
            'age': int(age),
            'sex': sex,
            'weight': float(weight),
            'goal_weight': float(goal_weight)
        }

    def write_demographics(self) -> None:
        """
        Write the demographic information to a JSON file.
        """
        with open("demographics.json", "w") as f:
            json.dump(self.demographics, f)

    def update_weight(self, new_weight: float) -> None:
        """
        Update the weight of the person.

        :param new_weight: New weight of the person
        """
        self.demographics['weight'] = new_weight

    @property
    def display_person_info(self) -> tuple:
        """
        Display the demographic information of the person.

        :return: A tuple containing name, age, sex, weight, and goal weight
        """
        return (self.demographics['name'], self.demographics['age'], self.demographics['sex'],
                self.demographics['weight'], self.demographics['goal_weight'])


def find_weight() -> tuple:
    """
    Find the current weight and goal weight from the JSON file.

    :return: A tuple containing current weight and goal weight
    """
    with open('demographics.json', 'r') as f:
        data = f.read()
        parse_data = json.loads(data)
    weight = parse_data['weight']
    goal_weight = parse_data['goal_weight']

    return weight, goal_weight


class Goals:
    def __init__(self, goal_type: str, calories_per_day: float, pounds: float, protein_goal: float,
                 carbs_goal: float, fat_goal: float):
        """
        Initialize a Goals object with goal information.

        :param goal_type: Type of goal (e.g., maintain, gain, lose)
        :param calories_per_day: Daily calorie intake goal
        :param pounds: Weight goal in pounds
        :param protein_goal: Daily protein intake goal
        :param carbs_goal: Daily carbohydrate intake goal
        :param fat_goal: Daily fat intake goal
        """
        self.goals = {
            'goal_type': goal_type,
            'calories_per_day': float(calories_per_day),
            'pounds': float(pounds),
            'protein_goal': float(protein_goal),
            'carbs_goal': float(carbs_goal),
            'fat_goal': float(fat_goal)
        }

    def write_goals(self) -> str:
        """
        Write the goal information to the JSON file.

        :return: A confirmation message indicating the goals have been saved
        """
        with open("demographics.json", "r") as f:
            goals = json.load(f)
        goals.update(self.goals)
        with open("demographics.json", "w") as f:
            json.dump(goals, f)

        return 'Your goals have been saved!'

    def update_goals(self, goal_type: str) -> None:
        """
        Update the goals based on the goal type.

        :param goal_type: Type of goal (e.g., maintain, gain, lose)
        """
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
    def display_goals_info(self) -> tuple:
        """
        Display the goal information.

        :return: A tuple containing goal type, daily calorie intake, weight goal, protein goal, fat goal, and carbohydrate goal
        """
        return (self.goals['goal_type'], self.goals['calories_per_day'], self.goals['pounds'],
                self.goals['protein_goal'], self.goals['fat_goal'], self.goals['carbs_goal'])
