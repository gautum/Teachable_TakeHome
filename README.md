# Teachable_TakeHome
Take Home Assignment for Teachable

# Requirements:

Python 2.7.x

Numpy installed


# How to Run
To view a sample demo of the application, run main.py.


build_grid(): Must be called before doing any subsequent grid operations. Creates a nxn grid instantiated with node objects. The grid is built left to right, top to bottom, with the first node created in top left, last in bottom. 
If the debug flag is given, then for each node in the grid, it's x coordinate, y coordinate and index (x,y,i) will be printed out in order of creation.


find_index(i): 
Returns a tuple with the x,y coordinates of the given index or raises value error if not in bounds. 

Params:
i - integer from 1 to n. Note that nodes are organized left to right, top to bottom, so the node in the top left has an index of 1, the node in the bottom right has an index of n.

find_neighbors(m = 1, ntype,  x = None, y = None, i = None):
Returns a list of neighbors in the specified shape or raises ValueError if not valid. 

Params :
m- radius of neighborhood shape
ntype - shape of neighborhood, can be either SQUARE, DIAMOND, CROSS
x - x coordinate of the origin mode, can't be used alongside i
y - y coordinate of origin node, can't be used alongside i
i - index of origin node, can't be used if x and y are also passed in as arguments




