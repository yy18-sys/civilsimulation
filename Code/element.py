class Element:

    def __init__(self,name):
        self.name = name

    def getname(self):
        return self.name

class Ground(Element):


    def isGround(self):
        return  True

class Food(Element):
    def __init__(self):
        super.__init__(self)

class Lava(Element):
    def __init__(self):
        super.__init__(self)

class Wall(Element):
    def __init__(self):
        super.__init__(self)
