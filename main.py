from NeighboringNodes import NeighboringNodes
from Node import Node



def main():


    node = NeighboringNodes(5,True)

    node.buildGrid()

    # ind = node.findIndex(3)
    # print("found ind 3")
    # print(ind)



    square = node.find_neighbors(m=1, ntype='SQUARE', x=2, y=2)

    print(square)

    cross = node.find_neighbors(m=2,ntype='CROSS', x = 3, y = 3)
    print('Cross neighbors')
    print(cross)

    diamond = node.find_neighbors(m = 3, ntype='DIAMOND', x = 3, y = 3)
    print('Diamond neighbors')
    print(diamond)


if __name__ == '__main__':
    main()