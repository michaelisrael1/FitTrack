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
    def __init__(self, goal_type, calories_per_day, pounds):
        self.goals = {
            'goal_type': goal_type,
            'calories_per_day': float(calories_per_day),
            'pounds': float(pounds)
        }

    def find_weight(self):
        with open('demographics.json', 'r') as f:
            data = f.read()
            parse_data = json.loads(data)
        weight = parse_data['weight']
        goal_weight = parse_data['goal_weight']

        return weight, goal_weight

    def write_goals(self):
        with open("demographics.json", "r") as f:
            goals = json.load(f)
        goals.update(self.goals)
        with open("demographics.json", "w") as f:
            json.dump(goals, f)

        return f'Your goals have been saved!'

    def time_to_reach_goal(self):
        if self.goals['goal_type'] == 'm':
            return 'We will be with you along the way to make sure you maintain your weight'
        else:
            current_weight = self.find_weight()[0]
            goal_weight = self.find_weight()[1]
            pound_week = self.goals['pounds']

            if current_weight > goal_weight and self.goals['goal_type'] == 'l':
                lose_amount = current_weight - goal_weight
                time_to_reach_goal = lose_amount/pound_week
                days = time_to_reach_goal * 7

                return f'You will reach your goal in {days:.0f} days'

            elif current_weight < goal_weight and self.goals['goal_type'] == 'g':
                gain_amount = goal_weight - current_weight
                time_to_reach_goal = gain_amount / pound_week
                days = time_to_reach_goal * 7

                return f'You will reach your goal in {days:.0f} days'

            else:
                return f'You reached your goal of {current_weight:.0f} pounds'









