# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'drawpicMainUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(679, 645)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.xlabel = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.xlabel.setFont(font)
        self.xlabel.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;\n"
"")
        self.xlabel.setObjectName("xlabel")
        self.horizontalLayout.addWidget(self.xlabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.xinput = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.xinput.setFont(font)
        self.xinput.setStyleSheet("background-color: rgb(240, 255, 247);\n"
"border:2px groove gray;border-radius:10px;padding:2px 4px;")
        self.xinput.setObjectName("xinput")
        self.verticalLayout_2.addWidget(self.xinput)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.ylabel = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ylabel.setFont(font)
        self.ylabel.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;")
        self.ylabel.setObjectName("ylabel")
        self.horizontalLayout_2.addWidget(self.ylabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.yinput = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.yinput.setFont(font)
        self.yinput.setStyleSheet("background-color: rgb(244, 255, 234);\n"
"border:2px groove gray;border-radius:10px;padding:2px 4px;")
        self.yinput.setObjectName("yinput")
        self.verticalLayout_2.addWidget(self.yinput)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_5.addWidget(self.line)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.title = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;")
        self.title.setText("")
        self.title.setObjectName("title")
        self.horizontalLayout_3.addWidget(self.title)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.image_show = QtWidgets.QLabel(self.centralwidget)
        self.image_show.setStyleSheet("background-color: rgb(255, 250, 229);\n"
"border:2px groove gray;border-radius:10px;padding:2px 4px;")
        self.image_show.setText("")
        self.image_show.setObjectName("image_show")
        self.horizontalLayout_8.addWidget(self.image_show)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.hvmode = QtWidgets.QHBoxLayout()
        self.hvmode.setObjectName("hvmode")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.hvmode.addWidget(self.label_6)
        self.methodinput = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.methodinput.setFont(font)
        self.methodinput.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;")
        self.methodinput.setPlaceholderText("")
        self.methodinput.setObjectName("methodinput")
        self.hvmode.addWidget(self.methodinput)
        self.hvmode.setStretch(0, 2)
        self.hvmode.setStretch(1, 3)
        self.verticalLayout.addLayout(self.hvmode)
        self.excelhorizontallayout = QtWidgets.QHBoxLayout()
        self.excelhorizontallayout.setObjectName("excelhorizontallayout")
        self.excelxlabel = QtWidgets.QLabel(self.centralwidget)
        self.excelxlabel.setObjectName("excelxlabel")
        self.excelhorizontallayout.addWidget(self.excelxlabel)
        self.excelxinput = QtWidgets.QLineEdit(self.centralwidget)
        self.excelxinput.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;")
        self.excelxinput.setObjectName("excelxinput")
        self.excelhorizontallayout.addWidget(self.excelxinput)
        self.excelylabel = QtWidgets.QLabel(self.centralwidget)
        self.excelylabel.setObjectName("excelylabel")
        self.excelhorizontallayout.addWidget(self.excelylabel)
        self.excelyinput = QtWidgets.QLineEdit(self.centralwidget)
        self.excelyinput.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;")
        self.excelyinput.setObjectName("excelyinput")
        self.excelhorizontallayout.addWidget(self.excelyinput)
        self.verticalLayout.addLayout(self.excelhorizontallayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.numinput = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.numinput.setFont(font)
        self.numinput.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;")
        self.numinput.setObjectName("numinput")
        self.horizontalLayout_4.addWidget(self.numinput)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.labell = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labell.setFont(font)
        self.labell.setObjectName("labell")
        self.horizontalLayout_7.addWidget(self.labell)
        self.labelinput = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labelinput.setFont(font)
        self.labelinput.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;")
        self.labelinput.setObjectName("labelinput")
        self.horizontalLayout_7.addWidget(self.labelinput)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.drawbtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.drawbtn.setFont(font)
        self.drawbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.drawbtn.setStyleSheet("background-color: rgb(85, 255, 255);\n"
"border:2px groove gray;border-radius:10px;padding:2px 4px;")
        self.drawbtn.setObjectName("drawbtn")
        self.verticalLayout.addWidget(self.drawbtn)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.hisupbtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.hisupbtn.setFont(font)
        self.hisupbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.hisupbtn.setStyleSheet("background-color: rgb(221, 226, 255);\n"
"border:2px groove gray;border-radius:10px;padding:2px 4px;")
        self.hisupbtn.setObjectName("hisupbtn")
        self.horizontalLayout_6.addWidget(self.hisupbtn)
        self.hisdownbtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.hisdownbtn.setFont(font)
        self.hisdownbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.hisdownbtn.setStyleSheet("background-color: rgb(221, 226, 255);\n"
"border:2px groove gray;border-radius:10px;padding:2px 4px;")
        self.hisdownbtn.setObjectName("hisdownbtn")
        self.horizontalLayout_6.addWidget(self.hisdownbtn)
        self.clearbtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.clearbtn.setFont(font)
        self.clearbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clearbtn.setStyleSheet("background-color: rgb(246, 255, 237);\n"
"border:2px groove gray;border-radius:10px;padding:2px 4px;\n"
"")
        self.clearbtn.setObjectName("clearbtn")
        self.horizontalLayout_6.addWidget(self.clearbtn)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)
        self.horizontalLayout_6.setStretch(2, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.verticalLayout.setStretch(1, 3)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.horizontalLayout_5.setStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 679, 20))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menu_3)
        self.menu_4.setObjectName("menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.txtfile = QtWidgets.QAction(MainWindow)
        self.txtfile.setObjectName("txtfile")
        self.excelfile = QtWidgets.QAction(MainWindow)
        self.excelfile.setObjectName("excelfile")
        self.helpdocu = QtWidgets.QAction(MainWindow)
        self.helpdocu.setObjectName("helpdocu")
        self.updatedocu = QtWidgets.QAction(MainWindow)
        self.updatedocu.setObjectName("updatedocu")
        self.grid = QtWidgets.QAction(MainWindow)
        self.grid.setCheckable(True)
        self.grid.setObjectName("grid")
        self.data_label = QtWidgets.QAction(MainWindow)
        self.data_label.setCheckable(True)
        self.data_label.setObjectName("data_label")
        self.legend = QtWidgets.QAction(MainWindow)
        self.legend.setCheckable(True)
        self.legend.setObjectName("legend")
        self.d10 = QtWidgets.QAction(MainWindow)
        self.d10.setCheckable(True)
        self.d10.setObjectName("d10")
        self.d20 = QtWidgets.QAction(MainWindow)
        self.d20.setCheckable(True)
        self.d20.setObjectName("d20")
        self.d30 = QtWidgets.QAction(MainWindow)
        self.d30.setCheckable(True)
        self.d30.setObjectName("d30")
        self.d45 = QtWidgets.QAction(MainWindow)
        self.d45.setCheckable(True)
        self.d45.setObjectName("d45")
        self.d50 = QtWidgets.QAction(MainWindow)
        self.d50.setCheckable(True)
        self.d50.setObjectName("d50")
        self.d60 = QtWidgets.QAction(MainWindow)
        self.d60.setCheckable(True)
        self.d60.setObjectName("d60")
        self.d75 = QtWidgets.QAction(MainWindow)
        self.d75.setCheckable(True)
        self.d75.setObjectName("d75")
        self.d80 = QtWidgets.QAction(MainWindow)
        self.d80.setCheckable(True)
        self.d80.setObjectName("d80")
        self.d90 = QtWidgets.QAction(MainWindow)
        self.d90.setCheckable(True)
        self.d90.setObjectName("d90")
        self.img_sep_show = QtWidgets.QAction(MainWindow)
        self.img_sep_show.setCheckable(True)
        self.img_sep_show.setObjectName("img_sep_show")
        self.export_image = QtWidgets.QAction(MainWindow)
        self.export_image.setObjectName("export_image")
        self.menu.addAction(self.txtfile)
        self.menu.addAction(self.excelfile)
        self.menu.addAction(self.export_image)
        self.menu_2.addAction(self.helpdocu)
        self.menu_2.addAction(self.updatedocu)
        self.menu_4.addAction(self.d10)
        self.menu_4.addAction(self.d20)
        self.menu_4.addAction(self.d30)
        self.menu_4.addAction(self.d45)
        self.menu_4.addAction(self.d50)
        self.menu_4.addAction(self.d60)
        self.menu_4.addAction(self.d75)
        self.menu_4.addAction(self.d80)
        self.menu_4.addAction(self.d90)
        self.menu_3.addAction(self.grid)
        self.menu_3.addAction(self.data_label)
        self.menu_3.addAction(self.legend)
        self.menu_3.addAction(self.menu_4.menuAction())
        self.menu_3.addAction(self.img_sep_show)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "绘图模式"))
        self.label_2.setText(_translate("MainWindow", "横坐标名称："))
        self.xinput.setPlaceholderText(_translate("MainWindow", "请在此处输入横坐标数据（空格分隔）"))
        self.label_3.setText(_translate("MainWindow", "纵坐标名称："))
        self.yinput.setPlaceholderText(_translate("MainWindow", "请在此处输入纵坐标数据"))
        self.label_4.setText(_translate("MainWindow", "图表标题："))
        self.label_6.setText(_translate("MainWindow", "横竖读法(横为1，竖为2，缺省为竖的读)"))
        self.excelxlabel.setText(_translate("MainWindow", "X"))
        self.excelylabel.setText(_translate("MainWindow", "Y"))
        self.label.setText(_translate("MainWindow", "含有几条曲线"))
        self.numinput.setPlaceholderText(_translate("MainWindow", "缺省相当于1条"))
        self.labell.setText(_translate("MainWindow", "本曲线标签名"))
        self.labelinput.setPlaceholderText(_translate("MainWindow", "请输入第1条曲线的标签"))
        self.drawbtn.setText(_translate("MainWindow", "开始绘制"))
        self.hisupbtn.setText(_translate("MainWindow", "上条历史记录"))
        self.hisdownbtn.setText(_translate("MainWindow", "下条历史记录"))
        self.clearbtn.setText(_translate("MainWindow", "归零"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "帮助"))
        self.menu_3.setTitle(_translate("MainWindow", "可选功能"))
        self.menu_4.setTitle(_translate("MainWindow", "坐标旋转"))
        self.txtfile.setText(_translate("MainWindow", "打开文本文件"))
        self.excelfile.setText(_translate("MainWindow", "打开Excel文件"))
        self.helpdocu.setText(_translate("MainWindow", "使用说明"))
        self.updatedocu.setText(_translate("MainWindow", "更新日志"))
        self.grid.setText(_translate("MainWindow", "网格线"))
        self.data_label.setText(_translate("MainWindow", "数据标签"))
        self.legend.setText(_translate("MainWindow", "图例"))
        self.d10.setText(_translate("MainWindow", "10°"))
        self.d20.setText(_translate("MainWindow", "20°"))
        self.d30.setText(_translate("MainWindow", "30°"))
        self.d45.setText(_translate("MainWindow", "45°"))
        self.d50.setText(_translate("MainWindow", "50°"))
        self.d60.setText(_translate("MainWindow", "60°"))
        self.d75.setText(_translate("MainWindow", "75°"))
        self.d80.setText(_translate("MainWindow", "80°"))
        self.d90.setText(_translate("MainWindow", "90°"))
        self.img_sep_show.setText(_translate("MainWindow", "图片单独显示"))
        self.export_image.setText(_translate("MainWindow", "导出图片"))