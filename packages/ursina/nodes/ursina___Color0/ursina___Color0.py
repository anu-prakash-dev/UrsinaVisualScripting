from NIENV import *


# API METHODS --------------

# self.main_widget
# self.update_shape()

# Ports
# self.input(index)
# self.set_output_val(index, val)
# self.exec_output(index)

# self.create_new_input(type_, label, widget_name=None, widget_pos='under', pos=-1)
# self.delete_input(index)
# self.create_new_output(type_, label, pos=-1)
# self.delete_output(index)

# Logging
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', target='global')
# self.log_message('that\'s not good', target='error')

# --------------------------

class Color_NodeInstance(NodeInstance):
    def __init__(self, params):
        super(Color_NodeInstance, self).__init__(params)
        for input in self.inputs :
            input.widget.set_data(255)
            input.widget.editing_finished()
        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...

    def update_event(self, input_called=-1):

        r = self.input(0)
        g = self.input(1)
        b = self.input(2)
        a = self.input(3)
            
        colour = (r,g,b,a)
            
        self.set_output_val(0, colour)

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass
