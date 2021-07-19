from PyQt5 import QtWidgets
from Lib.calculate.calModeHelpUI import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.display()

    def display(self):
        string = '计算模式使用说明\n\n'
        string = string + '误差功能的使用\n    误差默认为前一般是标准值，后一半是实际值，如输入1，2，0.9，1.8时，计算为1和0.9，2和1.8的误差。\n\n'
        string = string + '不确定度功能说明\n    不确定度功能暂时无法使用。\n\n'
        string = string + '历史记录和清零功能的使用\n'
        string = string + '点击历史记录会自动在所有位置返回上次的结果，若没有更多的历史记录则会以holdtxt提示历史纪录为空。\n'
        string = string + '归零功能会清空当前所有的输入，但不会清空历史记录。'
        self.helpdisplay.setText(string)

