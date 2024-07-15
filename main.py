# import json
from dataclasses import dataclass
import os

import numpy as np
import matplotlib.pyplot as plt
from foods import *
from getINFO import *
from essential import *

from datetime import date
today = date.today()
today = today.strftime('%Y-%m-%d')



# calorie_total = Totals('calories', today, 'total')
# protein_total = Totals('protein', today, 'total')
# fat_total = Totals('fat', today, 'total')
# carb_total = Totals('carbs', today, 'total')
#
#
# calorie_total = calorie_total.get_sum()
# protein_total = protein_total.get_sum()
# fat_total = fat_total.get_sum()
# carb_total = carb_total.get_sum()
#
# PROTEIN_GOAL = None  #grams
# FAT = None  #grams
# CARBS = None  #grams

# calorie_total = Totals('calories', date=today, type='total')
# calorie_total = calorie_total.get_sum()
# print(calorie_total)

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
    food_log = 1
    if "demographics.json" not in os.listdir():
        demo = input_demographics()
        secrets = Person(demo[0], demo[1], demo[2], demo[3], demo[4])
        secrets.write_demographics()

        goals = get_goals(secrets.demographics)
        set_goals = Goals(goals[0], goals[1], goals[2], goals[3], goals[4], goals[5])
        set_goals.write_goals()
        print('Your goals have been saved')
        print(set_goals.time_to_reach_goal())

    CALORIE_GOAL = Totals(name='calories_per_day', type='goal')
    PROTEIN_GOAL = Totals(name='protein_goal', type='goal')
    FAT_GOAL = Totals(name='fat_goal', type='goal')
    CARBS_GOAL = Totals(name='carbs_goal', type='goal')

    CALORIE_GOAL = CALORIE_GOAL.get_sum()
    PROTEIN_GOAL = PROTEIN_GOAL.get_sum()
    FAT_GOAL = FAT_GOAL.get_sum()
    CARBS_GOAL = CARBS_GOAL.get_sum()

    calorie_total = Totals('calories', date=today, type='total')
    protein_total = Totals('protein', date=today, type='total')
    fat_total = Totals('fat', date=today, type='total')
    carb_total = Totals('carbs', date=today, type='total')

    try:
        calorie_total = calorie_total.get_sum()
        protein_total = protein_total.get_sum()
        fat_total = fat_total.get_sum()
        carb_total = carb_total.get_sum()
    except FileNotFoundError:
        food_log -= 1
        pass

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

        elif choice == 2:
            if food_log < 1:
                try:
                    calorie_total = calorie_total.get_sum()
                    protein_total = protein_total.get_sum()
                    fat_total = fat_total.get_sum()
                    carb_total = carb_total.get_sum()

                    fig, axs = plt.subplots(2, 2)

                    axs[0, 0].pie([protein_total, fat_total, carb_total], labels=["Protein", "Fats", "Carbs"], autopct='%1.1f%%')
                    axs[0, 0].set_title('Macronutrient Distribution')
                    axs[0, 1].bar([0, 1, 2], [protein_total, fat_total, carb_total], width=0.4)
                    axs[0, 1].bar([0.5, 1.5, 2.5], [PROTEIN_GOAL, int(FAT_GOAL), int(CARBS_GOAL)], width=0.4)
                    axs[0, 1].set_title('Macronutrient Progress')
                    axs[0, 1].legend(['Progress', 'Goal'], loc='upper right')
                    axs[1, 0].pie([calorie_total, (CALORIE_GOAL - calorie_total)], labels=['Calories Used', 'Calories Remaining'],
                                  autopct='%1.1f%%')
                    axs[1, 0].set_title('Calories Remaining')
                    # calories1 = list(food['calories'] for food in today)
                    # axs[1, 1].plot(list(range(len(today))), np.cumsum([food['calories'] for food in today]),
                    #                label='Calories Used')
                    # axs[1, 1].plot(list(range(len(today))), [CALORIE_GOAL] * len(today), label="Calories Goal")
                    # axs[1, 1].legend()

                    fig.tight_layout()
                    plt.show()

                except FileNotFoundError:
                    print('No data to visualize')
                    continue
            else:
                fig, axs = plt.subplots(2, 2)

                axs[0, 0].pie([protein_total, fat_total, carb_total], labels=["Protein", "Fats", "Carbs"],
                              autopct='%1.1f%%')
                axs[0, 0].set_title('Macronutrient Distribution')
                axs[0, 1].bar([0, 1, 2], [protein_total, fat_total, carb_total], width=0.4)
                axs[0, 1].bar([0.5, 1.5, 2.5], [PROTEIN_GOAL, int(FAT_GOAL), int(CARBS_GOAL)], width=0.4)
                axs[0, 1].set_title('Macronutrient Progress')
                axs[0, 1].legend(['Progress', 'Goal'], loc='upper right')
                axs[1, 0].pie([calorie_total, (CALORIE_GOAL - calorie_total)],
                              labels=['Calories Used', 'Calories Remaining'],
                              autopct='%1.1f%%')
                axs[1, 0].set_title('Calories Remaining')
                # calories1 = list(food['calories'] for food in today)
                # axs[1, 1].plot(list(range(len(today))), np.cumsum([food['calories'] for food in today]),
                #                label='Calories Used')
                # axs[1, 1].plot(list(range(len(today))), [CALORIE_GOAL] * len(today), label="Calories Goal")
                # axs[1, 1].legend()

                fig.tight_layout()
                plt.show()

        elif choice == 3:
            print("Quitting")
            done = True

        else:
            print("Invalid choice")


if __name__ == '__main__':
    main()
