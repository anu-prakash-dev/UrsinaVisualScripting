from ursina.color import rgba
from NIENV import *

from ursina import *

# --------------------------


class NewEntityInstance_NodeInstance(NodeInstance):
    def __init__(self, params):
        super(NewEntityInstance_NodeInstance, self).__init__(params)


    def update_event(self, input_called=-1):
        if input_called == 0:
            app = self.get_var_val("app")
            
            entity_params = {}
            for input in self.inputs :
                if input.type_ == "data" :
                    if input.get_val() != "" or None:
                        entity_params[input.label_str.lower()] = input.get_val()
            
            if "color" in entity_params.keys() :
                entity_params["color"] = color.rgba(*self.input(3))
            entity = Entity(**entity_params)
            self.set_output_val(1, entity)
            self.set_var_val("app", app)
            self.exec_output(0)

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass
