class Cuadruplo:
        def __init__(self, pos1=None, pos2=None, pos3=None, pos4=None):
                self.pos1 = pos1
                self.pos2 = pos2
                self.pos3 = pos3
                self.pos4 = pos4

        def updatedir(self, pos4):
                self.pos4 = pos4

        def __repr__(self):
                return str(self.pos1) + ', '+ str(self.pos2) + ', ' + str(self.pos3) + ', '+ str(self.pos4) 
