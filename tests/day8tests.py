import unittest
import sys
sys.path.insert(1, '/workspaces/advent2021/src')
import day8

class testCommand(unittest.TestCase):
    def testGetNumberUniqueDigits(self):
        signalPatterns = day8.getSignalPatterns("/workspaces/advent2021/tests/day8test.txt")
        outputSignals = day8.getCompleteListOfFourDigitOutputSignals(signalPatterns, 11, 15)
        numberUniqueDigits = day8.getUniqueDigitSignalCount(outputSignals)
        self.assertEqual(26, numberUniqueDigits)

    def testGetTotalOfOutputSignals(self):
        signalPatterns = day8.getSignalPatterns("/workspaces/advent2021/tests/day8test.txt")
        outputSignals = day8.getCompleteListOfFourDigitOutputSignals(signalPatterns, 11, 15)
        total = day8.getTotalOfOutputSignals(outputSignals)
        self.assertEqual(61229, total)

if __name__ == '__main__':
    unittest.main()