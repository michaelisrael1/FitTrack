from dataclasses import dataclass
import os
from demographics import *
import numpy as np
import matplotlib.pyplot as plt
from foods import *
from getINFO import *
from essential import *
from datetime import date, timedelta

today = date.today()
yesterday = date.today() - timedelta(1)
today = today.strftime('%Y-%m-%d')
yesterday = yesterday.strftime('%Y-%m-%d')


def main():
    global user_goal
    global user_demo
    if "demographics.json" not in os.listdir():
        demo = input_demographics()
        secrets = Person(demo[0], demo[1], demo[2], demo[3], demo[4])
        secrets.write_demographics()

        goals = get_goals(secrets.demographics)
        set_goals = Goals(goals[0], goals[1], goals[2], goals[3], goals[4], goals[5])
        set_goals.write_goals()
        print('Your goals have been saved')
        print(set_goals.time_to_reach_goal())
    else:
        user = extract_info()
        user_demo = Person(user[0], user[1], user[2], user[3], user[4])
        user_goal = Goals(user[5], user[6], user[7], user[8], user[9], user[10])


    calorie_goal = Totals(name='calories_per_day', type='goal')
    protein_goal = Totals(name='protein_goal', type='goal')
    fat_goal = Totals(name='fat_goal', type='goal')
    carbs_goal = Totals(name='carbs_goal', type='goal')

    calorie_goal = calorie_goal.get_sum()
    protein_goal = protein_goal.get_sum()
    fat_goal = fat_goal.get_sum()
    carbs_goal = carbs_goal.get_sum()

    choice = menu()
    while choice != 3:
        if choice == 1:
            print("Adding new food!")
            new_food = add_food()
            adding = Food(str(date.today()), new_food[0], new_food[1], new_food[2], new_food[3], new_food[4])
            adding.WriteFood()
            print("Successfully added new food!")
            choice = menu()

        elif choice == 2:
            try:
                calorie_total = Totals('calories', date=today, type='total')
                protein_total = Totals('protein', date=today, type='total')
                fat_total = Totals('fat', date=today, type='total')
                carb_total = Totals('carbs', date=today, type='total')

                today_growth, yesterday_growth = calorie_total.growth_day(yesterday)
                calorie_total = calorie_total.get_sum()
                protein_total = protein_total.get_sum()
                fat_total = fat_total.get_sum()
                carb_total = carb_total.get_sum()

                if calorie_goal - calorie_total < 0:
                    remaining = 0
                else:
                    remaining = calorie_goal - calorie_total
                if calorie_total == 0 or protein_total == 0 or carb_total == 0 or fat_total == 0:
                    raise FileNotFoundError

                fig, axs = plt.subplots(2, 2)

                axs[0, 0].pie([protein_total, fat_total, carb_total], labels=["Protein", "Fats", "Carbs"],
                              autopct='%1.1f%%')
                axs[0, 0].set_title('Macronutrient Distribution')
                axs[0, 1].bar([0, 1, 2], [protein_total, fat_total, carb_total], width=0.4)
                axs[0, 1].bar([0.5, 1.5, 2.5], [protein_goal, fat_goal, carbs_goal], width=0.4)
                axs[0, 1].set_title('Macronutrient Progress')
                axs[0, 1].legend(['Progress', 'Goal'], loc='upper right')
                axs[1, 0].pie([calorie_total, (remaining)],
                              labels=['Calories Used', 'Calories Remaining'],
                              autopct='%1.1f%%')
                axs[1, 0].set_title('Calories Remaining')

                axs[1, 1].plot(list(range(len(today_growth))), np.cumsum([i for i in today_growth]), label="Today Cal")
                if len(yesterday_growth) > 0:
                    axs[1, 1].plot(list(range(len(yesterday_growth))), np.cumsum([i for i in yesterday_growth]),
                                   label="Yesterday Cal")
                    axs[1, 1].set_title('Comparison of Cal')
                else:
                    axs[1, 1].set_title('Cal Growth')
                axs[1, 1].legend()

                fig.tight_layout()
                plt.show()
                choice = menu()

            except FileNotFoundError:
                print('No data to visualize')
                choice = menu()
        elif choice == 3:
            print("Quitting")
            break
        elif choice == 4:
            user_goal.update_weight()
        else:
            print("Invalid choice")


if __name__ == '__main__':
    main()
