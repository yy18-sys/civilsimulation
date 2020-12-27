class Element:

    def __init__(self,name):
        self.name = name

    def getname(self):
        return self.name

class Ground(Element):


    def isGround(self):
        return True