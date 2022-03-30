"""
Implementatin of Day 3 of Advent of Code 2021.
More details of the challenge can be found here:
https://adventofcode.com/2021/day/3
"""
from typing import Final

COMMANDS_FILE: Final = "/workspaces/advent2021/src/inputs/day3.txt"
DIGIT_ZERO: Final = '0'
DIGIT_ONE: Final = '1'

def getDigitStringList(binaryStrs):
    """
    Given a list of binary numbers, returns a new list of binary numbers where each number is
    a concatenation of the 'i'th digit of each number in the original list.
    For example, consider the list [00100, 11110, 10110, 10111], the new list returned is
    [0111, 0100, 1111, 0111, 0001]

    Input: List of strings of binary numbers.

    Output: List of strings of binary numbers of 'i'th digits as described above.
    """
    digitStringList = []

    for i, line in enumerate(binaryStrs):
        chars = list(line)

        for j, char in enumerate(chars):
            if i == 0:
                digitStringList.append(char)
            else:
                digitStringList[j] += char
    
    return digitStringList

def getGammaBinary(digitStringList):
    """
    Given a list of binary numbers, returns a single string representing a binary number.
    The binary number is a concatenation of the most predominant digit (o or 1) in each
    binary number in the original list.
    
    For example, consider the list [0111, 0100, 1111, 0111, 0001], the binary number retruned
    is 10110.

    Input: List of strings representing binary numbers.

    Output: A single string representation of a binary number.
    """
    gammaBin = ''

    for digitStr in digitStringList:
        countZero = 0
        countOne = 0

        for digit in digitStr:
            if digit == DIGIT_ZERO:
                countZero += 1
            else:
                countOne += 1
        
        if countZero > countOne:
            gammaBin += DIGIT_ZERO
        else:
            gammaBin += DIGIT_ONE
    
    return gammaBin

def getEpsilonBinary(gammaBin):
    """
    Given a list of binary numbers, returns a single string representing a binary number.
    The binary number is a concatenation of the least predominant digit (o or 1) in each
    binary number in the original list.
    
    For example, consider the list [0111, 0100, 1111, 0111, 0001], the binary number retruned
    is 01001.

    Input: List of strings representing binary numbers.

    Output: A single string representation of a binary number.
    """
    epsilonBin = ''

    for char in gammaBin:
        if char == DIGIT_ZERO:
            epsilonBin += DIGIT_ONE
        else:
            epsilonBin += DIGIT_ZERO
    
    return epsilonBin

def getBinaryToDecimal(binary):
    """
    Converts the string representation of a binary number to a decimal number.
    
    Input: String representation of a binary number.
    
    Output: Decimal value of the given binary number.
    """
    return int(binary, 2)

def getBinaryStringsList(file):
    """
    Given an input file with the string representation of binary numbers on each line,
    returns a list of strings where each string is a binary number.

    Input: A file with binary numbers on each line.

    Output: list of strings, each representing a binary number.
    """
    try:
        inFile = open(file, 'r')
    except OSError:
        print("Could not open file")
        raise FileNotFoundError

    lines = inFile.readlines()

    # strip the trailing newline at the end of each line
    lines = [line.strip() for line in lines]

    inFile.close()

    return lines

def getPrunedBinaryList(binList, digitPos, digit):
    """
    Given a list of strings representing binary numbers, prune the list based on the digit (0 or 1),
    and the position, such that any string that does not have the given digit at the given position
    is removed.

    For example, consider the list [00100, 11110, 10110, 10111], for position 0 and digit 0, the new
    list returned is [00100].
    
    Input: List of strings representing binary numbers.

    Output: List of strings representing binary numbers with certain strings removed based on the
            criteria listed above.
    """
    binListCopy = binList[:]

    for binStr in binList:
        if binStr[digitPos] != digit:
            binListCopy.remove(binStr)
    
    return binListCopy

def getZeroAndOneCountForPos(binList, digitPos):
    """Given a list of strings representing binary numbers, returns the count of 0's and 1's for a
    given position in all the strings.
    
    For example, consider the list [00100, 11110, 10110, 10111], for position 0, the count
    returned is: countZero = 1, countOne = 3.
    
    Input: List of strings representing binary numbers, and a position.

    Output: A tuple that has the count of 0's and 1's at the given position for all strings.
    """
    countZero = 0
    countOne = 0

    for binStr in binList:
        if binStr[digitPos] == DIGIT_ZERO:
            countZero += 1
        else:
            countOne += 1
    
    return (countZero, countOne)

def getOxygenGeneratorRatingBinary(binList):
    """
    Given a list of strings representing binary numbers, returns the binary string for the
    oxygen generator rating, which is a string in the list, got by pruning the list based on
    the bit criteria described here: https://adventofcode.com/2021/day/3
    
    Input: List of strings representing binary numbers.

    Output: Single string from the list, the oxygen generator rating.
    """
    # keep track of the digit pos
    digitPos = 0

    while (len(binList) != 1):
        (countZero, countOne) = getZeroAndOneCountForPos(binList, digitPos)

        if countZero > countOne:
            binList = getPrunedBinaryList(binList, digitPos, DIGIT_ZERO)
        else:
            binList = getPrunedBinaryList(binList, digitPos, DIGIT_ONE)
        
        digitPos += 1
    
    # list has a single element, the oxygen generator rating
    return binList[0]

def getCO2ScrubberRatingBinary(binList):
    """
    Given a list of strings representing binary numbers, returns the binary string for the
    oxygen generator rating, which is a string in the list, got by pruning the list based on
    the bit criteria described here: https://adventofcode.com/2021/day/3
    
    Input: List of strings representing binary numbers.

    Output: Single string from the list, the co2 scrubber rating.
    """
    # keep track of the digit pos
    digitPos = 0

    while (len(binList) != 1):
        (countZero, countOne) = getZeroAndOneCountForPos(binList, digitPos)

        if countZero <= countOne:
            binList = getPrunedBinaryList(binList, digitPos, DIGIT_ZERO)
        else:
            binList = getPrunedBinaryList(binList, digitPos, DIGIT_ONE)
        
        digitPos += 1
    
    # list has a single element, the co2 scrubber rating
    return binList[0]

def main():
    """ Implementaion for Day 3 of Advent 2021. """

    # PART 1: Compute Power Consumption based on gamma and epsilon.
    binaryStrings = getBinaryStringsList(COMMANDS_FILE)
    digitStringList = getDigitStringList(binaryStrings)
    gammaBin = getGammaBinary(digitStringList)
    epsilonBin = getEpsilonBinary(gammaBin)
    
    gamma = getBinaryToDecimal(gammaBin)
    epsilon = getBinaryToDecimal(epsilonBin)
    powerConsumption = gamma * epsilon
    print("Power Consumption is {}".format(powerConsumption))

    # PART 2: Compute the life support rating based on the oxygen generator rating
    #         and the co2 scrubber rating.
    binaryStrings = getBinaryStringsList(COMMANDS_FILE)
    oxygenGeneratorRatingBin = getOxygenGeneratorRatingBinary(binaryStrings)
    co2ScrubberRatingBin = getCO2ScrubberRatingBinary(binaryStrings)

    oxygenGeneratorRating = getBinaryToDecimal(oxygenGeneratorRatingBin)
    co2ScrubberRating = getBinaryToDecimal(co2ScrubberRatingBin)
    lifeSupportRating = oxygenGeneratorRating * co2ScrubberRating
    print("Life Support Rating is {}".format(lifeSupportRating))

if __name__ == '__main__':
    main()
    