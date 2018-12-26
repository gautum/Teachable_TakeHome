from NeighboringNodes import NeighboringNodes
from Node import Node



def main():


    node = NeighboringNodes(7,True)

    print("Building grid")
    node.build_grid()

    ind = node.find_index(3)
    print("Finding the 3rd node")
    print(ind)


    square = node.find_neighbors(m=1, ntype='SQUARE', x=2, y=2)
    print('Square Neighbors')
    print(square)

    cross = node.find_neighbors(m=2,ntype='CROSS', x = 3, y = 3)
    print('Cross neighbors')
    print(cross)

    diamond = node.find_neighbors(m = 3, ntype='DIAMOND', x = 3, y = 3)
    print('Diamond neighbors')
    print(diamond)


    square_edge = node.find_neighbors(m = 1, ntype= 'SQUARE', i = 14)
    print('Square Edge Neighbors')
    print(square_edge)

if __name__ == '__main__':
    main()