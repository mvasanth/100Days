import unittest
import sys
sys.path.insert(1, '/workspaces/advent2021/src')
import day9
from day9 import HeightGrid

class testDay9(unittest.TestCase):
    def testDay9(self):
        rawHeights = day9.getRawHeights("/workspaces/advent2021/tests/inputs/day9test.txt")
        heightGrid = HeightGrid(rawHeights)
        heightGrid.markLowPoints()
        riskLevel = heightGrid.getRiskLevel()
        self.assertEqual(15, riskLevel)
        heightGrid.populateLowPointBasins()
        lowPoints = heightGrid.getLowPoints()
        self.assertEqual(0, 0)

if __name__ == '__main__':
    unittest.main()