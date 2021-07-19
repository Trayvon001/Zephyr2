from PySide2.QtWidgets import QFileDialog, QMainWindow
from PySide2 import QtGui
from PyQt5 import QtWidgets
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import xlrd
from Lib.drawpic.drawpicMainUI import Ui_MainWindow
# import Lib.drawpic.drawpichelp as help
# import Lib.drawpic.drawpicupdatelog as updatelog
import time
from PIL import Image


class drawpicmode(QtWidgets.QMainWindow, Ui_MainWindow):
    history = []
    h = -1
    cc = 0
    color = ['blue', 'red', 'purple', 'darkgreen', 'darkgoldenrod']  # 用于自动颜色选择的列表
    n = 1
    label = []  # 用于存储标签名称
    filename = ''  # 用于存储文件的绝对位置
    history_former = 0  # 用于判断历史记录的上下, 1代表上，-1代表下
    rotation_num = 0

    def __init__(self):
        super(drawpicmode, self).__init__()
        self.setupUi(self)
        # 将按钮和相应的函数联系起来
        self.clearbtn.clicked.connect(self.clear)
        self.hisupbtn.clicked.connect(self.history_up)
        self.hisdownbtn.clicked.connect(self.history_down)
        self.drawbtn.clicked.connect(self.draw)
        self.txtfile.triggered.connect(self.txtfileHandle)
        self.excelfile.triggered.connect(self.excelfileHandle)
        # self.helpdocu.triggered.connect(self.help)
        # self.updatedocu.triggered.connect(self.updatelog)
        self.d10.triggered.connect(self.rotation_state_pure10)
        self.d20.triggered.connect(self.rotation_state_pure20)
        self.d30.triggered.connect(self.rotation_state_pure30)
        self.d45.triggered.connect(self.rotation_state_pure45)
        self.d50.triggered.connect(self.rotation_state_pure50)
        self.d60.triggered.connect(self.rotation_state_pure60)
        self.d75.triggered.connect(self.rotation_state_pure75)
        self.d80.triggered.connect(self.rotation_state_pure80)
        self.d90.triggered.connect(self.rotation_state_pure90)
        # self.export_image.triggered.connect(self.export_image)
        # self.ui.updatedocu.triggered.connect(self.updatedocu)
        # 将按钮和相应的函数联系起来

    def export_image(self):
        imgs = Image.open('temp_image2.png')
        imgs.save('result\\result.png')

    def rotation_state_pure10(self):
        #  以下用于确定坐标旋转度
        self.rotation_num = 10
        self.ui.d20.setChecked(False)  # 用于实现只能勾选一个角度
        self.ui.d30.setChecked(False)
        self.ui.d45.setChecked(False)
        self.ui.d50.setChecked(False)
        self.ui.d60.setChecked(False)
        self.ui.d75.setChecked(False)
        self.ui.d80.setChecked(False)
        self.ui.d90.setChecked(False)

    def rotation_state_pure20(self):
        self.rotation_num = 20
        self.ui.d10.setChecked(False)  # 用于实现只能勾选一个角度
        self.ui.d30.setChecked(False)
        self.ui.d45.setChecked(False)
        self.ui.d50.setChecked(False)
        self.ui.d60.setChecked(False)
        self.ui.d75.setChecked(False)
        self.ui.d80.setChecked(False)
        self.ui.d90.setChecked(False)

    def rotation_state_pure30(self):
        self.rotation_num = 30
        self.ui.d10.setChecked(False)  # 用于实现只能勾选一个角度
        self.ui.d20.setChecked(False)
        self.ui.d45.setChecked(False)
        self.ui.d50.setChecked(False)
        self.ui.d60.setChecked(False)
        self.ui.d75.setChecked(False)
        self.ui.d80.setChecked(False)
        self.ui.d90.setChecked(False)

    def rotation_state_pure45(self):
        self.rotation_num = 45
        self.ui.d10.setChecked(False)  # 用于实现只能勾选一个角度
        self.ui.d20.setChecked(False)
        self.ui.d30.setChecked(False)
        self.ui.d50.setChecked(False)
        self.ui.d60.setChecked(False)
        self.ui.d75.setChecked(False)
        self.ui.d80.setChecked(False)
        self.ui.d90.setChecked(False)

    def rotation_state_pure50(self):
        self.rotation_num = 50
        self.ui.d10.setChecked(False)  # 用于实现只能勾选一个角度
        self.ui.d20.setChecked(False)
        self.ui.d30.setChecked(False)
        self.ui.d45.setChecked(False)
        self.ui.d60.setChecked(False)
        self.ui.d75.setChecked(False)
        self.ui.d80.setChecked(False)
        self.ui.d90.setChecked(False)

    def rotation_state_pure60(self):
        self.rotation_num = 60
        self.ui.d10.setChecked(False)  # 用于实现只能勾选一个角度
        self.ui.d20.setChecked(False)
        self.ui.d30.setChecked(False)
        self.ui.d45.setChecked(False)
        self.ui.d50.setChecked(False)
        self.ui.d75.setChecked(False)
        self.ui.d80.setChecked(False)
        self.ui.d90.setChecked(False)

    def rotation_state_pure75(self):
        self.rotation_num = 75
        self.ui.d10.setChecked(False)  # 用于实现只能勾选一个角度
        self.ui.d20.setChecked(False)
        self.ui.d30.setChecked(False)
        self.ui.d45.setChecked(False)
        self.ui.d50.setChecked(False)
        self.ui.d60.setChecked(False)
        self.ui.d80.setChecked(False)
        self.ui.d90.setChecked(False)

    def rotation_state_pure80(self):
        self.rotation_num = 80
        self.ui.d10.setChecked(False)  # 用于实现只能勾选一个角度
        self.ui.d20.setChecked(False)
        self.ui.d30.setChecked(False)
        self.ui.d45.setChecked(False)
        self.ui.d50.setChecked(False)
        self.ui.d60.setChecked(False)
        self.ui.d90.setChecked(False)

    def rotation_state_pure90(self):
        self.rotation_num = 90
        self.ui.d10.setChecked(False)  # 用于实现只能勾选一个角度
        self.ui.d20.setChecked(False)
        self.ui.d30.setChecked(False)
        self.ui.d45.setChecked(False)
        self.ui.d50.setChecked(False)
        self.ui.d60.setChecked(False)
        self.ui.d75.setChecked(False)
        self.ui.d80.setChecked(False)
        #  the code above is there to decide the value of rotation_num

    # def updatelog(self):
    #     self.updatelog = updatelog.updatelog()
    #     self.updatelog.ui.show()
    #
    # def help(self):
    #     self.help = help.help()
    #     self.help.ui.show()

    def clear(self):  # 所有参数都要清零
        self.ui.clearbtn.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;\n"
                                       "background-color: rgb(175, 175, 175);")
        start_time = time.time()
        self.ui.repaint()  # 刷新界面
        #  以上部分实现点击下沉的功能同时显示运行状态
        # The Clear Function Block #
        self.ui.xlabel.setText('')
        self.ui.xinput.setText('')
        self.ui.ylabel.setText('')
        self.ui.yinput.setText('')
        self.ui.title.setText('')
        self.ui.labelinput.setText('')
        self.ui.numinput.setText('')
        self.ui.xinput.setPlaceholderText('请在此处输入横坐标数据（用空格分隔）')
        self.ui.yinput.setPlaceholderText('请在此处输入横坐标数据（用空格分隔）')
        self.n = 1
        self.label = []
        self.cc = 0
        self.ui.labelinput.setPlaceholderText("请输入第1条曲线的标签名")
        # The Clear Function Block #
        # Reset the clear button's color
        end_time = time.time()
        if end_time - start_time <= 0.1:
            time.sleep(0.1 - (end_time - start_time))
        self.ui.clearbtn.setStyleSheet("background-color: rgb(246, 255, 237);\n"
                                       "border:2px groove gray;border-radius:10px;padding:2px 4px;\n"
                                       "")

    def draw(self):
        self.ui.drawbtn.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;\n"
                                      "background-color: rgb(175, 175, 175);")
        start_time = time.time()
        self.ui.repaint()  # 刷新界面
        #  以上部分实现点击下沉的功能同时显示运行状态
        # Main Functional Block
        # 解决中文乱码问题
        plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
        plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
        # 解决中文乱码问题
        num = self.ui.numinput.text()
        if num == '':
            num = 1  # 没输入时默认为1
        else:
            num = int(num)
        # 首先应该先读取要画的曲线的条数，然后再读取各个数据
        data1 = self.ui.xinput.toPlainText()
        xdata = data1.split(' ')  # 将输入的横坐标数据存入列表中
        length = len(xdata)
        legend = self.ui.labelinput.text()
        self.label.append(legend)
        x_tick = xdata.copy()
        is_num = 1  # 1表示数字，0表示中文
        if xdata[0].isdigit() == 0:  # 非数字的情况
            is_num = 0
            for i in range(len(xdata)):  # 用等间隔的数字代替
                xdata[i] = i + 1
        else:  # 是数字的情况
            is_num = 1
            for i in range(len(xdata)):  # 将字符转换成数字
                xdata[i] = eval(xdata[i])
        data2 = self.ui.yinput.toPlainText()
        ydata = data2.split(' ')  # 将输入的纵坐标数据存入ydata列表中
        for i in range(len(ydata)):  # 将字符转换成数字
            ydata[i] = eval(ydata[i])
        xlabel = self.ui.xlabel.text()
        ylabel = self.ui.ylabel.text()  # 设置横纵坐标
        title = self.ui.title.text()  # 获取图片标题
        len_history = len(self.history)
        if self.history_former == -1 and self.h != -1:
            self.h -= 1
        while self.h < len_history - 1:  # 删除后面的多余的历史数据
            self.history.pop()
            len_history = len(self.history)
        self.history.append([data1, data2, xlabel, ylabel, title, legend])
        self.h += 1
        self.history_former = 0
        # 以下代码块用于解决x不按从小到大的顺序输入时的处理
        dic = {}
        for i in range(length):
            dic[xdata[i]] = ydata[i]
        list.sort(xdata)  # 对x坐标进行排序
        for i in range(length):
            ydata[i] = dic[xdata[i]]
        # 以上代码块用于解决x不按从小到大的顺序输入时的图像的绘制
        x = np.array(xdata)
        y = np.array(ydata)
        # 以下代码块用于解决x不按从小到大的顺序输入时的处理
        xvalue = np.arange(min(x), max(x), 0.01)  # 通过0.001来控制光滑程度
        yvalue = make_interp_spline(x, y)(xvalue)  # 产生一组需要的数据来光滑绘制图像
        plt.plot(xvalue, yvalue, color=self.color[self.cc])
        #  plt.scatter(x, y, marker='o', color=self.color[self.cc])  绘制数据散点
        ##########################自选功能函数模块################################
        if self.ui.data_label.isChecked():  # 用于实现显示数据标签的功能
            for a, b in zip(x, y):
                plt.text(a, b + 0.37, '%.0f' % b, ha='center', va='bottom', fontsize=17)
        ##########################自选功能函数模块################################
        self.cc += 1
        self.cc = self.cc % 5  # 用于自动选择颜色
        if self.n == num:
            plt.xlabel(xlabel, size=17)
            plt.ylabel(ylabel, size=17)
            plt.title(title, size=17)
            #  自选功能函数模块
            if self.ui.legend.isChecked():
                if len(self.label) == 1:
                    self.label.append('实际数据点')
                plt.legend(loc='upper right', labels=self.label)
            if self.ui.grid.isChecked():
                plt.grid()
            #  自选功能函数模块
            if is_num == 0:  # 中文时需要替换图标
                plt.xticks(xdata, x_tick, rotation=self.rotation_num)
            else:  # 否则直接旋转图标
                plt.xticks(rotation=self.rotation_num)
            if self.ui.img_sep_show.isChecked():  # 图片单独显示
                plt.show()
            else:  # 默认显示到方框中
                plt.savefig('temp_image.png')
                plt.close()
                img = Image.open('temp_image.png')
                img1 = img.resize((338, 336))
                img1.save('temp_image2.png')
                self.ui.image_show.setPixmap(QtGui.QPixmap('temp_image2.png'))
        else:
            self.n += 1
            self.ui.labelinput.setText('')
            self.ui.labelinput.setPlaceholderText("请输入第" + str(self.n) + "条曲线的标签")
        # Main Functional Block
        # Reset the drawpicture button's color
        end_time = time.time()
        if end_time - start_time <= 0.1:
            time.sleep(0.1 - (end_time - start_time))
        self.ui.drawbtn.setStyleSheet("background-color: rgb(85, 255, 255);\n"
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
        else:  # 存在历史记录的话则显示历史记录
            if self.history_former == -1 and self.h != len(self.history) - 1:  # 用于解决历史记录由下往上要按两次的问题
                self.h -= 1
            self.history_former = 1
            self.ui.xlabel.setText(self.history[self.h][2])
            self.ui.xinput.setText(self.history[self.h][0])
            self.ui.ylabel.setText(self.history[self.h][3])
            self.ui.yinput.setText(self.history[self.h][1])
            self.ui.title.setText(self.history[self.h][4])
            self.ui.labelinput.setText(self.history[self.h][5])
            self.h -= 1
        #  Main Code Block To Realise History Up  #
        # Reset the hisUp button's color
        end_time = time.time()
        if end_time - start_time <= 0.1:
            time.sleep(0.1 - (end_time - start_time))
        self.ui.hisupbtn.setStyleSheet("background-color: rgb(221, 226, 255);\n"
                                       "border:2px groove gray;border-radius:10px;padding:2px 4px;")

    def history_down(self):  # 历史记录的下翻
        self.ui.hisdownbtn.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;\n"
                                         "background-color: rgb(175, 175, 175);")
        start_time = time.time()
        self.ui.repaint()  # 刷新界面
        #  程序运行时显示灰色
        #  Main Code Block To Realise History Up  #
        if self.h + 1 == len(self.history):
            self.ui.xinput.setText('')
            self.ui.xinput.setPlaceholderText('无更多的历史记录！！！')
            self.ui.yinput.setText('')
            self.ui.yinput.setPlaceholderText('无更多的历史记录！！！')
        else:
            if self.history_former == 1:  # 用于解决历史记录由上往下要按两次的问题
                if self.h == -1:
                    self.h += 1
                else:
                    self.h += 2
            else:
                self.h += 1
            self.history_former = -1
            self.ui.xlabel.setText(self.history[self.h][2])
            self.ui.xinput.setText(self.history[self.h][0])
            self.ui.ylabel.setText(self.history[self.h][3])
            self.ui.yinput.setText(self.history[self.h][1])
            self.ui.title.setText(self.history[self.h][4])
            self.ui.labelinput.setText(self.history[self.h][5])
            #  Main Code Block To Realise History Up  #
            # Reset the hisUp button's color
        end_time = time.time()
        if end_time - start_time <= 0.1:
            time.sleep(0.1 - (end_time - start_time))
        self.ui.hisdownbtn.setStyleSheet("background-color: rgb(221, 226, 255);\n"
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
