from PyQt5.uic import loadUiType
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_kongzaiQMainWindow import  Ui_MainWindow
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (FigureCanvasAgg as
                                                FigureCanvas,
                                                NavigationToolbar2QT as
                                                NavigationToolbar)

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 在这里引入matplotlib的代码结构，首先建立figure，然后建立canvas，其中canvas是子类
        # 然后将canvas加入到之前在Qt designer中建立的layout中去，关键是要在设计时留一个空出来
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ui.verticalLayout_mpl.addWidget(self.canvas)
        self.Reset()
        self.show()
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Main()
    MainWindow.show()
    sys.exit(app.exec_())
