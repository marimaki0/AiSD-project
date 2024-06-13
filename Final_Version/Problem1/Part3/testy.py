import unittest
from part3 import Point, Graham, EdmondsKarp, GeneratePoints

class TestAlgorithms(unittest.TestCase):
    
    def test_Graham_empty(self):
        points = []
        result = Graham(points)
        self.assertEqual(result, [])

    def test_Graham_single_point(self):
        points = [Point(0, 0)]
        result = Graham(points)
        self.assertEqual(result, [Point(0, 0)])

    def test_Graham_two_points(self):
        points = [Point(0, 0), Point(1, 1)]
        result = Graham(points)
        self.assertEqual(result, [Point(0, 0), Point(1, 1)])

    def test_Graham_multiple_points(self):
        points = [Point(0, 0), Point(1, 1), Point(2, 2), Point(0, 2), Point(2, 0)]
        result = Graham(points)
        expected_result = [Point(0, 0), Point(2, 0), Point(2, 2), Point(0, 2)]
        self.assertEqual(result, expected_result)

    def test_EdmondsKarp(self):
        graph = {
            0: {1: 16, 2: 13},
            1: {2: 10, 3: 12},
            2: {1: 4, 4: 14},
            3: {2: 9, 5: 20},
            4: {3: 7, 5: 4},
            5: {}
        }
        source = 0
        sink = 5
        max_flow = EdmondsKarp(graph, source, sink)
        self.assertEqual(max_flow, 23)

if __name__ == "__main__":
    unittest.main()
