# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/fly1057/lili_projects/python_projects/noloadcharacteristic/kongzaiQMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1261, 830)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_NoLoadCalculate = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_NoLoadCalculate.setGeometry(QtCore.QRect(0, 10, 131, 191))
        self.groupBox_NoLoadCalculate.setObjectName("groupBox_NoLoadCalculate")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_NoLoadCalculate)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 22, 111, 165))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.lineEdit_LinearScope = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_LinearScope.setMaxLength(7)
        self.lineEdit_LinearScope.setObjectName("lineEdit_LinearScope")
        self.horizontalLayout_4.addWidget(self.lineEdit_LinearScope)
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
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
<<<<<<< HEAD
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 250, 681, 461))
=======
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 290, 681, 481))
>>>>>>> 2e5ede1e888c9679f1570c07ed3f20a8da8bf05f
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_mpl = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_mpl.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_mpl.setObjectName("verticalLayout_mpl")
        self.groupBox_ExciterTransferCalculate = QtWidgets.QGroupBox(self.centralwidget)
<<<<<<< HEAD
        self.groupBox_ExciterTransferCalculate.setGeometry(QtCore.QRect(130, 10, 191, 191))
        self.groupBox_ExciterTransferCalculate.setObjectName("groupBox_ExciterTransferCalculate")
        self.layoutWidget_3 = QtWidgets.QWidget(self.groupBox_ExciterTransferCalculate)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 20, 171, 158))
=======
        self.groupBox_ExciterTransferCalculate.setGeometry(QtCore.QRect(120, 10, 191, 251))
        self.groupBox_ExciterTransferCalculate.setObjectName("groupBox_ExciterTransferCalculate")
        self.layoutWidget_3 = QtWidgets.QWidget(self.groupBox_ExciterTransferCalculate)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 20, 171, 221))
>>>>>>> 2e5ede1e888c9679f1570c07ed3f20a8da8bf05f
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
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_2.addWidget(self.label_22)
        self.pushButton_ExciterTranformerCalculate = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_ExciterTranformerCalculate.setObjectName("pushButton_ExciterTranformerCalculate")
        self.verticalLayout_2.addWidget(self.pushButton_ExciterTranformerCalculate)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit_STN = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_STN.setMaxLength(7)
        self.lineEdit_STN.setObjectName("lineEdit_STN")
        self.verticalLayout_3.addWidget(self.lineEdit_STN)
        self.lineEdit_Uk = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_Uk.setMaxLength(7)
        self.lineEdit_Uk.setObjectName("lineEdit_Uk")
        self.verticalLayout_3.addWidget(self.lineEdit_Uk)
        self.lineEdit_ULN = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_ULN.setMaxLength(7)
        self.lineEdit_ULN.setObjectName("lineEdit_ULN")
        self.verticalLayout_3.addWidget(self.lineEdit_ULN)
        self.lineEdit_XcReal = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_XcReal.setMaxLength(7)
        self.lineEdit_XcReal.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.lineEdit_XcReal.setObjectName("lineEdit_XcReal")
        self.verticalLayout_3.addWidget(self.lineEdit_XcReal)
        self.lineEdit_XcRealEqual = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_XcRealEqual.setMaxLength(7)
        self.lineEdit_XcRealEqual.setObjectName("lineEdit_XcRealEqual")
        self.verticalLayout_3.addWidget(self.lineEdit_XcRealEqual)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_3.addWidget(self.lineEdit_2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.tableWidget_RawData = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_RawData.setGeometry(QtCore.QRect(1020, 0, 221, 771))
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
<<<<<<< HEAD
        self.groupBox_ControlAngleCalculate.setGeometry(QtCore.QRect(570, 10, 441, 241))
=======
        self.groupBox_ControlAngleCalculate.setGeometry(QtCore.QRect(570, 10, 441, 251))
>>>>>>> 2e5ede1e888c9679f1570c07ed3f20a8da8bf05f
        self.groupBox_ControlAngleCalculate.setAcceptDrops(False)
        self.groupBox_ControlAngleCalculate.setFlat(False)
        self.groupBox_ControlAngleCalculate.setCheckable(False)
        self.groupBox_ControlAngleCalculate.setObjectName("groupBox_ControlAngleCalculate")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_ControlAngleCalculate)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 50, 104, 131))
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
        self.pushButton_AngleScopeCalculate = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_AngleScopeCalculate.setObjectName("pushButton_AngleScopeCalculate")
        self.verticalLayout_5.addWidget(self.pushButton_AngleScopeCalculate)
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox_ControlAngleCalculate)
<<<<<<< HEAD
        self.layoutWidget2.setGeometry(QtCore.QRect(120, 20, 311, 212))
