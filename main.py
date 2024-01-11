import pandas as pd
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

import sys
class GUI(object):
    def __init__(self,widget):
        self.widget = widget
        self.set_UI()
    def set_UI(self):
        self.setWidget()
        self.setLabel()
        self.setComBox()
    def setWidget(self):
        self.widget.setFixedSize(1067, 762)
        self.Title = QtWidgets.QLabel(widget)
        self.Title.setGeometry(QtCore.QRect(360, 0, 381, 61))
        font = QtGui.QFont()
        font.setFamily("方正小标宋_GBK")
        font.setPointSize(20)
        self.Title.setFont(font)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        widget.setWindowTitle("投促中心报销软件应用")
        self.Title.setText( "投促中心报销软件应用")
    def setLabel(self):
        self.decide_label = QtWidgets.QLabel(self.widget)
        self.decide_label.setGeometry(QtCore.QRect(40, 60, 81, 21))
        self.decide_label.setObjectName("decide_label")
        self.decide_label.setText("报销事项")
    def setComBox(self):
        item_List = ["市外出行","市内出行","招待用餐","市外出行 + 招待用餐","市内出行 + 招待用餐"]
        list_items = list(item_List)
        self.decide_comboBox = QtWidgets.QComboBox( self.widget)
        self.decide_comboBox.setGeometry(QtCore.QRect(120, 60, 181, 31))
        self.decide_comboBox.setObjectName("decide_comboBox")
        self.decide_comboBox.addItems(list_items)
        self.decide_comboBox.currentIndexChanged.connect(self.onComboBoxChanged)

        item_List = ["公务差旅费报销单","费用生成单"]
        list_items = list(item_List)
        self.generate_form_comboBox = QtWidgets.QComboBox(self.widget)
        self.generate_form_comboBox.setGeometry(QtCore.QRect(550, 60, 151, 31))
        self.generate_form_comboBox.setObjectName("generate_form_comboBox")
        self.generate_form_comboBox.addItems(list_items)

    def onComboBoxChanged(self,index):
        value = self.decide_comboBox.currentText()
        if("市外出行" == value ):
            item_List = ["公务差旅费报销单", "费用生成单"]
        else:
            item_List = [""]
        list_items = list(item_List)
        self.generate_form_comboBox.clear()
        self.generate_form_comboBox.addItems(list_items)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QWidget()  # 创建主窗口部件
    my_widget = GUI(widget)  # 创建MyWidget实例，并将主窗口部件作为参数传递给它
    widget.show()  # 显示主窗口部件
    sys.exit(app.exec_())
