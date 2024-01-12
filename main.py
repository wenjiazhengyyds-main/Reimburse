import pandas as pd
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from Inside_City_Travel import Inside_City_Travel


import sys
class GUI(object):
    def __init__(self,widget):
        self.widget = widget
        self.initUI()
    def initUI(self):
        self.widget.setFixedSize(1123, 796)
        self.widget.setWindowTitle( "投促中心报销软件应用")
        self.Title = QtWidgets.QLabel(widget)
        self.Title.setGeometry(QtCore.QRect(420, 0, 381, 61))
        font = QtGui.QFont()
        font.setFamily("方正小标宋_GBK")
        font.setPointSize(20)
        self.Title.setFont(font)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.Title.setText("投促中心报销软件应用")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QWidget()  # 创建主窗口部件
    my_widget = GUI(widget)  # 创建MyWidget实例，并将主窗口部件作为参数传递给它
    widget.show()  # 显示主窗口部件
    sys.exit(app.exec_())
