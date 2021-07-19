from PySide2 import QtGui
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PySide2.QtWidgets import QFileDialog, QMainWindow
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import Func_class.drawpic.drawpichelp as help
import Func_class.drawpic.drawpicupdatelog as updatelog
import time
from PIL import Image
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D


class advdrawpic:
    history = []
    h = -1
    n = 1
    label = []  # 用于存储标签名称
    filename = ''  # 用于存储文件的绝对位置
    history_former = 0  # 用于判断历史记录的上下, 1代表上，-1代表下
    rotation_num = 0
    image_num = 1

    def __init__(self):
        qfile_status = QFile(
            "Func_class\\advanceddraw\\advanceddrawwin.ui")  # 要在主目录中运行时加上Func_class\calculate\calmodewindow.ui
        qfile_status.open(QFile.ReadOnly)
        qfile_status.close()
        # 从UI定义中动态创建一个相应的窗口对象
        # 注意：这里面的空间对象也成为窗口对象的属性了
        # 比如self.ui.buttom, self.ui.textEdit
        self.ui = QUiLoader().load(qfile_status)
        # 将按钮和相应的函数联系起来
        self.ui.clearbtn.clicked.connect(self.clear)
        self.ui.hisupbtn.clicked.connect(self.history_up)
        self.ui.hisdownbtn.clicked.connect(self.history_down)
        self.ui.drawbtn.clicked.connect(self.draw)
        self.ui.txtfile.triggered.connect(self.txtfile)
        self.ui.excelfile.triggered.connect(self.excelfile)
        self.ui.helpdocu.triggered.connect(self.help)
        self.ui.updatedocu.triggered.connect(self.updatelog)
        # 用于限制旋转这个子菜单下只能有一个被打勾 #
        self.ui.d10.triggered.connect(self.rotation_state_pure10)
        self.ui.d20.triggered.connect(self.rotation_state_pure20)
        self.ui.d30.triggered.connect(self.rotation_state_pure30)
        self.ui.d45.triggered.connect(self.rotation_state_pure45)
        self.ui.d50.triggered.connect(self.rotation_state_pure50)
        self.ui.d60.triggered.connect(self.rotation_state_pure60)
        self.ui.d75.triggered.connect(self.rotation_state_pure75)
        self.ui.d80.triggered.connect(self.rotation_state_pure80)
        self.ui.d90.triggered.connect(self.rotation_state_pure90)
        # 用于限制旋转这个子菜单下只能有一个被打勾 #
        # 用于限制图片数量这个子菜单下只能有一个被打勾 #
        self.ui.num12.triggered.connect(self.num_pure12)
        self.ui.num13.triggered.connect(self.num_pure13)
        self.ui.num21.triggered.connect(self.num_pure21)
        self.ui.num22.triggered.connect(self.num_pure22)
        self.ui.num23.triggered.connect(self.num_pure23)
        self.ui.num31.triggered.connect(self.num_pure31)
        self.ui.num32.triggered.connect(self.num_pure32)
        self.ui.num33.triggered.connect(self.num_pure33)
        # 用于限制图片数量这个子菜单下只能有一个被打勾 #
        self.ui.export_image.triggered.connect(self.export_image)
        # self.ui.updatedocu.triggered.connect(self.updatedocu)
        # 将按钮和相应的函数联系起来

    def export_image(self):
        imgs = Image.open('temp_image2.png')
        imgs.save('result\\result.png')

    def num_pure12(self):
        self.image_num = 121
        self.ui.num12.setChecked(True)
        self.ui.num13.setChecked(False)
        self.ui.num21.setChecked(False)
        self.ui.num22.setChecked(False)
        self.ui.num23.setChecked(False)
        self.ui.num31.setChecked(False)
        self.ui.num32.setChecked(False)
        self.ui.num33.setChecked(False)

    def num_pure13(self):
        self.image_num = 131
        self.ui.num12.setChecked(False)
        self.ui.num21.setChecked(False)
        self.ui.num22.setChecked(False)
        self.ui.num23.setChecked(False)
        self.ui.num31.setChecked(False)
        self.ui.num32.setChecked(False)
        self.ui.num33.setChecked(False)

    def num_pure21(self):
        self.image_num = 211
        self.ui.num12.setChecked(False)
        self.ui.num13.setChecked(False)
        self.ui.num22.setChecked(False)
        self.ui.num23.setChecked(False)
        self.ui.num31.setChecked(False)
        self.ui.num32.setChecked(False)
        self.ui.num33.setChecked(False)

    def num_pure22(self):
        self.image_num = 221
        self.ui.num12.setChecked(False)
        self.ui.num13.setChecked(False)
        self.ui.num21.setChecked(False)
        self.ui.num23.setChecked(False)
        self.ui.num31.setChecked(False)
        self.ui.num32.setChecked(False)
        self.ui.num33.setChecked(False)

    def num_pure23(self):
        self.image_num = 231
        self.ui.num12.setChecked(False)
        self.ui.num13.setChecked(False)
        self.ui.num21.setChecked(False)
        self.ui.num22.setChecked(False)
        self.ui.num31.setChecked(False)
        self.ui.num32.setChecked(False)
        self.ui.num33.setChecked(False)

    def num_pure31(self):
        self.image_num = 311
        self.ui.num12.setChecked(False)
        self.ui.num13.setChecked(False)
        self.ui.num21.setChecked(False)
        self.ui.num22.setChecked(False)
        self.ui.num23.setChecked(False)
        self.ui.num32.setChecked(False)
        self.ui.num33.setChecked(False)

    def num_pure32(self):
        self.image_num = 321
        self.ui.num12.setChecked(False)
        self.ui.num13.setChecked(False)
        self.ui.num21.setChecked(False)
        self.ui.num22.setChecked(False)
        self.ui.num23.setChecked(False)
        self.ui.num31.setChecked(False)
        self.ui.num33.setChecked(False)

    def num_pure33(self):
        self.image_num = 331
        self.ui.num12.setChecked(False)
        self.ui.num13.setChecked(False)
        self.ui.num21.setChecked(False)
        self.ui.num22.setChecked(False)
        self.ui.num23.setChecked(False)
        self.ui.num31.setChecked(False)
        self.ui.num32.setChecked(False)

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

    def updatelog(self):
        self.updatelog = updatelog.updatelog()
        self.updatelog.ui.show()

    def help(self):
        self.help = help.help()
        self.help.ui.show()

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
        self.ui.zinput.setText('')
        self.ui.zlabel.setText('')
        self.ui.title.setText('')
        self.ui.labelinput.setText('')
        self.ui.xline.setText('')
        self.ui.yline.setText('')
        self.ui.zline.setText('')
        self.ui.xinput.setPlaceholderText('请在此处输入X轴数据（用空格分隔）')
        self.ui.yinput.setPlaceholderText('请在此处输入Y轴数据（用空格分隔）')
        self.ui.zinput.setPlaceholderText('请在此处输入Z轴数据（用空格分隔）')
        self.n = 1
        self.label = []
        self.cc = 0
        self.ui.labelinput.setPlaceholderText("请输入第1条图像的标签名")
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
        self.label = []  # reset the values of label
        fig = plt.figure()
        ax1 = plt.axes(projection='3d')
        # get the total numbers of figures and set the default value#
        num = self.ui.numinput.text()
        if num == '':
            num = 1
        else:
            num = int(num)
        # get the total numbers of figures and set the default value#
        # 首先应该先读取要画的曲线的条数，然后再读取各个数据
        # get the image's name #
        legend = self.ui.labelinput.text()
        self.label.append(legend)
        # get the image's name #
        # read x's input values and transfer to digits#
        data1 = self.ui.xinput.toPlainText()
        xdata = data1.split(' ')  # 将输入的横坐标数据存入列表中
        length = len(xdata)
        if length == 1 and xdata[0].isdigit() == 0:  # 说明是公式
            xdata[0] = eval(xdata[0])
        else:
            for i in range(len(xdata)):  # 将字符转换成数字
                xdata[i] = eval(xdata[i])
        # read x's input values and transfer to digits#
        # read y's input values and transfer to digits#
        data2 = self.ui.yinput.toPlainText()
        ydata = data2.split(' ')  # 将输入的纵坐标数据存入ydata列表中
        length_y = len(ydata)
        if length_y == 1 and ydata[0].isdigit() == 0:  # 说明是公式
            ydata[0] = eval(ydata[0])
        else:  # 对数字的情况进行处理
            for i in range(len(ydata)):  # 将字符转换成数字
                ydata[i] = eval(ydata[i])
        # read y's input values and transfer to digits#
        X, Y = np.meshgrid(xdata[0], ydata[0])
        # 读取z轴坐标 #
        data3 = self.ui.zinput.toPlainText()
        zdata = data3.split(' ')
        length_z = len(zdata)
        if length_z == 1 and zdata[0].isdigit() == 0:
            zdata[0] = eval(zdata[0])
        else:
            for i in range(len(zdata)):
                zdata[i] = eval(zdata[i])
        # 读取z轴坐标 #
        # read the labels of each axis #
        xlabel = self.ui.xlabel.text()
        ylabel = self.ui.ylabel.text()  # 设置横纵坐标
        zlabel = self.ui.zlabel.text()
        title = self.ui.title.text()  # 获取图片标题
        # read the labels of each axis #
        # 存储相应的历史记录 #
        len_history = len(self.history)
        if self.history_former == -1 and self.h != -1:
            self.h -= 1
        while self.h < len_history - 1:  # 删除后面的多余的历史数据
            self.history.pop()
            len_history = len(self.history)
        x_line = self.ui.xline.text()
        y_line = self.ui.yline.text()  # 设置横纵坐标
        z_line = self.ui.zline.text()
        self.history.append([data1, data2, xlabel, ylabel, title, legend, zlabel, data3, x_line, y_line, z_line])
        self.h += 1
        self.history_former = 0
        # 存储相应的历史记录 #
        # 以下代码块用于解决x不按从小到大的顺序输入时的处理
        if length != 1:
            dic = {}
            dicz = {}
            for i in range(length):
                dic[xdata[i]] = ydata[i]
                dicz[xdata[i]] = zdata[i]
            list.sort(xdata)  # 对x坐标进行排序
            for i in range(length):
                ydata[i] = dic[xdata[i]]
                zdata[i] = dicz[xdata[i]]
            # 以上代码块用于解决x不按从小到大的顺序输入时的图像的绘制
            x = np.array(xdata)
            y = np.array(ydata)
            z = np.array(zdata)
        else:
            x = xdata[0]
            y = ydata[0]
            z = zdata[0]
        # set the label of each axis
        if xlabel != '':
            ax1.set_xlabel(xlabel)
        if ylabel != '':
            ax1.set_ylabel(ylabel)
        if zlabel != '':
            ax1.set_zlabel(zlabel)
        # set the label of each axis
        # set the title of this child image #
        if title != '':
            ax1.set_title(title)
        if num == 1:
            if self.ui.dscatter.isChecked():  # 选择绘制图片的格式
                ax1.scatter3D(x, y, z, c=z, cmap='Oranges')  # 绘制三维散点图,根据zd的数据分配颜色，总体为橙色
            elif self.ui.dplot.isChecked():
                ax1.plot3D(x, y, z, 'orange')  # 绘制三维空间曲线
            elif self.ui.d3image.isChecked():  # 绘制三维图
                ax1.plot_surface(x, y, z, rstride=1, cstride=1, cmap='rainbow')
            else:  # 默认绘制散点图
                ax1.scatter3D(x, y, z, c=z, cmap='Oranges')  # 绘制三维散点图,根据zd的数据分配颜色，总体为橙色
            plt.savefig('temp_image.png')
            plt.close()
            img = Image.open('temp_image.png')
            img1 = img.resize((395, 335))
            img1.save('temp_image2.png')
            self.ui.image_show.setPixmap(QtGui.QPixmap('temp_image2.png'))
        else:
            self.n += 1

        '''if self.n == num:
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
            self.ui.labelinput.setPlaceholderText("请输入第" + str(self.n) + "条曲线的标签")'''
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
            self.ui.zinput.setText('')
            self.ui.zinput.setPlaceholderText('无更多的历史记录！！！')
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
            self.ui.zlabel.setText(self.history[self.h][6])
            self.ui.zinput.setText(self.history[self.h][7])
            self.ui.xline.setText(self.history[self.h][8])
            self.ui.yline.setText(self.history[self.h][9])
            self.ui.zline.setText(self.history[self.h][10])
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
            self.ui.zlabel.setText(self.history[self.h][6])
            self.ui.zinput.setText(self.history[self.h][7])
            self.ui.xline.setText(self.history[self.h][8])
            self.ui.yline.setText(self.history[self.h][9])
            self.ui.zline.setText(self.history[self.h][10])
            #  Main Code Block To Realise History Up  #
            # Reset the hisUp button's color
        end_time = time.time()
        if end_time - start_time <= 0.1:
            time.sleep(0.1 - (end_time - start_time))
        self.ui.hisdownbtn.setStyleSheet("background-color: rgb(221, 226, 255);\n"
                                         "border:2px groove gray;border-radius:10px;padding:2px 4px;")

    def txtfile(self):  # 对txt文件进行操作,将其内容添加到文本框中
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
        self.ui.xinput.setText(xdisplay)
        self.ui.yinput.setText(ydisplay)

    def excelfile(self):  # 读取excel文件并进行相关计算
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
        columns_num = sheet.ncols  # 获取列数
        x_display = ''
        y_display = ''
        z_display = ''
        # 以下用于获取x,y,z的excel读取行列数 #
        x_line = self.ui.xline.text()
        y_line = self.ui.yline.text()  # 设置横纵坐标
        z_line = self.ui.zline.text()
        if x_line == '':
            x_line = 1
        else:
            x_line = int(x_line)
        if y_line == '':
            y_line = 2
        else:
            y_line = int(y_line)
        if z_line == '':
            z_line = 3
        else:
            z_line = int(z_line)
        # 以上用于获取x,y,z的excel读取行列数 #
        read_method = 2
        if self.ui.readmethod1.isChecked():
            read_method = 1
        elif self.ui.readmethod2.isChecked():
            read_method = 2
        ######################以下用于读取excel中的数据#####################
        if read_method == 1:
            for i in range(0, columns_num):
                x_display = x_display + str(sheet.cell(x_line, i).value) + ' '
                y_display = y_display + str(sheet.cell(y_line, i).value) + ' '
                z_display = z_display + str(sheet.cell(z_line, i).value) + ' '
        elif read_method == 2:
            for i in range(0, rows_num):
                x_display = x_display + str(sheet.cell(i, x_line).value) + ' '
                y_display = y_display + str(sheet.cell(i, y_line).value) + ' '
                z_display = z_display + str(sheet.cell(i, z_line).value) + ' '
        x_display = x_display[:-1]
        if x_display[0] == ' ':
            x_display = x_display[1:]  # 避免出现开头为0的情况
        y_display = y_display[:-1]
        if y_display[0] == ' ':  # 避免出现开头为0的情况
            y_display = y_display[1:]
        z_display = z_display[:-1]
        if z_display[0] == ' ':  # 避免出现开头为0的情况
            z_display = z_display[1:]
        self.ui.xinput.setText(x_display)
        self.ui.yinput.setText(y_display)
        self.ui.zinput.setText(z_display)
