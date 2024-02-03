import unittest
from dynamic_alg import dynamic_programming
from greedy_alg import greedy_algorithm

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


class Test(unittest.TestCase):
    def test_greedy_alg(self):
        result = greedy_algorithm(items, 150)

        self.assertEqual(result, ["cola", "potato", "pepsi", "hot-dog", "hamburger"])

    def test_dynamic_alg(self):
        result = dynamic_programming(items, 150)

        self.assertEqual(result, ["pizza", "hamburger", "pepsi", "cola", "potato"])
