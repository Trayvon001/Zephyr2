from PyQt5 import QtWidgets
from Lib.drawpic.drawpicupdatelogUI import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.display()

    def display(self):
        string = '绘图模式更新日志\n\n'
        string = string + 'Version 3.0.0\n'
        string = string + '    1、支持了横坐标中文绘制，此时必须按顺序输入\n'
        string = string + '    2、legend支持了自选功能\n'
        self.updatelogdisplay.setText(string)
