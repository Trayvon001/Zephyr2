from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile


class help:

    def __init__(self):
        qfile_status = QFile(
            "Func_class\\fit\\fitHelpUI.ui")  # 要在主目录中运行时加上Func_class\calculate\calmodewindow.ui
        qfile_status.open(QFile.ReadOnly)
        qfile_status.close()
        # 从UI定义中动态创建一个相应的窗口对象
        # 注意：这里面的空间对象也成为窗口对象的属性了
        # 比如self.ui.buttom, self.ui.textEdit
        self.ui = QUiLoader().load(qfile_status)
        self.display()

    def display(self):
        string = '拟合模式使用说明\n\n'
        string = string + '拟合功能的使用\n首先在相应的位置输入x，y的值，一定要用一个空格分开，结尾不需要空格。\n'
        string = string + '如果点击拟合之后没反应，那很有可能就是没有严格用空格分开。\n'
        string = string + 'x轴标签，y轴标签，图表标题可以不填，则画出来的图中也不含有这些标签。\n\n'
        string = string + '读取Excel和txt文件功能的使用\n'
        string = string + '读取功能只是自动把文件里面的内容填到x，y文本框中，不涉及计算，计算需要点击拟合按钮'
        string = string + '不需要读取excel和txt时，excel和txt对应的空可以不填。\n'
        string = string + '需要读取时也可以不填写对应的空，此时excel默认第一列为x，第二列为y，默认竖地从第0行开始读。\n\n'
        string = string + '历史记录和清零功能的使用\n'
        string = string + '点击历史记录会自动在所有位置返回上次的结果，若没有更多的历史记录则会以holdtxt提示历史纪录为空。\n'
        string = string + '归零功能会清空当前所有的输入，但不会清空历史记录。'
        self.ui.helpdisplay.setText(string)