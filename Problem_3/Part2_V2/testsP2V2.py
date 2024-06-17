import unittest
from p3_with_visualization import GetOptimalStops

class TestRospis(unittest.TestCase):
    def testGetOptimalStops(self):
        # Przykład kodu
        test1 = {1: 9, 2: 8, 3: 6, 4: 5, 5: 19, 6: 10, 7: 15}
        self.assertEqual(GetOptimalStops(test1, 6), [8, 6, 5, 19, 15])

        # Test z pustym słownikiem
        test2 = {}
        self.assertEqual(GetOptimalStops(test2, 6), [])

        # Test z jednym punktem
        test3 = {1: 5}
        self.assertEqual(GetOptimalStops(test3, 1), [5])

        # Test z dwoma punktami
        test4 = {1: 10, 2: 5}
        self.assertEqual(GetOptimalStops(test4, 1), [5, 10])

        # Test z dwoma punktami w odwrotnej kolejności
        test5 = {1: 5, 2: 10}
        self.assertEqual(GetOptimalStops(test5, 1), [10, 5])

        # Test z dużą wartością energii
        test6 = {1: 5, 2: 4, 3: 3, 4: 2, 5: 1}
        self.assertEqual(GetOptimalStops(test6, 10), [4, 3, 2, 1])

        # Test z maksymalną wartością energii
        test7 = {1: 7, 2: 5, 3: 9, 4: 4, 5: 6, 6: 8, 7: 10}
        self.assertEqual(GetOptimalStops(test7, 7), [6, 5, 4, 10, 9])

if __name__ == "__main__":
    unittest.main()
