import sys
# import sys
from PyQt6 import QtGui,QtCore,QtWidgets
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton,QRadioButton,QHBoxLayout,QLineEdit,QInputDialog,
                             QToolTip, QMessageBox, QLabel)
from PyQt6 import QtCore, QtGui,QtWidgets
from PyQt6.QtGui import QIcon
from COCOMO import Basic
class Intermediate:
    def __init__(self):
        pass

class Advanced:
    def __init__(self):
        pass

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(15)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(213, 251, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(360, 160, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.radioButton.setFont(font)
        self.radioButton.setToolTipDuration(50000)
        self.radioButton.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.radioButton.setAutoFillBackground(False)
        self.radioButton.setIconSize(QtCore.QSize(15, 15))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(360, 210, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setToolTipDuration(50000)
        self.radioButton_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.radioButton_2.setAutoFillBackground(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 20, 801, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.clicked.connect(self.proceed)
        self.pushButton.setGeometry(QtCore.QRect(370, 280, 56, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 540, 21, 21))
        self.pushButton_2.setToolTipDuration(0)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 50px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushButton_2.setText("")
        icon = QIcon('back.png')
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 540, 21, 21))
        self.pushButton_3.setToolTipDuration(0)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 50px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushButton_3.setText("")
        icon = QIcon('home.png')
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton.setToolTip(_translate("MainWindow", "COCOMO I is used for ......"))
        self.radioButton.setText(_translate("MainWindow", "COCOMO I"))
        self.radioButton_2.setToolTip(_translate("MainWindow", "COCOMO I is used for ......"))
        self.radioButton_2.setText(_translate("MainWindow", "COCOMO II"))
        self.label_2.setText(_translate("MainWindow", "SOFTWARE ESTIMATION TOOL"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
    def proceed(self):
        if self.radioButton.isChecked():
            self.w=MainWindow2()
            self.w.show()
            self.hide()
        elif self.radioButton.isChecked():
            print('Hello')
        else:
            print('Hello')

class MainWindow1(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow1, self).__init__()
        self.setupUi(self)
        self.show()

class SecondPage(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(836, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.background = QtWidgets.QFrame(self.centralwidget)
        self.background.setStyleSheet("\n"
"    background-color: rgb(19, 19, 19);\n"
"")
        self.background.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.background.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.background.setObjectName("background")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.background)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QFrame(self.background)
        self.header.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.header.setObjectName("header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.header)
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(15)
        self.title.setFont(font)
        self.title.setStyleSheet("color : rgb(0, 0, 0);\n"
"background-color: rgb(170, 255, 255);")
        self.title.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.title.setScaledContents(True)
        self.title.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.title.setObjectName("title")
        self.verticalLayout_2.addWidget(self.title, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.modelname = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.modelname.setFont(font)
        self.modelname.setStyleSheet("color:rgb(255, 255, 255)")
        self.modelname.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.modelname.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.modelname.setObjectName("modelname")
        self.verticalLayout_2.addWidget(self.modelname)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.header)
        self.main = QtWidgets.QFrame(self.background)
        self.main.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.main.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.main.setObjectName("main")
        self.table_constant = QtWidgets.QTableWidget(self.main)
        self.table_constant.setGeometry(QtCore.QRect(90, 0, 481, 131))
        self.table_constant.setStyleSheet("background-color :rgb(170, 255, 255) ")
        self.table_constant.setObjectName("table_constant")
        self.table_constant.setColumnCount(5)
        self.table_constant.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.table_constant.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_constant.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(10)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 0))
        self.table_constant.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Project Type")
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_constant.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_constant.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_constant.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_constant.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_constant.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(10)
        item.setFont(font)
        self.table_constant.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.table_constant.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.table_constant.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.table_constant.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.table_constant.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(10)
        item.setFont(font)
        self.table_constant.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.table_constant.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.table_constant.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.table_constant.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.table_constant.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(10)
        item.setFont(font)
        self.table_constant.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.table_constant.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.table_constant.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.table_constant.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.table_constant.setItem(2, 4, item)
        self.model_chose = QtWidgets.QFrame(self.main)
        self.model_chose.setGeometry(QtCore.QRect(0, 160, 832, 51))
        self.model_chose.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.model_chose.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.model_chose.setObjectName("model_chose")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.model_chose)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton = QtWidgets.QRadioButton(self.model_chose)
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("color:rgb(255, 255, 255)")
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_3.addWidget(self.radioButton, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.radioButton_2 = QtWidgets.QRadioButton(self.model_chose)
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("color:rgb(255, 255, 255)")
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_3.addWidget(self.radioButton_2, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.radioButton_3 = QtWidgets.QRadioButton(self.model_chose)
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setStyleSheet("color:rgb(255, 255, 255)")
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_3.addWidget(self.radioButton_3, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.verticalLayout.addWidget(self.main)
        self.footer = QtWidgets.QFrame(self.background)
        self.footer.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.footer.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.footer.setObjectName("footer")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.footer)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.footer)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame = QtWidgets.QFrame(self.frame_3)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label = QtWidgets.QLabel(self.frame_5)
        self.label.setGeometry(QtCore.QRect(80, 30, 311, 20))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(255, 255, 255)")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit.setGeometry(QtCore.QRect(0, 30, 113, 22))
        self.lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.frame_6)
        self.verticalLayout_4.addWidget(self.frame)
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        self.pushButton.setGeometry(QtCore.QRect(360, 30, 120, 40))
        self.lineEdit.setStyleSheet(
            "color:rgb(255, 255, 255);"
        )
        self.pushButton.clicked.connect(self.calculate)
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("\n"
"background-color: rgb(170, 255, 255);")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 540, 21, 21))
        self.pushButton_2.setToolTipDuration(0)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
                                        "    color: #333;\n"
                                        "    border: 2px solid #555;\n"
                                        "    border-radius: 50px;\n"
                                        "    border-style: outset;\n"
                                        "    background: qradialgradient(\n"
                                        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                        "        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
                                        "        );\n"
                                        "    padding: 5px;\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    background: qradialgradient(\n"
                                        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                        "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
                                        "        );\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    border-style: inset;\n"
                                        "    background: qradialgradient(\n"
                                        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                        "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                        "        );\n"
                                        "    }")
        self.pushButton_2.setText("")
        icon = QIcon('back.png')
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 540, 21, 21))
        self.pushButton_3.setToolTipDuration(0)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
                                        "    color: #333;\n"
                                        "    border: 2px solid #555;\n"
                                        "    border-radius: 50px;\n"
                                        "    border-style: outset;\n"
                                        "    background: qradialgradient(\n"
                                        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                        "        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
                                        "        );\n"
                                        "    padding: 5px;\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    background: qradialgradient(\n"
                                        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                        "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
                                        "        );\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    border-style: inset;\n"
                                        "    background: qradialgradient(\n"
                                        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                        "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                        "        );\n"
                                        "    }")
        self.pushButton_3.setText("")
        icon = QIcon('home.png')
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2.clicked.connect(self.go_back)
        self.pushButton_3.clicked.connect(self.go_back)
        self.verticalLayout_4.addWidget(self.frame_4)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.footer)
        self.horizontalLayout.addWidget(self.background)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Software Estimation Tool"))
        self.modelname.setText(_translate("MainWindow", "Basic COCOMO"))
        item = self.table_constant.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.table_constant.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.table_constant.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.table_constant.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "a"))
        item = self.table_constant.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "b"))
        item = self.table_constant.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "c"))
        item = self.table_constant.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "d"))
        __sortingEnabled = self.table_constant.isSortingEnabled()
        self.table_constant.setSortingEnabled(False)
        item = self.table_constant.item(0, 0)
        item.setText(_translate("MainWindow", "Organic"))
        item = self.table_constant.item(0, 1)
        item.setText(_translate("MainWindow", "2.4"))
        item = self.table_constant.item(0, 2)
        item.setText(_translate("MainWindow", "1.05"))
        item = self.table_constant.item(0, 3)
        item.setText(_translate("MainWindow", "2.5"))
        item = self.table_constant.item(0, 4)
        item.setText(_translate("MainWindow", "0.38"))
        item = self.table_constant.item(1, 0)
        item.setText(_translate("MainWindow", "Semidetached"))
        item = self.table_constant.item(1, 1)
        item.setText(_translate("MainWindow", "3"))
        item = self.table_constant.item(1, 2)
        item.setText(_translate("MainWindow", "1.12"))
        item = self.table_constant.item(1, 3)
        item.setText(_translate("MainWindow", "2.5"))
        item = self.table_constant.item(1, 4)
        item.setText(_translate("MainWindow", "0.35"))
        item = self.table_constant.item(2, 0)
        item.setText(_translate("MainWindow", "Embedded"))
        item = self.table_constant.item(2, 1)
        item.setText(_translate("MainWindow", "3.6"))
        item = self.table_constant.item(2, 2)
        item.setText(_translate("MainWindow", "1.2"))
        item = self.table_constant.item(2, 3)
        item.setText(_translate("MainWindow", "2.5"))
        item = self.table_constant.item(2, 4)
        item.setText(_translate("MainWindow", "0.32"))
        self.table_constant.setSortingEnabled(__sortingEnabled)
        self.radioButton.setText(_translate("MainWindow", "Organic"))
        self.radioButton_2.setText(_translate("MainWindow", "Semidetached"))
        self.radioButton_3.setText(_translate("MainWindow", "Embedded"))
        self.label.setText(_translate("MainWindow", "Enter KLOC for your project"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
    def go_back(self):
        self.w = MainWindow1()
        self.w.show()
        self.hide()

    def calculate(self):
        bas=Basic()
        kloc=int(self.lineEdit.text())
        print(kloc)
        if self.radioButton.isChecked():
            ans=bas.organic(2.4,1.05,2.5,0.38,kloc)
            self.w=MainWindow3(ans)
            self.w.show()
            self.hide()
        elif self.radioButton_2.isChecked():
            ans=bas.organic(3,1.12,2.5,0.35,kloc)
            self.w = MainWindow3(ans)
            self.w.show()
            self.hide()
        elif self.radioButton_3.isChecked():
            ans = bas.organic(3.6, 1.2, 2.5, 0.32, kloc)
            self.w = MainWindow3(ans)
            self.w.show()
            self.hide()
        else:
            print('Nothing')
            # print(bas.organic(1,2,3,4,50))



class MainWindow2(QtWidgets.QMainWindow, SecondPage):
    def __init__(self):
        super(MainWindow2, self).__init__()
        self.setupUi(self)
        self.show()

class Page3(object):
    def setupUi(self, MainWindow,ans):
        self.ans=ans
        print(self.ans)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(15)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 791, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 110, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel {\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: rgb(85, 255, 255);\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QLabel:hover {\n"
"    background:  rgb(170, 255, 255);\n"
"    }\n"
"\n"
"QLabel:pressed {\n"
"    border-style: inset;\n"
"    background:  rgb(170, 255, 255);\n"
"    }")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(440, 110, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel {\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: rgb(85, 255, 255);\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QLabel:hover {\n"
"    background:  rgb(170, 255, 255);\n"
"    }\n"
"\n"
"QLabel:pressed {\n"
"    border-style: inset;\n"
"    background:  rgb(170, 255, 255);\n"
"    }")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(440, 190, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel {\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: rgb(85, 255, 255);\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QLabel:hover {\n"
"    background:  rgb(170, 255, 255);\n"
"    }\n"
"\n"
"QLabel:pressed {\n"
"    border-style: inset;\n"
"    background:  rgb(170, 255, 255);\n"
"    }")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(180, 190, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel {\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: rgb(85, 255, 255);\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QLabel:hover {\n"
"    background:  rgb(170, 255, 255);\n"
"    }\n"
"\n"
"QLabel:pressed {\n"
"    border-style: inset;\n"
"    background:  rgb(170, 255, 255);\n"
"    }")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(440, 270, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel {\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: rgb(85, 255, 255);\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QLabel:hover {\n"
"    background:  rgb(170, 255, 255);\n"
"    }\n"
"\n"
"QLabel:pressed {\n"
"    border-style: inset;\n"
"    background:  rgb(170, 255, 255);\n"
"    }")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(180, 270, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel {\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: rgb(85, 255, 255);\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QLabel:hover {\n"
"    background:  rgb(170, 255, 255);\n"
"    }\n"
"\n"
"QLabel:pressed {\n"
"    border-style: inset;\n"
"    background:  rgb(170, 255, 255);\n"
"    }")
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 400, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.clicked.connect(self.go_back)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    background: rgb(214, 214, 214);\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: rgb(228, 228, 228);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background:  rgb(170, 255, 255);\n"
"    }")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 540, 21, 21))
        self.pushButton_3.setToolTipDuration(0)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
                                        "    color: #333;\n"
                                        "    border: 2px solid #555;\n"
                                        "    border-radius: 50px;\n"
                                        "    border-style: outset;\n"
                                        "    background: qradialgradient(\n"
                                        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                        "        radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
                                        "        );\n"
                                        "    padding: 5px;\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    background: qradialgradient(\n"
                                        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                        "        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
                                        "        );\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    border-style: inset;\n"
                                        "    background: qradialgradient(\n"
                                        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                        "        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
                                        "        );\n"
                                        "    }")
        self.pushButton_3.setText("")
        icon = QIcon('home.png')
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.go_home)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "SOFTWARE ESTIMATION TOOL"))
        self.label_2.setText(_translate("MainWindow", "Effort  :"))
        self.label_3.setText(_translate(f"MainWindow", str(self.ans[0])))
        self.label_4.setText(_translate(f"MainWindow", str(self.ans[1])))
        self.label_5.setText(_translate("MainWindow", "Time  :"))
        self.label_6.setText(_translate(f"MainWindow", str(self.ans[2])))
        self.label_7.setText(_translate("MainWindow", "Persons :"))
        self.pushButton.setText(_translate("MainWindow", "Back"))

    def go_back(self):
        self.w=MainWindow2()
        self.w.show()
        self.hide()
    def go_home(self):
        self.w = MainWindow1()
        self.w.show()
        self.hide()

class MainWindow3(QtWidgets.QMainWindow, Page3):
    def __init__(self,ans):
        super(MainWindow3, self).__init__()
        self.setupUi(self,ans)
        self.show()

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow1()
    sys.exit(app.exec())