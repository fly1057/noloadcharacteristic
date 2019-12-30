from PyQt5.uic import loadUiType
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
    from PyQt5 import QtGui
    app = QtGui.QGuiApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
