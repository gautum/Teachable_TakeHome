import numpt as np
from Node import Node


class NeighboringNodes(object):

    def __init__(self,size,debug):
        self.size = size
        self.debug = debug
        self.grid = np.empty(shape = (self.size,self.size), dtype = object)



    def buildGrid(self):
        # index from 1 - > size
        count = 1

        for i in range self.size:
            for j in range self.size:
                self.grid[i][j] = Node(i,j,count)
                count+=1
        if self.debug == True:
            for i in range self.size:
                for j in range self.size:
                    print (self.grid[i][j].getValues())
