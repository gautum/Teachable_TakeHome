from NeighboringNodes import NeighboringNodes
from Node import Node



def main():


    node = NeighboringNodes(3,True)

    node.buildGrid()

    ind = node.findIndex(3)
    print("found ind 3")
    print(ind)


    ind = node.findIndex(10)





if __name__ == '__main__':
    main()