# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\setup\github\noloadcharacteristic\kongzaiQMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1347, 726)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_NoLoadCalculate = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_NoLoadCalculate.setGeometry(QtCore.QRect(10, 10, 151, 191))
        self.groupBox_NoLoadCalculate.setObjectName("groupBox_NoLoadCalculate")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_NoLoadCalculate)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 22, 132, 165))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.lineEdit_NoLoadCalculateLinearScope = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_NoLoadCalculateLinearScope.setObjectName("lineEdit_NoLoadCalculateLinearScope")
        self.horizontalLayout_4.addWidget(self.lineEdit_NoLoadCalculateLinearScope)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.pushButton_NoLoadCalculateAutoCalculate = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_NoLoadCalculateAutoCalculate.setObjectName("pushButton_NoLoadCalculateAutoCalculate")
        self.verticalLayout_4.addWidget(self.pushButton_NoLoadCalculateAutoCalculate)
        self.pushButton_NoLoadCalculateReadCSV = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_NoLoadCalculateReadCSV.setObjectName("pushButton_NoLoadCalculateReadCSV")
        self.verticalLayout_4.addWidget(self.pushButton_NoLoadCalculateReadCSV)
        self.pushButton_NoLoadCalculateSaveCSV = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_NoLoadCalculateSaveCSV.setObjectName("pushButton_NoLoadCalculateSaveCSV")
        self.verticalLayout_4.addWidget(self.pushButton_NoLoadCalculateSaveCSV)
        self.pushButton_Reset = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_Reset.setObjectName("pushButton_Reset")
        self.verticalLayout_4.addWidget(self.pushButton_Reset)
        self.groupBox_LimiterCalculate = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_LimiterCalculate.setGeometry(QtCore.QRect(850, 10, 211, 171))
        self.groupBox_LimiterCalculate.setObjectName("groupBox_LimiterCalculate")
        self.layoutWidget_2 = QtWidgets.QWidget(self.groupBox_LimiterCalculate)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 20, 187, 135))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_17 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 0, 0, 1, 1)
        self.lineEdit_LimiterCalculateIFDB = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_LimiterCalculateIFDB.setObjectName("lineEdit_LimiterCalculateIFDB")
        self.gridLayout_2.addWidget(self.lineEdit_LimiterCalculateIFDB, 0, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 0, 2, 1, 1)
        self.lineEdit_LimiterCalculatea = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_LimiterCalculatea.setObjectName("lineEdit_LimiterCalculatea")
        self.gridLayout_2.addWidget(self.lineEdit_LimiterCalculatea, 0, 3, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 1, 0, 1, 1)
        self.lineEdit_LimiterCalculateUFDB = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_LimiterCalculateUFDB.setObjectName("lineEdit_LimiterCalculateUFDB")
        self.gridLayout_2.addWidget(self.lineEdit_LimiterCalculateUFDB, 1, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 1, 2, 1, 1)
        self.lineEdit_LimiterCalculateb = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_LimiterCalculateb.setObjectName("lineEdit_LimiterCalculateb")
        self.gridLayout_2.addWidget(self.lineEdit_LimiterCalculateb, 1, 3, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_29.setObjectName("label_29")
        self.gridLayout_2.addWidget(self.label_29, 2, 0, 1, 1)
        self.lineEdit_LimiterCalculateKFD = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_LimiterCalculateKFD.setObjectName("lineEdit_LimiterCalculateKFD")
        self.gridLayout_2.addWidget(self.lineEdit_LimiterCalculateKFD, 2, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 2, 2, 1, 1)
        self.lineEdit_LimiterCalculaten = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_LimiterCalculaten.setObjectName("lineEdit_LimiterCalculaten")
        self.gridLayout_2.addWidget(self.lineEdit_LimiterCalculaten, 2, 3, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_30.setObjectName("label_30")
        self.gridLayout_2.addWidget(self.label_30, 3, 0, 1, 1)
        self.lineEdit_LimiterCalculateUmax = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_LimiterCalculateUmax.setObjectName("lineEdit_LimiterCalculateUmax")
        self.gridLayout_2.addWidget(self.lineEdit_LimiterCalculateUmax, 3, 1, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_28.setObjectName("label_28")
        self.gridLayout_2.addWidget(self.label_28, 3, 2, 1, 1)
        self.lineEdit_LimiterCalculateSG10 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_LimiterCalculateSG10.setObjectName("lineEdit_LimiterCalculateSG10")
        self.gridLayout_2.addWidget(self.lineEdit_LimiterCalculateSG10, 3, 3, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_27.setObjectName("label_27")
        self.gridLayout_2.addWidget(self.label_27, 4, 0, 1, 1)
        self.lineEdit_LimiterCalculateUmin = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_LimiterCalculateUmin.setObjectName("lineEdit_LimiterCalculateUmin")
        self.gridLayout_2.addWidget(self.lineEdit_LimiterCalculateUmin, 4, 1, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_31.setObjectName("label_31")
        self.gridLayout_2.addWidget(self.label_31, 4, 2, 1, 1)
        self.lineEdit_LimiterCalculateSG12 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_LimiterCalculateSG12.setObjectName("lineEdit_LimiterCalculateSG12")
        self.gridLayout_2.addWidget(self.lineEdit_LimiterCalculateSG12, 4, 3, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 210, 761, 421))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_mpl = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_mpl.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_mpl.setObjectName("verticalLayout_mpl")
        self.groupBox_ExciterTransferCalculate = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_ExciterTransferCalculate.setGeometry(QtCore.QRect(160, 10, 201, 171))
        self.groupBox_ExciterTransferCalculate.setObjectName("groupBox_ExciterTransferCalculate")
        self.layoutWidget_3 = QtWidgets.QWidget(self.groupBox_ExciterTransferCalculate)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 26, 181, 137))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit_ExciterTransferCalculateSTN = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_ExciterTransferCalculateSTN.setObjectName("lineEdit_ExciterTransferCalculateSTN")
        self.verticalLayout_3.addWidget(self.lineEdit_ExciterTransferCalculateSTN)
        self.lineEdit_ExciterTransferCalculateUk = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_ExciterTransferCalculateUk.setObjectName("lineEdit_ExciterTransferCalculateUk")
        self.verticalLayout_3.addWidget(self.lineEdit_ExciterTransferCalculateUk)
        self.lineEdit_ExciterTransferCalculateULN = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_ExciterTransferCalculateULN.setObjectName("lineEdit_ExciterTransferCalculateULN")
        self.verticalLayout_3.addWidget(self.lineEdit_ExciterTransferCalculateULN)
        self.lineEdit_ExciterTransferCalculateXcReal = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_ExciterTransferCalculateXcReal.setObjectName("lineEdit_ExciterTransferCalculateXcReal")
        self.verticalLayout_3.addWidget(self.lineEdit_ExciterTransferCalculateXcReal)
        self.lineEdit_ExciterTransferCalculateXcpu = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_ExciterTransferCalculateXcpu.setObjectName("lineEdit_ExciterTransferCalculateXcpu")
        self.verticalLayout_3.addWidget(self.lineEdit_ExciterTransferCalculateXcpu)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.tableWidget_RawData = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_RawData.setGeometry(QtCore.QRect(1100, 20, 221, 611))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_RawData.sizePolicy().hasHeightForWidth())
        self.tableWidget_RawData.setSizePolicy(sizePolicy)
        self.tableWidget_RawData.setMinimumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.tableWidget_RawData.setFont(font)
        self.tableWidget_RawData.setStyleSheet("")
        self.tableWidget_RawData.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_RawData.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_RawData.setAutoScroll(False)
        self.tableWidget_RawData.setRowCount(1)
        self.tableWidget_RawData.setObjectName("tableWidget_RawData")
        self.tableWidget_RawData.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_RawData.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_RawData.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_RawData.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_RawData.setHorizontalHeaderItem(2, item)
        self.tableWidget_RawData.horizontalHeader().setDefaultSectionSize(67)
        self.tableWidget_RawData.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_RawData.verticalHeader().setVisible(True)
        self.tableWidget_RawData.verticalHeader().setDefaultSectionSize(22)
        self.tableWidget_RawData.verticalHeader().setMinimumSectionSize(7)
        self.groupBox_ControlAngleCalculate = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_ControlAngleCalculate.setGeometry(QtCore.QRect(370, 10, 481, 181))
        self.groupBox_ControlAngleCalculate.setAcceptDrops(False)
        self.groupBox_ControlAngleCalculate.setFlat(False)
        self.groupBox_ControlAngleCalculate.setCheckable(False)
        self.groupBox_ControlAngleCalculate.setObjectName("groupBox_ControlAngleCalculate")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_ControlAngleCalculate)
        self.layoutWidget1.setGeometry(QtCore.QRect(12, 40, 133, 141))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_5.addWidget(self.label_15)
        self.pushButton_ControlAngleCalculate = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_ControlAngleCalculate.setObjectName("pushButton_ControlAngleCalculate")
        self.verticalLayout_5.addWidget(self.pushButton_ControlAngleCalculate)
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox_ControlAngleCalculate)
        self.layoutWidget2.setGeometry(QtCore.QRect(150, 20, 323, 157))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 0, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 0, 3, 1, 1)
        self.lineEdit_ControlAngleCalculateRisingFirstPointUt = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_ControlAngleCalculateRisingFirstPointUt.setObjectName("lineEdit_ControlAngleCalculateRisingFirstPointUt")
        self.gridLayout.addWidget(self.lineEdit_ControlAngleCalculateRisingFirstPointUt, 1, 0, 1, 1)
        self.ControlAngleCalculateRisingSecondPointUt = QtWidgets.QLineEdit(self.layoutWidget2)
        self.ControlAngleCalculateRisingSecondPointUt.setObjectName("ControlAngleCalculateRisingSecondPointUt")
        self.gridLayout.addWidget(self.ControlAngleCalculateRisingSecondPointUt, 1, 1, 1, 1)
        self.ControlAngleCalculateRisingThirdPointUt_2 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.ControlAngleCalculateRisingThirdPointUt_2.setObjectName("ControlAngleCalculateRisingThirdPointUt_2")
        self.gridLayout.addWidget(self.ControlAngleCalculateRisingThirdPointUt_2, 1, 2, 1, 1)
        self.ControlAngleCalculateRisingFourthPointUt = QtWidgets.QLineEdit(self.layoutWidget2)
        self.ControlAngleCalculateRisingFourthPointUt.setObjectName("ControlAngleCalculateRisingFourthPointUt")
        self.gridLayout.addWidget(self.ControlAngleCalculateRisingFourthPointUt, 1, 3, 1, 1)
        self.lineEdit_ControlAngleCalculateRisingFirstPointUfd = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_ControlAngleCalculateRisingFirstPointUfd.setObjectName("lineEdit_ControlAngleCalculateRisingFirstPointUfd")
        self.gridLayout.addWidget(self.lineEdit_ControlAngleCalculateRisingFirstPointUfd, 2, 0, 1, 1)
        self.lineEdit_ControlAngleCalculateRisingSecondPointUfd_2 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_ControlAngleCalculateRisingSecondPointUfd_2.setObjectName("lineEdit_ControlAngleCalculateRisingSecondPointUfd_2")
        self.gridLayout.addWidget(self.lineEdit_ControlAngleCalculateRisingSecondPointUfd_2, 2, 1, 1, 1)
        self.lineEdit_ControlAngleCalculateRisingThirdPointUfd_3 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_ControlAngleCalculateRisingThirdPointUfd_3.setObjectName("lineEdit_ControlAngleCalculateRisingThirdPointUfd_3")
        self.gridLayout.addWidget(self.lineEdit_ControlAngleCalculateRisingThirdPointUfd_3, 2, 2, 1, 1)
        self.lineEdit_ControlAngleCalculateRisingFourthPointUfd_4 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_ControlAngleCalculateRisingFourthPointUfd_4.setObjectName("lineEdit_ControlAngleCalculateRisingFourthPointUfd_4")
        self.gridLayout.addWidget(self.lineEdit_ControlAngleCalculateRisingFourthPointUfd_4, 2, 3, 1, 1)
        self.lineEdit_ControlAngleCalculateRisingFirstPointIfd = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_ControlAngleCalculateRisingFirstPointIfd.setObjectName("lineEdit_ControlAngleCalculateRisingFirstPointIfd")
        self.gridLayout.addWidget(self.lineEdit_ControlAngleCalculateRisingFirstPointIfd, 3, 0, 1, 1)
        self.lineEdit_ControlAngleCalculateRisingSecondPointIfd_2 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_ControlAngleCalculateRisingSecondPointIfd_2.setObjectName("lineEdit_ControlAngleCalculateRisingSecondPointIfd_2")
        self.gridLayout.addWidget(self.lineEdit_ControlAngleCalculateRisingSecondPointIfd_2, 3, 1, 1, 1)
        self.lineEdit_ControlAngleCalculateRisingThirdPointIfd_3 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_ControlAngleCalculateRisingThirdPointIfd_3.setObjectName("lineEdit_ControlAngleCalculateRisingThirdPointIfd_3")
        self.gridLayout.addWidget(self.lineEdit_ControlAngleCalculateRisingThirdPointIfd_3, 3, 2, 1, 1)
        self.lineEdit_ControlAngleCalculateRisingFourthPointIfd_4 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_ControlAngleCalculateRisingFourthPointIfd_4.setObjectName("lineEdit_ControlAngleCalculateRisingFourthPointIfd_4")
        self.gridLayout.addWidget(self.lineEdit_ControlAngleCalculateRisingFourthPointIfd_4, 3, 3, 1, 1)
        self.lineEdit_ControlAngleCalculateRisingFirstPointAngle = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_ControlAngleCalculateRisingFirstPointAngle.setObjectName("lineEdit_ControlAngleCalculateRisingFirstPointAngle")
        self.gridLayout.addWidget(self.lineEdit_ControlAngleCalculateRisingFirstPointAngle, 4, 0, 1, 1)
        self.lineEdit_ControlAngleCalculateRisingSecondPointAngle = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_ControlAngleCalculateRisingSecondPointAngle.setObjectName("lineEdit_ControlAngleCalculateRisingSecondPointAngle")
        self.gridLayout.addWidget(self.lineEdit_ControlAngleCalculateRisingSecondPointAngle, 4, 1, 1, 1)
        self.lineEdit_ControlAngleCalculateRisingThirdPointAngle = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_ControlAngleCalculateRisingThirdPointAngle.setObjectName("lineEdit_ControlAngleCalculateRisingThirdPointAngle")
        self.gridLayout.addWidget(self.lineEdit_ControlAngleCalculateRisingThirdPointAngle, 4, 2, 1, 1)
        self.lineEdit_ControlAngleCalculateRisingFourthPointAngle = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_ControlAngleCalculateRisingFourthPointAngle.setObjectName("lineEdit_ControlAngleCalculateRisingFourthPointAngle")
        self.gridLayout.addWidget(self.lineEdit_ControlAngleCalculateRisingFourthPointAngle, 4, 3, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 5, 0, 1, 1)
        self.lineEdit_ControlAngleCalculateAVGmax = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_ControlAngleCalculateAVGmax.setObjectName("lineEdit_ControlAngleCalculateAVGmax")
        self.gridLayout.addWidget(self.lineEdit_ControlAngleCalculateAVGmax, 5, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 5, 2, 1, 1)
        self.lineEdit_ControlAngleCalculateAVGmin = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_ControlAngleCalculateAVGmin.setObjectName("lineEdit_ControlAngleCalculateAVGmin")
        self.gridLayout.addWidget(self.lineEdit_ControlAngleCalculateAVGmin, 5, 3, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(870, 190, 191, 441))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1347, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_NoLoadCalculate.setTitle(_translate("MainWindow", "空载特性计算"))
        self.label.setText(_translate("MainWindow", "线性段选择"))
        self.lineEdit_NoLoadCalculateLinearScope.setText(_translate("MainWindow", "0.4"))
        self.pushButton_NoLoadCalculateAutoCalculate.setText(_translate("MainWindow", "自动计算绘图"))
        self.pushButton_NoLoadCalculateReadCSV.setText(_translate("MainWindow", "读取CSV"))
        self.pushButton_NoLoadCalculateSaveCSV.setText(_translate("MainWindow", "保存CSV"))
        self.pushButton_Reset.setText(_translate("MainWindow", "复位"))
        self.groupBox_LimiterCalculate.setTitle(_translate("MainWindow", "限幅值计算结果"))
        self.label_17.setText(_translate("MainWindow", "IFDB"))
        self.label_19.setText(_translate("MainWindow", "a"))
        self.label_18.setText(_translate("MainWindow", "UFDB"))
        self.label_20.setText(_translate("MainWindow", "b"))
        self.label_29.setText(_translate("MainWindow", "KFD"))
        self.label_21.setText(_translate("MainWindow", "n"))
        self.label_30.setText(_translate("MainWindow", "Umax"))
        self.label_28.setText(_translate("MainWindow", "SG1.0"))
        self.label_27.setText(_translate("MainWindow", "Umin"))
        self.label_31.setText(_translate("MainWindow", "SG1.2"))
        self.groupBox_ExciterTransferCalculate.setTitle(_translate("MainWindow", "励磁变参数计算"))
        self.label_2.setText(_translate("MainWindow", "STN（kW）"))
        self.label_3.setText(_translate("MainWindow", "Uk（p.u.）"))
        self.label_4.setText(_translate("MainWindow", "阳极电压ULN（V）"))
        self.label_5.setText(_translate("MainWindow", "Xc（有名）"))
        self.label_6.setText(_translate("MainWindow", "Xc（p.u.）"))
        self.lineEdit_ExciterTransferCalculateSTN.setText(_translate("MainWindow", "1000"))
        self.lineEdit_ExciterTransferCalculateUk.setText(_translate("MainWindow", "0.06"))
        self.lineEdit_ExciterTransferCalculateULN.setText(_translate("MainWindow", "450"))
        self.tableWidget_RawData.setSortingEnabled(True)
        item = self.tableWidget_RawData.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_RawData.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "UAB(pu)"))
        item = self.tableWidget_RawData.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "IFD (A)"))
        item = self.tableWidget_RawData.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "UFD (V)"))
        self.groupBox_ControlAngleCalculate.setTitle(_translate("MainWindow", "控制角范围计算（最大最小角）"))
        self.label_7.setText(_translate("MainWindow", "机端电压（p.u.）"))
        self.label_8.setText(_translate("MainWindow", "励磁电压（V）"))
        self.label_9.setText(_translate("MainWindow", "励磁电流（A）"))
        self.label_15.setText(_translate("MainWindow", "αmin/αmax（°）"))
        self.pushButton_ControlAngleCalculate.setText(_translate("MainWindow", "角度范围计算"))
        self.label_10.setText(_translate("MainWindow", "上升第一点"))
        self.label_11.setText(_translate("MainWindow", "上升第二点"))
        self.label_12.setText(_translate("MainWindow", "下降第一点"))
        self.label_13.setText(_translate("MainWindow", "下降第二点"))
        self.label_14.setText(_translate("MainWindow", "αAVGmax"))
        self.label_16.setText(_translate("MainWindow", "αAVGmin"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

