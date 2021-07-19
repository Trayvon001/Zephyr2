from PyQt5 import QtWidgets
import numpy
from Lib.calculate.calModeUI import Ui_MainWindow
import Lib.calculate.calModeHelpMain as help
import Lib.calculate.calModeLogMain as updatelog
import time


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    history = []
    h = -1

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # self.display()
        # 从UI定义中动态创建一个相应的窗口对象
        # 注意：这里面的空间对象也成为窗口对象的属性了
        # 比如self.buttom, self.textEdit
        # 将按钮和相应的函数联系起来
        self.averagebtn.clicked.connect(self.average)
        self.maxminbtn.clicked.connect(self.extrnum)
        self.mostbtn.clicked.connect(self.most)
        self.uncertainbtn.clicked.connect(self.uncertainty)
        self.variancebtn.clicked.connect(self.var)
        self.clearbtn.clicked.connect(self.clear)
        self.midnumbtn.clicked.connect(self.midnum)
        self.historybtn.clicked.connect(self.his)
        self.errorbtn.clicked.connect(self.ess)  # 误差计算函数
        self.helpdocu.triggered.connect(self.help)
        self.updatedocu.triggered.connect(self.updatelog)
        self.magnifybtn.clicked.connect(self.magnify)
        self.frequencybtn.clicked.connect(self.frenquency_func)
        # 将按钮和相应的函数联系起来

    def frenquency_func(self):  # 通过周期计算放大倍数
        self.frequencybtn.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;\n"
                                           "background-color: rgb(175, 175, 175);")
        start_time = time.time()
        self.repaint()  # 刷新界面
        #  以上部分实现点击下沉的功能同时显示运行状态
        data = self.input.toPlainText()
        lis = data.split(' ')
        n = len(lis)
        for i in range(n):
            lis[i] = eval(lis[i])
        # 以上用于读取数据,和其他函数一致
        length = len(lis)
        w_result = ''
        f_result = ''
        for i in range(length):  # 由于数据是偶数，所以只需要知道其中一半的长度即可
            if lis[i] == 0:
                f_result = f_result + '错误数据 '
                w_result = w_result + '错误数据 '
            else:
                f = 1 / lis[i]
                w = 2 * numpy.pi / lis[i]
                f_result = f_result + str(round(f, 2)) + 'hz '
                w_result = w_result + str(round(w, 3)) + 'rad/s '

        # 恢复按钮颜色
        end_time = time.time()
        if end_time - start_time <= 0.1:
            time.sleep(0.1 - (end_time - start_time))
        self.frequencybtn.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;\n"
                                           "background-color: rgb(255, 254, 237);")
        #  以上代码用于根据时间决定是否需要sleep，并恢复颜色
        self.result.setText('这' + str(n) + '个数据的\n频率分别为：' + f_result + '\n' + '角速度分别为：' + w_result)
        hs = '这' + str(n) + '个数据的\n频率分别为：' + f_result + '\n' + '角速度分别为：' + w_result
        self.h += 1
        self.history.append([data, hs])  # 存储该记录方便之后查找

    def magnify(self):  # 计算放大倍数
        self.magnifybtn.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;\n"
                                         "background-color: rgb(175, 175, 175);")
        start_time = time.time()
        self.repaint()  # 刷新界面
        #  以上部分实现点击下沉的功能同时显示运行状态
        data = self.input.toPlainText()
        lis = data.split(' ')
        n = len(lis)
        for i in range(n):
            lis[i] = eval(lis[i])
        # 以上用于读取数据
        s = int(len(lis) / 2)
        former = lis[0:s]
        later = lis[s:]
        result = ''
        for i in range(len(former)):  # 由于数据是偶数，所以只需要知道其中一半的长度即可
            if former[i] == 0:
                result = result + '错误数据 '
            else:
                times = later[i] / former[i]
                result = result + str(round(times, 2)) + ' '

        # 恢复按钮颜色
        end_time = time.time()
        if end_time - start_time <= 0.1:
            time.sleep(0.1 - (end_time - start_time))
        self.magnifybtn.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;\n"
                                         "background-color: rgb(255, 254, 237);")
        #  以上代码用于根据时间决定是否需要sleep，并恢复颜色
        self.result.setText('这' + str(int(n / 2)) + '个数据的\n放大倍数分别为：' + result)
        hs = '这' + str(int(n / 2)) + '个数据的\n放大倍数分别为：' + result
        self.h += 1
        self.history.append([data, hs])  # 存储该记录方便之后查找

    def updatelog(self):
        self.updatelogUI = updatelog.MainWindow()
        self.updatelogUI.show()

    def help(self):
        self.helpUI = help.MainWindow()
        self.helpUI.show()
        # self.calModeHelpUI.ui.setWindowIcon(QIcon('Func_class\\calculate\\callogo.png'))
        # self.close()  # 加上这段代码可以自动关闭之前的窗口，也可以选择不关闭之前的窗口

    def clear(self):  # 清除所有内容
        self.clearbtn.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;\n"
                                       "background-color: rgb(175, 175, 175);")
        start_time = time.time()
        self.repaint()  # 刷新界面
        #  以上部分实现点击下沉的功能同时显示运行状态
        #  Main Function Block  #
        self.result.setText('')
        self.input.setText('')
        self.input.setPlaceholderText('请在此处输入要处理的数据(用空格分隔)\n计算误差时默认前一半为标准值后一半为实际值')
        self.result.setPlaceholderText('此处将会显示计算结果')
        #  Main Function Block  #
        # Reset the button's color
        end_time = time.time()
        if end_time - start_time <= 0.1:
            time.sleep(0.1 - (end_time - start_time))
        self.clearbtn.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;\n"
                                       "background-color: rgb(255, 254, 237);")
        #  以上代码用于根据时间决定是否需要sleep，并恢复颜色

    def average(self):  # 求取输入的数的平均值
        self.averagebtn.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;\n"
                                         "background-color: rgb(175, 175, 175);")
        start_time = time.time()
        self.repaint()  # 刷新界面
        #  以上部分实现点击下沉的功能同时显示运行状态
        #  Get The Average number Block #
        data = self.input.toPlainText()
        aver = 0
        lis = data.split(' ')
        n = len(lis)
        for i in range(n):
            aver = aver + eval(lis[i])
        aver = aver / n
        self.result.setText("这" + str(n) + '个数的平均值为' + str(aver) + '\n')
        hs = "这" + str(n) + '个数的平均值为' + str(aver) + '\n'
        self.h += 1
        self.history.append([data, hs])  # 将历史记录存储起来
        #  Get The Average number Block #
        # Reset the average button's color
        end_time = time.time()
        if end_time - start_time <= 0.1:
            time.sleep(0.1 - (end_time - start_time))
        self.averagebtn.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;\n"
                                         "background-color: rgb(255, 254, 237);")
        #  以上代码用于根据时间决定是否需要sleep，并恢复颜色

    def extrnum(self):  # 求取最大值和最小值
        self.maxminbtn.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;\n"
                                        "background-color: rgb(175, 175, 175);")
        start_time = time.time()
        self.repaint()  # 刷新界面
        #  以上部分实现点击下沉的功能同时显示运行状态
        #  Get The Maximum And Minimum number Block #
        data = self.input.toPlainText()
        lis = data.split(' ')
        n = len(lis)
        min = 10000000000000000
        max = -10000000000000000
        for i in range(n):
            if eval(lis[i]) > max:
                max = eval(lis[i])
            if eval(lis[i]) < min:
                min = eval(lis[i])
        self.result.setText("最大值为" + str(max) + "\n最小值为" + str(min) + '\n')
        hs = "最大值为" + str(max) + "\n最小值为" + str(min) + '\n'
        self.h += 1
        self.history.append([data, hs])  # 存储该记录方便之后查找
        #  Get The Maximum And Minimum number Block #
        # Reset the maxmin button's color
        end_time = time.time()
        if end_time - start_time <= 0.1:
            time.sleep(0.1 - (end_time - start_time))
        self.maxminbtn.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;\n"
                                        "background-color: rgb(255, 254, 237);")
        #  以上代码用于根据时间决定是否需要sleep，并恢复颜色

    def midnum(self):  # 求中位数
        self.midnumbtn.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;\n"
                                        "background-color: rgb(175, 175, 175);")
        start_time = time.time()
        self.repaint()  # 刷新界面
        #  以上部分实现点击下沉的功能同时显示运行状态
        #  Get The Middle Number Block  #
        data = self.input.toPlainText()
        lis = data.split(' ')
        n = len(lis)
        for i in range(n):
            lis[i] = eval(lis[i])
        lis.sort()  # 对列表进行排序
        if (n + 1) % 2 == 0:  # 说明中位数时一个数，不需要求平均值
            midnum = lis[int((n + 1) / 2)]
            self.result.setText("这" + str(n) + '个数的中位数为' + str(midnum) + '\n')
            hs = "这" + str(n) + '个数的中位数为' + str(midnum) + '\n'
        else:
            midnum = (lis[int(n / 2) - 1] + lis[int(n / 2 + 1) - 1]) / 2
            self.result.setText("这" + str(n) + '个数的中位数为' + str(midnum) + '\n')
            hs = "这" + str(n) + '个数的中位数为' + str(midnum) + '\n'
        self.h += 1
        self.history.append([data, hs])  # 存储该记录方便之后查找
        #  Get The Middle Number Block  #
        # Reset the midnum button's color
        end_time = time.time()
        if end_time - start_time <= 0.1:
            time.sleep(0.1 - (end_time - start_time))
        self.midnumbtn.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;\n"
                                        "background-color: rgb(255, 254, 237);")
        #  以上代码用于根据时间决定是否需要sleep，并恢复颜色

    def most(self):  # 求众数的代码块
        self.mostbtn.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;\n"
                                      "background-color: rgb(175, 175, 175);")
        start_time = time.time()
        self.repaint()  # 刷新界面
        #  以上部分实现点击下沉的功能同时显示运行状态
        #  Get The Most Number Block  #
        data = self.input.toPlainText()
        lis = data.split(' ')  # 获取文本数据并按空格分隔数据然后进行处理
        n = len(lis)  # 获取输入的数据的长度
        for i in range(n):  # 将字符转换成数字
            lis[i] = eval(lis[i])
        lis.sort()  # 列表排序，方便后面进行众数的统计
        count = 1
        maxnum = 0  # 初始化统计变量
        buf = lis[0]
        lis1 = list.copy(lis)  # 用于确定需要开一个多大的结果列表来存储数据
        rlen = len(set(lis1))
        result = [0 for x in range(rlen)]  # 采用列表的形式解决有多个众数的情况
        r = 0
        for i in range(1, n):
            if lis[i] == buf:  # 与前一个数相同时，该数出现的次数加1
                count += 1
            else:
                if count > maxnum:  # 不同时，如果count大于maxnum，则说明众数是当前这个数
                    r = 0
                    result[r] = buf
                    buf = lis[i]
                    maxnum = count
                    count = 1
                else:
                    if count == maxnum:  # 有多个众数时的处理
                        r += 1
                        result[r] = buf
                        result[r] = buf
                        buf = lis[i]
                        count = 1
        # #################################这段代码用于解决最后出现的数没法通过循环记录到结果中去的问题
        if count > maxnum:
            r = 0
            result[r] = buf
            buf = lis[i]
            maxnum = count
            count = 1
        else:
            if count == maxnum:
                r += 1
                result[r] = buf
                result[r] = buf
                buf = lis[i]
                count = 1
        # #################################这段代码用于解决最后出现的数没法通过循环记录到结果中去的问题
        if r == 0:  # 说明只有一个众数
            self.result.setText("这" + str(n) + '个数据只有一个众数为' + str(result[0]) + ',一共出现了' + str(maxnum) + '次\n')
            hs = "这" + str(n) + '个数据只有一个众数为' + str(result[0]) + ',一共出现了' + str(maxnum) + '次\n'
            self.h += 1
            self.history.append([data, hs])  # 存储该记录方便之后查找
        else:  # 有多个众数时
            output = "这" + str(n) + '个数据有' + str(r + 1) + '个众数，分别为'
            for i in range(0, r + 1):
                output = output + str(result[i]) + ' '
            output = output + '，均出现了' + str(maxnum) + '次\n'
            self.result.setText(output)
            self.h += 1
            self.history.append([data, output])  # 存储该记录方便之后查找
        #  Get The Most Number Block  #
        # Reset the most button's color
        end_time = time.time()
        if end_time - start_time <= 0.1:
            time.sleep(0.1 - (end_time - start_time))
        self.mostbtn.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;\n"
                                        "background-color: rgb(255, 254, 237);")
        #  以上代码用于根据时间决定是否需要sleep，并恢复颜色

    def uncertainty(self):  # 计算不确定度的函数
        data = self.input.toPlainText()
        aver = 0
        lis = data.split(' ')
        n = len(lis)
        uncertain = 0
        self.h += 1
        self.history.append([data, uncertain])  # 存储该记录方便之后查找

    def var(self):  # 计算方差的函数
        self.variancebtn.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;\n"
                                          "background-color: rgb(175, 175, 175);")
        start_time = time.time()
        self.repaint()  # 刷新界面
        #  以上部分实现点击下沉的功能同时显示运行状态
        #  Get The Variance Number Block  #
        data = self.input.toPlainText()
        lis = data.split(' ')
        n = len(lis)
        for i in range(n):
            lis[i] = eval(lis[i])
        var = numpy.var(lis)
        self.result.setText('这' + str(n) + '个数据的\n方差为：' + str(var) + '\n标准差为：' + str(var ** 0.5))
        hs = '这' + str(n) + '个数据的\n方差为：' + str(var) + '\n标准差为：' + str(var ** 0.5)
        self.h += 1
        self.history.append([data, hs])  # 存储该记录方便之后查找
        #  Get the Variance Number Block  #
        # Reset the variance button's color
        end_time = time.time()
        if end_time - start_time <= 0.1:
            time.sleep(0.1 - (end_time - start_time))
        self.variancebtn.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;\n"
                                          "background-color: rgb(255, 254, 237);")
        #  以上代码用于根据时间决定是否需要sleep，并恢复颜色

    def ess(self):
        self.errorbtn.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;\n"
                                       "background-color: rgb(175, 175, 175);")
        start_time = time.time()
        self.repaint()  # 刷新界面
        #  以上部分实现点击下沉的功能同时显示运行状态
        #  Get The Error Block  #
        data = self.input.toPlainText()
        lis = data.split(' ')
        n = len(lis)
        for i in range(n):
            lis[i] = eval(lis[i])
        # 以上用于读取数据
        s = int(len(lis) / 2)
        standard = lis[0:s]
        actual = lis[s:]
        relate = ''
        absolute = ''
        for i in range(len(standard)):
            ac = actual[i] - standard[i]
            if standard[i] == 0:
                relate = relate + str('错误数据 ')
                absolute = absolute + str('错误数据 ')
            else:
                re = ac / standard[i] * 100
                relate = relate + str(round(re, 4)) + '% '
                absolute = absolute + str(round(ac, 4)) + ' '
        self.result.setText('这' + str(int(n / 2)) + '个数据的\n相对误差分别为：' + relate + '\n绝对误差分别为：' + absolute)
        hs = '这' + str(int(n / 2)) + '个数据的\n相对误差分别为：' + relate + '\n绝对误差分别为：' + absolute
        self.h += 1
        self.history.append([data, hs])  # 存储该记录方便之后查找
        #  Get the Error Block  #
        # Reset the error button's color
        end_time = time.time()
        if end_time - start_time <= 0.1:
            time.sleep(0.1 - (end_time - start_time))
        self.errorbtn.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;\n"
                                       "background-color: rgb(255, 254, 237);")
        #  以上代码用于根据时间决定是否需要sleep，并恢复颜色

    def his(self):  # 用来访问历史记录的函数
        self.historybtn.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;\n"
                                         "background-color: rgb(175, 175, 175);")
        start_time = time.time()
        self.repaint()  # 刷新界面
        #  以上部分实现点击下沉的功能同时显示运行状态
        #  Get The History Block  #
        if self.h == -1:  # 防止历史记录为空时出现数组越界的情况
            self.input.setText("")  # 先清空当前的内容，然后设置placeholdertext
            self.input.setPlaceholderText("历史记录为空!!!")
            self.result.setText('')
            self.result.setPlaceholderText("历史记录为空!!!")
        else:
            self.input.setText(self.history[self.h][0])
            self.result.setText(str(self.history[self.h][1]))
            self.h -= 1
            self.history.pop()
        #  Get The History Block  #
        # Reset the history button's color
        end_time = time.time()
        if end_time - start_time <= 0.1:
            time.sleep(0.1 - (end_time - start_time))
        self.historybtn.setStyleSheet("border:2px groove gray;border-radius:10px;padding:2px 4px;\n"
                                         "background-color: rgb(255, 254, 237);")
        #  以上代码用于根据时间决定是否需要sleep，并恢复颜色

# QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
# app = QApplication([])
# app.setWindowIcon(QIcon('callogo.png'))
# stats = calculatemode()
# stats.ui.show()
# app.exec_()
