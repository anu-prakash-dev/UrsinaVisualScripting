from NIENV import *
from ursina import * 

# USEFUL
# self.input(index)                   <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget


class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)


    def update_event(self, input_called=-1):
        global app 
        if input_called == 0:
            app = Ursina()
            self.exec_output(0)

    def set_data(self, data):
        pass
        # ...


    def remove_event(self):
        pass
