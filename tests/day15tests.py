import unittest
import sys
from unittest import result
sys.path.insert(1, '/workspaces/advent2021/src')
import day15

class testDay15(unittest.TestCase):
    def testDay15(self):
        lines = [
            "1163751742",
            "1381373672",
            "2136511328",
            "3694931569",
            "7463417111",
            "1319128137",
            "1359912421",
            "3125421639",
            "1293138521",
            "2311944581"
        ]
        riskLevelGrid = day15.getRiskLevelGrid(lines)
        pass

if __name__ == '__main__':
    unittest.main()