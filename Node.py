class Node(object):
    def __init__(self,x,y,i):
        self.x = x
        self.y = y
        self.i = i


    def getValues(self):
        return self.x, self.y, self.i


    def getXYCoords(self):
        return self.x,self.y