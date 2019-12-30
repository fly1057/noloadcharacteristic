from PyQt5.uic import loadUiType
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (FigureCanvasAgg as
                                                FigureCanvas,
                                                NavigationToolbar2QT as
                                                NavigationToolbar)
Ui_MainWindow , QMainWindow = loadUiType("kongzai.ui") 