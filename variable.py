class Variable:
        def __init__(self, type, id, memory, size, context):
                self.type = type
                self.memory = memory
                self.id = id
                self.size = size
                self.context = context

        def __repr__(self):
                return "\n" + str(self.type) + ', '+ str(self.id) + ', ' + str(self.memory) + ', ' + str(self.size) + ', ' + str(self.context)

        def updatesize(self, size):
                self.size = size

        def updatememory(self, memory):
                self.memory = memory
