# coding=UTF-8
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
import numpy as np
from numpy.lib.shape_base import column_stack
import pandas as pd
from Ui_kongzaiQMainWindow import Ui_MainWindow

import matplotlib
matplotlib.use("QT5Agg") #声明使用pyqt5
#matplotlib.figure 模块提供了顶层的Artist（图中所有可见的元素都是Artist的子类）
from matplotlib.figure import Figure 
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg , #不是FigureCanvasAgg，pyqt5已经更新了
    NavigationToolbar2QT) 
from scipy.optimize import least_squares, leastsq

from docx import Document
from docx.shared import Pt
from docx.shared import Inches
from docx.oxml.ns import qn

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 在这里引入matplotlib的代码结构，首先建立figure，然后建立canvas，其中canvas是子类
        # 然后将canvas加入到之前在Qt designer中建立的layout中去，关键是要在设计时留一个空出来
        # 控件与函数的连接  self+ui容器+控件+动作+connect（函数名称）
        self.ui.pushButton_NoLoadCalculateAutoCalculate.clicked.connect(self.NoLoadCalculateAutoCalculate)
        self.ui.pushButton_NoLoadCalculateReadCSV.clicked.connect(self.NoLoadCalculateReadCSV)
        self.ui.pushButton_NoLoadCalculateSaveCSV.clicked.connect(self.NoLoadCalculateSaveCSV)
        self.ui.pushButton_Reset.clicked.connect(self.Reset)
        self.ui.pushButton_AngleScopeCalculate.clicked.connect(self.AngleScopeCalculate)
        self.ui.pushButton_NoLoadCalculateSaveDOCX.clicked.connect(self.NoLoadCalculateSaveDOCX)
        #self.Reset()

    def NoLoadCalculateReadCSV(self):
        try:
            print("hello world! ReadCSV")
            #openfile_name = ["C:/Users/ll/Desktop/zaoshi1.csv", 1]
            openfile_name = QtWidgets.QFileDialog.getOpenFileName(
                self, '选择文件', '', '(*.csv ; *.xlsx ; *.xls )')

            # openfile_name是元组，第一个元素是路径
            if openfile_name[0] == '':
                QtWidgets.QMessageBox.information(self, "读取CSV", "已经放弃打开文件",
                                                  QtWidgets.QMessageBox.Yes)
            else:
                self.df = pd.read_csv(openfile_name[0])
                print(self.df)
            self.UpdatePanelFromDataFrame()
            self.UpdateSelfFromDataFrame()
        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
            print(e.__traceback__.tb_lineno)  # 发生异常所在的行数
    
    def NoLoadCalculateSaveCSV(self):
        try:
            print("hello world! SaveCSV")

            self.UpdateDataFrameFromPanel()
            openfile_name = QtWidgets.QFileDialog.getSaveFileName(
                self, '选择文件', '', '(*.csv ; *.xlsx ; *.xls )')

            # openfile_name是元组，第一个元素是路径
            if openfile_name[0] == '':
                QtWidgets.QMessageBox.information(self, "保存CSV", "已经放弃保存文件",
                                                  QtWidgets.QMessageBox.Yes)
            else:
                self.df.to_csv(openfile_name[0],index = False)

        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
            print(e.__traceback__.tb_lineno)  # 发生异常所在的行数    
    
    def NoLoadCalculateSaveDOCX(self):
        try:
            print("hello world! SaveCSV")

            self.UpdateDataFrameFromPanel()                     
            # 新建空白文档
            doc1 = Document()
            # 新增文档标题
            doc1.add_heading('如何使用 Python 创建 Word',0)
            openfile_name = QtWidgets.QFileDialog.getSaveFileName(
                self, '选择文件', '', '(*.docx )')

            # openfile_name是元组，第一个元素是路径
            if openfile_name[0] == '':
                QtWidgets.QMessageBox.information(self, "保存DOCX", "已经放弃保存文件",
                                                  QtWidgets.QMessageBox.Yes)
            else:
                # 保存文件
                doc1.save('word1.docx')

        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
            print(e.__traceback__.tb_lineno)  # 发生异常所在的行数    

    def Reset(self):
        try:
            data = {
                    "parameters": ['STN','LinearScale','Uk','ULN','XcReal','XcRealEqual','XcpuEqual','IFDN','UFDN','IFDB_std','UFDB_std','KFD_std','UFDB_LL','KFD_LL','a','b','n','SG100','SG120','Rising1Ut','Rising1Ufd','Rising1Ifd','Rising2Ut','Rising2Ufd','Rising2Ifd','Falling1Ut','Falling1Ufd','Falling1Ifd','Falling2Ut','Falling2Ufd','Falling2Ifd','Rising1Angle','Rising2Angle','Falling1Angle','Falling2Angle','AngleAVGmin','AngleAVGmax','Umax','Umin'],
                    "value":[3270,	0.45,	0.065,	743,	0.01097,	0.01047,	0.08112,	2756,	356,	913.119,	117.95,	8.50402,	97.8861,	9.33464,	1,	0.129,	8.12358,	0.129,	0.4727,	0.72469,	669.08,	1194.8,	0.77703,	713.9,	1553.6,	0.88462,	-671.84,	256.13,	0.87319,	-662.7,	136.61,	20.3344,	20.4711,	138.9497,	139.0253,	20.4027,	138.9875,	7.97052,	-6.4168],
                    "UAB": [0.6675,	0.6645,	10.273,	15.525,	20.031,	25.143,	30.077,	35.122,	39.893,	45.493,	50.508,	55.407,	60.459,	65.167,	70.69,	75.275,	81.406,	86.352,	90.864,	95.453,	100.55,	105.48,	105.51,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN],
                    "UFD": [0.8488,	0.8785,	15.694,	16.789,	20.657,	26.013,	30.409,	35.525,	40.178,	45.48,	50.405,	55.131,	60.198,	64.948,	70.971,	75.771,	83.003,	89.068,	94.779,	102.43,	111.62,	123.12,	123.3,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN],
                    "IFD": [0.1468,	0.2666,	96.592,	139.06,	180.43,	227.25,	271.11,	316.37,	360.6,	411.27,	456.86,	501.18,	549.27,	594.55,	650.28,	693.56,	764.38,	824.47,	878.97,	943.32,	1032.3,	1137.7,	1138.4,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN,np.NaN]
                    }
            self.df = pd.DataFrame(data)
            self.UpdatePanelFromDataFrame()
            self.UpdateSelfFromDataFrame()

            # 如果函数A内部有异常机制，那么可以随意在别的函数B里面调用A，不会影响函数B的流程
            # 也就是说在self.rmmpl()内有异常机制，调用这个函数如果出现了错误也只会报异常
            # 还会在Reset里面继续走下去
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
                       self.UAB_saturation_sq, color='k', marker='*')

            ax1f1.plot(self.IFD_air_sq, 
                       self.UAB_air_sq, color='k', marker='')

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

            ax1f1.text(self.IFD_air_100_value / 5.5,
                       1,
                       'a=' + str(round(self.a, 3)),
                       horizontalalignment='center',
                       verticalalignment='center')

            ax1f1.text(self.IFD_air_100_value / 5.5,
                       0.9,
                       'b=' + str(round(self.b, 3)),
                       horizontalalignment='center',
                       verticalalignment='center')

            ax1f1.text(self.IFD_air_100_value / 5.5,
                       0.8,
                       'n=' + str(round(self.n, 3)),
                       horizontalalignment='center',
                       verticalalignment='center')

            ax1f1.text(self.IFD_air_100_value / 5.5,
                       0.7,
                       'SG1.0=' + str(round(self.SG100, 3)),
                       horizontalalignment='center',
                       verticalalignment='center')

            ax1f1.text(self.IFD_air_100_value / 5.5,
                       0.6,
                       'SG1.2=' + str(round(self.SG120, 3)),
                       horizontalalignment='center',
                       verticalalignment='center')

            ax1f1.text(self.IFD_air_100_value / 2,
                       1,
                       'IFDB_std=' + str(round(self.IFDB_std, 1)) + "A",
                       horizontalalignment='center',
                       verticalalignment='center')

            ax1f1.text(self.IFD_air_100_value / 2,
                       0.9,
                       'UFDB_std=' + str(round(self.UFDB_std, 1)) + "V",
                       horizontalalignment='center',
                       verticalalignment='center')

            ax1f1.text(self.IFD_air_100_value / 2,
                       0.8,
                       'KFD_std=' + str(round(self.KFD_std, 2)),
                       horizontalalignment='center',
                       verticalalignment='center')

            #ax1f1.text(self.IFD_air_100_value / 2,
            #           0.7,
            #           'KFD_LL=' + str(round(self.KFD_LL, 2)),
            #           horizontalalignment='center',
            #           verticalalignment='center')

            # 设定图像大小，像素，去除边框
            ax1f1.axes.spines['top'].set_visible(False)  # 去掉上边框
            ax1f1.axes.spines['right'].set_visible(False)  # 去掉右边框

            # 坐标图框架
            ax1f1.axes.set_xlabel("Ifd /A")
            ax1f1.axes.set_ylabel("Ug /p.u.")
            ax1f1.axes.set_xlim([0, self.IFD_saturation_sq.max()])
            ax1f1.axes.set_ylim([0, 1.3])

            #先增加再删，再增加
            self.addmpl(fig1)


            
        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
            print(e.__traceback__.tb_lineno)  # 发生异常所在的行数

    def UpdatePanelFromDataFrame(self):
        try:
            print("begin UpdatePanelFromDataFrame")
            # 动态改变tablewidget的行数，保证行数是动态改变，不再要求上升阶段的点数是固定的
            # 可以先在qt designer里面改一下，然后借鉴里面的写法，和利用Excel的宏一样
            # df.shape是一个tuple，第一个参数是行数，第二个参数是列数

            for i  in  np.arange(len(self.df['value'])):
                temp = self.findChild(QtWidgets.QLineEdit,"lineEdit_"+self.df["parameters"].iloc[i])
                temp.setText(str(self.df['value'].iloc[i]))

            #构造在 panel上构造 tableWidget
            self.UAB = self.df["UAB"].dropna()
            self.UFD = self.df["UFD"].dropna()
            self.IFD = self.df["IFD"].dropna()
            temp = pd.DataFrame({'UAB':self.UAB,'UFD':self.UFD,'IFD':self.IFD})
            #构造 tableWidget
            self.ui.tableWidget_RawData.setRowCount(temp.shape[0])
            self.ui.tableWidget_RawData.setColumnCount(temp.shape[1])

            for i in np.arange(temp.shape[0]):
                for j in np.arange(temp.shape[1]):
                    self.ui.tableWidget_RawData.setItem(i, j,QtWidgets.QTableWidgetItem(str(temp.iloc[i, j])))  # 这里必须采用str强制转换
            
            print("end UpdatePanelFromDataFrame")

        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
            print(e.__traceback__.tb_lineno)  # 发生异常所在的行数
    
    def UpdateDataFrameFromPanel(self):
        try:
            print("begin UpdateDataFrameFromPanel")

            #保证csv表中的名称和ui中的名称一致，这样就好通过循环索引
            #将value中的变量值赋值给LineEdit对应的变量。不能使用iloc这种相对索引，应使用loc[i,string]这种绝对索引
            for i  in  np.arange(len(self.df['value'])):
                temp = self.findChild(QtWidgets.QLineEdit,"lineEdit_"+self.df.loc[i,"parameters"])
                self.df.loc[i,'value'] = float(temp.text())
            
            #更新df中的UAB，UFD ,IFD
            rowcount = self.ui.tableWidget_RawData.rowCount()
            columncount = self.ui.tableWidget_RawData.columnCount()
            # 动态改变tablewidget的行数，保证行数是动态改变，不再要求上升阶段的点数是固定的
            # 可以先在qt designer里面改一下，然后借鉴里面的写法，和利用Excel的宏一样
            # df.shape是一个tuple，第一个参数是行数，第二个参数是列数

            #方法1
            for i in np.arange(rowcount):
                self.df.loc[i,"UAB"] =  float(self.ui.tableWidget_RawData.item(i,0).text())
                self.df.loc[i,"UFD"] =  float(self.ui.tableWidget_RawData.item(i,1).text())
                self.df.loc[i,"IFD"] =  float(self.ui.tableWidget_RawData.item(i,2).text())

            #方法2
            #for i in np.arange(rowcount):
            #    for j in np.arange(columncount-2):
            #        self.df.iloc[i,2+j] =  float(self.ui.tableWidget_RawData.item(i,j).text())

            print("end UpdateDataFrameFromPanel")

        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
            print(e.__traceback__.tb_lineno)  # 发生异常所在的行数ss 

    def UpdateSelfFromDataFrame(self):
        try:
            print("begin UpdateSelfFromDataFrame")

            temp = [self.df.loc[i,'value'] for i in np.arange(len(self.df['value']))]
            temp =[temp,self.df['UAB'].dropna(),self.df['UFD'].dropna(),self.df['IFD'].dropna()]
            [[self.STN,self.LinearScale,self.Uk,self.ULN,self.XcReal,self.XcRealEqual,self.XcpuEqual,\
            self.IFDN,self.UFDN,self.IFDB_std,self.UFDB_std,self.KFD_std,self.UFDB_LL,self.KFD_LL,\
            self.a,self.b,self.n,self.SG100,self.SG120,\
            self.Rising1Ut,self.Rising1Ufd,self.Rising1Ifd,\
            self.Rising2Ut,self.Rising2Ufd,self.Rising2Ifd,\
            self.Falling1Ut,self.Falling1Ufd,self.Falling1Ifd,\
            self.Falling2Ut,self.Falling2Ufd,self.Falling2Ifd,\
            self.Rising1Angle,self.Rising2Angle,self.Falling1Angle,self.Falling2Angle,\
            self.AngleAVGmin,self.AngleAVGmax,self.Umax,self.Umin],self.UAB,self.UFD,self.IFD] = temp
            
            print("end UpdateSelfFromDataFrame")
        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
            print(e.__traceback__.tb_lineno)  # 发生异常所在的行数

    def UpdateDataFrameFromSelf(self):
        try:
            print("begin UpdateDataFrameFromSelf")

            temp = [[self.STN,self.LinearScale,self.Uk,self.ULN,self.XcReal,self.XcRealEqual,self.XcpuEqual,\
            self.IFDN,self.UFDN,self.IFDB_std,self.UFDB_std,self.KFD_std,self.UFDB_LL,self.KFD_LL,\
            self.a,self.b,self.n,self.SG100,self.SG120,\
            self.Rising1Ut,self.Rising1Ufd,self.Rising1Ifd,\
            self.Rising2Ut,self.Rising2Ufd,self.Rising2Ifd,\
            self.Falling1Ut,self.Falling1Ufd,self.Falling1Ifd,\
            self.Falling2Ut,self.Falling2Ufd,self.Falling2Ifd,\
            self.Rising1Angle,self.Rising2Angle,self.Falling1Angle,self.Falling2Angle,\
            self.AngleAVGmin,self.AngleAVGmax,self.Umax,self.Umin],self.UAB,self.UFD,self.IFD]
            [self.df['value'],self.df['UAB'],self.df['UFD'],self.df['IFD'] ]= temp

            print("end UpdateDataFrameFromSelf")
        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
            print(e.__traceback__.tb_lineno)  # 发生异常所在的行数

    def ShowResultsText(self):
        try:
            self.ui.textBrowser.setText("IFDB_std=" + str(round(self.IFDB_std, 4)) + "\n"
                                        "UFDB_std=" + str(round(self.UFDB_std, 4)) + "\n"
                                        "KFD_std=" + str(round(self.KFD_std, 4)) + "\n"
                                        "UFDB_LL=" + str(round(self.UFDB_LL, 4)) + "\n"
                                        "KFD_LL=" + str(round(self.KFD_LL, 4)) + "\n"
                                        "a=" + str(self.a) + "\n"
                                        "b=" + str(round(self.b, 4)) + "\n"
                                        "n=" + str(round(self.n, 4)) + "\n"
                                        "SG1.0=" +
                                        str(round(self.SG100, 4)) + "\n"
                                        "SG1.2=" +
                                        str(round(self.SG120, 4)) + "\n"
                                        "Rising1Angle=" +
                                        str(round(self.Rising1Angle, 4)) + "\n"
                                        "Rising2Angle=" +
                                        str(round(self.Rising2Angle, 4)) + "\n"
                                        "Falling1Angle=" +
                                        str(round(self.Falling1Angle, 4)) + "\n"
                                        "Falling2Angle=" +
                                        str(round(self.Falling2Angle, 4)) + "\n"
                                        "αAVGmin=" +
                                        str(round(self.AngleAVGmin, 4)) + "\n"
                                        "αAVGmax=" +
                                        str(round(self.AngleAVGmax, 4)) + "\n"
                                        "Umax=" +
                                        str(round(self.Umax, 4)) + "\n"
                                        "Umin=" +
                                        str(round(self.Umin, 4)) + "\n"
                                        )

        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
            print(e.__traceback__.tb_lineno)  # 发生异常所在的行数

    def addmpl(self, fig): 
        try:
            self.canvas = FigureCanvasQTAgg(fig)
            self.ui.verticalLayout_mpl.addWidget(self.canvas)
            self.canvas.draw()
            self.toolbar = NavigationToolbar2QT(self.canvas,self,coordinates=True)
            self.ui.verticalLayout_mpl.addWidget(self.toolbar)
        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
            print(e.__traceback__.tb_lineno)  # 发生异常所在的行数

    def rmmpl(self):  # 如果函数A内部有异常机制，那么可以随意在别的函数B里面调用A，不会影响函数B的流程
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
            #1 pick up the linear data ，that is UAB and Ifd，such as UAB <0.4 ，could be choosen according HMI ,
            # and then pick up the same scale of Ifd and Ufd according to the index 
            #2 linear fitting using the picked data ,then got the line UAB = k*IFD+h, UAB is in p.u.,IFD is in real
            # then  UAB -h to get the new UAB 
            # 舍弃h理由是，残差电压并非由励磁电流引起，因此需要舍弃，空载特性应该是以Ifd从0开始.
            #3  calculate the basevalue of IFD . By UAB(1.0)/k ,we got the IFDB , according the same method we got the UFDB
            #4  calculate IFDB1.2 ,UFDB1.2 according to the airline 
            #5  nolinear fitting using all data to  get  a,b,n. This time we also using the data of UAB in step 2
            #6  calculate the IFD01.0 and IFD01.2 according to the a,b,n
            #7  calculate the KFD .   

            self.UpdateDataFrameFromPanel()
            self.UpdateSelfFromDataFrame() 
            #（1） 选取前部分数据进行计算
            # 首先做一个判断，UAB是百分数还是标幺值，最终转换为标幺值
            if self.UAB.max() > 50:
                self.UAB = self.UAB / 100

            # 取IFD和UAB前面0.4额定电压的段作为气隙线的拟合基本数据
            # 通过UAB[(UAB>0.35)&(UAB<0.45)].index.get_values()得到index的array
            # 由于head需要int型变量，那么array是不行的，取个巧，取这个array的最大
            # 值得到index的int值
            tempindex = self.UAB[(self.UAB > self.LinearScale) & (self.UAB < 1.2*self.LinearScale)].index.to_numpy().max()
            self.UAB_40_sq = self.UAB.head(tempindex)
            self.IFD_40_sq = self.IFD.head(tempindex)
            self.UFD_40_sq = self.UFD.head(tempindex)

            ###############################################################################
            # （2）线性拟合
            def residuals_airgap_line_IFD(p):
                k, h = p
                return self.UAB_40_sq - (k * self.IFD_40_sq + h)
            def residuals_airgap_line_UFD(p):
                k, h = p
                return self.UAB_40_sq - (k * self.UFD_40_sq + h)

            self.res_IFD = leastsq(residuals_airgap_line_IFD, [1, 0])
            self.k_IFD, self.h_IFD = self.res_IFD[0]
            self.UAB = self.UAB - self.h_IFD  # clear zero margin
            print("k_IFD = ", self.k_IFD, "h_IFD = ", self.h_IFD, "\n")

            self.res_UFD = leastsq(residuals_airgap_line_UFD, [1, 0])
            self.k_UFD, self.h_UFD = self.res_UFD[0]
            print("k_UFD = ", self.k_UFD, "h_UFD = ", self.h_UFD, "\n")

            # 得到气隙线
            self.UAB_air_sq = np.linspace(0, 1.3, 131)  # 得到消除残压后的实际发电机本体的气隙线
            #直接指定截距为0的原因是：剩磁并不是由励磁电流产生的，而是由于别的原因产生的，
            #而空载特性是励磁电流与机端电压之间的关系，这种关系是从原点开始的，所以不用
            #考虑剩磁的影响，直接将截距置0
            self.h_IFD = 0
            self.h_UFD = 0
            self.IFD_air_sq = (self.UAB_air_sq) / self.k_IFD
            self.UFD_air_sq = (self.UAB_air_sq) / self.k_UFD

            # 计算气隙线上的点
            self.IFD_air_100_value = (1.0) / self.k_IFD  # 1.0UN对应的励磁电流
            self.IFD_air_120_value = (1.2) / self.k_IFD  # 1.2UN对应的励磁电流

            self.UFD_air_100_value = (1.0) / self.k_UFD  # 1.0UN对应的励磁电压
            self.UFD_air_120_value = (1.2) / self.k_UFD  # 1.2UN对应的励磁电压

            # 形成气隙线上1.0及1.2倍UN的下垂线数据
            #linspace有一个很好的特性是，如果第一和第二参数是一致的，那么将会生成一系列相同的点
            self.UAB_air_100_vertical_sq = np.linspace(0, 1.0, 141)  # 注意点数要都一致
            self.IFD_air_100_vertical_sq = np.linspace(self.IFD_air_100_value,self.IFD_air_100_value,141)
            self.UAB_air_120_vertical_sq = np.linspace(0, 1.2, 141)
            self.IFD_air_120_vertical_sq = np.linspace(self.IFD_air_120_value,self.IFD_air_120_value,141)
            ###############################################################################

            # 计算空载特性曲线上的点
            # 根据PSASP说明书中空载曲线的形式为 IFD=a*UAB+b*UAB^n，a取为1，则实际未知参数只有b、n。

            # 空载特性曲线残差函数
            def residuals_saturation_curve(p):
                b, n = p
            # 需要对IFD进行标幺化后再进行计算，否则误差会很大，UAB为实际上的电压，需要减去h
                return   self.IFD/self.IFD_air_100_value - (self.UAB+b*(self.UAB)**n)

            # 进行计算前的初始化条件
            self.lb = np.array([0.01, 0.01])
            self.ub = np.array([10.0, 15.0])
            self.x0 = [0.1, 8]
            self.res2 = least_squares(residuals_saturation_curve,
                                      self.x0,
                                      ftol=0.001,
                                      bounds=(self.lb, self.ub),
                                      method='trf')
            self.b, self.n = self.res2.x
            self.a = 1

            # 得到空载饱和曲线
            self.UAB_saturation_sq = np.linspace(0, 1.22, 141)
            self.IFD_saturation_sq = (self.UAB_saturation_sq + self.b * self.UAB_saturation_sq**self.n) * self.IFD_air_100_value
            self.UFD_saturation_sq = (self.UAB_saturation_sq + self.b * self.UAB_saturation_sq**self.n) * self.UFD_air_100_value

            # 计算空载饱和曲线上的点
            self.IFD_sat_100_value = (1 + self.b * 1**self.n) * self.IFD_air_100_value  # 1.0UN对应的励磁电流
            self.IFD_sat_120_value = (1.2 +self.b * 1.2**self.n) * self.IFD_air_100_value  # 1.2UN对应的励磁电流

            # 形成空载特性曲线上1.0及1.2倍UN的下垂线
            self.UAB_sat_100_vertical_sq = np.linspace(0, 1.0, 141)  # 注意点数要都一致
            self.IFD_sat_100_vertical_sq = np.linspace(self.IFD_sat_100_value,self.IFD_sat_100_value,141)
            self.UAB_sat_120_vertical_sq = np.linspace(0, 1.2, 141)
            self.IFD_sat_120_vertical_sq = np.linspace(self.IFD_sat_120_value,self.IFD_sat_120_value,141)

            self.SG100 = (self.IFD_sat_100_value - self.IFD_air_100_value) / self.IFD_air_100_value
            self.SG120 = (self.IFD_sat_120_value - self.IFD_air_120_value) / self.IFD_air_120_value

            ## 按照公式再算一遍a b n，在这里使用IFD0的实际值，而在excel中使用的约等值，因此有误差
            #self.a = 1
            #self.b = self.SG100
            #self.n = 1 + np.log(self.SG120 / self.SG100) / np.log(1.2)

            ###############################################################################
            # KFD 静态放大倍数计算
            # 通过abn先计算SG
            def SG_function(UAB, a, b, n):
                SG = b / a * UAB**(n - 1)
                return SG

            self.SG = SG_function(self.UAB_saturation_sq,self.a, self.b, self.n)
            print("SG = ", self.SG)

            #考察每个饱和点对应的气隙线上的点
            self.IFDB_seq = []
            self.UFDB_seq = []
            self.KFD_seq = []

            self.XcReal = self.ULN**2/self.STN/10**3*self.Uk  #有名值，不包含了换相导致的系数3/pi
            self.XcRealEqual = self.XcReal*3.0/np.pi  #有名值，包含了换相导致的系数3/pi

            for i in np.arange(self.IFD_saturation_sq.__len__()):
                if i == 0:
                    pass
                else:
                    # (self.IFD_saturation_sq[i]/ (1 + self.SG[i])) we got the linear Ifd , because 
                    # UAB = Ifd/ IFDB ,so Ifd / UAB we got IFDB , so as to UFDB
                    self.IFDB_seq.append((self.IFD_saturation_sq[i]/ (1 + self.SG[i]))/ self.UAB_saturation_sq[i])
                    self.UFDB_seq.append((self.UFD_saturation_sq[i]/ (1 + self.SG[i]))/ self.UAB_saturation_sq[i])
                    self.KFD_seq.append(1.35*self.ULN*self.UAB_saturation_sq[i]/((self.UFD_saturation_sq[i]+self.IFD_saturation_sq[i]*self.XcRealEqual)/(1 + self.SG[i])))

            print("IFDB = ", self.IFDB_seq)
            print("UFDB = ", self.UFDB_seq)
            print("KFD = ", self.KFD_seq)
            
            self.IFDB_std = self.IFDB_seq[0]
            self.UFDB_std =  self.IFDB_std*self.UFDN/self.IFDN
            self.KFD_std = 1.35*self.ULN/self.UFDB_std
            self.UFDB_LL = self.UFDB_seq[0]
            self.KFD_LL = self.KFD_seq[0]
            self.XcpuEqual = self.XcRealEqual / (self.UFDB_std / self.IFDB_std)

            ###############################################################################
            #计算后，更新是第一要务
            self.UpdateDataFrameFromSelf()
            self.UpdatePanelFromDataFrame()
            self.AngleScopeCalculate()  #不能放在更新之前，这个函数要根据panel更新self，如果放前面就错了         
            self.ShowPlot()
            self.ShowResultsText()

        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
            print(e.__traceback__.tb_lineno)  # 发生异常所在的行数

    def AngleScopeCalculate(self):
        try:
            # 根据panel更新self
            self.UpdateDataFrameFromPanel()
            self.UpdateSelfFromDataFrame()

            self.Rising1Angle = 180/np.pi * \
                np.arccos((self.Rising1Ufd + self.Rising1Ifd *self.XcRealEqual)/(1.35*self.ULN*self.Rising1Ut))
            self.Rising2Angle = 180/np.pi * \
                np.arccos((self.Rising2Ufd + self.Rising2Ifd *self.XcRealEqual)/(1.35*self.ULN*self.Rising2Ut))

            self.Falling1Angle = 180/np.pi * \
                np.arccos((self.Falling1Ufd + self.Falling1Ifd *self.XcRealEqual)/(1.35*self.ULN*self.Falling1Ut))
            self.Falling2Angle = 180/np.pi * \
                np.arccos((self.Falling2Ufd + self.Falling2Ifd *self.XcRealEqual)/(1.35*self.ULN*self.Falling2Ut))

            self.AngleAVGmin = np.average(
                [self.Rising1Angle, self.Rising2Angle])
            self.AngleAVGmax = np.average(
                [self.Falling1Angle, self.Falling2Angle])

            self.Umax = 1.35*self.ULN * \
                np.cos(self.AngleAVGmin/180*np.pi) / self.UFDB_std
            self.Umin = 1.35*self.ULN * \
                np.cos(self.AngleAVGmax/180*np.pi) / self.UFDB_std

            # 根据self更新panel和text
            self.UpdateDataFrameFromSelf()
            self.UpdatePanelFromDataFrame()
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
