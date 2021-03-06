# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(646, 680)
        MainWindow.setMinimumSize(QtCore.QSize(646, 680))
        MainWindow.setMaximumSize(QtCore.QSize(646, 680))
        MainWindow.setStyleSheet("QPushButton { \n"
"    color: blue ;\n"
"    font-size:28px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 490, 651, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fit = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fit.sizePolicy().hasHeightForWidth())
        self.fit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.fit.setFont(font)
        self.fit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fit.setStyleSheet("background-color: rgb(183, 255, 216);\n"
"border:2px groove gray;border-radius:10px;padding:2px 4px;")
        self.fit.setObjectName("fit")
        self.horizontalLayout.addWidget(self.fit)
        self.calculate = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calculate.sizePolicy().hasHeightForWidth())
        self.calculate.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.calculate.setFont(font)
        self.calculate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculate.setStyleSheet("background-color: rgb(251, 255, 196);\n"
"border:2px groove gray;border-radius:10px;padding:2px 4px;\n"
"")
        self.calculate.setObjectName("calculate")
        self.horizontalLayout.addWidget(self.calculate)
        self.timer = QtWidgets.QLabel(self.centralwidget)
        self.timer.setGeometry(QtCore.QRect(200, 170, 271, 41))
        self.timer.setMinimumSize(QtCore.QSize(271, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.timer.setFont(font)
        self.timer.setStyleSheet("color: rgb(244, 244, 244);")
        self.timer.setObjectName("timer")
        self.greetings = QtWidgets.QLabel(self.centralwidget)
        self.greetings.setGeometry(QtCore.QRect(240, 210, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.greetings.setFont(font)
        self.greetings.setStyleSheet("color: rgb(244, 244, 244);")
        self.greetings.setText("")
        self.greetings.setObjectName("greetings")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 570, 651, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.drawpicture = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drawpicture.sizePolicy().hasHeightForWidth())
        self.drawpicture.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.drawpicture.setFont(font)
        self.drawpicture.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.drawpicture.setStyleSheet("background-color: rgb(239, 255, 219);\n"
"border:2px groove gray;border-radius:10px;padding:2px 4px;")
        self.drawpicture.setObjectName("drawpicture")
        self.horizontalLayout_2.addWidget(self.drawpicture)
        self.advanceddraw = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.advanceddraw.sizePolicy().hasHeightForWidth())
        self.advanceddraw.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        self.advanceddraw.setFont(font)
        self.advanceddraw.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.advanceddraw.setStyleSheet("background-color: rgb(255, 246, 249);\n"
"border:2px groove gray;border-radius:10px;padding:2px 4px;")
        self.advanceddraw.setObjectName("advanceddraw")
        self.horizontalLayout_2.addWidget(self.advanceddraw)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 646, 22))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menuBar)
        self.tokeepwin = QtWidgets.QAction(MainWindow)
        self.tokeepwin.setCheckable(True)
        self.tokeepwin.setObjectName("tokeepwin")
        self.helpdocu = QtWidgets.QAction(MainWindow)
        self.helpdocu.setObjectName("helpdocu")
        self.updatedocu = QtWidgets.QAction(MainWindow)
        self.updatedocu.setObjectName("updatedocu")
        self.menu.addAction(self.tokeepwin)
        self.menu_2.addAction(self.helpdocu)
        self.menu_2.addAction(self.updatedocu)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Zephyr2--Desiged by ?????????--Version 1.0.0--Last Update???2021-7-13"))
        self.fit.setText(_translate("MainWindow", "????????????"))
        self.calculate.setText(_translate("MainWindow", "????????????"))
        self.timer.setText(_translate("MainWindow", "TextLabel"))
        self.drawpicture.setText(_translate("MainWindow", "????????????"))
        self.advanceddraw.setText(_translate("MainWindow", "????????????"))
        self.menu.setTitle(_translate("MainWindow", "????????????"))
        self.menu_2.setTitle(_translate("MainWindow", "??????"))
        self.tokeepwin.setText(_translate("MainWindow", "???????????????"))
        self.helpdocu.setText(_translate("MainWindow", "????????????"))
        self.updatedocu.setText(_translate("MainWindow", "????????????"))
