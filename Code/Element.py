class Elements:

    def __init__(self,name):
        self.name = name

    def getname(self):
        return self.name

class Ground(Elements):


    def isGround(self):
        return  True