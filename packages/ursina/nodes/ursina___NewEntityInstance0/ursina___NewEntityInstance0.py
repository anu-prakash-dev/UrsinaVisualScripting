from ursina.color import rgba
from NIENV import *

from ursina import *

# --------------------------

class RyvenEntity(Entity):
    def __init__(self,dict_args):
        super().__init__(**dict_args)
        self.init_node.set_output_val(3, entity)

    def update(self):
        self.update_node.exec()

    def input(self,keyInput):
        node = self.input_node
        for input,output in zip(node.inputs[1:],node.outputs[1:]) :
            keyTest = input.get_val()
            if keyTest == keyInput :
                output.exec()

    def set_input_node(self,node) :
        self.input_node = node

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

            entity_params["input_node"] = self.outputs[1].connected_port_instances[0].parent_node_instance
            entity_params["update_node"] = self.outputs[2]
            entity_params["init_node"] = self

            if "color" in entity_params.keys() :
                entity_params["color"] = color.rgba(*self.input(3))
            entity = RyvenEntity(entity_params)
            self.set_output_val(3, entity)
            self.set_var_val("app", app)
            self.exec_output(0)

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass
