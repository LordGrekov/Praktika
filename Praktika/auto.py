from PyQt6 import QtGui
from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QApplication, QLineEdit, QLabel,
                            QPushButton, QGridLayout, QDialog, QRadioButton, QStackedWidget, QHBoxLayout)
from PyQt6.QtCore import QTimer, Qt
import random
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.mainStack = QStackedWidget()
# Авторизация ......................................
        self.setWindowTitle('Autorise')
        loginLabel = QLabel('<center>Login</center>')
        self.loginLine = QLineEdit()
        passLabel = QLabel('<center>Password</center>')
        self.passLine = QLineEdit()
        entryBtn = QPushButton('Enrty')
        entryBtn.clicked.connect(self.entryBtn_click)

        main_grid = QGridLayout()

        main_grid.addWidget(loginLabel,0,0)
        main_grid.addWidget(self.loginLine,1,0)
        main_grid.addWidget(passLabel,2,0)
        main_grid.addWidget(self.passLine,3,0)
        main_grid.addWidget(entryBtn,4,0)

        widget = QWidget()
        widget.setLayout(main_grid)

# Ввод имени .....................................
        
        nameWidget = QWidget()
        nameLayout = QVBoxLayout()
        
        nameLabel = QLabel('<center>Name</center>')
        nameLine = QLineEdit()
        nameBtn = QPushButton('Enrty')
        nameBtn.clicked.connect(self.nameBtn_click)

        nameLayout.addWidget(nameLabel)
        nameLayout.addWidget(nameLine)
        nameLayout.addWidget(nameBtn)

        nameWidget.setLayout(nameLayout)

        with open('Praktika/styles.css', 'r') as css:
            nameWidget.setStyleSheet(css.read())
# mainStack ..............................................

        self.mainStack.addWidget(widget)  
        self.mainStack.addWidget(nameWidget)

        self.setCentralWidget(self.mainStack)
    
        with open('Praktika/styles.css', 'r') as css:
            widget.setStyleSheet(css.read())        


    def entryBtn_click(self):
        self.login = "user"
        password = "user"
        if self.loginLine.text() == self.login and self.passLine.text() == password:
            self.mainStack.setCurrentIndex(1)
        if self.loginLine.text() != self.login or self.passLine.text() != password:
            copchaWindow.show()
    
    def nameBtn_click(self):
        testWindow.show()


