from ursina.color import rgba
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

from ursina import *

# --------------------------


class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...

    def update_event(self, input_called=-1):
        if input_called == 0:
            app = self.input(1)
            
            name = str(self.input(2))
            model = str(self.input(3))
            color = self.input(4)
            texture = str(self.input(5))
            position = tuple(self.input(6))
            rotation = tuple(self.input(7))
            scale = tuple(self.input(8))
            
            entity = Entity(
                name=name,
                model=model,
                color=color
                )
            
            self.set_output_val(1, entity)
            self.set_output_val(2, app)
            self.exec_output(0)

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass
