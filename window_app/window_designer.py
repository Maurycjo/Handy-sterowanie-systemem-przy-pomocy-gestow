# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_designer.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(725, 571)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.gestureTab = QtWidgets.QWidget()
        self.gestureTab.setObjectName("gestureTab")
        self.gridLayout = QtWidgets.QGridLayout(self.gestureTab)
        self.gridLayout.setObjectName("gridLayout")
        self.applyButton_2 = QtWidgets.QPushButton(self.gestureTab)
        self.applyButton_2.setObjectName("applyButton_2")
        self.gridLayout.addWidget(self.applyButton_2, 3, 3, 1, 1)
        self.resetButton = QtWidgets.QPushButton(self.gestureTab)
        self.resetButton.setObjectName("resetButton")
        self.gridLayout.addWidget(self.resetButton, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 2, 1, 1)
        self.cancelButton = QtWidgets.QPushButton(self.gestureTab)
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout.addWidget(self.cancelButton, 3, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.gestureTab)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 664, 437))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox)
        self.verticalLayout_2.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_2)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.comboBox_3 = QtWidgets.QComboBox(self.widget_3)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBox_3)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.comboBox_4 = QtWidgets.QComboBox(self.widget_4)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBox_4)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.widget_5)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.comboBox_5 = QtWidgets.QComboBox(self.widget_5)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBox_5)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_6 = QtWidgets.QLabel(self.widget_6)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_9.addWidget(self.label_6)
        self.comboBox_6 = QtWidgets.QComboBox(self.widget_6)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.horizontalLayout_9.addWidget(self.comboBox_6)
        self.verticalLayout_2.addWidget(self.widget_6)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.scrollArea, 2, 0, 1, 4)
        self.tabWidget.addTab(self.gestureTab, "")
        self.cameraTab = QtWidgets.QWidget()
        self.cameraTab.setObjectName("cameraTab")
        self.tabWidget.addTab(self.cameraTab, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 725, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.applyButton_2.setText(_translate("MainWindow", "Zastosuj"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
        self.cancelButton.setText(_translate("MainWindow", "Anuluj"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Gest 1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Gest 2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Gest 3"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Gest 4"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Gest 5"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Gest 6"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Gest 7"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Gest 8"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Gest 9"))
        self.comboBox.setItemText(9, _translate("MainWindow", "Gest 10"))
        self.comboBox.setItemText(10, _translate("MainWindow", "Gest 11"))
        self.comboBox.setItemText(11, _translate("MainWindow", "Gest 12"))
        self.comboBox.setItemText(12, _translate("MainWindow", "Gest 13"))
        self.comboBox.setItemText(13, _translate("MainWindow", "Gest 14"))
        self.comboBox.setItemText(14, _translate("MainWindow", "Gest 15"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Gest 1"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Gest 2"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Gest 3"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Gest 4"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Gest 5"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "Gest 6"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "Gest 7"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "Gest 8"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "Gest 9"))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "Gest 10"))
        self.comboBox_2.setItemText(10, _translate("MainWindow", "Gest 11"))
        self.comboBox_2.setItemText(11, _translate("MainWindow", "Gest 12"))
        self.comboBox_2.setItemText(12, _translate("MainWindow", "Gest 13"))
        self.comboBox_2.setItemText(13, _translate("MainWindow", "Gest 14"))
        self.comboBox_2.setItemText(14, _translate("MainWindow", "Gest 15"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Gest 1"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Gest 2"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Gest 3"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Gest 4"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "Gest 5"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "Gest 6"))
        self.comboBox_3.setItemText(6, _translate("MainWindow", "Gest 7"))
        self.comboBox_3.setItemText(7, _translate("MainWindow", "Gest 8"))
        self.comboBox_3.setItemText(8, _translate("MainWindow", "Gest 9"))
        self.comboBox_3.setItemText(9, _translate("MainWindow", "Gest 10"))
        self.comboBox_3.setItemText(10, _translate("MainWindow", "Gest 11"))
        self.comboBox_3.setItemText(11, _translate("MainWindow", "Gest 12"))
        self.comboBox_3.setItemText(12, _translate("MainWindow", "Gest 13"))
        self.comboBox_3.setItemText(13, _translate("MainWindow", "Gest 14"))
        self.comboBox_3.setItemText(14, _translate("MainWindow", "Gest 15"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Gest 1"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Gest 2"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "Gest 3"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "Gest 4"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "Gest 5"))
        self.comboBox_4.setItemText(5, _translate("MainWindow", "Gest 6"))
        self.comboBox_4.setItemText(6, _translate("MainWindow", "Gest 7"))
        self.comboBox_4.setItemText(7, _translate("MainWindow", "Gest 8"))
        self.comboBox_4.setItemText(8, _translate("MainWindow", "Gest 9"))
        self.comboBox_4.setItemText(9, _translate("MainWindow", "Gest 10"))
        self.comboBox_4.setItemText(10, _translate("MainWindow", "Gest 11"))
        self.comboBox_4.setItemText(11, _translate("MainWindow", "Gest 12"))
        self.comboBox_4.setItemText(12, _translate("MainWindow", "Gest 13"))
        self.comboBox_4.setItemText(13, _translate("MainWindow", "Gest 14"))
        self.comboBox_4.setItemText(14, _translate("MainWindow", "Gest 15"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "Gest 1"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "Gest 2"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "Gest 3"))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "Gest 4"))
        self.comboBox_5.setItemText(4, _translate("MainWindow", "Gest 5"))
        self.comboBox_5.setItemText(5, _translate("MainWindow", "Gest 6"))
        self.comboBox_5.setItemText(6, _translate("MainWindow", "Gest 7"))
        self.comboBox_5.setItemText(7, _translate("MainWindow", "Gest 8"))
        self.comboBox_5.setItemText(8, _translate("MainWindow", "Gest 9"))
        self.comboBox_5.setItemText(9, _translate("MainWindow", "Gest 10"))
        self.comboBox_5.setItemText(10, _translate("MainWindow", "Gest 11"))
        self.comboBox_5.setItemText(11, _translate("MainWindow", "Gest 12"))
        self.comboBox_5.setItemText(12, _translate("MainWindow", "Gest 13"))
        self.comboBox_5.setItemText(13, _translate("MainWindow", "Gest 14"))
        self.comboBox_5.setItemText(14, _translate("MainWindow", "Gest 15"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "Gest 1"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "Gest 2"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "Gest 3"))
        self.comboBox_6.setItemText(3, _translate("MainWindow", "Gest 4"))
        self.comboBox_6.setItemText(4, _translate("MainWindow", "Gest 5"))
        self.comboBox_6.setItemText(5, _translate("MainWindow", "Gest 6"))
        self.comboBox_6.setItemText(6, _translate("MainWindow", "Gest 7"))
        self.comboBox_6.setItemText(7, _translate("MainWindow", "Gest 8"))
        self.comboBox_6.setItemText(8, _translate("MainWindow", "Gest 9"))
        self.comboBox_6.setItemText(9, _translate("MainWindow", "Gest 10"))
        self.comboBox_6.setItemText(10, _translate("MainWindow", "Gest 11"))
        self.comboBox_6.setItemText(11, _translate("MainWindow", "Gest 12"))
        self.comboBox_6.setItemText(12, _translate("MainWindow", "Gest 13"))
        self.comboBox_6.setItemText(13, _translate("MainWindow", "Gest 14"))
        self.comboBox_6.setItemText(14, _translate("MainWindow", "Gest 15"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.gestureTab), _translate("MainWindow", "Gesty"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cameraTab), _translate("MainWindow", "Kamera"))

if __name__ == '__main__':
   app=QtWidgets.QApplication(sys.argv)
   MainWindow=QtWidgets.QMainWindow()
   ui=Ui_MainWindow()
   ui.setupUi(MainWindow)
   MainWindow.show()
   sys.exit(app.exec())