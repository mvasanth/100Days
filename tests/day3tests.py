import unittest
import sys
sys.path.insert(1, '/workspaces/advent2021/src')
import day3

class testCommand(unittest.TestCase):
    def testGetDigitStringList(self):
        digitStringList = day3.getDigitStringList("/workspaces/advent2021/tests/day3test.txt")
        self.assertIsNotNone(digitStringList)
        self.assertEqual(5, len(digitStringList))
        self.assertEqual('011110011100', digitStringList[0])
        self.assertEqual('010001010101', digitStringList[1])
        self.assertEqual('111111110000', digitStringList[2])
        self.assertEqual('011101100011', digitStringList[3])
        self.assertEqual('000111100100', digitStringList[4])

if __name__ == '__main__':
    unittest.main()
