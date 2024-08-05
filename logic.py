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
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.buttonBegin.clicked.connect(lambda : self.check_data())
        self.labelErrorInfo.hide()
        self.group_pounds_week.hide()
        self.button_submitINFO.clicked.connect(lambda : self.setDemo())
        self.buttonSubmitGoalType.clicked.connect(lambda : self.set_goal_type())

    def check_data(self):
        # try:
        if "demographics.json" not in os.listdir():
            self.stackedWidgetFitTrack.setCurrentWidget(self.page_GetINFO)
        else:
            # user = extract_info()
            # user = Person(user[0], user[1], user[2], user[3], user[4])
            # user_goal = Goals(user[5], user[6], user[7], user[8], user[9], user[10])
            self.stackedWidgetFitTrack.setCurrentWidget(self.page_MainMenu)
        # except Exception as e:
        #     user = extract_info()
        #     user = Person(user[0], user[1], user[2], user[3], user[4])
        #     user_goal = Goals(user[5], user[6], user[7], user[8], user[9], user[10])
        #     self.stackedWidgetFitTrack.setCurrentWidget(self.page_MainMenu)


    def setDemo(self):
            self.labelErrorInfo.hide()
            try:
                name, age, sex, current_weight, goal_weight = (self.input_name.text().strip(), self.input_age.text().strip(), self.input_sex.text().strip().lower(), self.input_currentWeight.text().strip(), self.input_goalWeight.text().strip())
                if name == '' or age == '' or current_weight == '' or sex == '' or goal_weight == '':
                    raise TypeError
                age = int(age)
                if sex not in ['m', 'f']:
                    raise TypeError
                current_weight = float(current_weight)
                goal_weight = float(goal_weight)

            except TypeError or ValueError:
                # with open('errors.json', 'w') as f:
                #     json.dump(str(e), f)
                self.labelErrorInfo.show()

            else:
                user = Person(name, age, sex, current_weight, goal_weight)
                user.write_demographics()
                self.stackedWidgetFitTrack.setCurrentWidget(self.page_GetGoals)
    # def set_goal_type(self):
    #     user_goals =



