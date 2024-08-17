import sys
from datetime import date, timedelta


from demographics import *
from foods import *
from getINFO import *

today = date.today()
yesterday = date.today() - timedelta(1)
today = today.strftime('%Y-%m-%d')
yesterday = yesterday.strftime('%Y-%m-%d')


class Logic(QMainWindow, Ui_MainWindow):
    FOOD_LOG_COUNT = 0
    NEW_FOOD_ADDED = 0
    GOAL_TYPE = 'lose'
    user = None
    user_goal = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.labelErrorInfo.hide()
        self.group_pounds_week.hide()
        self.label_error_food.hide()
        self.label_food_added.hide()
        self.group_update_weight.hide()
        self.label_congrats.hide()

        self.input_line = QLineEdit()

        self.stackedWidgetFitTrack.setCurrentWidget(self.stackedWidgetPageWelcome)

        self.buttonBegin.clicked.connect(lambda: self.check_data())
        self.button_submitINFO.clicked.connect(lambda: self.set_demo())

        self.buttonSubmitGoalPoundsaWeek.clicked.connect(lambda: self.set_pounds())

        self.button_MainMenu.clicked.connect(lambda: self.main_menu())

        self.button_addFood.clicked.connect(lambda: self.add_food())
        self.button_clearAddFood.clicked.connect(lambda: self.clear_food())
        self.button_returnMainAddFood.clicked.connect(lambda: self.return_main_menu())

        self.button_profileMainMenu.clicked.connect(lambda: self.return_main_menu())
        self.button_update_weight.clicked.connect(lambda: self.update_weight())

        self.button_foodlog_MainMenu.clicked.connect(lambda: self.return_main_menu())

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
                sex = 'male'
            else:
                sex = 'female'
            if not name.isalpha():
                raise TypeError

        except TypeError:
            self.labelErrorInfo.show()

        else:
            self.user = Person(name, age, sex, current_weight, goal_weight)
            self.user.write_demographics()
            self.stackedWidgetFitTrack.setCurrentWidget(self.page_GetGoals)
            self.set_goal_type()

    def set_goal_type(self):
        if self.user.demographics['weight'] < self.user.demographics['goal_weight']:
            self.group_pounds_week.show()
            self.GOAL_TYPE = 'gain'
        elif self.user.demographics['weight'] > self.user.demographics['goal_weight']:
            self.group_pounds_week.show()
        elif self.user.demographics['weight'] == self.user.demographics['goal_weight']:
            goals = get_goals('maintain')
            set_goals = Goals(goals[0], goals[1], goals[2], goals[3], goals[4], goals[5])
            set_goals.write_goals()
            self.stackedWidgetFitTrack.setCurrentWidget(self.page_MainMenu)
            os.execl(sys.executable, sys.executable, *sys.argv)

    def set_pounds(self):
        goals = get_goals(self.GOAL_TYPE, self.input_pounds_a_week.value())
        self.user_goal = Goals(goals[0], goals[1], goals[2], goals[3], goals[4], goals[5])
        self.user_goal.write_goals()
        self.stackedWidgetFitTrack.setCurrentWidget(self.page_MainMenu)
        os.execl(sys.executable, sys.executable, *sys.argv)

    def main_menu(self):
        if self.radioButtonAddfood.isChecked():
            self.stackedWidgetFitTrack.setCurrentWidget(self.page_addFood)
        elif self.radioButton_ProfileInfo.isChecked():
            self.stackedWidgetFitTrack.setCurrentWidget(self.page_ProfileInfo)
            self.profile_info()
            if self.user_goal.goals['goal_type'] != 'maintain':
                self.group_update_weight.show()
        elif self.radioButton_FoodLog.isChecked():
            self.stackedWidgetFitTrack.setCurrentWidget(self.page_FoodLog)
            self.food_log()
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
            new_food.write_food()
            self.NEW_FOOD_ADDED += 1
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

        self.table_porofile_info.setItem(0, 0, QTableWidgetItem(str(profile_info[0]).capitalize()))
        self.table_porofile_info.setItem(1, 0, QTableWidgetItem(str(profile_info[1])))
        self.table_porofile_info.setItem(2, 0, QTableWidgetItem(str(profile_info[2])))
        self.table_porofile_info.setItem(3, 0, QTableWidgetItem(str(profile_info[3])))
        self.table_porofile_info.setItem(4, 0, QTableWidgetItem(str(profile_info[4])))

        self.table_porofile_info.setItem(5, 0, QTableWidgetItem(str(goal_info[0])))
        self.table_porofile_info.setItem(6, 0, QTableWidgetItem(str(goal_info[1])))
        self.table_porofile_info.setItem(7, 0, QTableWidgetItem(str(goal_info[2])))
        self.table_porofile_info.setItem(8, 0, QTableWidgetItem(str(goal_info[3])))
        self.table_porofile_info.setItem(9, 0, QTableWidgetItem(str(goal_info[4])))
        self.table_porofile_info.setItem(10, 0, QTableWidgetItem(str(goal_info[5])))

    def update_weight(self):
        new_weight = self.input_update_weight.value()
        self.user.update_weight(new_weight)
        self.user.write_demographics()
        self.profile_info()

        if (new_weight >= self.user.demographics['goal_weight'] and self.user_goal.goals['goal_type'] == 'gain') or \
                (new_weight <= self.user.demographics['goal_weight'] and self.user_goal.goals['goal_type'] == 'lose'):
            self.label_congrats.show()
            self.user_goal.update_goals('maintain')
        else:
            self.label_congrats.hide()
            self.user_goal.update_goals(self.user_goal.goals['goal_type'])

        self.user_goal.write_goals()
        self.food_log()
        self.profile_info()

    def food_log(self):
        try:
            if self.FOOD_LOG_COUNT == 0:
                self.food_log_data()
                self.FOOD_LOG_COUNT += 1
            elif self.NEW_FOOD_ADDED > 0:
                self.food_log_data()
        except KeyError:
            self.list_food_log.addItem('No food logs for today. Add a food to get started!')

    def food_log_data(self):
        try:
            self.list_food_log.clear()
            daily_log = food_log_data(today)
            for item in daily_log:
                self.list_food_log.addItem(item)
            self.totals()
        except FileNotFoundError:
            raise KeyError

    def totals(self):
        calorie_goal = Totals(name='calories_per_day', type='goal')
        protein_goal = Totals(name='protein_goal', type='goal')
        fat_goal = Totals(name='fat_goal', type='goal')
        carbs_goal = Totals(name='carbs_goal', type='goal')

        calorie_goal = calorie_goal.get_sum()
        protein_goal = protein_goal.get_sum()
        fat_goal = fat_goal.get_sum()
        carbs_goal = carbs_goal.get_sum()

        calorie_total = Totals('calories', today, type='total')
        protein_total = Totals('protein', today, type='total')
        fat_total = Totals('fat', today, type='total')
        carb_total = Totals('carbs', today, type='total')

        calorie_total = calorie_total.get_sum()
        protein_total = protein_total.get_sum()
        fat_total = fat_total.get_sum()
        carb_total = carb_total.get_sum()

        self.list_food_log.addItems(
            [
                f'Calories Total = {calorie_total}  |  Calories Remaining = {get_remaining(calorie_goal, calorie_total):.2f}',
                f'Protein Total = {protein_total}  |  Protein Remaining = {get_remaining(protein_goal, protein_total):.2f}',
                f'Fat Total = {fat_total}  |  Fat Remaining = {get_remaining(fat_goal, fat_total):.2f}',
                f'Carbs Total = {carb_total}  |  Carbs Remaining = {get_remaining(carbs_goal, carb_total):.2f}'])
