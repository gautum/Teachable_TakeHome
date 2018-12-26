import numpy as np
from Node import Node
import itertools


class NeighboringNodes(object):

    def __init__(self,size,debug):
        self.size = size
        self.debug = debug
        self.grid = []
        self.types = ['SQUARE', 'CROSS', 'DIAMOND']



    def build_grid(self):
        # index from 1 - > size
        counter = itertools.count()
        counter.next()

        self.grid = [[Node(i,j,counter.next()) for i in range (self.size)] for j in range(self.size)]

        if self.debug == True:
            for i in range (self.size):
                for j in range (self.size):
                    print (self.grid[i][j].getValues())


    def find_index(self, index):
        if (index > np.power(self.size, 2) or index <= 0):
            raise ValueError("Index out of range")

        # flatten array and return index
        return np.reshape(self.grid, (-1,))[index-1].getXYCoords()

    def is_on_grid(self, x, y):
        if x < 0  or x >= self.size or y < 0 or y >= self.size:
            return False
        return True


    def find_neighbors(self, m, ntype, x = None, y = None, i = None):

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

        # if coord is not on grid then throw error
        if not self.isOnGrid(x,y):
            raise ValueError("Coordinates not in grid")


        neighbors = []


        if ntype == 'SQUARE':
            for i in range (-1 * m, m+1):
                for j in range(-1 * m, m + 1):
                    if i == 0 and j == 0:
                        continue
                    if self.isOnGrid(x+i,y+j):
                        neighbors.append(self.grid[x + i][y + j].getXYCoords())


        elif ntype == 'CROSS':

            # go to the right and left, up and down
            for i in range(-1 * m, m+1):

                if i == 0:
                    continue
                if self.isOnGrid(x + i, y):
                    neighbors.append(self.grid[x+i][y].getXYCoords())
                if self.isOnGrid(x, y + i):
                     neighbors.append(self.grid[x][y+i].getXYCoords())


        elif ntype == 'DIAMOND':

            for i in range (-1 * m, m+1):
                for j in range(-1 * m, m+1):
                        # manhattan of point equals radius
                        if abs(i) + abs(j) <=m:
                            # don't add origin to neighbors
                            if i == 0 and j == 0:
                                continue
                            if self.isOnGrid(x + i, y + j):
                                neighbors.append(self.grid[x+i][y+j].getXYCoords())

        return neighbors


