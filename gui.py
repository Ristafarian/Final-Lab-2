# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(340, 300)
        MainWindow.setMinimumSize(QtCore.QSize(180, 300))
        MainWindow.setMaximumSize(QtCore.QSize(340, 300))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input_name = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input_name.setGeometry(QtCore.QRect(30, 20, 111, 20))
        self.input_name.setObjectName("input_name")
        self.label_name = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(20, 50, 131, 51))
        self.label_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_name.setWordWrap(True)
        self.label_name.setObjectName("label_name")
        self.input_tests = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input_tests.setGeometry(QtCore.QRect(50, 110, 71, 20))
        self.input_tests.setObjectName("input_tests")
        self.label_tests = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_tests.setGeometry(QtCore.QRect(20, 140, 131, 71))
        self.label_tests.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_tests.setWordWrap(True)
        self.label_tests.setObjectName("label_tests")
        self.button_submit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_submit.setGeometry(QtCore.QRect(50, 220, 71, 23))
        self.button_submit.setObjectName("button_submit")
        self.label_spring_midterm = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_spring_midterm.setGeometry(QtCore.QRect(210, 140, 91, 16))
        self.label_spring_midterm.setObjectName("label_spring_midterm")
        self.input_spring_midterm = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input_spring_midterm.setGeometry(QtCore.QRect(210, 120, 41, 20))
        self.input_spring_midterm.setObjectName("input_spring_midterm")
        self.label_spring_final = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_spring_final.setGeometry(QtCore.QRect(210, 180, 81, 21))
        self.label_spring_final.setObjectName("label_spring_final")
        self.input_spring_final = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input_spring_final.setGeometry(QtCore.QRect(210, 160, 41, 20))
        self.input_spring_final.setObjectName("input_spring_final")
        self.label_fall_midterm = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_fall_midterm.setGeometry(QtCore.QRect(210, 40, 81, 16))
        self.label_fall_midterm.setObjectName("label_fall_midterm")
        self.input_fall_midterm = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input_fall_midterm.setGeometry(QtCore.QRect(210, 20, 41, 20))
        self.input_fall_midterm.setText("")
        self.input_fall_midterm.setObjectName("input_fall_midterm")
        self.label_fall_final = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_fall_final.setGeometry(QtCore.QRect(210, 80, 81, 21))
        self.label_fall_final.setObjectName("label_fall_final")
        self.input_fall_final = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input_fall_final.setGeometry(QtCore.QRect(210, 60, 41, 20))
        self.input_fall_final.setText("")
        self.input_fall_final.setObjectName("input_fall_final")
        self.button_enter = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_enter.setGeometry(QtCore.QRect(200, 220, 81, 23))
        self.button_enter.setObjectName("button_enter")
        self.label_submit = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_submit.setGeometry(QtCore.QRect(20, 160, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_submit.setFont(font)
        self.label_submit.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_submit.setWordWrap(True)
        self.label_submit.setObjectName("label_submit")
        self.button_reset = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_reset.setGeometry(QtCore.QRect(120, 220, 71, 23))
        self.button_reset.setObjectName("button_reset")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 340, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Test Recorder"))
        self.label_name.setText(_translate("MainWindow", "Student Name"))
        self.label_tests.setText(_translate("MainWindow", "Number of Tests Taken"))
        self.button_submit.setText(_translate("MainWindow", "Submit"))
        self.label_spring_midterm.setText(_translate("MainWindow", "Spring Midterm"))
        self.label_spring_final.setText(_translate("MainWindow", "Spring Final"))
        self.label_fall_midterm.setText(_translate("MainWindow", "Fall Midterm"))
        self.label_fall_final.setText(_translate("MainWindow", "Fall Final"))
        self.button_enter.setText(_translate("MainWindow", "Enter Grades"))
        self.label_submit.setText(_translate("MainWindow", "Please enter valid input"))
        self.button_reset.setText(_translate("MainWindow", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
