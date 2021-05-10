from NIWENV import *


# from PySide2.QtWidgets import ...
# from PySide2.QtCore import ...
# from PySide2.QtGui import ...

from PySide2 import QtWidgets, QtGui, QtCore

class %CLASS%(QtWidgets.QPushButton, MWB):
    def __init__(self, params):
        MWB.__init__(self, params)
        QtWidgets.QPushButton.__init__(self)
        self.clicked.connect(self.on_clicked)
        self.color = (255,255,255,255)
        self.setFixedSize(110, 110)

    def on_clicked(self):
        color = QtWidgets.QColorDialog.getColor(options=QtWidgets.QColorDialog.ShowAlphaChannel)
        if color.isValid():
            self.color = color.getRgb()
            self.setStyleSheet("border : none; background-color: rgb{};".format(self.color[:3]))
            self.parent_node_instance.update_color(self.color)

        


    def get_data(self):
        return {"color" : self.color}


    def set_data(self, data):
        self.color = tuple(data["color"])
        self.setStyleSheet("border : none; background-color: rgb{};".format(self.color[:3]))
        pass



    def remove_event(self):
        pass