class Capcha(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Captcha')
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        capcha = QLabel("Вы ввели неправильный логин или пфроль, заполните капчу")
        self.capchaLine = QLineEdit()

        rnd = random.randint(1000,9999)

        self.label = QLabel()
        self.label.setText(str(rnd))

        
        self.lblTim = QLabel("")

        self.capchaBtn = QPushButton('Ok')
        self.capchaBtn.clicked.connect(self.capchaBtn_click)
        capchaGrid = QGridLayout()

        capchaGrid.addWidget(capcha,0,0)
        capchaGrid.addWidget(self.capchaLine,1,0)
        capchaGrid.addWidget(self.label,2,0)
        capchaGrid.addWidget(self.lblTim,3,0)
        capchaGrid.addWidget(self.capchaBtn,4,0)

        self.setLayout(capchaGrid)

        with open('Praktika/styles.css', 'r') as css:
            self.setStyleSheet(css.read())        


    def capchaBtn_click(self):
        if self.capchaLine.text() == self.label.text():
            self.close()
            
        else:
            self.timer = QTimer()
            self.timer.setInterval(1000) # 1000 милисек через каждые 1000 милесек запускается tim
            self.timer.timeout.connect(self.tim) # указываем что запускается tim
            self.startTim()
            self.capchaBtn.setEnabled(False)


    def tim(self):
        self.counter -= 1
        self.lblTim.setText(f'осталось {self.counter}')
        if self.counter == 0:
            self.lblTim.setText('')
            self.label.setText('')
            self.timer.stop()
            self.capchaBtn.setEnabled(True)
            rnd = random.randint(1000,9999)
            self.label.setText(str(rnd))
    
    def startTim(self):
        self.counter = 3
        self.timer.start()
        

class Test(QWidget):
    def __init__(self):
        super().__init__()
        self.ball = 0
        self.setWindowTitle('Test')
        self.resize(400, 200)
        
        self.stack = QStackedWidget()
        self.bigStack = QStackedWidget()

# Кнопки переключения ...................................................

        buttonWidget = QWidget()

        buttonLayout = QHBoxLayout()

        backBtn = QPushButton('Назад')
        backBtn.clicked.connect(self.backBtn_click)

        goBtn = QPushButton('Вперёд')
        goBtn.clicked.connect(self.goBtn_click)

        buttonLayout.addWidget(backBtn)
        buttonLayout.addWidget(goBtn)

        buttonWidget.setLayout(buttonLayout)   
          
# первое окно теста ..........................................................
        
        testWidget = QWidget()

        testLayout = QVBoxLayout()
        self.testQuestonLabel = QLabel()
        self.radioBtn1 = QRadioButton('QMainWIndow это главное окно')
        self.radioBtn1.clicked.connect(self.radioBtn_click)
        self.radioBtn2 = QRadioButton('QWidget это глакное окно')
        self.radioBtn2.clicked.connect(self.radioBtn2_click)
        self.radioBtn3 = QRadioButton('QDialig это глшавное окно')
        self.radioBtn3.clicked.connect(self.radioBtn3_click)

        testLayout.addWidget(self.radioBtn1)
        testLayout.addWidget(self.radioBtn2)
        testLayout.addWidget(self.radioBtn3)

        testWidget.setLayout(testLayout)
        
# второе окно теста .........................................................

        testWidget2 = QWidget()

        testLayout2 = QVBoxLayout()
        
        self.radioBtn21 = QRadioButton('QMainWendow')
        self.radioBtn21.clicked.connect(self.radioBtn21_click)
        self.radioBtn22 = QRadioButton('QMainWindow')
        self.radioBtn22.clicked.connect(self.radioBtn22_click)
        self.radioBtn23 = QRadioButton('QMainWindov')
        self.radioBtn23.clicked.connect(self.radioBtn23_click)
        

        testLayout2.addWidget(self.radioBtn21)
        testLayout2.addWidget(self.radioBtn22)
        testLayout2.addWidget(self.radioBtn23)

        testWidget2.setLayout(testLayout2)

# окно подведения этогов ..................................

        testResultWidget = QWidget()

        testResultLayout = QVBoxLayout()

        testResultBtn = QPushButton('Поспотреть итоги')
        testResultBtn.clicked.connect(self.testResultBtn_click)

        testResultLayout.addWidget(testResultBtn)

        testResultWidget.setLayout(testResultLayout)

# окно вывода баллов .....................................
        
        self.resultWidget = QWidget()

        resultLayout = QVBoxLayout()

        self.resultLabel = QLabel()
        # self.resultLabel.setText(f'{self.ball}')
        resultBtn = QPushButton('Вывесть баллы')
        resultBtn.clicked.connect(self.resultBtn_click)
        closeBtn = QPushButton('Закончить тест')
        closeBtn.clicked.connect(self.closeBtn_click)

        resultLayout.addWidget(self.resultLabel)
        resultLayout.addWidget(resultBtn)
        resultLayout.addWidget(closeBtn)

        self.resultWidget.setLayout(resultLayout)

        with open('Praktika/styles.css', 'r') as css:
            self.resultWidget.setStyleSheet(css.read())  

# Stack ....................................................................

        self.stack.addWidget(testWidget)
        self.stack.addWidget(testWidget2)
        self.stack.addWidget(testResultWidget)

# Grid ..................................................................
        
        grid = QGridLayout(self)
        
        grid.addWidget(self.stack)
        grid.addWidget(buttonWidget)

   
        with open('Praktika/styles.css', 'r') as css:
            self.setStyleSheet(css.read())       
       
# Функции кнопок переключения ...........................................

    def backBtn_click(self):
        self.stack.setCurrentIndex(self.stack.currentIndex()-1)


    def goBtn_click(self):
        self.stack.setCurrentIndex(self.stack.currentIndex()+1)


    def testResultBtn_click(self):
        self.resultWidget.show()

# Функция проверки ........................................................

    def radioBtn_click(self):
        self.radioBtn1.setEnabled(False)
        self.radioBtn2.setEnabled(False)
        self.radioBtn3.setEnabled(False)

        if self.radioBtn1.isChecked():
            self.ball += 1


    def radioBtn22_click(self):
        self.radioBtn21.setEnabled(False)
        self.radioBtn22.setEnabled(False)
        self.radioBtn23.setEnabled(False)

        if self.radioBtn1.isChecked():
            self.ball += 1
            
# Функция блокировки фуекций .................................
#    
    def radioBtn2_click(self):
        self.radioBtn1.setEnabled(False)
        self.radioBtn2.setEnabled(False)
        self.radioBtn3.setEnabled(False)

    def radioBtn3_click(self):
        self.radioBtn1.setEnabled(False)
        self.radioBtn2.setEnabled(False)
        self.radioBtn3.setEnabled(False)  

    def radioBtn21_click(self):
        self.radioBtn1.setEnabled(False)
        self.radioBtn2.setEnabled(False)
        self.radioBtn3.setEnabled(False)
    def radioBtn23_click(self):

        self.radioBtn1.setEnabled(False)
        self.radioBtn2.setEnabled(False)
        self.radioBtn3.setEnabled(False)          
# ///////////////////////////////////////////////
    def closeBtn_click(self):
        bossWindow.close()
        copchaWindow.close()
        testWindow.close()
        self.resultWidget.close()

    
    def resultBtn_click(self):
        self.resultLabel.setText(str(self.ball))
 

app = QApplication(sys.argv)
bossWindow = MainWindow()
copchaWindow = Capcha()
testWindow = Test()
bossWindow.show()
app.exec()
