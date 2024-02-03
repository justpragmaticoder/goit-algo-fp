import unittest
from dijkstra_alg import dijkstra


class Test(unittest.TestCase):
    def test_dijkstra(self):
        graph = {
            "A": {"B": 1, "C": 4},
            "B": {"A": 1, "C": 2, "D": 5},
            "C": {"A": 4, "B": 2, "D": 1},
            "D": {"B": 5, "C": 1},
        }

        start_vertex = "A"
        shortest_distances = dijkstra(graph, start_vertex)

        self.assertEqual(shortest_distances, {"A": 0, "B": 1, "C": 3, "D": 4})
