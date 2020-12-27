class Element:

    def __init__(self,state):
        self.state = state

    def getState(self):
        if(self.state == 0):
            print("ground")