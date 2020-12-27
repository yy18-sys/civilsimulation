class Element:

    def __init__(self,state):
        self.state = state

    def getAction(self):
        if self.state == 0:
            print("ground")
        elif self.state == 1:
            print("food")
        elif self.state == 2:
            print("wall")
        elif self.state == 3:
            print("lava")
