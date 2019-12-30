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
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Main()
    MainWindow.show()
    sys.exit(app.exec_())
