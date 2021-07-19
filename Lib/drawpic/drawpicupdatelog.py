from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile


class updatelog:
    def __init__(self):
        qfile_status = QFile(
            "Func_class\drawpic\drawpicupdatelog.ui")  # 要在主目录中运行时加上Func_class\calculate\calmodewindow.ui
        qfile_status.open(QFile.ReadOnly)
        qfile_status.close()
        # 从UI定义中动态创建一个相应的窗口对象
        # 注意：这里面的空间对象也成为窗口对象的属性了
        # 比如self.ui.buttom, self.ui.textEdit
        self.ui = QUiLoader().load(qfile_status)
        self.display()

    def display(self):
        string = '绘图模式更新日志\n\n'
        string = string + 'Version 3.0.0\n'
        string = string + '    1、支持了横坐标中文绘制，此时必须按顺序输入\n'
        string = string + '    2、legend支持了自选功能\n'
        self.ui.updatelogdisplay.setText(string)
