from PyQt5.uic import loadUiType
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from os import path
import pandas as pd
from Ui_kongzaiQMainWindow import Ui_MainWindow
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as  #不是FigureCanvasAgg，pyqt5已经更新了
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

        #控件与函数的连接  self+ui容器+控件+动作+connect（函数名称）
        self.ui.pushButton_NoLoadCalculateAutoCalculate.clicked.connect(
            self.NoLoadCalculateAutoCalculate)
        self.ui.pushButton_NoLoadCalculateReadCSV.clicked.connect(
            self.NoLoadCalculateReadCSV)

        self.Reset()
        self.ShowResultsText()

    def NoLoadCalculateReadCSV(self):
        try:
            print("hello world! ReadCSV")
            openfile_name = ["C:/Users/fly1057/Desktop/zaoshi1.csv", 1]
            # openfile_name = QtWidgets.QFileDialog.getOpenFileName(
            #     self, '选择文件', '', '(*.csv ; *.xlsx ; *.xls )')

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
        fig1 = Figure()
        ax1f1 = fig1.add_subplot(111)
        ax1f1.pcolormesh(np.random.rand(10, 10))
        self.addmpl(fig1)

    def ShowPlot(self):
        try:
            self.rmmpl()  #这句话必须要有，不然canvas会一直增加
            fig1 = Figure()
            ax1f1 = fig1.add_subplot(111)
            #ax1f1.pcolormesh(np.random.rand(10, 10))
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
            ax1f1.legend(['Saturation curve','Air-gap line'])
            #ax1f1.plot.legend(['空载特性曲线', '气隙线'])
            self.addmpl(fig1)
        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
            print(e.__traceback__.tb_lineno)  # 发生异常所在的行数

    def UpdateTableWidgetFromDataFrame(self):
        try:
            print("begin UpdateTableWidgetFromDataFrame")
            #动态改变tablewidget的行数，保证行数是动态改变，不再要求上升阶段的点数是固定的
            #可以先在qt designer里面改一下，然后借鉴里面的写法，和利用Excel的宏一样
            #df.shape是一个tuple，第一个参数是行数，第二个参数是列数
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

    def ShowResultsText(self):
        try:
            self.ui.textBrowser.setText("hello world")
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

    def rmmpl(self):
        try:
            self.ui.verticalLayout_mpl.removeWidget(self.canvas)
            self.canvas.close()
            self.ui.verticalLayout_mpl.removeWidget(self.toolbar)
            self.toolbar.close()
        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
            print(e.__traceback__.tb_lineno)  # 发生异常所在的行数

    def NoLoadCalculateAutoCalculate(self):
        try:

            self.df = self.df.rename(columns={
                u'UAB(p.u.)': u'UAB',
                u'UFD(V)': u'UFD',
                u'IFD(A)': u'IFD'
            })
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
            # 值的到index的int值
            self.UAB_40_sq = self.UAB.head(
                self.UAB[(self.UAB > 0.45)
                         & (self.UAB < 0.6)].index.to_numpy().max())
            self.IFD_40_sq = self.IFD.head(
                self.UAB[(self.UAB > 0.45)
                         & (self.UAB < 0.6)].index.to_numpy().max())
            self.UFD_40_sq = self.UFD.head(
                self.UAB[(self.UAB > 0.45)
                         & (self.UAB < 0.6)].index.to_numpy().max())

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
            #静态放大倍数计算
            #通过abn先计算SG
            def SG_function(UAB, a, b, n):
                SG = b / a * UAB**(n - 1)
                return SG

            self.SG = SG_function(self.UAB_saturation_sq, self.a, self.b,
                                  self.n)
            print("SG = ", self.SG)

            self.IFDB = []
            self.UFDB = []
            self.KFD = []
            self.ULN = 450  # V
            self.STN = 10**6  # W
            self.Uk = 0.06

            for i in np.arange(self.IFD_saturation_sq.__len__()):
                if i == 0:
                    pass
                else:
                    self.IFDB.append(
                        (self.IFD_saturation_sq[i] /
                         (1 + self.SG[i])) / self.UAB_saturation_sq[i])
                    self.UFDB.append(
                        (self.UFD_saturation_sq[i] /
                         (1 + self.SG[i])) / self.UAB_saturation_sq[i])
                    self.KFD.append(
                        1.35 * self.ULN * self.UAB_saturation_sq[i] /
                        ((self.UFD_saturation_sq[i] + self.IFD_saturation_sq[i]
                          * self.ULN**2 / self.STN * self.Uk) /
                         (1 + self.SG[i])))

            print("IFDB = ", self.IFDB)
            print("UFDB = ", self.UFDB)
            print("KFD = ", self.KFD)
            ###############################################################################

            self.ShowPlot()
            self.ShowResultsText()

        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
            print(e.__traceback__.tb_lineno)  # 发生异常所在的行数


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Main()
    MainWindow.show()
    sys.exit(app.exec_())
