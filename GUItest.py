from PyQt5.uic import loadUiType
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (FigureCanvasAgg as
                                                FigureCanvas,
                                                NavigationToolbar2QT as
                                                NavigationToolbar)
Ui_MainWindow, QMainWindow = loadUiType("kongzaiQMainWindow.ui")


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, ):
        super(Main, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
