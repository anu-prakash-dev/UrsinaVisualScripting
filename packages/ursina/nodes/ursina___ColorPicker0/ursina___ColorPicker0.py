from NIENV import *



# USEFUL
# self.input(index)                   <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget
# self.exec_output(index)             <- executes an execution output
# self.create_new_input(type_, label, widget_name=None, widget_pos='under')
# self.delete_input(input or index)
# self.create_new_output(type_, label, append=True)
# self.delete_output(output or index)




class ColorPicker_NodeInstance(NodeInstance):
    def __init__(self, params):
        super(ColorPicker_NodeInstance, self).__init__(params)
        self.title_label.hide()
        print(len(self.outputs))
        for i in range(len(self.outputs)):
            self.set_output_val(i,255)
        # self.special_actions['action name'] = {'method': M(self.action_method)}


    def update_color(self,color):
        for i in enumerate(color):
            self.set_output_val(*i)


    def update_event(self, input_called=-1):
        pass


    def get_data(self):
        data = {}
        # ...
        return data


    def set_data(self, data):
        pass
        # ...



    def remove_event(self):
        pass

