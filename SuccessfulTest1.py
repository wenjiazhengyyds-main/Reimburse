import pandas as pd
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
import sys

class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1067, 762)
        self.click = QtWidgets.QPushButton(self)
        self.click.setGeometry(QtCore.QRect(280, 590, 93, 28))
        self.click.setText("click")
        self.click.clicked.connect(self.button_clicked)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(470, 200, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        self.label.setText("有病！")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

    def button_clicked(self):
        self.label.setText("点我干啥")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = GUI()
    widget.show()
    sys.exit(app.exec_())
