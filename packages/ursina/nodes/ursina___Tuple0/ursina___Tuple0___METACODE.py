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


class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)
        self.elements = 1
        
        self.special_actions['Add Element'] = {'method': M(self.action_add_element)}


    def update_event(self, input_called=-1):
        the_list = []
        for inp in self.inputs:
            the_list.append(inp.get_val())
        self.set_output_val(0, tuple(the_list))

    def action_add_element(self):
        new_elem = self.elements+1
        self.create_new_input('data', 'ELEMENT #'+str(new_elem), widget_name='std line edit m', widget_pos='besides')
        self.elements += 1
        
        self.special_actions['Remove Element'] = {'method': M(self.action_remove_element)}

    def action_remove_element(self):
        self.delete_input(-1)
        self.elements -= 1
        
        if self.elements == 1:
            del self.special_actions['Remove Element']

    def get_data(self):
        data = {}
        return data


    def remove_event(self):
        pass
