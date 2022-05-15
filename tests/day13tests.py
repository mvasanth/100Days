import unittest
import sys
from unittest import result
sys.path.insert(1, '/workspaces/advent2021/src')
import day13

class testDay13(unittest.TestCase):
    def testDay13(self):
        lines = [
            "6,10",
            "0,14",
            "9,10",
            "0,3",
            "10,4",
            "4,11",
            "6,0",
            "6,12",
            "4,1",
            "0,13",
            "10,12",
            "3,4",
            "3,0",
            "8,4",
            "1,10",
            "2,14",
            "8,10",
            "9,0",

            "fold along y=7",
            "fold along x=5"
        ]
        
        (grid, foldInstructions) = day13.parseLines(lines)
        grid = day13.executeInstructions(grid, foldInstructions)
        for coord in grid.keys():
            print("x = {}, y = {}".format(coord.getX(), coord.getY()))
        self.assertEqual(16, len(grid))

if __name__ == '__main__':
    unittest.main()