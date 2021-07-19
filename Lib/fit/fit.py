from PyQt5 import QtWidgets
from PySide2.QtWidgets import QMainWindow, QFileDialog
from Lib.fit.fitmodeMainUI import Ui_MainWindow
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import Lib.fit.fithelp as help
import Lib.fit.fitupdatelog as updatelog
import time


class fitmode(QtWidgets.QMainWindow, Ui_MainWindow):
    history = []
    h = -1
    history_former = 0  # 用于判断历史记录的上下, 1代表上，-1代表下

    def __init__(self):
        super(fitmode, self).__init__()
        self.setupUi(self)
        # 将按钮和相应的函数联系起来
        self.hisupbtn.clicked.connect(self.history_up)
        self.hisdownbtn.clicked.connect(self.history_down)
        self.fitbtn.clicked.connect(self.fit)
        self.clearbtn.clicked.connect(self.clear)
        self.txtfile.triggered.connect(self.txtfileHandle)
        self.excelfile.triggered.connect(self.excelfileHandle)
        self.helpdocu.triggered.connect(self.help)
        self.updatedocu.triggered.connect(self.updatelog)
        # 将按钮和相应的函数联系起来

    def updatelog(self):
        self.updatelog = updatelog.MainWindow()
        self.updatelog.show()

    def help(self):
        self.help = help.MainWindow()
        self.help.show()

    def clear(self):  # 清楚所有内容
        self.ui.clearbtn.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;\n"
                                       "background-color: rgb(175, 175, 175);")
        start_time = time.time()
        self.ui.repaint()  # 刷新界面
        #  程序运行时显示灰色
        #  Main Code Block To Realise Clear  #
        self.ui.xinput.setText('')
        self.ui.yinput.setText('')
        self.ui.xlabel.setText('')
        self.ui.ylabel.setText('')
        self.ui.title.setText('')
        self.ui.power.setText('')
        self.ui.expressionoutput.setText('')
        self.ui.xinput.setPlaceholderText('请在此处输入横坐标数据（用空格分隔）')
        self.ui.yinput.setPlaceholderText('请在此处输入横坐标数据（用空格分隔）')
        #  Main Code Block To Realise Clear  #
        # Reset the clear button's color
        end_time = time.time()
        if end_time - start_time <= 0.1:
            time.sleep(0.1 - (end_time - start_time))
        self.ui.clearbtn.setStyleSheet("background-color: rgb(255, 214, 208);\n"
                                       "border:2px groove gray;border-radius:10px;padding:2px 4px;")

    def fit(self):
        self.ui.fitbtn.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;\n"
                                     "background-color: rgb(175, 175, 175);")
        start_time = time.time()
        self.ui.repaint()  # 刷新界面
        #  程序运行时显示灰色
        #  Main Code Block To Realise Clear  #
        data1 = self.ui.xinput.toPlainText()
        xdata = data1.split(' ')  # 将输入的横坐标数据存入列表中
        for i in range(len(xdata)):  # 将字符转换成数字
            xdata[i] = eval(xdata[i])
        data2 = self.ui.yinput.toPlainText()
        length = len(xdata)
        ydata = data2.split(' ')  # 将输入的纵坐标数据存入ydata列表中
        for i in range(len(ydata)):  # 将字符转换成数字
            ydata[i] = eval(ydata[i])
        xlabel = self.ui.xlabel.text()
        ylabel = self.ui.ylabel.text()  # 设置横纵坐标
        title = self.ui.title.text()  # 获取图片标题
        power = int(self.ui.power.text())
        # 以下代码块用于解决x不按从小到大的顺序输入时的处理
        dic = {}
        for i in range(length):
            dic[xdata[i]] = ydata[i]
        list.sort(xdata)  # 对x坐标进行排序
        for i in range(length):
            ydata[i] = dic[xdata[i]]
        # 以上代码块用于解决x不按从小到大的顺序输入时的图像的绘制
        x = np.array(xdata)  # 转换成numpy需要的格式
        y = np.array(ydata)
        z1 = np.polyfit(xdata, ydata, power)  # 对函数进行拟合及输出表达式
        p1 = np.poly1d(z1)
        # 解决中文乱码问题
        plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
        plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
        # 解决中文乱码问题
        plt.scatter(xdata, ydata, marker='o')  # 绘制散点图
        plt.xlabel(xlabel, size=17)
        plt.ylabel(ylabel, size=17)
        # 处理需要画电阻导数为横坐标的图像
        if max(xdata) < 1:  # 说明此时应该将x的所有数值都乘以3个数量级或6个或9个数量级
            if min(xdata) <= 0.00000001:  # 乘以10的9次方
                xvalue = np.arange(min(xdata)*(10**9), max(xdata)*(10**9), 1)  # 生成此条件下适合的x的数值
                yvalue = np.polyval(z1, xvalue / (10**9))
                for i in range(len(xvalue)):
                    xvalue[i] = xvalue[i] / (10**9)
            elif min(xdata) <= 0.00001:
                xvalue = np.arange(min(xdata) * (10 ** 6), max(xdata) * (10 ** 6), 0.001)
                yvalue = np.polyval(z1, xvalue / (10 ** 6))
                for i in range(len(xvalue)):
                    xvalue[i] = xvalue[i] / (10**6)
            elif min(xdata) <= 0.01:
                xvalue = np.arange(min(xdata) * (10 ** 3), max(xdata) * (10 ** 3), 0.001)
                yvalue = np.polyval(z1, xvalue / (10 ** 3))
                for i in range(len(xvalue)):
                    xvalue[i] = xvalue[i] / (10**3)
        else:
            xvalue = np.arange(min(xdata), max(xdata), 0.001)  # 确保生成的xvalue可以按要求画出数据
            yvalue = np.polyval(z1, xvalue)
        # 处理需要画电阻导数为横坐标的图像
        r = np.corrcoef(x, y)
        relate = r.min()
        result_out = str(p1) + '\nX和Y的相关系数r为：' + str(relate)
        self.ui.expressionoutput.setText(result_out)
        len_history = len(self.history)
        if self.history_former == -1 and self.h != -1:
            self.h -= 1
        while self.h < len_history - 1:  # 删除后面的多余的历史数据
            self.history.pop()
            len_history = len(self.history)
        self.history.append([data1, data2, xlabel, ylabel, title, power, result_out])
        self.h += 1
        self.history_former = 0
        plt.plot(xvalue, yvalue, color='red')  # 在同一幅图上画出拟合曲线
        plt.title(title, size=17) #0.496 0.856 1.181 1.520 1.735 1.943  1/470 1/1000 1/2000 1/5100 1/10000 1/39000
        plt.legend(loc='upper right', labels=['拟合曲线', '实际数据点'])
        if self.ui.grid.isChecked():  # 用于达到可以自选网格线的功能
            plt.grid()
        if self.ui.data_label.isChecked():  # 用于实现显示数据标签的功能
            for a, b in zip(x, y):
                plt.text(a, b + 0.25, '%.0f' % b, ha='center', va='bottom', fontsize=17)
        plt.show()
        #  Main Code Block To Realise Clear  #
        # Reset the fit button's color
        end_time = time.time()
        if end_time - start_time <= 0.1:
            time.sleep(0.1 - (end_time - start_time))
        self.ui.fitbtn.setStyleSheet("background-color: rgb(170, 170, 255);\n"
                                     "border:2px groove gray;border-radius:10px;padding:2px 4px;")

    def history_up(self):  # 历史记录不再清空
        self.ui.hisupbtn.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;\n"
                                       "background-color: rgb(175, 175, 175);")
        start_time = time.time()
        self.ui.repaint()  # 刷新界面
        #  程序运行时显示灰色
        #  Main Code Block To Realise History Up  #
        if self.h == -1:  # 说明历史记录为空
            self.ui.xinput.setText('')
            self.ui.xinput.setPlaceholderText('无更多的历史记录！！！')
            self.ui.yinput.setText('')
            self.ui.yinput.setPlaceholderText('无更多的历史记录！！！')
            self.ui.expressionoutput.setText('')
        else:  # 存在历史记录的话则显示历史记录
            if self.history_former == -1 and self.h != len(self.history) - 1:  # 用于解决历史记录由下往上要按两次的问题
                self.h -= 1
            self.history_former = 1
            self.ui.xinput.setText(self.history[self.h][0])
            self.ui.yinput.setText(self.history[self.h][1])
            self.ui.xlabel.setText(self.history[self.h][2])
            self.ui.ylabel.setText(self.history[self.h][3])
            self.ui.title.setText(self.history[self.h][4])
            self.ui.power.setText(str(self.history[self.h][5]))
            self.ui.expressionoutput.setText(self.history[self.h][6])
            self.h -= 1
        # Reset the hisUp button's color
        end_time = time.time()
        if end_time - start_time <= 0.1:
            time.sleep(0.1 - (end_time - start_time))
        self.ui.hisupbtn.setStyleSheet("background-color: rgb(241, 188, 255);\n"
                                       "border:2px groove gray;border-radius:10px;padding:2px 4px;")

    def history_down(self):  # 历史记录的下翻
        self.ui.hisdownbtn.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;\n"
                                       "background-color: rgb(175, 175, 175);")
        start_time = time.time()
        self.ui.repaint()  # 刷新界面
        #  程序运行时显示灰色
        #  Main Code Block To Realise History Down  #
        if self.h + 1 == len(self.history):
            self.ui.xinput.setText('')
            self.ui.xinput.setPlaceholderText('无更多的历史记录！！！')
            self.ui.yinput.setText('')
            self.ui.yinput.setPlaceholderText('无更多的历史记录！！！')
            self.ui.expressionoutput.setText('')
        else:
            if self.history_former == 1:  # 用于解决历史记录由上往下要按两次的问题
                if self.h == -1:
                    self.h += 1
                else:
                    self.h += 2
            else:
                self.h += 1
            self.history_former = -1
            self.ui.xinput.setText(self.history[self.h][0])
            self.ui.yinput.setText(self.history[self.h][1])
            self.ui.xlabel.setText(self.history[self.h][2])
            self.ui.ylabel.setText(self.history[self.h][3])
            self.ui.title.setText(self.history[self.h][4])
            self.ui.power.setText(str(self.history[self.h][5]))
            self.ui.expressionoutput.setText(self.history[self.h][6])
        # Reset the hisDown button's color
        end_time = time.time()
        if end_time - start_time <= 0.1:
            time.sleep(0.1 - (end_time - start_time))
        self.ui.hisdownbtn.setStyleSheet("background-color: rgb(241, 188, 255);\n"
                                         "border:2px groove gray;border-radius:10px;padding:2px 4px;")

    def txtfileHandle(self):  # 对txt文件进行操作,将其内容添加到文本框中
        # 以下代码可以打开文本对话框并获取文件的绝对路径
        selectwindow = QMainWindow()  # 建立一个新的窗口
        Filewindow = QFileDialog(selectwindow)  # 设置成打开文件的窗口
        FileDialog = Filewindow.getOpenFileName(selectwindow, "选择文件")  # 设置窗口名称
        selectwindow.show()  # 显示该文本框
        # 以上代码可以打开文本对话框并获取文件的绝对路径
        filepath = FileDialog[0]  # 获取文本文件的绝对位置
        textfile = open(filepath, "r")
        xdisplay = ''
        ydisplay = ''
        lines = textfile.readline()
        while lines:  # 读取文本文件的内容
            if lines[len(lines) - 1] == '\n':
                lines = lines[:-1]  # 去掉换行符
            line = lines.split(" ")
            xdisplay = xdisplay + line[0] + ' '
            ydisplay = ydisplay + line[1] + ' '
            lines = textfile.readline()
        xdisplay = xdisplay[:-1]
        ydisplay = ydisplay[:-1]
        self.xinput.setText(xdisplay)
        self.yinput.setText(ydisplay)

    def excelfileHandle(self):  # 读取excel文件并进行相关计算
        # 以下代码可以打开文本对话框并获取文件的绝对路径
        selectwindow = QMainWindow()  # 建立一个新的窗口
        Filewindow = QFileDialog(selectwindow)  # 设置成打开文件的窗口
        FileDialog = Filewindow.getOpenFileName(selectwindow, "选择文件")  # 设置窗口名称
        print(FileDialog[0])  # FileDialog[0]就是所选择的文件的绝对路径
        selectwindow.show()  # 显示该文本框
        # 以上代码可以打开文本对话框并获取文件的绝对路径
        fielpath = FileDialog[0]  # 获取文本文件的绝对位置
        efile = xlrd.open_workbook(fielpath)
        sheet = efile.sheet_by_name('Sheet1')  # 打开sheet1
        rows_num = sheet.nrows  # 获取行数即可用来作为循环条件
        columns_num = sheet.ncols  # 获取列数来作为循环条件
        x_display = ''
        y_display = ''
        x_line = self.excelxinput.text()  # 从UI界面读取x要读取的excel文件的列数
        y_line = self.excelyinput.text()  # 从UI界面读取y要读取的excel文件的列数
        read_method = self.methodinput.text()  # 横竖读法读取,1为横，2为竖
        ######################以下用于设置x,y,readmethod的缺省值#####################
        if x_line == '':  # 设置缺省值
            x_line = 0
        else:
            x_line = int(x_line)
        if y_line == '':
            y_line = 1
        else:
            y_line = int(y_line)
        if read_method == '':
            read_method = 2
        else:
            read_method = int(read_method)
        ######################以下用于读取excel中的数据#####################
        if read_method == 1:
            for i in range(0, columns_num):
                x_display = x_display + str(sheet.cell(x_line, i).value) + ' '
                y_display = y_display + str(sheet.cell(y_line, i).value) + ' '
        elif read_method == 2:
            for i in range(0, rows_num):
                x_display = x_display + str(sheet.cell(i, x_line).value) + ' '
                y_display = y_display + str(sheet.cell(i, y_line).value) + ' '
        x_display = x_display[:-1]
        if x_display[0] == ' ':  # 避免出现开头为0的情况
            x_display = x_display[1:]
        y_display = y_display[:-1]
        if y_display[0] == ' ':  # 避免出现开头为0的情况
            y_display = y_display[1:]
        self.xinput.setText(x_display)
        self.yinput.setText(y_display)

# QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
# app = QApplication([])
# app.setWindowIcon(QIcon('fitmodeicon.png'))
# stats = fitmode()
# stats.ui.show()
# app.exec_()
