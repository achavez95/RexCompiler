class Variable:
        def __init__(self, type, id, memory, size):
                self.type = type
                self.memory = memory
                self.id = id
                self.size = size

        def __repr__(self):
                return str(self.type) + ', '+ str(self.id) + ', ' + str(self.memory) + ', ' + str(self.size)

        def updatesize(self, size):
                self.size = size

        def updatememory(self, memory):
                self.memory = memory
