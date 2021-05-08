from NIWENV import *


# from PySide2.QtWidgets import ...
# from PySide2.QtCore import ...
# from PySide2.QtGui import ...

from PySide2 import QtWidgets, QtGui, QtCore

class ColorPicker_NodeInstance_MainWidget(QtWidgets.QPushButton, MWB):
    def __init__(self, params):
        MWB.__init__(self, params)
        QtWidgets.QPushButton.__init__(self)
        self.clicked.connect(self.on_clicked)
        self.setStyleSheet("border : none; background-color: (255,255,255,255)")
        self.color = (255,255,255,255)
        self.setFixedSize(110, 110)

    def on_clicked(self):
        color = QtWidgets.QColorDialog.getColor(options=QtWidgets.QColorDialog.ShowAlphaChannel)
        if color.isValid():
            r,g,b,a = color.getRgb()
            self.color = (r,g,b,a)
            self.setStyleSheet("border : none; background-color: {}".format(color.name()))
            self.parent_node_instance.update_color(self.color)

        


    def get_data(self):
        return {}


    def set_data(self, data):
        pass



    def remove_event(self):
        pass


