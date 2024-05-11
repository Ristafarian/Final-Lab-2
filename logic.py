from PyQt6.QtWidgets import *
from gui import *
import csv
import os.path


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        """
        Class initialization.
        """
        super().__init__()
        self.setupUi(self)
        self.reset()

        self.button_submit.clicked.connect(lambda: self.submit())
        self.button_enter.clicked.connect(lambda: self.enter())
        self.button_reset.clicked.connect(lambda: self.reset())

    def submit(self) -> None:
        """
        Submit name and # tests.
        """
        try:
            name = self.input_name.text()
            number_tests = int(self.input_tests.text())

            if name.replace(' ', '').isalpha():
                pass
            else:
                raise

            if number_tests == 1:
                pass
            elif number_tests == 2:
                self.input_fall_midterm.setFocus()
                self.label_fall_final.show()
                self.input_fall_final.show()
            elif number_tests == 3:
                self.input_fall_midterm.setFocus()
                self.label_fall_final.show()
                self.input_fall_final.show()
                self.label_spring_midterm.show()
                self.input_spring_midterm.show()
            elif number_tests == 4:
                self.input_fall_midterm.setFocus()
                self.label_fall_final.show()
                self.input_fall_final.show()
                self.label_spring_midterm.show()
                self.input_spring_midterm.show()
                self.label_spring_final.show()
                self.input_spring_final.show()
            else:
                raise

            self.setFixedWidth(340)
            self.setFixedHeight(300)
            self.label_name.setText(f'{name}')
            self.label_name.setStyleSheet('font-weight: bold; font-size: 10;')
            self.input_name.hide()
            self.input_tests.hide()
            self.label_submit.clear()
            self.button_submit.hide()
            self.button_reset.show()
            self.label_tests.setText('Number of tests submitted!')
            self.label_tests.setStyleSheet('color: blue; font-size: 10;')

        except:
            self.label_submit.setText('Please enter valid name. Please enter # tests (1-4).')
            self.label_submit.setStyleSheet('color: red; font-weight: bold;')

    def enter(self) -> None:
        """
        Enter test scores into data file and calculate grade.
        """
        try:
            self.label_tests.clear()
            path = './data.csv'

            if os.path.exists(path):
                pass
            else:
                with open('data.csv', 'a', newline='') as data:
                    content = csv.writer(data)
                    content.writerow(['Name', 'Fall Midterm', 'Fall Final', 'Spring Midterm',
                                      'Spring Final', 'Final Grade'])

            name = self.input_name.text()

            score1 = '0'
            score2 = '0'
            score3 = '0'
            score4 = '0'
            final = '0'

            if self.input_spring_final.text() == '':
                pass
            else:
                if 0 <= int(self.input_spring_final.text()) <= 100:
                    score1 = int(self.input_fall_midterm.text())
                    score2 = int(self.input_fall_final.text())
                    score3 = int(self.input_spring_midterm.text())
                    score4 = int(self.input_spring_final.text())
                    final = (score1 + score2 + score3 + score4) / 4
                    score_list = [name, score1, score2, score3, score4, "{0:.2f}".format(final)]
                    with open('data.csv', 'a', newline='') as data:
                        content = csv.writer(data)
                        content.writerow(score_list)
                    self.reset()
                    self.label_submit.setText('Test score(s) entered!')
                    self.label_submit.setStyleSheet('color: blue; font-weight: bold;')
                    return
                else:
                    raise

            if self.input_spring_midterm.text() == '':
                pass
            else:
                if 0 <= int(self.input_spring_midterm.text()) <= 100:
                    score1 = int(self.input_fall_midterm.text())
                    score2 = int(self.input_fall_final.text())
                    score3 = int(self.input_spring_midterm.text())
                    final = (score1 + score2 + score3) / 3
                    score_list = [name, score1, score2, score3, score4, "{0:.2f}".format(final)]
                    with open('data.csv', 'a', newline='') as data:
                        content = csv.writer(data)
                        content.writerow(score_list)
                    self.reset()
                    self.label_submit.setText('Test score(s) entered!')
                    self.label_submit.setStyleSheet('color: blue; font-weight: bold;')
                    return
                else:
                    raise

            if self.input_fall_final.text() == '':
                pass
            else:
                if 0 <= int(self.input_fall_final.text()) <= 100:
                    score1 = int(self.input_fall_midterm.text())
                    score2 = int(self.input_fall_final.text())
                    final = (score1 + score2) / 2
                    score_list = [name, score1, score2, score3, score4, "{0:.2f}".format(final)]
                    with open('data.csv', 'a', newline='') as data:
                        content = csv.writer(data)
                        content.writerow(score_list)
                    self.reset()
                    self.label_submit.setText('Test score(s) entered!')
                    self.label_submit.setStyleSheet('color: blue; font-weight: bold;')
                    return
                else:
                    raise

            if self.input_fall_midterm.text() == '':
                pass
            else:
                if 0 <= int(self.input_fall_midterm.text()) <= 100:
                    score1 = int(self.input_fall_midterm.text())
                    final = score1
                    score_list = [name, score1, score2, score3, score4, final]
                    with open('data.csv', 'a', newline='') as data:
                        content = csv.writer(data)
                        content.writerow(score_list)
                    self.reset()
                    self.label_submit.setText('Test score(s) entered!')
                    self.label_submit.setStyleSheet('color: blue; font-weight: bold;')
                    return
                else:
                    raise

            if self.input_fall_midterm.text() == '':
                raise

            if self.input_fall_final.text() == '':
                raise

            if self.input_spring_midterm.text() == '':
                raise

            if self.input_spring_final.text() == '':
                raise


        except:
            self.label_tests.setText('Please enter valid scores (0-100)')
            self.label_tests.setStyleSheet('color: red; font-size: 10; font-weight: bold;')

    def reset(self) -> None:
        """
        Reset to defaults.
        """
        self.setFixedWidth(180)
        self.setFixedHeight(300)
        self.input_name.show()
        self.input_name.clear()
        self.input_name.setFocus()
        self.label_name.setText('Student Name')
        self.label_name.setStyleSheet('font-weight: regular; font-size: 8;')
        self.input_tests.show()
        self.input_tests.clear()
        self.label_tests.setText('Number of Tests Taken')
        self.label_tests.setStyleSheet('font-size: 8; font-weight: regular; color: black')
        self.label_submit.clear()
        self.button_submit.show()
        self.label_fall_final.hide()
        self.input_fall_final.hide()
        self.label_spring_midterm.hide()
        self.input_spring_midterm.hide()
        self.label_spring_final.hide()
        self.input_spring_final.hide()
        self.button_reset.hide()
