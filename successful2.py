import pandas as pd
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

import sys


from Components import Button_Events

# self 代表第一个实例对象，对于这个函数，就是widget
class GUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(1067, 762)
        self.Title = QtWidgets.QLabel(self)
        self.Title.setGeometry(QtCore.QRect(360, 0, 381, 61))
        font = QtGui.QFont()
        font.setFamily("方正小标宋_GBK")
        font.setPointSize(20)
        self.Title.setFont(font)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")


        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(130, 60, 111, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("要填的")
        self.comboBox.addItem("招待用餐")
        self.comboBox.addItem("市外出行")
        self.comboBox.addItem("市内出行")
        self.comboBox.addItem("市外出行 + 招待用餐")
        self.comboBox.addItem("市内出行 + 招待用餐")
        self.comboBox.currentIndexChanged.connect(self.printtl)
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setGeometry(QtCore.QRect(30, 70, 81, 21))
        self.label1.setObjectName("label1")
        self.label1.setText("报销事项")


        self.dateEdit = QtWidgets.QDateEdit(self)
        self.dateEdit.setGeometry(QtCore.QRect(160, 170, 110, 22))
        self.dateEdit.setObjectName("dateEdit")

        number = Button_Events();
        number.return_element(self,widget);




    def printtl(self):
        option = self.comboBox.currentText()
        print(option)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = GUI()
    widget.show()
    widget.setWindowTitle("投促中心报销软件应用")
    sys.exit(app.exec_())
