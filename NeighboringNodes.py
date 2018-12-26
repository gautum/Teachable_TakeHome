import numpy as np
from Node import Node


class NeighboringNodes(object):

    def __init__(self,size,debug):
        self.size = size
        self.debug = debug
        self.grid = np.empty(shape = (self.size,self.size), dtype = object)
        self.types = ['SQUARE', 'CROSS', 'DIAMOND']



    def buildGrid(self):
        # index from 1 - > size
        count = 1

        for i in range (self.size):
            for j in range (self.size):
                self.grid[i][j] = Node(i,j,count)
                count+=1
        if self.debug == True:
            for i in range (self.size):
                for j in range (self.size):
                    print (self.grid[i][j].getValues())


    def findIndex(self, index):
        if (index > np.power(self.size, 2) or index <= 0):
            raise ValueError("Index out of range")

        # flatten array and return index
        return np.reshape(self.grid, (-1,))[index-1].getXYCoords()

    def isOnGrid(self, x, y):
        """
        :param x: x coordinate in grid
        :param y: y coordinate in grid
        :return: true if point is in grid bounds, false otherwise
        """
        if x < 0  or x >= self.size or y < 0 or y >= self.size:
            return False
        return True


    def findNeighbors(self, m, ntype, x = None, y = None, i = None):

        # checks to make sure input is valid
        if ntype not in self.types:
            raise ValueError("Not valid type")
        if m > self.size /2:
            raise ValueError("m is too large")
        if (x is not None or y is not None) and i is not None:
            raise ValueError("(X and Y) OR I, not both")
        if x is not None and y is None:
            raise ValueError("(X and Y) OR I")
        if x is None and y is not None:
            raise ValueError("(X and Y) OR I")
        if x is  None and y is None and i is None:
            raise ValueError("Must input some value")

        if i is not None:
            x, y = self.findIndex(i)

        neighbors = []


        if ntype == 'SQUARE':
            radius = 1
            while radius <= m:
                for i in range(-1 * radius, radius+1):
                    for j in range (-1 *radius, radius+1):
                        # dont add origin to neighbors list
                        if i == 0 and j == 0:
                            continue
                        # make sure point is valid
                        if self.isOnGrid(x + i, y + j):
                            neighbors.append(self.grid[x+i][y+j].getXYCoords())
                radius+=1

        return neighbors


