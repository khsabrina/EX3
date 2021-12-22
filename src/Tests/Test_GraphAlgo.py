import unittest
import sys
sys.path.append('C:\\Users\\Sabrina\\PycharmProjects\\OOP-Ex3\\src')
from node_data import node_data
from DiGraph import DiGraph
from GraphInterface import GraphInterface
from GraphAlgo import GraphAlgo
from GraphAlgoInterface import GraphAlgoInterface


class MyTestCase(unittest.TestCase):
    def test_get_graph(self):
        Graph = GraphAlgo()
        Graph.load_from_json('A1.json')
        g= Graph.get_graph().v_size()
        self.assertEqual(11, g)  # add assertion here
        g = Graph.get_graph().e_size()
        self.assertEqual(22, g)
        Graph.save_to_json("a")


if __name__ == '__main__':
    unittest.main()
