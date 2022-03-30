import unittest
import sys
sys.path.insert(1, '/workspaces/advent2021/src')
import day3

class testCommand(unittest.TestCase):
    def testGetDigitStringList(self):
        binaryStrings = day3.getBinaryStringsList("/workspaces/advent2021/tests/inputs/day3test.txt")
        digitStringList = day3.getDigitStringList(binaryStrings)
        self.assertIsNotNone(digitStringList)
        self.assertEqual(5, len(digitStringList))
        self.assertEqual('011110011100', digitStringList[0])
        self.assertEqual('010001010101', digitStringList[1])
        self.assertEqual('111111110000', digitStringList[2])
        self.assertEqual('011101100011', digitStringList[3])
        self.assertEqual('000111100100', digitStringList[4])
    
    def testGetDigitStringListInvalidFile(self):
        binaryStrings = day3.getBinaryStringsList("/workspaces/advent2021/tests/inputs/day3test.txt")
        try:
            digitStringList = day3.getDigitStringList(binaryStrings)
        except:
            self.assertRaises(FileNotFoundError)

    def testGetGammaBinary(self):
        binaryStrings = day3.getBinaryStringsList("/workspaces/advent2021/tests/inputs/day3test.txt")
        digitStringList = day3.getDigitStringList(binaryStrings)
        gammaBin = day3.getGammaBinary(digitStringList)
        self.assertEqual('10110', gammaBin)
    
    def testGetEpsilonBinary(self):
        gammaBin = '10110'
        epsilonBin = day3.getEpsilonBinary(gammaBin)
        self.assertEqual('01001', epsilonBin)
    
    def testGetBinaryToDecimal(self):
        binary = '01001'
        decimal = day3.getBinaryToDecimal(binary)
        self.assertEqual(9, decimal)
    
    def testGetPrunedBinaryList(self):
        binaryStrs = day3.getBinaryStringsList("/workspaces/advent2021/tests/inputs/day3test.txt")
        prunedList = day3.getPrunedBinaryList(binaryStrs, 0, '1')
        self.assertEqual(7, len(prunedList))
    
    def testGetOxygenGeneratorRatingBinary(self):
        binaryStrs = day3.getBinaryStringsList("/workspaces/advent2021/tests/inputs/day3test.txt")
        oxygenGeneratorRating = day3.getOxygenGeneratorRatingBinary(binaryStrs)
        self.assertEqual('10111', oxygenGeneratorRating)
    
    def testGetCO2ScrubberRatingBinary(self):
        binaryStrs = day3.getBinaryStringsList("/workspaces/advent2021/tests/inputs/day3test.txt")
        oxygenGeneratorRating = day3.getCO2ScrubberRatingBinary(binaryStrs)
        self.assertEqual('01010', oxygenGeneratorRating)
    
if __name__ == '__main__':
    unittest.main()
