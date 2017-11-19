class Function:
        def __init__(self, type, id, parameters, dir):
                self.type = type
                self.id = id
                self.parameters = parameters
                self.dir = dir

        def __repr__(self):
                 return str(self.type) + ', '+ str(self.id)

        def updatesize(self, size):
                self.size = size

        def updatememory(self, memory):
                self.memory = memory
