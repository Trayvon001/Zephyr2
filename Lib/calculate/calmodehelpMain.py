from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile


class help:
    def __init__(self):
        qfile_status = QFile(
            "Func_class\calculate\calhelp.ui")  # 要在主目录中运行时加上Func_class\calculate\calmodewindow.ui
        qfile_status.open(QFile.ReadOnly)
        qfile_status.close()
        # 从UI定义中动态创建一个相应的窗口对象
        # 注意：这里面的空间对象也成为窗口对象的属性了
        # 比如self.ui.buttom, self.ui.textEdit
        self.ui = QUiLoader().load(qfile_status)
        self.display()

    def display(self):
        string = '计算模式使用说明\n\n'
        string = string + '误差功能的使用\n    误差默认为前一般是标准值，后一半是实际值，如输入1，2，0.9，1.8时，计算为1和0.9，2和1.8的误差。\n\n'
        string = string + '不确定度功能说明\n    不确定度功能暂时无法使用。\n\n'
        string = string + '历史记录和清零功能的使用\n'
        string = string + '点击历史记录会自动在所有位置返回上次的结果，若没有更多的历史记录则会以holdtxt提示历史纪录为空。\n'
        string = string + '归零功能会清空当前所有的输入，但不会清空历史记录。'
        self.ui.helpdisplay.setText(string)
