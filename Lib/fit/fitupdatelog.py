from PyQt5 import QtWidgets
from Lib.fit.fitUpdateLogUI import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.display()

    def display(self):
        string = '拟合模式更新日志\n\n'
        self.updatelogdisplay.setText(string)
