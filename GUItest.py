from PyQt5.uic import loadUiType
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from Ui_kongzaiQMainWindow import Ui_MainWindow
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as  #不是FigureCanvasAgg，pyqt5已经更新了
    FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 在这里引入matplotlib的代码结构，首先建立figure，然后建立canvas，其中canvas是子类
        # 然后将canvas加入到之前在Qt designer中建立的layout中去，关键是要在设计时留一个空出来
        fig1 = Figure()
        ax1f1 = fig1.add_subplot(111)
        ax1f1.pcolormesh(np.random.rand(10,10))
        self.addmpl(fig1)
        self.ui.pushButton_NoLoadCalculateAutoCalculate.clicked.connect(
            self.NoLoadCalculateAutoCalculate)

    def addmpl(self, fig):
        self.canvas = FigureCanvas(fig)
        self.ui.verticalLayout_mpl.addWidget(self.canvas)
        self.canvas.draw()
        self.toolbar = NavigationToolbar(self.canvas,self,coordinates=True)
        self.ui.verticalLayout_mpl.addWidget(self.toolbar)

    def rmmpl(self):
        self.ui.verticalLayout_mpl.removeWidget(self.canvas)
        self.canvas.close()
        self.ui.verticalLayout_mpl.removeWidget(self.toolbar)
        self.toolbar.close()

    def NoLoadCalculateAutoCalculate(self):
        self.rmmpl()  #这句话必须要有，不然canvas会一直增加
        fig1 = Figure()
        ax1f1 = fig1.add_subplot(111)
        ax1f1.pcolormesh(np.random.rand(10,10))
        self.addmpl(fig1)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Main()
    MainWindow.show()
    sys.exit(app.exec_())
