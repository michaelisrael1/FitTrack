# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        MainWindow.resize(700, 500)
        MainWindow.setMinimumSize(QtCore.QSize(700, 500))
        MainWindow.setMaximumSize(QtCore.QSize(700, 500))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidgetFitTrack = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidgetFitTrack.setEnabled(True)
        self.stackedWidgetFitTrack.setMinimumSize(QtCore.QSize(700, 500))
        self.stackedWidgetFitTrack.setMaximumSize(QtCore.QSize(700, 500))
        self.stackedWidgetFitTrack.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.stackedWidgetFitTrack.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.stackedWidgetFitTrack.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.stackedWidgetFitTrack.setObjectName("stackedWidgetFitTrack")
        self.stackedWidgetPageWelcome = QtWidgets.QWidget()
        self.stackedWidgetPageWelcome.setObjectName("stackedWidgetPageWelcome")
        self.label_welcome = QtWidgets.QLabel(parent=self.stackedWidgetPageWelcome)
        self.label_welcome.setGeometry(QtCore.QRect(0, 10, 671, 271))
        self.label_welcome.setObjectName("label_welcome")
        self.buttonBegin = QtWidgets.QPushButton(parent=self.stackedWidgetPageWelcome)
        self.buttonBegin.setGeometry(QtCore.QRect(260, 300, 151, 81))
        self.buttonBegin.setObjectName("buttonBegin")
        self.stackedWidgetFitTrack.addWidget(self.stackedWidgetPageWelcome)
        self.page_GetINFO = QtWidgets.QWidget()
        self.page_GetINFO.setObjectName("page_GetINFO")
        self.label_infoenter = QtWidgets.QLabel(parent=self.page_GetINFO)
        self.label_infoenter.setGeometry(QtCore.QRect(0, 0, 651, 21))
        self.label_infoenter.setObjectName("label_infoenter")
        self.label_Name = QtWidgets.QLabel(parent=self.page_GetINFO)
        self.label_Name.setGeometry(QtCore.QRect(150, 60, 101, 16))
        self.label_Name.setObjectName("label_Name")
        self.label_Age = QtWidgets.QLabel(parent=self.page_GetINFO)
        self.label_Age.setGeometry(QtCore.QRect(150, 100, 51, 21))
        self.label_Age.setObjectName("label_Age")
        self.input_name = QtWidgets.QLineEdit(parent=self.page_GetINFO)
        self.input_name.setGeometry(QtCore.QRect(370, 60, 171, 21))
        self.input_name.setObjectName("input_name")
        self.input_age = QtWidgets.QLineEdit(parent=self.page_GetINFO)
        self.input_age.setGeometry(QtCore.QRect(370, 100, 171, 21))
        self.input_age.setObjectName("input_age")
        self.input_sex = QtWidgets.QLineEdit(parent=self.page_GetINFO)
        self.input_sex.setGeometry(QtCore.QRect(370, 140, 171, 21))
        self.input_sex.setObjectName("input_sex")
        self.input_currentWeight = QtWidgets.QLineEdit(parent=self.page_GetINFO)
        self.input_currentWeight.setGeometry(QtCore.QRect(370, 180, 171, 21))
        self.input_currentWeight.setObjectName("input_currentWeight")
        self.input_goalWeight = QtWidgets.QLineEdit(parent=self.page_GetINFO)
        self.input_goalWeight.setGeometry(QtCore.QRect(370, 220, 171, 21))
        self.input_goalWeight.setObjectName("input_goalWeight")
        self.label_goalWeight = QtWidgets.QLabel(parent=self.page_GetINFO)
        self.label_goalWeight.setGeometry(QtCore.QRect(150, 220, 151, 21))
        self.label_goalWeight.setObjectName("label_goalWeight")
        self.label_currentWeight = QtWidgets.QLabel(parent=self.page_GetINFO)
        self.label_currentWeight.setGeometry(QtCore.QRect(150, 180, 161, 21))
        self.label_currentWeight.setObjectName("label_currentWeight")
        self.label_sex = QtWidgets.QLabel(parent=self.page_GetINFO)
        self.label_sex.setGeometry(QtCore.QRect(150, 140, 91, 21))
        self.label_sex.setObjectName("label_sex")
        self.button_submitINFO = QtWidgets.QPushButton(parent=self.page_GetINFO)
        self.button_submitINFO.setGeometry(QtCore.QRect(270, 260, 101, 31))
        self.button_submitINFO.setObjectName("button_submitINFO")
        self.labelErrorInfo = QtWidgets.QLabel(parent=self.page_GetINFO)
        self.labelErrorInfo.setGeometry(QtCore.QRect(250, 290, 181, 181))
        self.labelErrorInfo.setObjectName("labelErrorInfo")
        self.stackedWidgetFitTrack.addWidget(self.page_GetINFO)
        self.page_GetGoals = QtWidgets.QWidget()
        self.page_GetGoals.setObjectName("page_GetGoals")
        self.labelGOALS = QtWidgets.QLabel(parent=self.page_GetGoals)
        self.labelGOALS.setGeometry(QtCore.QRect(10, 10, 251, 21))
        self.labelGOALS.setObjectName("labelGOALS")
        self.label_goalradio = QtWidgets.QLabel(parent=self.page_GetGoals)
        self.label_goalradio.setGeometry(QtCore.QRect(0, 50, 681, 41))
        self.label_goalradio.setObjectName("label_goalradio")
        self.radioButtonGain = QtWidgets.QRadioButton(parent=self.page_GetGoals)
        self.radioButtonGain.setGeometry(QtCore.QRect(120, 120, 82, 17))
        self.radioButtonGain.setObjectName("radioButtonGain")
        self.radioButtonLose = QtWidgets.QRadioButton(parent=self.page_GetGoals)
        self.radioButtonLose.setGeometry(QtCore.QRect(460, 120, 82, 17))
        self.radioButtonLose.setObjectName("radioButtonLose")
        self.radioButtonMaintain = QtWidgets.QRadioButton(parent=self.page_GetGoals)
        self.radioButtonMaintain.setGeometry(QtCore.QRect(280, 120, 131, 17))
        self.radioButtonMaintain.setObjectName("radioButtonMaintain")
        self.buttonSubmitGoalType = QtWidgets.QPushButton(parent=self.page_GetGoals)
        self.buttonSubmitGoalType.setGeometry(QtCore.QRect(250, 170, 171, 41))
        self.buttonSubmitGoalType.setObjectName("buttonSubmitGoalType")
        self.group_pounds_week = QtWidgets.QGroupBox(parent=self.page_GetGoals)
        self.group_pounds_week.setGeometry(QtCore.QRect(40, 260, 591, 181))
        self.group_pounds_week.setTitle("")
        self.group_pounds_week.setObjectName("group_pounds_week")
        self.labelPoundsAWeek = QtWidgets.QLabel(parent=self.group_pounds_week)
        self.labelPoundsAWeek.setGeometry(QtCore.QRect(0, 20, 441, 31))
        self.labelPoundsAWeek.setObjectName("labelPoundsAWeek")
        self.input_pounds_a_week = QtWidgets.QDoubleSpinBox(parent=self.group_pounds_week)
        self.input_pounds_a_week.setGeometry(QtCore.QRect(450, 20, 61, 31))
        self.input_pounds_a_week.setMinimum(0.5)
        self.input_pounds_a_week.setMaximum(2.0)
        self.input_pounds_a_week.setSingleStep(0.5)
        self.input_pounds_a_week.setObjectName("input_pounds_a_week")
        self.buttonSubmitGoalPoundsaWeek = QtWidgets.QPushButton(parent=self.group_pounds_week)
        self.buttonSubmitGoalPoundsaWeek.setGeometry(QtCore.QRect(210, 90, 171, 41))
        self.buttonSubmitGoalPoundsaWeek.setObjectName("buttonSubmitGoalPoundsaWeek")
        self.stackedWidgetFitTrack.addWidget(self.page_GetGoals)
        self.page_MainMenu = QtWidgets.QWidget()
        self.page_MainMenu.setObjectName("page_MainMenu")
        self.label_mainMenu = QtWidgets.QLabel(parent=self.page_MainMenu)
        self.label_mainMenu.setGeometry(QtCore.QRect(0, 10, 681, 21))
        self.label_mainMenu.setObjectName("label_mainMenu")
        self.label_Addfood = QtWidgets.QLabel(parent=self.page_MainMenu)
        self.label_Addfood.setGeometry(QtCore.QRect(190, 100, 161, 41))
        self.label_Addfood.setObjectName("label_Addfood")
        self.label_VizualizeProgress = QtWidgets.QLabel(parent=self.page_MainMenu)
        self.label_VizualizeProgress.setGeometry(QtCore.QRect(190, 160, 191, 41))
        self.label_VizualizeProgress.setObjectName("label_VizualizeProgress")
        self.label_Quit = QtWidgets.QLabel(parent=self.page_MainMenu)
        self.label_Quit.setGeometry(QtCore.QRect(190, 280, 161, 41))
        self.label_Quit.setObjectName("label_Quit")
        self.label_UpdateWeight = QtWidgets.QLabel(parent=self.page_MainMenu)
        self.label_UpdateWeight.setGeometry(QtCore.QRect(190, 220, 161, 41))
        self.label_UpdateWeight.setObjectName("label_UpdateWeight")
        self.radioButtonAddfood = QtWidgets.QRadioButton(parent=self.page_MainMenu)
        self.radioButtonAddfood.setGeometry(QtCore.QRect(430, 110, 21, 21))
        self.radioButtonAddfood.setText("")
        self.radioButtonAddfood.setObjectName("radioButtonAddfood")
        self.radioButton_Visualize = QtWidgets.QRadioButton(parent=self.page_MainMenu)
        self.radioButton_Visualize.setGeometry(QtCore.QRect(430, 170, 21, 21))
        self.radioButton_Visualize.setText("")
        self.radioButton_Visualize.setObjectName("radioButton_Visualize")
        self.radioButton_UpdateWeight = QtWidgets.QRadioButton(parent=self.page_MainMenu)
        self.radioButton_UpdateWeight.setGeometry(QtCore.QRect(430, 230, 21, 21))
        self.radioButton_UpdateWeight.setText("")
        self.radioButton_UpdateWeight.setObjectName("radioButton_UpdateWeight")
        self.radioButton_Quit = QtWidgets.QRadioButton(parent=self.page_MainMenu)
        self.radioButton_Quit.setGeometry(QtCore.QRect(430, 290, 21, 21))
        self.radioButton_Quit.setText("")
        self.radioButton_Quit.setObjectName("radioButton_Quit")
        self.button_MainMenu = QtWidgets.QPushButton(parent=self.page_MainMenu)
        self.button_MainMenu.setGeometry(QtCore.QRect(280, 360, 131, 51))
        self.button_MainMenu.setObjectName("button_MainMenu")
        self.stackedWidgetFitTrack.addWidget(self.page_MainMenu)
        self.page_addFood = QtWidgets.QWidget()
        self.page_addFood.setObjectName("page_addFood")
        self.label_addFood = QtWidgets.QLabel(parent=self.page_addFood)
        self.label_addFood.setGeometry(QtCore.QRect(0, 60, 681, 31))
        self.label_addFood.setObjectName("label_addFood")
        self.label_foodName = QtWidgets.QLabel(parent=self.page_addFood)
        self.label_foodName.setGeometry(QtCore.QRect(200, 110, 111, 16))
        self.label_foodName.setObjectName("label_foodName")
        self.input_foodname = QtWidgets.QLineEdit(parent=self.page_addFood)
        self.input_foodname.setGeometry(QtCore.QRect(360, 110, 113, 20))
        self.input_foodname.setObjectName("input_foodname")
        self.input_calories = QtWidgets.QLineEdit(parent=self.page_addFood)
        self.input_calories.setGeometry(QtCore.QRect(360, 150, 113, 20))
        self.input_calories.setObjectName("input_calories")
        self.input_protein = QtWidgets.QLineEdit(parent=self.page_addFood)
        self.input_protein.setGeometry(QtCore.QRect(360, 190, 113, 20))
        self.input_protein.setObjectName("input_protein")
        self.input_fat = QtWidgets.QLineEdit(parent=self.page_addFood)
        self.input_fat.setGeometry(QtCore.QRect(360, 230, 113, 20))
        self.input_fat.setObjectName("input_fat")
        self.input_carbs = QtWidgets.QLineEdit(parent=self.page_addFood)
        self.input_carbs.setGeometry(QtCore.QRect(360, 270, 113, 20))
        self.input_carbs.setObjectName("input_carbs")
        self.label_calories = QtWidgets.QLabel(parent=self.page_addFood)
        self.label_calories.setGeometry(QtCore.QRect(200, 150, 111, 16))
        self.label_calories.setObjectName("label_calories")
        self.label_protein = QtWidgets.QLabel(parent=self.page_addFood)
        self.label_protein.setGeometry(QtCore.QRect(200, 190, 111, 16))
        self.label_protein.setObjectName("label_protein")
        self.label_fat = QtWidgets.QLabel(parent=self.page_addFood)
        self.label_fat.setGeometry(QtCore.QRect(200, 230, 111, 16))
        self.label_fat.setObjectName("label_fat")
        self.label_carbs = QtWidgets.QLabel(parent=self.page_addFood)
        self.label_carbs.setGeometry(QtCore.QRect(200, 270, 111, 16))
        self.label_carbs.setObjectName("label_carbs")
        self.button_addFood = QtWidgets.QPushButton(parent=self.page_addFood)
        self.button_addFood.setGeometry(QtCore.QRect(210, 310, 101, 41))
        self.button_addFood.setObjectName("button_addFood")
        self.button_clearAddFood = QtWidgets.QPushButton(parent=self.page_addFood)
        self.button_clearAddFood.setGeometry(QtCore.QRect(360, 310, 101, 41))
        self.button_clearAddFood.setObjectName("button_clearAddFood")
        self.button_returnMainAddFood = QtWidgets.QPushButton(parent=self.page_addFood)
        self.button_returnMainAddFood.setGeometry(QtCore.QRect(10, 10, 111, 41))
        self.button_returnMainAddFood.setObjectName("button_returnMainAddFood")
        self.stackedWidgetFitTrack.addWidget(self.page_addFood)
        self.page_Visualize = QtWidgets.QWidget()
        self.page_Visualize.setObjectName("page_Visualize")
        self.stackedWidgetFitTrack.addWidget(self.page_Visualize)
        self.gridLayout.addWidget(self.stackedWidgetFitTrack, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidgetFitTrack.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FitTRACK"))
        self.label_welcome.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Welcome to FitTrack! </span></p><p align=\"center\"><span style=\" font-size:10pt;\">Please select begin to start!</span></p></body></html>"))
        self.buttonBegin.setText(_translate("MainWindow", "Begin"))
        self.label_infoenter.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Enter your information to get started:</span></p></body></html>"))
        self.label_Name.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Name (first):</span></p></body></html>"))
        self.label_Age.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Age:</span></p></body></html>"))
        self.label_goalWeight.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Goal Weight (lbs):</span></p></body></html>"))
        self.label_currentWeight.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Current Weight (lbs):</span></p></body></html>"))
        self.label_sex.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Sex (m/f):</span></p></body></html>"))
        self.button_submitINFO.setText(_translate("MainWindow", "Submit"))
        self.labelErrorInfo.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; text-decoration: underline; color:#aa0000;\">Error!</span></p><p align=\"center\"><span style=\" font-size:10pt; color:#aa0000;\">Ex- Name: John</span></p><p align=\"center\"><span style=\" font-size:10pt; color:#aa0000;\">Age: 25</span></p><p align=\"center\"><span style=\" font-size:10pt; color:#aa0000;\">Sex: m</span></p><p align=\"center\"><span style=\" font-size:10pt; color:#aa0000;\">Current Weight: 180</span></p><p align=\"center\"><span style=\" font-size:10pt; color:#aa0000;\">Goal: 175</span></p></body></html>"))
        self.labelGOALS.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">GOALS</span></p></body></html>"))
        self.label_goalradio.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">What is your goal?</span></p></body></html>"))
        self.radioButtonGain.setText(_translate("MainWindow", "Gain Weight"))
        self.radioButtonLose.setText(_translate("MainWindow", "Lose Weight"))
        self.radioButtonMaintain.setText(_translate("MainWindow", "Maintain Weight"))
        self.buttonSubmitGoalType.setText(_translate("MainWindow", "Submit"))
        self.labelPoundsAWeek.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">How many pounds do you want to lose/gain a week? :</span></p></body></html>"))
        self.buttonSubmitGoalPoundsaWeek.setText(_translate("MainWindow", "Submit"))
        self.label_mainMenu.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Main Menu</span></p></body></html>"))
        self.label_Addfood.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Add a new food: </span></p></body></html>"))
        self.label_VizualizeProgress.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Vizualize Progress:</span></p></body></html>"))
        self.label_Quit.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Quit:</span></p></body></html>"))
        self.label_UpdateWeight.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Update Weight:</span></p></body></html>"))
        self.button_MainMenu.setText(_translate("MainWindow", "Select"))
        self.label_addFood.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Add a food:</span></p></body></html>"))
        self.label_foodName.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Name:</span></p></body></html>"))
        self.label_calories.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Calories:</span></p></body></html>"))
        self.label_protein.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Protein:</span></p></body></html>"))
        self.label_fat.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Fat:</span></p></body></html>"))
        self.label_carbs.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Carbs:</span></p></body></html>"))
        self.button_addFood.setText(_translate("MainWindow", "Add Food"))
        self.button_clearAddFood.setText(_translate("MainWindow", "Clear"))
        self.button_returnMainAddFood.setText(_translate("MainWindow", "Main Menu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
