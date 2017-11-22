class Function:
        def __init__(self, type, id, parameters, size, dir, rtn, paramnumber):
                self.type = type
                self.id = id
                self.dir = dir
                self.size = size
                self.rtn = rtn
                self.parameters = parameters
                self.paramnumber = paramnumber

        def __repr__(self):
                 return str(self.type) + ', '+ str(self.id)

        def updatesize(self, size):
                self.size = size

        def updatememory(self, memory):
                self.memory = memory
