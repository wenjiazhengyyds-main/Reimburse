import pandas as pd
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton
import sys

class Label_Generator:
    def __init__(self,widget):
        self.widget = widget
    def generate_label(self):

