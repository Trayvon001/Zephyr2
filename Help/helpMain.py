from PyQt5 import QtWidgets
from Help.helpdoc import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.display()

    def display(self):
        string = '程序入口使用说明\n\n'
        string = string + '进入各主要功能窗口只需要点击相应按钮即可，圆角画图标后按钮不会下沉，但为了美观这值得/嘿嘿\n'
        string = string + '该入口程序使用说明，更新日志和各个功能界面只能打开一次，暂时无法解决这个问题\n'
        string = string + '该程序最多只能显示三个窗口(使用说明，更新日志都算一个窗口)\n\n'
        string = string + '自选功能\n'
        string = string + '将保留该窗口打勾后进入相应的功能创就入口界面将不会消失\n'
        string = string + 'pyinstaller main.py --noconsole --hidden-import PySide2.QtXml --hidden-import pkg_resources.py2_warn  --icon="mainlogo.ico"'
        self.helpdisplay.setText(string)


