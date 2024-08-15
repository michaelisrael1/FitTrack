import logging
import json
from PyQt6.QtWidgets import *
from gui import *
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


class Logic(QMainWindow, Ui_MainWindow):
    GOAL_TYPE = 'l'
    user = None
    user_goal = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.labelErrorInfo.hide()
        self.group_pounds_week.hide()
        self.label_error_food.hide()
        self.label_food_added.hide()

        self.stackedWidgetFitTrack.setCurrentWidget(self.stackedWidgetPageWelcome)

        self.buttonBegin.clicked.connect(lambda: self.check_data())
        self.button_submitINFO.clicked.connect(lambda: self.set_demo())

        self.buttonSubmitGoalType.clicked.connect(lambda: self.set_goal_type())
        self.buttonSubmitGoalPoundsaWeek.clicked.connect(lambda: self.set_pounds())

        self.button_MainMenu.clicked.connect(lambda: self.main_menu())

        self.button_addFood.clicked.connect(lambda: self.add_food())
        self.button_clearAddFood.clicked.connect(lambda: self.clear_food())
        self.button_returnMainAddFood.clicked.connect(lambda: self.return_main_menu())

    def check_data(self):
        if "demographics.json" in os.listdir():
            user = extract_info()
            name, age, sex, weight, goal_weight = user[0], user[1], user[2], user[3], user[4]
            goal_type, calories_per_day, pounds, protein_goal, carbs_goal, fat_goal = user[5], user[6], user[7], user[
                8], user[9], user[10]
            self.user = Person(name, age, sex, weight, goal_weight)
            self.user_goal = Goals(goal_type, calories_per_day, pounds, protein_goal, carbs_goal, fat_goal)
            self.stackedWidgetFitTrack.setCurrentWidget(self.page_MainMenu)
        else:
            self.stackedWidgetFitTrack.setCurrentWidget(self.page_GetINFO)

    def set_demo(self):
        self.labelErrorInfo.hide()
        try:
            name, age = self.input_name.text().strip().lower(), self.input_age.value()
            current_weight, goal_weight = float(self.input_currentWeight.value()), float(self.input_goalWeight.value())
            if self.radioButtonMale.isChecked():
                sex = 'm'
            else:
                sex = 'f'
            if not name.isalpha():
                raise TypeError

        except TypeError:
            self.labelErrorInfo.show()

        else:
            user = Person(name, age, sex, current_weight, goal_weight)
            user.write_demographics()
            self.stackedWidgetFitTrack.setCurrentWidget(self.page_GetGoals)

    def set_goal_type(self):
        if self.radioButtonMaintain.isChecked():
            goals = get_goals('m')
            set_goals = Goals(goals[0], goals[1], goals[2], goals[3], goals[4], goals[5])
            set_goals.write_goals()
            self.stackedWidgetFitTrack.setCurrentWidget(self.page_MainMenu)
        else:
            self.group_pounds_week.show()
            if self.radioButtonGain.isChecked():
                self.GOAL_TYPE = 'g'

    def set_pounds(self):
        goals = get_goals(self.GOAL_TYPE, self.input_pounds_a_week.value())
        set_goals = Goals(goals[0], goals[1], goals[2], goals[3], goals[4], goals[5])
        set_goals.write_goals()
        self.stackedWidgetFitTrack.setCurrentWidget(self.page_MainMenu)

    def main_menu(self):
        if self.radioButtonAddfood.isChecked():
            self.stackedWidgetFitTrack.setCurrentWidget(self.page_addFood)
        elif self.radioButton_ProfileInfo.isChecked():
            self.stackedWidgetFitTrack.setCurrentWidget(self.page_ProfileInfo)
            self.profile_info()
        elif self.radioButton_FoodLog.isChecked():
            self.stackedWidgetFitTrack.setCurrentWidget(self.page_FoodLog)
        elif self.radioButton_Quit.isChecked():
            quit()

    def return_main_menu(self):
        self.stackedWidgetFitTrack.setCurrentWidget(self.page_MainMenu)

    def add_food(self):
        try:
            self.label_error_food.hide()
            name_food = self.input_foodname.text().strip().lower()
            if not name_food.isalpha():
                raise TypeError

            calories, protein, fat, carbs = float(self.input_calories.value()), float(
                self.input_protein.value()), float(self.input_fat.value()), float(self.input_carbs.value())

            new_food = Food(today, name_food, calories, protein, fat, carbs)
            new_food.WriteFood()
            self.clear_food()
            self.label_food_added.show()

        except TypeError:
            self.label_food_added.hide()
            self.label_error_food.show()

    def clear_food(self):
        self.input_foodname.clear()
        self.input_calories.setValue(1)
        self.input_protein.setValue(0)
        self.input_fat.setValue(0)
        self.input_carbs.setValue(0)

        self.label_food_added.hide()
        self.label_error_food.hide()

    def profile_info(self):
        profile_info = self.user.display_person_info
        goal_info = self.user_goal.display_goals_info

        self.table_porofile_info.(0, 1, item=profile_info[0])

    def food_log(self):
        pass
