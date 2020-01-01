# coding=UTF-8
from PyQt5 import  QtWidgets
from PyQt5.QtCore import Qt
import numpy as np
import pandas as pd
from Ui_kongzaiQMainWindow import Ui_MainWindow
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as  # 不是FigureCanvasAgg，pyqt5已经更新了
    FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from scipy.optimize import least_squares, leastsq


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 在这里引入matplotlib的代码结构，首先建立figure，然后建立canvas，其中canvas是子类
        # 然后将canvas加入到之前在Qt designer中建立的layout中去，关键是要在设计时留一个空出来

        # 控件与函数的连接  self+ui容器+控件+动作+connect（函数名称）
        self.ui.pushButton_NoLoadCalculateAutoCalculate.clicked.connect(
            self.NoLoadCalculateAutoCalculate)
        self.ui.pushButton_NoLoadCalculateReadCSV.clicked.connect(
            self.NoLoadCalculateReadCSV)
        self.ui.pushButton_Reset.clicked.connect(self.Reset)
        self.ui.pushButton_AngleScopeCalculate.clicked.connect(self.AngleScopeCalculate)

        self.Reset()

    def NoLoadCalculateReadCSV(self):
        try:
            print("hello world! ReadCSV")
            #openfile_name = ["C:/Users/fly1057/Desktop/zaoshi1.csv", 1]
            openfile_name = QtWidgets.QFileDialog.getOpenFileName(
            self, '选择文件', '', '(*.csv ; *.xlsx ; *.xls )')

            # openfile_name是元组，第一个元素是路径
            if openfile_name[0] == '':
                QtWidgets.QMessageBox.information(self, "读取CSV", "已经放弃打开文件",
                                                  QtWidgets.QMessageBox.Yes)
            else:
                self.df = pd.read_csv(openfile_name[0])
                print(self.df)
            self.UpdateTableWidgetFromDataFrame()
        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
            print(e.__traceback__.tb_lineno)  # 发生异常所在的行数

    def Reset(self):
        try:
            #如果函数A内部有异常机制，那么可以随意在别的函数B里面调用A，不会影响函数B的流程
            #也就是说在self.rmmpl()内有异常机制，调用这个函数如果出现了错误也只会报异常
            #还会在Reset里面继续走下去
            self.rmmpl() 
            fig1 = Figure(tight_layout=True)
            ax1f1 = fig1.add_subplot(111)
            ax1f1.pcolormesh(np.random.rand(10, 10))
            self.addmpl(fig1)

        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
            print(e.__traceback__.tb_lineno)  # 发生异常所在的行数

    def ShowPlot(self):
        try:
            self.rmmpl()  # 这句话必须要有，不然canvas会一直增加
            fig1 = Figure(tight_layout=True)
            # 由于未采用pyplot而采用的figure，那么实际上ax1f1是一个包含axes的汇总的集合
            # 这个可以在debug窗口看出来，那么可以ax1f1.axes来使用axes的所有属性，如果有
            # 些出入的话，比如plt.axes.xlabel可以用ax1f1.axes.set_xlabel来实现，总之可以在
            # debug窗口确认这个ax1f1是怎样的class，然后猜大概的属性
            ax1f1 = fig1.add_subplot(111)

            # 所画曲线
            ax1f1.plot(self.IFD_saturation_sq,
                       self.UAB_saturation_sq,
                       color='k',
                       marker='*')
            ax1f1.plot(self.IFD_air_sq, self.UAB_air_sq, color='k', marker='')
            ax1f1.plot(self.IFD_air_100_vertical_sq,
                       self.UAB_air_100_vertical_sq,
                       ':',
                       color='k')
            ax1f1.plot(self.IFD_air_120_vertical_sq,
                       self.UAB_air_120_vertical_sq,
                       ':',
                       color='k')
            ax1f1.plot(self.IFD_sat_100_vertical_sq,
                       self.UAB_sat_100_vertical_sq,
                       ':',
                       color='k')
            ax1f1.plot(self.IFD_sat_120_vertical_sq,
                       self.UAB_sat_120_vertical_sq,
                       ':',
                       color='k')
            # legend
            ax1f1.legend(['Saturation curve', 'Air-gap line'])
            #ax1f1.plot.legend(['空载特性曲线', '气隙线'])
            # 标注IFDB、a、b、n、SG1.0、SG1.2
            ax1f1.text(self.IFD_air_100_value,
                       1.05,
                       'IFDB1.0=' +
                       str(round(float(self.IFD_air_100_value), 1)) + 'A',
                       horizontalalignment='center',
                       verticalalignment='center')

            ax1f1.text(self.IFD_air_120_value,
                       1.25,
                       'IFDB1.2=' +
                       str(round(float(self.IFD_air_120_value), 1)) + 'A',
                       horizontalalignment='center',
                       verticalalignment='center')

            ax1f1.text(self.IFD_sat_100_value,
                       0.5,
                       'IFD01.0=' +
                       str(round(float(self.IFD_sat_100_value), 1)) + 'A',
                       horizontalalignment='center',
                       verticalalignment='center')

            ax1f1.text(self.IFD_sat_120_value,
                       0.5,
                       'IFD01.2=' +
                       str(round(float(self.IFD_sat_120_value), 1)) + 'A',
                       horizontalalignment='center',
                       verticalalignment='center')

            ax1f1.text(self.IFD_air_100_value / 5.0,
                       1,
                       'a=' + str(round(self.a, 3)),
                       horizontalalignment='center',
                       verticalalignment='center')

            ax1f1.text(self.IFD_air_100_value / 5,
                       0.9,
                       'b=' + str(round(self.b, 3)),
                       horizontalalignment='center',
                       verticalalignment='center')

            ax1f1.text(self.IFD_air_100_value / 5,
                       0.8,
                       'n=' + str(round(self.n, 3)),
                       horizontalalignment='center',
                       verticalalignment='center')

            ax1f1.text(self.IFD_air_100_value / 5,
                       0.7,
                       'SG1.0=' + str(round(self.SG100, 3)),
                       horizontalalignment='center',
                       verticalalignment='center')

            ax1f1.text(self.IFD_air_100_value / 5,
                       0.6,
                       'SG1.2=' + str(round(self.SG120, 3)),
                       horizontalalignment='center',
                       verticalalignment='center')

            ax1f1.text(self.IFD_air_100_value / 2,
                       1,
                       'IFDB=' + str(round(self.IFDB, 1)) + "A",
                       horizontalalignment='center',
                       verticalalignment='center')

            ax1f1.text(self.IFD_air_100_value / 2,
                       0.9,
                       'UFDB=' + str(round(self.UFDB, 1)) + "V",
                       horizontalalignment='center',
                       verticalalignment='center')

            ax1f1.text(self.IFD_air_100_value / 2,
                       0.8,
                       'KFD=' + str(round(self.KFD, 2)),
                       horizontalalignment='center',
                       verticalalignment='center')

            # 设定图像大小，像素，去除边框
            ax1f1.axes.spines['top'].set_visible(False)  # 去掉上边框
            ax1f1.axes.spines['right'].set_visible(False)  # 去掉右边框

            # 坐标图框架
            ax1f1.axes.set_xlabel("Ifd /A")
            ax1f1.axes.set_ylabel("Ug /p.u.")
            ax1f1.axes.set_xlim([0, self.IFD_saturation_sq.max()])
            ax1f1.axes.set_ylim([0, 1.3])

            self.addmpl(fig1)
        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
            print(e.__traceback__.tb_lineno)  # 发生异常所在的行数

    def UpdateTableWidgetFromDataFrame(self):
        try:
            print("begin UpdateTableWidgetFromDataFrame")
            # 动态改变tablewidget的行数，保证行数是动态改变，不再要求上升阶段的点数是固定的
            # 可以先在qt designer里面改一下，然后借鉴里面的写法，和利用Excel的宏一样
            # df.shape是一个tuple，第一个参数是行数，第二个参数是列数
            self.ui.tableWidget_RawData.setRowCount(self.df.shape[0])
            self.ui.tableWidget_RawData.setColumnCount(self.df.shape[1])

            for i in np.arange(self.df.shape[0]):
                for j in np.arange(self.df.shape[1]):
                    self.ui.tableWidget_RawData.setItem(
                        i, j,
                        QtWidgets.QTableWidgetItem(str(
                            self.df.iloc[i, j])))  # 这里必须采用str强制转换
            print("end UpdateTableWidgetFromDataFrame")
        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
            print(e.__traceback__.tb_lineno)  # 发生异常所在的行数

    def UpdateSelfFromPanel(self):
        try:
            print("begin UpdateSelfFromPanel")
            self.LinearScope = float(self.ui.lineEdit_LinearScope.text())
            self.STN = float(self.ui.lineEdit_STN.text())*1000
            self.Uk = float(self.ui.lineEdit_Uk.text())
            self.ULN = float(self.ui.lineEdit_ULN.text())

            self.Rising1Ut = float(self.ui.lineEdit_Rising1Ut.text())
            self.Rising1Ufd = float(self.ui.lineEdit_Rising1Ufd.text())
            self.Rising1Ifd = float(self.ui.lineEdit_Rising1Ifd.text())
            self.Rising2Ut = float(self.ui.lineEdit_Rising2Ut.text())
            self.Rising2Ufd = float(self.ui.lineEdit_Rising2Ufd.text())
            self.Rising2Ifd = float(self.ui.lineEdit_Rising2Ifd.text())

            self.Falling1Ut = float(self.ui.lineEdit_Falling1Ut.text())
            self.Falling1Ufd = float(self.ui.lineEdit_Falling1Ufd.text())
            self.Falling1Ifd = float(self.ui.lineEdit_Falling1Ifd.text())
            self.Falling2Ut = float(self.ui.lineEdit_Falling2Ut.text())
            self.Falling2Ufd = float(self.ui.lineEdit_Falling2Ufd.text())
            self.Falling2Ifd = float(self.ui.lineEdit_Falling2Ifd.text())

            print("end UpdateSelfFromPanel")
        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
            print(e.__traceback__.tb_lineno)  # 发生异常所在的行数

    def UpdatePanelFromSelf(self):
        try:
            print("begin UpdatePanelFromSelf")
            self.ui.lineEdit_XcReal.setText(str(self.XcReal))
            self.ui.lineEdit_Xcpu.setText(str(self.Xcpu))
            self.ui.lineEdit_Rising1Angle.setText(str(self.Rising1Angle))
            self.ui.lineEdit_Rising2Angle.setText(str(self.Rising2Angle))
            self.ui.lineEdit_Falling1Angle.setText(str(self.Falling1Angle))
            self.ui.lineEdit_Falling2Angle.setText(str(self.Falling2Angle))
            self.ui.lineEdit_AngleAVGmax.setText(str(self.AngleAVGmax))
            self.ui.lineEdit_AngleAVGmin.setText(str(self.AngleAVGmin))           
            self.ui.lineEdit_IFDB.setText(str(self.IFDB))
            self.ui.lineEdit_UFDB.setText(str(self.UFDB))
            self.ui.lineEdit_KFD.setText(str(self.KFD))
            self.ui.lineEdit_Umax.setText(str(self.Umax))
            self.ui.lineEdit_Umin.setText(str(self.Umin))
            self.ui.lineEdit_a.setText(str(self.a))
            self.ui.lineEdit_b.setText(str(self.b))
            self.ui.lineEdit_n.setText(str(self.n))
            self.ui.lineEdit_SG100.setText(str(self.SG100))
            self.ui.lineEdit_SG120.setText(str(self.SG120))

            print("end UpdatePanelFromSelf")
        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
            print(e.__traceback__.tb_lineno)  # 发生异常所在的行数

    def ShowResultsText(self):
        try:
            self.ui.textBrowser.setText("IFDB=" + str(round(self.IFDB,4)) +"\n" \
                                        "UFDB=" + str(round(self.UFDB,4)) + "\n" \
                                        "KFD=" + str(round(self.KFD,4)) + "\n" \
                                        "a=" + str(self.a) + "\n" \
                                        "b=" + str(round(self.b,4)) + "\n" \
                                        "n=" + str(round(self.n,4)) + "\n" \
                                        "SG1.0=" + str(round(self.SG100,4)) + "\n" \
                                        "SG1.2=" + str(round(self.SG120, 4)) + "\n"
                                        "Rising1Angle=" + str(round(self.Rising1Angle, 4)) + "\n" \
                                        "Rising2Angle=" + str(round(self.Rising2Angle, 4)) + "\n" \
                                        "Falling1Angle=" + str(round(self.Falling1Angle, 4)) + "\n" \
                                        "Falling2Angle=" + str(round(self.Falling2Angle, 4)) + "\n" \
                                        "αAVGmin=" + str(round(self.AngleAVGmin, 4)) + "\n" \
                                        "αAVGmax=" + str(round(self.AngleAVGmax, 4)) + "\n" \
                                        "Umax=" + str(round(self.Umax, 4)) + "\n"\
                                        "Umin=" + str(round(self.Umin, 4)) + "\n"\
                                        )

        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
            print(e.__traceback__.tb_lineno)  # 发生异常所在的行数

    def addmpl(self, fig):
        try:
            self.canvas = FigureCanvas(fig)
            self.ui.verticalLayout_mpl.addWidget(self.canvas)
            self.canvas.draw()
            self.toolbar = NavigationToolbar(self.canvas,
                                             self,
                                             coordinates=True)
            self.ui.verticalLayout_mpl.addWidget(self.toolbar)
        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
            print(e.__traceback__.tb_lineno)  # 发生异常所在的行数

    def rmmpl(self):#如果函数A内部有异常机制，那么可以随意在别的函数B里面调用A，不会影响函数B的流程
        try:
            self.ui.verticalLayout_mpl.removeWidget(self.canvas)
            self.canvas.close()
            self.ui.verticalLayout_mpl.removeWidget(self.toolbar)
            self.toolbar.close()
        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
            print(e.__traceback__.tb_lineno)  # 发生异常所在的行数
            print("Exception caused by deleting figure Firstly! ")

    def NoLoadCalculateAutoCalculate(self):
        try:
            self.UpdateSelfFromPanel()
            # self.df = self.df.rename(columns={
            #     u'UAB(p.u.)': u'UAB',
            #     u'UFD(V)': u'UFD',
            #     u'IFD(A)': u'IFD'
            # })
            self.df.columns = ['UAB', 'UFD', 'IFD']
            # 截取上升段的数据，注意需要找到最大值index后加1
            self.UAB = self.df.UAB[0:(self.df.UAB.idxmax() + 1)]
            self.IFD = self.df.IFD[0:(self.df.UAB.idxmax() + 1)]
            self.UFD = self.df.UFD[0:(self.df.UAB.idxmax() + 1)]

            # 首先做一个判断，UAB是百分数还是标幺值，最终转换为标幺值
            if self.UAB.max() > 50:
                self.UAB = self.UAB / 100

            # 取IFD和UAB前面0.4额定电压的段作为气隙线的拟合基本数据
            # 通过UAB[(UAB>0.35)&(UAB<0.45)].index.get_values()得到index的array
            # 由于head需要int型变量，那么array是不行的，取个巧，取这个array的最大
            # 值得到index的int值
            tempindex = self.UAB[(self.UAB > self.LinearScope)& (self.UAB < 1.2*self.LinearScope)].index.to_numpy().max()
            self.UAB_40_sq = self.UAB.head(tempindex)
            self.IFD_40_sq = self.IFD.head(tempindex)
            self.UFD_40_sq = self.UFD.head(tempindex)

            ###############################################################################
            # 气隙线残差函数

            def residuals_airgap_line_IFD(p):
                k, h = p
                return self.UAB_40_sq - (k * self.IFD_40_sq + h)

            def residuals_airgap_line_UFD(p):
                k, h = p
                return self.UAB_40_sq - (k * self.UFD_40_sq + h)

            self.res_IFD = leastsq(residuals_airgap_line_IFD, [1, 0])
            self.k_IFD, self.h_IFD = self.res_IFD[0]
            print("k_IFD = ", self.k_IFD, "h_IFD = ", self.h_IFD, "\n")

            self.res_UFD = leastsq(residuals_airgap_line_UFD, [1, 0])
            self.k_UFD, self.h_UFD = self.res_UFD[0]
            print("k_UFD = ", self.k_UFD, "h_UFD = ", self.h_UFD, "\n")

            # 对UAB减去残压，然后对IFD也同样进行筛选
            self.UAB_sq_IFD = self.UAB.head(
                self.UAB[(self.UAB > self.h_IFD)].index.to_numpy().max())
            self.IFD_sq_IFD = self.IFD.head(
                self.UAB[(self.UAB > self.h_IFD)].index.to_numpy().max())

            self.UAB_sq_UFD = self.UAB.head(
                self.UAB[(self.UAB > self.h_UFD)].index.to_numpy().max())
            self.IFD_sq_UFD = self.IFD.head(
                self.UAB[(self.UAB > self.h_UFD)].index.to_numpy().max())

            self.h_IFD = 0
            self.h_UFD = 0
            # 得到气隙线
            self.UAB_air_sq = np.linspace(0, 1.3, 131)  # 得到消除残压后的实际发电机本体的气隙线
            self.IFD_air_sq = (self.UAB_air_sq) / self.k_IFD
            self.UFD_air_sq = (self.UAB_air_sq) / self.k_UFD

            # 计算气隙线上的点
            self.IFD_air_100_value = (1.0) / self.k_IFD  # 1.0UN对应的励磁电流
            self.IFD_air_120_value = (1.2) / self.k_IFD  # 1.2UN对应的励磁电流

            self.UFD_air_100_value = (1.0) / self.k_UFD  # 1.0UN对应的励磁电压
            self.UFD_air_120_value = (1.2) / self.k_UFD  # 1.2UN对应的励磁电压

            # 形成气隙线上1.0及1.2倍UN的下垂线
            self.UAB_air_100_vertical_sq = np.linspace(0, 1.0, 141)  # 注意点数要都一致
            self.IFD_air_100_vertical_sq = np.linspace(self.IFD_air_100_value,
                                                       self.IFD_air_100_value,
                                                       141)
            self.UAB_air_120_vertical_sq = np.linspace(0, 1.2, 141)
            self.IFD_air_120_vertical_sq = np.linspace(self.IFD_air_120_value,
                                                       self.IFD_air_120_value,
                                                       141)

            ###############################################################################

            # 计算空载特性曲线上的点
            # 根据PSASP说明书中空载曲线的形式为 IFD=a*UAB+b*UAB^n，a取为1，则实际未知参数只有b、n。

            # 空载特性曲线残差函数

            def residuals_saturation_curve(p):
                b, n = p
                # 标幺化后进行的计算，否则误差会很大,UAB为实际上的电压，需要减去h
                return self.IFD / self.IFD_air_100_value - (self.UAB + b *
                                                            (self.UAB)**n)

            # 进行计算前的初始化条件
            self.lb = np.array([0.01, 0.01])
            self.ub = np.array([10.0, 15.0])
            self.x0 = [0.1, 7]
            self.res2 = least_squares(residuals_saturation_curve,
                                      self.x0,
                                      ftol=0.001,
                                      bounds=(self.lb, self.ub),
                                      method='trf')
            self.b, self.n = self.res2.x
            self.a = 1

            #print ("a=",1," b=",b," n=",n,"\n")
            #print ("cost=",res2.cost)

            # 得到空载特性曲线
            self.UAB_saturation_sq = np.linspace(0, 1.22, 141)
            self.IFD_saturation_sq = (self.UAB_saturation_sq +
                                      self.b * self.UAB_saturation_sq**self.n
                                      ) * self.IFD_air_100_value
            self.UFD_saturation_sq = (self.UAB_saturation_sq +
                                      self.b * self.UAB_saturation_sq**self.n
                                      ) * self.UFD_air_100_value

            # 计算空载特性曲线上的点
            self.IFD_sat_100_value = (
                1 +
                self.b * 1**self.n) * self.IFD_air_100_value  # 1.0UN对应的励磁电流
            self.IFD_sat_120_value = (
                1.2 +
                self.b * 1.2**self.n) * self.IFD_air_100_value  # 1.2UN对应的励磁电流

            # 形成空载特性曲线上1.0及1.2倍UN的下垂线
            self.UAB_sat_100_vertical_sq = np.linspace(0, 1.0, 141)  # 注意点数要都一致
            self.IFD_sat_100_vertical_sq = np.linspace(self.IFD_sat_100_value,
                                                       self.IFD_sat_100_value,
                                                       141)
            self.UAB_sat_120_vertical_sq = np.linspace(0, 1.2, 141)
            self.IFD_sat_120_vertical_sq = np.linspace(self.IFD_sat_120_value,
                                                       self.IFD_sat_120_value,
                                                       141)

            self.SG100 = (self.IFD_sat_100_value -
                          self.IFD_air_100_value) / self.IFD_air_100_value
            self.SG120 = (self.IFD_sat_120_value -
                          self.IFD_air_120_value) / self.IFD_air_120_value

            # 按照公式再算一遍a b n，在这里使用IFD0的实际值，而在excel中使用的约等值，因此有误差
            self.a = 1
            self.b = self.SG100
            self.n = 1 + np.log(self.SG120 / self.SG100) / np.log(1.2)

            ###############################################################################
            # 静态放大倍数计算
            # 通过abn先计算SG
            def SG_function(UAB, a, b, n):
                SG = b / a * UAB**(n - 1)
                return SG

            self.SG = SG_function(self.UAB_saturation_sq, self.a, self.b,
                                  self.n)
            print("SG = ", self.SG)

            self.IFDBseq = []
            self.UFDBseq = []
            self.KFDseq = []

            self.XcReal = self.ULN ** 2 / self.STN * self.Uk

            for i in np.arange(self.IFD_saturation_sq.__len__()):
                if i == 0:
                    pass
                else:
                    self.IFDBseq.append(
                        (self.IFD_saturation_sq[i] /
                         (1 + self.SG[i])) / self.UAB_saturation_sq[i])
                    self.UFDBseq.append(
                        (self.UFD_saturation_sq[i] /
                         (1 + self.SG[i])) / self.UAB_saturation_sq[i])
                    self.KFDseq.append(
                        1.35 * self.ULN * self.UAB_saturation_sq[i] /
                        ((self.UFD_saturation_sq[i] + self.IFD_saturation_sq[i]
                          * self.XcReal) /
                         (1 + self.SG[i])))

            print("IFDB = ", self.IFDBseq)
            print("UFDB = ", self.UFDBseq)
            print("KFD = ", self.KFDseq)

            self.UFDB = self.UFDBseq[0]
            self.IFDB = self.IFDBseq[0]
            self.KFD = self.KFDseq[0]
            self.Xcpu = self.XcReal / (self.UFDB / self.IFDB)

            self.AngleScopeCalculate()

            ###############################################################################

            self.ShowPlot()
            self.UpdatePanelFromSelf()
            self.ShowResultsText()

        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
            print(e.__traceback__.tb_lineno)  # 发生异常所在的行数

    def AngleScopeCalculate(self):
        try:
            #根据panel更新self
            self.UpdateSelfFromPanel()

            self.Rising1Angle = 180/np.pi*np.arccos((self.Rising1Ufd + self.Rising1Ifd * self.XcReal)/(1.35*self.ULN*self.Rising1Ut ))
            self.Rising2Angle = 180/np.pi*np.arccos((self.Rising2Ufd + self.Rising2Ifd * self.XcReal)/(1.35*self.ULN*self.Rising2Ut ))

            self.Falling1Angle = 180/np.pi*np.arccos((self.Falling1Ufd + self.Falling1Ifd * self.XcReal)/(1.35*self.ULN*self.Falling1Ut ))
            self.Falling2Angle = 180/np.pi*np.arccos((self.Falling2Ufd + self.Falling2Ifd * self.XcReal)/(1.35*self.ULN*self.Falling2Ut ))
            
            self.AngleAVGmin = np.average(
                [self.Rising1Angle, self.Rising2Angle])
            self.AngleAVGmax = np.average(
                [self.Falling1Angle, self.Falling2Angle])

            self.Umax = 1.35*self.ULN * \
                np.cos(self.AngleAVGmin/180*np.pi) / self.UFDB
            self.Umin = 1.35*self.ULN * \
                np.cos(self.AngleAVGmax / 180 * np.pi) / self.UFDB

            #根据self更新panel和text
            self.UpdatePanelFromSelf()
            self.ShowResultsText()
        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
            print(e.__traceback__.tb_lineno)  # 发生异常所在的行数

if __name__ == "__main__":
    import sys
    QtWidgets.QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Main()
    MainWindow.show()
    # MainWindow.showMaximized()
    sys.exit(app.exec_())
