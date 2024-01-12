from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget


class Inside_City_Travel:
    def __init__(self,main_widget):
        self.main_widget = main_widget
        self.own_widget = QWidget(main_widget)
        self.initUI()
    def initUI(self):
        self.own_widget.setGeometry(QtCore.QRect(160, 480, 821, 80))


        self.widget_3.setGeometry(QtCore.QRect(160, 480, 821, 80))
        self.widget_3.setObjectName("widget_3")

    def show_widget(self):
        self.own_widget.show()
    def hide_widget(self):
        self.own_widget.hide()