class Node(object):
    def __init__(self,x,y,i):
        self.x = x
        self.y = y
        self.i = i


    def get_values(self):
        return self.x, self.y, self.i


    def get_xy_coords(self):
        return self.x,self.y