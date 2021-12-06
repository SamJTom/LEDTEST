# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LED_HW.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import RPi.GPIO as GPIO

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 480)
        MainWindow.setMinimumSize(QtCore.QSize(720, 480))
        MainWindow.setMaximumSize(QtCore.QSize(720, 480))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(280, 200, 130, 28))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LedButton = QtWidgets.QPushButton(self.layoutWidget)
        self.LedButton.setCheckable(True)
        self.LedButton.setObjectName("LedButton")
        self.horizontalLayout.addWidget(self.LedButton)
        self.PressIndicator = QtWidgets.QRadioButton(self.layoutWidget)
        self.PressIndicator.setCheckable(True)
        self.PressIndicator.setAutoExclusive(True)
        self.PressIndicator.setObjectName("PressIndicator")
        self.horizontalLayout.addWidget(self.PressIndicator)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.LedButton.clicked.connect(self.PressIndicator.toggle)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.LedButton.clicked.connect(self.LED)

        GPIO.setmode(GPIO.BCM)
        pin = 18
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

    def LED(self):
        pin = 18
        
        if self.LedButton.clicked == True:
            GPIO.output(pin, GPIO.HIGH)
        else:
            GPIO.output(pin, GPIO.LOW)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LedButton.setText(_translate("MainWindow", "LED "))
        self.PressIndicator.setText(_translate("MainWindow", "O/I"))