=======
        self.layoutWidget2.setGeometry(QtCore.QRect(120, 30, 311, 212))
>>>>>>> 2e5ede1e888c9679f1570c07ed3f20a8da8bf05f
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
        self.lineEdit_Rising1Ut = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_Rising1Ut.setMaxLength(7)
        self.lineEdit_Rising1Ut.setObjectName("lineEdit_Rising1Ut")
        self.gridLayout.addWidget(self.lineEdit_Rising1Ut, 1, 0, 1, 1)
        self.lineEdit_Rising2Ut = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_Rising2Ut.setMaxLength(7)
        self.lineEdit_Rising2Ut.setObjectName("lineEdit_Rising2Ut")
        self.gridLayout.addWidget(self.lineEdit_Rising2Ut, 1, 1, 1, 1)
        self.lineEdit_Falling1Ut = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_Falling1Ut.setMaxLength(7)
        self.lineEdit_Falling1Ut.setObjectName("lineEdit_Falling1Ut")
        self.gridLayout.addWidget(self.lineEdit_Falling1Ut, 1, 2, 1, 1)
        self.lineEdit_Falling2Ut = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_Falling2Ut.setMaxLength(7)
        self.lineEdit_Falling2Ut.setObjectName("lineEdit_Falling2Ut")
        self.gridLayout.addWidget(self.lineEdit_Falling2Ut, 1, 3, 1, 1)
        self.lineEdit_Rising1Ufd = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_Rising1Ufd.setMaxLength(7)
        self.lineEdit_Rising1Ufd.setObjectName("lineEdit_Rising1Ufd")
        self.gridLayout.addWidget(self.lineEdit_Rising1Ufd, 2, 0, 1, 1)
        self.lineEdit_Rising2Ufd = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_Rising2Ufd.setMaxLength(7)
        self.lineEdit_Rising2Ufd.setObjectName("lineEdit_Rising2Ufd")
        self.gridLayout.addWidget(self.lineEdit_Rising2Ufd, 2, 1, 1, 1)
        self.lineEdit_Falling1Ufd = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_Falling1Ufd.setMaxLength(7)
        self.lineEdit_Falling1Ufd.setObjectName("lineEdit_Falling1Ufd")
        self.gridLayout.addWidget(self.lineEdit_Falling1Ufd, 2, 2, 1, 1)
        self.lineEdit_Falling2Ufd = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_Falling2Ufd.setMaxLength(7)
        self.lineEdit_Falling2Ufd.setObjectName("lineEdit_Falling2Ufd")
        self.gridLayout.addWidget(self.lineEdit_Falling2Ufd, 2, 3, 1, 1)
        self.lineEdit_Rising1Ifd = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_Rising1Ifd.setMaxLength(7)
        self.lineEdit_Rising1Ifd.setObjectName("lineEdit_Rising1Ifd")
        self.gridLayout.addWidget(self.lineEdit_Rising1Ifd, 3, 0, 1, 1)
        self.lineEdit_Rising2Ifd = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_Rising2Ifd.setMaxLength(7)
        self.lineEdit_Rising2Ifd.setObjectName("lineEdit_Rising2Ifd")
        self.gridLayout.addWidget(self.lineEdit_Rising2Ifd, 3, 1, 1, 1)
        self.lineEdit_Falling1Ifd = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_Falling1Ifd.setMaxLength(7)
        self.lineEdit_Falling1Ifd.setObjectName("lineEdit_Falling1Ifd")
        self.gridLayout.addWidget(self.lineEdit_Falling1Ifd, 3, 2, 1, 1)
        self.lineEdit_Falling2Ifd = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_Falling2Ifd.setMaxLength(7)
        self.lineEdit_Falling2Ifd.setObjectName("lineEdit_Falling2Ifd")
        self.gridLayout.addWidget(self.lineEdit_Falling2Ifd, 3, 3, 1, 1)
        self.lineEdit_Rising1Angle = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_Rising1Angle.setMaxLength(7)
        self.lineEdit_Rising1Angle.setObjectName("lineEdit_Rising1Angle")
        self.gridLayout.addWidget(self.lineEdit_Rising1Angle, 4, 0, 1, 1)
        self.lineEdit_Rising2Angle = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_Rising2Angle.setMaxLength(7)
        self.lineEdit_Rising2Angle.setObjectName("lineEdit_Rising2Angle")
        self.gridLayout.addWidget(self.lineEdit_Rising2Angle, 4, 1, 1, 1)
        self.lineEdit_Falling1Angle = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_Falling1Angle.setMaxLength(7)
        self.lineEdit_Falling1Angle.setObjectName("lineEdit_Falling1Angle")
        self.gridLayout.addWidget(self.lineEdit_Falling1Angle, 4, 2, 1, 1)
        self.lineEdit_Falling2Angle = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_Falling2Angle.setMaxLength(7)
        self.lineEdit_Falling2Angle.setObjectName("lineEdit_Falling2Angle")
        self.gridLayout.addWidget(self.lineEdit_Falling2Angle, 4, 3, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 5, 0, 1, 1)
        self.lineEdit_AngleAVGmin = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_AngleAVGmin.setMaxLength(7)
        self.lineEdit_AngleAVGmin.setObjectName("lineEdit_AngleAVGmin")
        self.gridLayout.addWidget(self.lineEdit_AngleAVGmin, 5, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 5, 2, 1, 1)
        self.lineEdit_AngleAVGmax = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_AngleAVGmax.setMaxLength(7)
        self.lineEdit_AngleAVGmax.setObjectName("lineEdit_AngleAVGmax")
        self.gridLayout.addWidget(self.lineEdit_AngleAVGmax, 5, 3, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_30.setObjectName("label_30")
        self.gridLayout.addWidget(self.label_30, 6, 0, 1, 1)
        self.lineEdit_Umax = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_Umax.setMaxLength(7)
        self.lineEdit_Umax.setObjectName("lineEdit_Umax")
        self.gridLayout.addWidget(self.lineEdit_Umax, 6, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 6, 2, 1, 1)
        self.lineEdit_Umin = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_Umin.setMaxLength(7)
        self.lineEdit_Umin.setObjectName("lineEdit_Umin")
        self.gridLayout.addWidget(self.lineEdit_Umin, 6, 3, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
<<<<<<< HEAD
        self.textBrowser.setGeometry(QtCore.QRect(690, 250, 311, 461))
=======
        self.textBrowser.setGeometry(QtCore.QRect(690, 280, 311, 481))
>>>>>>> 2e5ede1e888c9679f1570c07ed3f20a8da8bf05f
        self.textBrowser.setObjectName("textBrowser")
        self.groupBox_LimiterCalculate = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_LimiterCalculate.setGeometry(QtCore.QRect(320, 10, 241, 251))
        self.groupBox_LimiterCalculate.setObjectName("groupBox_LimiterCalculate")
        self.layoutWidget_2 = QtWidgets.QWidget(self.groupBox_LimiterCalculate)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 20, 221, 221))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_17 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 0, 0, 1, 1)
        self.lineEdit_IFDB = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_IFDB.setMaxLength(7)
        self.lineEdit_IFDB.setObjectName("lineEdit_IFDB")
        self.gridLayout_2.addWidget(self.lineEdit_IFDB, 0, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 0, 2, 1, 1)
        self.lineEdit_a = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_a.setMaxLength(7)
        self.lineEdit_a.setObjectName("lineEdit_a")
        self.gridLayout_2.addWidget(self.lineEdit_a, 0, 3, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 1, 0, 1, 1)
        self.lineEdit_UFDB_BZ = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_UFDB_BZ.setMaxLength(7)
        self.lineEdit_UFDB_BZ.setObjectName("lineEdit_UFDB_BZ")
        self.gridLayout_2.addWidget(self.lineEdit_UFDB_BZ, 1, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 1, 2, 1, 1)
        self.lineEdit_b = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_b.setMaxLength(7)
        self.lineEdit_b.setObjectName("lineEdit_b")
        self.gridLayout_2.addWidget(self.lineEdit_b, 1, 3, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.layoutWidget_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.label_29.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setTextFormat(QtCore.Qt.RichText)
        self.label_29.setObjectName("label_29")
        self.gridLayout_2.addWidget(self.label_29, 2, 0, 1, 1)
        self.lineEdit_KFD_BZ = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_KFD_BZ.setMaxLength(7)
        self.lineEdit_KFD_BZ.setObjectName("lineEdit_KFD_BZ")
        self.gridLayout_2.addWidget(self.lineEdit_KFD_BZ, 2, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 2, 2, 1, 1)
        self.lineEdit_n = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_n.setMaxLength(7)
        self.lineEdit_n.setObjectName("lineEdit_n")
        self.gridLayout_2.addWidget(self.lineEdit_n, 2, 3, 1, 1)
        self.lineEdit_XcEqualpu = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_XcEqualpu.setMaxLength(7)
        self.lineEdit_XcEqualpu.setObjectName("lineEdit_XcEqualpu")
        self.gridLayout_2.addWidget(self.lineEdit_XcEqualpu, 5, 1, 1, 1)
        self.lineEdit_SG100 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_SG100.setMaxLength(7)
        self.lineEdit_SG100.setObjectName("lineEdit_SG100")
        self.gridLayout_2.addWidget(self.lineEdit_SG100, 3, 3, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_28.setObjectName("label_28")
        self.gridLayout_2.addWidget(self.label_28, 3, 2, 1, 1)
        self.lineEdit_SG120 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_SG120.setMaxLength(7)
        self.lineEdit_SG120.setObjectName("lineEdit_SG120")
        self.gridLayout_2.addWidget(self.lineEdit_SG120, 4, 3, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_31.setObjectName("label_31")
        self.gridLayout_2.addWidget(self.label_31, 4, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_6.setTextFormat(QtCore.Qt.PlainText)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_23.setTextFormat(QtCore.Qt.PlainText)
        self.label_23.setObjectName("label_23")
        self.gridLayout_2.addWidget(self.label_23, 3, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_24.setTextFormat(QtCore.Qt.PlainText)
        self.label_24.setObjectName("label_24")
        self.gridLayout_2.addWidget(self.label_24, 4, 0, 1, 1)
        self.lineEdit_UFDB_LL = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_UFDB_LL.setMaxLength(7)
        self.lineEdit_UFDB_LL.setObjectName("lineEdit_UFDB_LL")
        self.gridLayout_2.addWidget(self.lineEdit_UFDB_LL, 3, 1, 1, 1)
        self.lineEdit_KFD_LL = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_KFD_LL.setMaxLength(7)
        self.lineEdit_KFD_LL.setObjectName("lineEdit_KFD_LL")
        self.gridLayout_2.addWidget(self.lineEdit_KFD_LL, 4, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1261, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ExcitationSystemModelingCalculator"))
        self.groupBox_NoLoadCalculate.setTitle(_translate("MainWindow", "空载特性计算"))
        self.label.setText(_translate("MainWindow", "线性段选择"))
        self.lineEdit_LinearScope.setText(_translate("MainWindow", "0.45"))
        self.pushButton_NoLoadCalculateAutoCalculate.setText(_translate("MainWindow", "空载特性计算"))
        self.pushButton_NoLoadCalculateReadCSV.setText(_translate("MainWindow", "读取CSV"))
        self.pushButton_NoLoadCalculateSaveCSV.setText(_translate("MainWindow", "保存CSV"))
        self.pushButton_Reset.setText(_translate("MainWindow", "复位"))
        self.groupBox_ExciterTransferCalculate.setTitle(_translate("MainWindow", "励磁变参数计算"))
        self.label_2.setText(_translate("MainWindow", "STN（kW）"))
        self.label_3.setText(_translate("MainWindow", "Uk（p.u.）"))
        self.label_4.setText(_translate("MainWindow", "阳极电压ULN（V）"))
        self.label_5.setText(_translate("MainWindow", "Xc（有名）"))
        self.label_22.setText(_translate("MainWindow", "XcEqual（有名）"))
        self.pushButton_ExciterTranformerCalculate.setText(_translate("MainWindow", "参数计算"))
        self.lineEdit_STN.setText(_translate("MainWindow", "1000"))
        self.lineEdit_Uk.setText(_translate("MainWindow", "0.06"))
        self.lineEdit_ULN.setText(_translate("MainWindow", "450"))
        self.tableWidget_RawData.setSortingEnabled(True)
        item = self.tableWidget_RawData.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_RawData.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "UAB(%)"))
        item = self.tableWidget_RawData.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "UFD (V)"))
        item = self.tableWidget_RawData.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "IFD (A)"))
        self.groupBox_ControlAngleCalculate.setTitle(_translate("MainWindow", "控制角范围计算（最大最小角）"))
        self.label_7.setText(_translate("MainWindow", "机端电压（p.u.）"))
        self.label_8.setText(_translate("MainWindow", "励磁电压（V）"))
        self.label_9.setText(_translate("MainWindow", "励磁电流（A）"))
        self.label_15.setText(_translate("MainWindow", "αmin/αmax（°）"))
        self.pushButton_AngleScopeCalculate.setText(_translate("MainWindow", "角度范围计算"))
        self.label_10.setText(_translate("MainWindow", "上升第一点"))
        self.label_11.setText(_translate("MainWindow", "上升第二点"))
        self.label_12.setText(_translate("MainWindow", "下降第一点"))
        self.label_13.setText(_translate("MainWindow", "下降第二点"))
        self.lineEdit_Rising1Ut.setText(_translate("MainWindow", "0.69323"))
        self.lineEdit_Rising2Ut.setText(_translate("MainWindow", "0.73180"))
        self.lineEdit_Falling1Ut.setText(_translate("MainWindow", "0.74304"))
        self.lineEdit_Falling2Ut.setText(_translate("MainWindow", "0.62"))
        self.lineEdit_Rising1Ufd.setText(_translate("MainWindow", "403.9"))
        self.lineEdit_Rising2Ufd.setText(_translate("MainWindow", "426.7"))
        self.lineEdit_Falling1Ufd.setText(_translate("MainWindow", "-382.4"))
        self.lineEdit_Falling2Ufd.setText(_translate("MainWindow", "-318"))
        self.lineEdit_Rising1Ifd.setText(_translate("MainWindow", "324.7"))
        self.lineEdit_Rising2Ifd.setText(_translate("MainWindow", "350.9"))
        self.lineEdit_Falling1Ifd.setText(_translate("MainWindow", "311.5"))
        self.lineEdit_Falling2Ifd.setText(_translate("MainWindow", "242.2"))
        self.label_16.setText(_translate("MainWindow", "αAVGmin"))
        self.label_14.setText(_translate("MainWindow", "αAVGmax"))
        self.label_30.setText(_translate("MainWindow", "Umax"))
        self.label_27.setText(_translate("MainWindow", "Umin"))
        self.groupBox_LimiterCalculate.setTitle(_translate("MainWindow", "空载特性计算结果"))
        self.label_17.setText(_translate("MainWindow", "IFDB"))
        self.label_19.setText(_translate("MainWindow", "a"))
        self.label_18.setText(_translate("MainWindow", "UFDB_BZ"))
        self.label_20.setText(_translate("MainWindow", "b"))
        self.label_29.setText(_translate("MainWindow", "KFD_BZ"))
        self.label_21.setText(_translate("MainWindow", "n"))
        self.label_28.setText(_translate("MainWindow", "SG1.0"))
        self.label_31.setText(_translate("MainWindow", "SG1.2"))
        self.label_6.setText(_translate("MainWindow", "XcEqual(p.u.)"))
        self.label_23.setText(_translate("MainWindow", "UFDB_LL"))
        self.label_24.setText(_translate("MainWindow", "KFD_LL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

