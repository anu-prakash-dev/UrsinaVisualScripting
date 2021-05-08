from NIWENV import *


# from PySide2.QtWidgets import ...
# from PySide2.QtCore import ...
# from PySide2.QtGui import ...


from PySide2.QtWidgets import QCheckBox



class %CLASS%(QCheckBox, MWB):
    def __init__(self, params):
        MWB.__init__(self, params)
        QCheckBox.__init__(self)


        
        self.setStyleSheet('''
        QCheckBox::indicator { 
            width:50px; 
            height: 50px; 
            }
        ''')
        self.clicked.connect(M(self.parent_node_instance.stateChanged))


    def get_data(self):
        return {}


    def set_data(self, data):
        pass



    def remove_event(self):
        pass

