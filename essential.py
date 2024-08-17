import json
import main


def menu():
    print("""
    (1) Add a new food
    (2) Visualize progress
    (3) Quit
    (4) Update Weight
    """)

    choice = input("Enter your choice: ")
    while choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice: ")
    return int(choice)


def add_food():
    """Takes food input from user and returns it in proper order for class"""
    name = input("Input the name of the food: ")
    calories = None
    protein = None
    fat = None
    carbs = None
    while True:
        try:
            if calories == None or calories <= 0:
                calories = int(input("Input the calorie of the food: "))
                if calories <= 0:
                    raise TypeError
            if protein == None or protein <= 0:
                protein = int(input("Input the protein of the food: "))
                if protein <= 0:
                    raise TypeError
            if fat == None or fat <= 0:
                fat = int(input("Input the fat of the food: "))
                if fat <= 0:
                    raise TypeError
            if carbs == None or carbs <= 0:
                carbs = int(input("Input the carbs of the food: "))
                if carbs <= 0:
                    raise TypeError
            break
        except ValueError:
            print('Must enter a digits')
        except TypeError:
            print('Must enter a number greater than zero')

    return name, calories, protein, fat, carbs


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
