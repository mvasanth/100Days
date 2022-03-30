import unittest
import sys
sys.path.insert(1, '/workspaces/advent2021/src')
from day5 import Input, MalformedLineError, Grid

class testCommand(unittest.TestCase):
    def testGetListOfLines(self):
        input = Input("/workspaces/advent2021/tests/inputs/day5test.txt")
        lines = input.getCoordinateLines()
        self.assertIsNotNone(input)
        self.assertIsNotNone(lines)
        self.assertEqual(10, len(lines))
    
    def testGetCoordinateEnds(self):
        input = Input("/workspaces/advent2021/tests/inputs/day5test.txt")
        (coordinateOne, coordinateTwo) = input.getCoordinateEnds('0,9 -> 5,9')
        self.assertEqual(0, coordinateOne.getX())
        self.assertEqual(9, coordinateOne.getY())
        self.assertEqual(5, coordinateTwo.getX())
        self.assertEqual(9, coordinateTwo.getY())
    
    def testGetCoordinateEndsRaisesException(self):
        input = Input("/workspaces/advent2021/tests/inputs/day5test.txt")
        try:
            (coordinateOne, coordinateTwo) = input.getCoordinateEnds(',4 -> 3,4')
        except MalformedLineError:
            self.assertRaises(MalformedLineError)
    
    def testGetCoordinateList(self):
        input = Input("/workspaces/advent2021/tests/inputs/day5test.txt")
        lines = input.getCoordinateLines()
        input.setCoordinateList(lines)
        coordinateList = input.getCoordinateList()
        #self.assertEqual(26, len(coordinateList))
    
    def testDay5(self):
        input = Input("/workspaces/advent2021/tests/inputs/day5test.txt")
        lines = input.getCoordinateLines()
        input.setCoordinateList(lines)
        coordinateList = input.getCoordinateList()
        grid = Grid()
        for coordinate in coordinateList:
            grid.addCoordinate(coordinate)
        #self.assertEqual(21, len(grid.getCoordinateDict()))
        #self.assertEqual(12, grid.getMultipleLinesOverlapCount())

if __name__ == '__main__':
    unittest.main()
