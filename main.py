# import json
# from dataclasses import dataclass
import os

import numpy as np
import matplotlib.pyplot as plt
from foods import *
from getINFO import *
from essential import *

from datetime import date
CALORIE_GOAL = None  #cal
calorie_total = Totals('calories', date.today())
PROTEIN_GOAL = None  #grams
FAT = None  #grams
CARBS = None  #grams
today = []

# if "demographics.json" not in os.listdir():
#     demo = input_demographics()
#     secrets = Person(demo[0], demo[1], demo[2], demo[3], demo[4])
#     secrets.write_demographics()
#
#     goals = get_goals(secrets.demographics)
#     set_goals = Goals(goals[0], goals[1], goals[2])
#     set_goals.write_goals()
#     print('Your goals have been saved')
#     print(set_goals.time_to_reach_goal())


def main():
    if "demographics.json" not in os.listdir():
        demo = input_demographics()
        secrets = Person(demo[0], demo[1], demo[2], demo[3], demo[4])
        secrets.write_demographics()

        goals = get_goals(secrets.demographics)
        set_goals = Goals(goals[0], goals[1], goals[2])
        set_goals.write_goals()
        print('Your goals have been saved')
        print(set_goals.time_to_reach_goal())

    done = False

    while not done:
        print("""
        (1) Add a new food
        (2) Visualize progress
        (3) Quit
        """)

        choice = input("Enter your choice: ")
        while choice not in ['1', '2', '3']:
            print("Invalid choice. Please try again.")
            choice = input("Enter your choice: ")

        choice = int(choice)

        if choice == 1:
            print("Adding new food!")
            new_food = add_food()
            adding = Food(str(date.today()), new_food[0], new_food[1], new_food[2], new_food[3], new_food[4])
            adding.WriteFood()
            print("Successfully added new food!")

            print(calorie_total.get_date())
        elif choice == 2:
            calories_sum = sum(food['calories'] for food in today)
            protein_sum = sum(food['protein'] for food in today)
            fat_sum = sum(food['fat'] for food in today)
            carbs_sum = sum(food['carbs'] for food in today)
            fig, axs = plt.subplots(2, 2)

            axs[0, 0].pie([protein_sum, fat_sum, carbs_sum], labels=["Protein", "Fats", "Carbs"], autopct='%1.1f%%')
            axs[0, 0].set_title('Macronutrient Distribution')
            axs[0, 1].bar([0, 1, 2], [protein_sum, fat_sum, carbs_sum], width=0.4)
            axs[0, 1].bar([0.5, 1.5, 2.5], [PROTEIN_GOAL, FAT, CARBS], width=0.4)
            axs[0, 1].set_title('Macronutrient Progress')
            axs[0, 1].legend(['Progress', 'Goal'], loc='upper right')
            axs[1, 0].pie([calories_sum, (CALORIE_GOAL - calories_sum)], labels=['Calories Used', 'Calories Remaining'],
                          autopct='%1.1f%%')
            axs[1, 0].set_title('Calories Remaining')
            calories1 = list(food['calories'] for food in today)
            axs[1, 1].plot(list(range(len(today))), np.cumsum([food['calories'] for food in today]),
                           label='Calories Used')
            axs[1, 1].plot(list(range(len(today))), [CALORIE_GOAL] * len(today), label="Calories Goal")
            axs[1, 1].legend()

            fig.tight_layout()
            plt.show()

        elif choice == 3:
            print("Quitting")
            done = True

        else:
            print("Invalid choice")


if __name__ == '__main__':
    main()
