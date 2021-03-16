from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, QDateTime, QTimer
from PySide2 import QtWidgets
import PySide2.QtCore as QtCore  # 用于确保windows下运行的窗口和Qt中看到的窗口一致
from PySide2.QtGui import QIcon
# import Func_class.calculate.calculate as calculate
# import Func_class.fit.fit as fit  # 导入用于计算的三个自定义类文件
# import Func_class.drawpic.drawpictures as drawpic
# import Func_class.advanceddraw.advanceddraw as adv_draw
# import main_help as help_log
# import main_updatelog as update_log
import sys
import time


class Stats(QtWidgets.QMainWindow):
    username = '齐承文'

    def __init__(self):
        super().__init__()
        qfile_status = QFile("mainwindow.ui")
        qfile_status.open(QFile.ReadOnly)
        qfile_status.close()
        # 从UI定义中动态创建一个相应的窗口对象
        # 注意：这里面的空间对象也成为窗口对象的属性了
        # 比如self.ui.buttom, self.ui.textEdit
        self.ui = QUiLoader().load(qfile_status)
        # 以下代码用于在入口界面动态显示时间
        self.time = QTimer()
        self.time.start(500)
        self.time.timeout.connect(self.Timeupdate)
        # 以上代码用于在入口界面动态显示时间
        # 绑定按钮和相应程序
        self.ui.calculate.clicked.connect(self.cal)
        self.ui.fit.clicked.connect(self.fit)
        self.ui.drawpicture.clicked.connect(self.drawpic)
        self.ui.advanceddraw.clicked.connect(self.advanced_drawpic)
        self.ui.helpdocu.triggered.connect(self.help)
        self.ui.updatedocu.triggered.connect(self.updatelog)
        # 绑定按钮和相应程序
        self.set_background_image()

    def set_background_image(self):  # 在此处设置背景图片，以便用于在不同日期显示不同图片
        current_time = QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss dddd')
        if int(current_time[5]) == 0 and int(current_time[6]) == 8 and int(current_time[8]) == 2 and int(
                current_time[9]) == 5:  # 七夕节
            self.ui.setStyleSheet("QPushButton { \n"
                                  "    color: blue ;\n"
                                  "    font-size:28px;\n"
                                  "}\n"
                                  "#MainWindow {\n"
                                  "    border-image: url(picture/Valen_day.png);\n"
                                  "}")
            self.ui.greetings.setStyleSheet("QLabel { \n"  # 根据颜色设置标签的样式
                                            "    color: rgb(244, 244, 244);\n"
                                            "}\n"
                                            )
            self.ui.timer.setStyleSheet("QLabel { \n"
                                        "    color: rgb(244, 244, 244);\n"
                                        "}\n"
                                        )

        elif int(current_time[5]) == 0 and int(current_time[6]) == 9 and int(current_time[8]) == 1 and int(
                current_time[9]) == 0:  # 教师节
            self.ui.setStyleSheet("QPushButton { \n"
                                  "    color: blue ;\n"
                                  "    font-size:28px;\n"
                                  "}\n"
                                  "#MainWindow {\n"
                                  "    border-image: url(picture/teacher_day.png);\n"
                                  "}")
            self.ui.greetings.setStyleSheet("QLabel { \n"  # 根据颜色设置标签的样式
                                            "    color: rgb(244, 244, 244);\n"
                                            "}\n"
                                            )
            self.ui.timer.setStyleSheet("QLabel { \n"
                                        "    color: rgb(244, 244, 244);\n"
                                        "}\n"
                                        )
        elif int(current_time[5]) == 1 and int(current_time[6]) == 0 and int(current_time[8]) == 0 and int(
                current_time[9]) == 1:  # 中秋节
            self.ui.setStyleSheet("QPushButton { \n"
                                  "    color: blue ;\n"
                                  "    font-size:28px;\n"
                                  "}\n"
                                  "#MainWindow {\n"
                                  "    border-image: url(picture/midautumn_fes.png);\n"
                                  "}")
        elif int(current_time[5]) == 1 and int(current_time[6]) == 0 and int(current_time[8]) == 0 and int(
                current_time[9]) <= 7:  # 国庆节
            self.ui.setStyleSheet("QPushButton { \n"
                                  "    color: blue ;\n"
                                  "    font-size:28px;\n"
                                  "}\n"
                                  "#MainWindow {\n"
                                  "    border-image: url(picture/national_day.png);\n"
                                  "}")
            self.ui.greetings.setStyleSheet("QLabel { \n"  # 根据颜色设置标签的样式
                                            "    color: rgb(255, 6, 43);\n"
                                            "}\n"
                                            )
            self.ui.timer.setStyleSheet("QLabel { \n"
                                        "    color: rgb(255, 6, 43);\n"
                                        "}\n"
                                        )
        elif int(current_time[5]) == 1 and int(current_time[6]) == 2 and int(current_time[8]) == 2 and int(
                current_time[9]) == 5:  # 圣诞节
            self.ui.setStyleSheet("QPushButton { \n"
                                  "    color: blue ;\n"
                                  "    font-size:28px;\n"
                                  "}\n"
                                  "#MainWindow {\n"
                                  "    border-image: url(picture/chrismas_day.png);\n"
                                  "}")
            self.ui.greetings.setStyleSheet("QLabel { \n"  # 根据颜色设置标签的样式
                                            "    color: rgb(0, 0, 0);\n"
                                            "}\n"
                                            )
            self.ui.timer.setStyleSheet("QLabel { \n"
                                        "    color: rgb(0, 0, 0);\n"
                                        "}\n"
                                        )
        elif int(current_time[5]) == 0 and int(current_time[6]) == 1 and int(current_time[8]) == 0 and int(
                current_time[9]) == 1:  # 元旦节
            self.ui.setStyleSheet("QPushButton { \n"
                                  "    color: blue ;\n"
                                  "    font-size:28px;\n"
                                  "}\n"
                                  "#MainWindow {\n"
                                  "    border-image: url(picture/mwbdpic.png);\n"
                                  "}")
        elif int(current_time[5]) == 0 and int(current_time[6]) == 2 and int(current_time[8]) == 1 and int(
                current_time[9]) == 1:  # 除夕节
            self.ui.setStyleSheet("QPushButton { \n"
                                  "    color: blue ;\n"
                                  "    font-size:28px;\n"
                                  "}\n"
                                  "#MainWindow {\n"
                                  "    border-image: url(picture/mwbdpic.png);\n"
                                  "}")
        elif int(current_time[5]) == 0 and int(current_time[6]) == 2 and int(current_time[8]) == 1 and int(
                current_time[9]) < 4:  # 春节
            self.ui.setStyleSheet("QPushButton { \n"
                                  "    color: blue ;\n"
                                  "    font-size:28px;\n"
                                  "}\n"
                                  "#MainWindow {\n"
                                  "    border-image: url(picture/mwbdpic.png);\n"
                                  "}")
        elif int(current_time[5]) == 0 and int(current_time[6]) == 2 and int(current_time[8]) == 1 and int(
                current_time[9]) == 4:  # 情人节
            self.ui.setStyleSheet("QPushButton { \n"
                                  "    color: blue ;\n"
                                  "    font-size:28px;\n"
                                  "}\n"
                                  "#MainWindow {\n"
                                  "    border-image: url(picture/mwbdpic.png);\n"
                                  "}")
        elif int(current_time[5]) == 0 and int(current_time[6]) == 2 and int(current_time[8]) == 2 and int(
                current_time[9]) == 6:  # 元宵节
            self.ui.setStyleSheet("QPushButton { \n"
                                  "    color: blue ;\n"
                                  "    font-size:28px;\n"
                                  "}\n"
                                  "#MainWindow {\n"
                                  "    border-image: url(picture/mwbdpic.png);\n"
                                  "}")
        elif int(current_time[5]) == 0 and int(current_time[6]) == 3 and int(current_time[8]) == 1 and int(
                current_time[9]) == 2:  # 植树节
            self.ui.setStyleSheet("QPushButton { \n"
                                  "    color: blue ;\n"
                                  "    font-size:28px;\n"
                                  "}\n"
                                  "#MainWindow {\n"
                                  "    border-image: url(picture/mwbdpic.png);\n"
                                  "}")
        elif int(current_time[5]) == 0 and int(current_time[6]) == 4 and int(current_time[8]) == 0 and int(
                current_time[9]) <= 5 and int(current_time[9]) >= 2:  # 清明节
            self.ui.setStyleSheet("QPushButton { \n"
                                  "    color: blue ;\n"
                                  "    font-size:28px;\n"
                                  "}\n"
                                  "#MainWindow {\n"
                                  "    border-image: url(picture/mwbdpic.png);\n"
                                  "}")
        elif int(current_time[5]) == 0 and int(current_time[6]) == 4 and int(current_time[8]) == 1 and int(
                current_time[9]) == 7:  # 生日
            self.ui.setStyleSheet("QPushButton { \n"
                                  "    color: blue ;\n"
                                  "    font-size:28px;\n"
                                  "}\n"
                                  "#MainWindow {\n"
                                  "    border-image: url(picture/birthday21.png);\n"
                                  "}")
            self.ui.greetings.setText('21岁生日快乐，' + self.username)
        elif current_time[len(current_time) - 1] == '六' or current_time[len(current_time) - 1] == '日':  # 周末
            self.ui.setStyleSheet("QPushButton { \n"
                                  "    color: blue ;\n"
                                  "    font-size:28px;\n"
                                  "}\n"
                                  "#MainWindow {\n"
                                  "    border-image: url(picture/weekend.png);\n"
                                  "}")
            self.ui.greetings.setStyleSheet("QLabel { \n"  # 根据颜色设置标签的样式
                                            "    color: rgb(0, 0, 0);\n"
                                            "}\n"
                                            )
            self.ui.timer.setStyleSheet("QLabel { \n"
                                        "    color: rgb(0, 0, 0);\n"
                                        "}\n"
                                        )
        else:  # 平时的背景图
            self.ui.setStyleSheet("QPushButton { \n"
                                  "    color: blue ;\n"
                                  "    font-size:28px;\n"
                                  "}\n"
                                  "#MainWindow {\n"
                                  "    border-image: url(picture/normal_day.png);\n"
                                  "}")

    def updatelog(self):
        self.updatelog = update_log.updatelog()
        self.updatelog.ui.show()

    def help(self):
        self.help = help_log.help()
        self.help.ui.show()

    def Timeupdate(self):  # 用于实时获取时间
        self.ui.timer.setText(QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss dddd'))
        current_time = QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss dddd')
        if (int(current_time[11]) >= 2 and int(current_time[12]) >= 3) or (
                int(current_time[11]) == 0 and int(current_time[12]) <= 4):
            if int(current_time[5]) == 0 and int(current_time[6]) == 4 and int(current_time[8]) == 1 and int(
                    current_time[9]) == 7:  # 生日特殊处理
                self.ui.greetings.setText('21岁生日快乐，' + self.username)
            else:
                self.ui.greetings.setText('夜深了，' + self.username)

    def cal(self):
        self.calculation = calculate.calculatemode()
        self.calculation.ui.show()
        self.calculation.ui.setWindowIcon(QIcon('Func_class\\calculate\\callogo.png'))
        if self.ui.tokeepwin.isChecked():
            keep_window = 1
        else:
            keep_window = 0
        if keep_window == 0:
            self.ui.close()  # 加上这段代码可以自动关闭之前的窗口，也可以选择不关闭之前的窗口
        self.ui.calculate.setStyleSheet("background-color: rgb(175, 175, 175);\n"
                                        "border:2px groove gray;border-radius:10px;padding:2px 4px;")

    def fit(self):
        self.fit = fit.fitmode()
        self.fit.ui.show()
        self.fit.ui.setWindowIcon(QIcon('Func_class\\fit\\fitmodeicon.png'))
        if self.ui.tokeepwin.isChecked():
            keep_window = 1
        else:
            keep_window = 0
        if keep_window == 0:
            self.ui.close()  # 加上这段代码可以自动关闭之前的窗口，也可以选择不关闭之前的窗口
        self.ui.fit.setStyleSheet("background-color: rgb(175, 175, 175);\n"
                                  "border:2px groove gray;border-radius:10px;padding:2px 4px;")

    def drawpic(self):
        self.drawpic = drawpic.drawpicmode()
        self.drawpic.ui.show()
        self.drawpic.ui.setWindowIcon(QIcon('Func_class\\drawpic\\drawicon.png'))
        if self.ui.tokeepwin.isChecked():
            keep_window = 1
        else:
            keep_window = 0
        if keep_window == 0:
            self.ui.close()  # 加上这段代码可以自动关闭之前的窗口，也可以选择不关闭之前的窗口
        self.ui.drawpicture.setStyleSheet("background-color: rgb(175, 175, 175);\n"
                                          "border:2px groove gray;border-radius:10px;padding:2px 4px;")

    def advanced_drawpic(self):
        self.advdraw = adv_draw.advdrawpic()
        self.advdraw.ui.show()
        self.advdraw.ui.setWindowIcon(QIcon('Func_class\\advanceddraw\\advanceddrawicon.png'))
        if self.ui.tokeepwin.isChecked():
            keep_window = 1
        else:
            keep_window = 0
        if keep_window == 0:
            self.ui.close()  # 加上这段代码可以自动关闭之前的窗口，也可以选择不关闭之前的窗口
        self.ui.advanceddraw.setStyleSheet("background-color: rgb(175, 175, 175);\n"
                                           "border:2px groove gray;border-radius:10px;padding:2px 4px;")


QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # 使得窗口比例和用Qt设计时完全一致

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # 加载图标
    app.setWindowIcon(QIcon('logo.png'))
    stats = Stats()
    stats.ui.show()
    sys.exit(app.exec_())

# 使用pyinstaller main.py --noconsole --hidden-import PySide2.QtXml --hidden-import pkg_resources.py2_warn  --icon="mainlogo.ico" 生成可执行文件exe
# 使用 D: 和CD D:\Pycharm Project更换目录
# 需要将mwbdpic.png, mainwindow.ui,logo.png, Func_class, picture放到dist的main文件夹中，
# 同时需要在dist的main文件夹中创建一个新的Func_class文件夹并再建立一个calculate文件夹用于存放calmodewindow.ui和callogo.png
