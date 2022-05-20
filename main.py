import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from window_app.main_window import Ui_MainWindow as win
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = win()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
