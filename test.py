import unittest
import NeighboringNodes as NN



class TestNodes(unittest.TestCase):

    def test_building_correct(self):
        node = NN.NeighboringNodes(3,True)
        node.build_grid()

    def test_building_incorrect(self):
        node = NN.NeighboringNodes(2, True)
        node.build_grid()

    def test_square_center_coord(self):
        node = NN.NeighboringNodes(5,False)
        node.buildGrid()
        expected_neighbors = [(1,1),(2,1),(3,1), (1,2), (3,2), (1,3), (2,3), (3,3)]
        self.assertEqual(expected_neighbors, node.find_neighbors(m=1, ntype='SQUARE', x=2, y=2))

    def test_1_index(self):
        node = NN.NeighboringNodes(3,False)
        node.build_grid()
        self.assertEqual((0,1), node.find_index(4))


    def test_square_edge_index(self):
        node = NN.NeighboringNodes(5,False)
        node.build_grid()
        expected_neighbors = [(1,0),(0,1),(1,1)]
        self.assertEqual(expected_neighbors, node.find_neighbors(m=1, ntype='SQUARE', i=1))


    def test_not_in_grid(self):
        node = NN.NeighboringNodes(5, False)
        node.build_grid()

        self.assertRaises(ValueError, node.findNeighbors, 2, ntype = 'DIAMOND', i = 2)
