import sys
# import sys
from PyQt6 import QtGui
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton,QRadioButton,QHBoxLayout,QLineEdit,QInputDialog,
                             QToolTip, QMessageBox, QLabel)


class Intermediate:
    def __init__(self):
        pass

class Advanced:
    def __init__(self):
        pass

class Window1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "First Window"
        self.setGeometry(100,100,680,500)
        self.pushButton = QPushButton("Back", self)
        self.pushButton.clicked.connect(self.go_back)
        self.pushButton.move(200,200)
        self.le = QLineEdit(self)
        self.le.move(300,400)
        text, ok = QInputDialog.getText(self, 'Input Dialog',
                                        'Enter your name:')
        b = Basic()  # <===
        ans = b.organic(1, 2, 3, 4, 5)
        print(ans[2])
        self.pushButton3 = QPushButton(str(ans[0]), self)
        self.pushButton3.move(175, 0)
        self.pushButton1 = QPushButton(str(ans[1]), self)
        self.pushButton2 = QPushButton(str(ans[2]), self)
        self.pushButton2.move(275, 0)
        self.setWindowTitle("Window1")

        # self.main_window()
    def go_back(self):
        self.w = Window()
        self.w.show()
        self.hide()

class Window2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Second Window"
        self.setGeometry(100,100,680,500)
        self.pushButton = QPushButton("Back", self)
        self.pushButton.clicked.connect(self.go_back)
        # b = Basic()  # <===
        # ans = b.organic(1, 2, 3, 4, 5)
        # print(ans[2])
        # self.pushButton3 = QPushButton(str(ans[0]), self)
        # self.pushButton3.move(175, 0)
        # self.pushButton1 = QPushButton(str(ans[1]), self)
        # self.pushButton2 = QPushButton(str(ans[2]), self)
        # self.pushButton2.move(275, 0)
        self.setWindowTitle("Window2")

        # self.main_window()
    def go_back(self):
        self.w = Window()
        self.w.show()
        self.hide()

class Window3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Third Window"
        self.setGeometry(100,100,680,500)
        self.pushButton = QPushButton("Back", self)
        self.pushButton.clicked.connect(self.go_back)
        # b = Basic()  # <===
        # ans = b.organic(1, 2, 3, 4, 5)
        # print(ans[2])
        # self.pushButton3 = QPushButton(str(ans[0]), self)
        # self.pushButton3.move(175, 0)
        # self.pushButton1 = QPushButton(str(ans[1]), self)
        # self.pushButton2 = QPushButton(str(ans[2]), self)
        # self.pushButton2.move(275, 0)
        self.setWindowTitle("Window3")

        # self.main_window()
    def go_back(self):
        self.w = Window()
        self.w.show()
        self.hide()

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Welcome"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        layout = QHBoxLayout()
        self.b1 = QRadioButton("Basic",self)
        self.b1.move(200,100)
        self.b1.setChecked(True)
        # self.b1.toggled.connect(lambda: self.btnstate())
        layout.addWidget(self.b1)

        self.b2 = QRadioButton("Intermediate",self)
        # self.b2.toggled.connect(lambda: self.btnstate())
        self.b2.move(300, 100)
        self.b3 = QRadioButton("Advanced", self)
        # self.b3.toggled.connect(lambda: self.btnstate())
        self.b3.move(400, 100)
        layout.addWidget(self.b2)
        self.pushButton = QPushButton("Start", self)
        self.pushButton.move(275, 200)
        self.pushButton.setToolTip("<h3>Start the Session</h3>")
        # self.btnstate()
        windows = [self.window1,self.window2,self.window3]
        # print(self.btnstate())
        self.pushButton.clicked.connect(self.btnstate)
        if self.pushButton.isChecked():
            print(1)
            self.btnstate()
        # self.pushButton.clicked(self.btnstate())
        print(123)
        self.main_window()


    def btnstate(self):
        print(self.b1.isChecked())
        print(self.b2.isChecked())
        if self.b1.isChecked()==True:
            self.window1()
        if self.b2.isChecked()==True:
            self.window2()
        if self.b3.isChecked()==True:
            self.window3()
        # else :
        #     self.window3()

    def main_window(self):
        self.label = QLabel("Manager", self)
        self.label.move(285, 175)
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def window1(self):                                             # <===
        self.w = Window1()
        self.w.show()
        self.hide()
    def window2(self):                                             # <===
        self.w = Window2()
        self.w.show()
        self.hide()
    def window3(self):                                             # <===
        self.w = Window3()
        self.w.show()
        self.hide()


class Basic(QMainWindow):
    def __init__(self):
        super().__init__()

    def organic(self, a, b, c, d, KLOC):
        # E = a(KLOC) ^ b
        E = a*((KLOC) ^ b)
        time = c*((E) ^ d)
        person = E / time
        # self.w = Window()
        # self.w.show()
        # self.hide()
        return [E,time,person]


    def semiorganic(self):
        pass

    def embeded(self):
        pass
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())