import unittest
import sys
sys.path.insert(1, '/workspaces/advent2021/src')
import day9

class testDay9(unittest.TestCase):
    def testDay9Part1(self):
        # test getting list of strings off the file
        heightLines = day9.getHeightLines("/workspaces/advent2021/tests/inputs/day9test.txt")

        # test building the height map
        (heightMap, rows, columns) = day9.getHeightMap(heightLines)
        self.assertEqual(50, len(heightMap))
        self.assertEqual(5, rows)
        self.assertEqual(10, columns)

        # test getting low points 
        lowPoints = day9.getLowPoints(heightMap, rows, columns)
        self.assertEqual(4, len(lowPoints))

        # test getting risk level
        riskLevel = day9.getTotalRiskLevel(lowPoints)
        self.assertEqual(15, riskLevel)

    # def testGetTotalOfOutputSignals(self):
    #     signalPatterns = day8.getSignalPatterns("/workspaces/advent2021/tests/inputs/day8test.txt")
    #     outputSignals = day8.getCompleteListOfFourDigitOutputSignals(signalPatterns, 11, 15)
    #     total = day8.getTotalOfOutputSignals(outputSignals)
    #     self.assertEqual(61229, total)

if __name__ == '__main__':
    unittest.main()