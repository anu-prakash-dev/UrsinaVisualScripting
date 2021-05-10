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
        self.pairs = 1
        self.special_actions['Add Input/Action pair'] = {'method': M(self.action_add_element)}

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...

    def action_add_element(self):
        new_elem = self.pairs+1
        self.create_new_input('data', 'Key #'+str(new_elem), widget_name='std line edit m', widget_pos='besides')
        self.create_new_output('exec', 'Action #'+str(new_elem))
        self.pairs += 1
        
        self.special_actions['Remove Input/Action pair'] = {'method': M(self.action_remove_element)}

    def action_remove_element(self):
        self.delete_input(-1)
        self.delete_output(-1)
        self.pairs -= 1
        if self.pairs == 1:
            del self.special_actions['Remove Input/Action pair']

    def update_event(self, input_called=-1):
        if input_called == 0 :
            app = self.get_var_val("app")
            entity = self.input(0)
            entity.set_input_node(self)

        self.set_var_val("app", app)

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass
