import unittest
import random
from P1 import GetOptimalStops, MakeRandomBrightness

class TestRospis(unittest.TestCase):
    def testGetOptimalStops(self):
        test1 = {1:9, 2:8, 3:6, 4:5, 5:19, 6:10, 7:15} # answer = [8,6,5,19,15,10,9]
        self.assertEqual(GetOptimalStops(test1, 6), [8,6,5,19,15, 10,9])
        test2 = {}

if __name__ == "__main__":
    unittest.main()

### TODO
# - [X] Протестировать алгоритм вручную
# - [ ] Возможно поправить алгоритм
# - [ ] Сделать тесты