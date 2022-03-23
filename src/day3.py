"""
Implementatin of Day 3 of Advent of Code 2021.
More details of the challenge can be found here:
https://adventofcode.com/2021/day/3
"""

COMMANDS_FILE = "/workspaces/advent2021/src/day3.txt"

def getDigitStringList(file):
    """
    Given a list of binary numbers
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

    digitStringList = []

    for i, line in enumerate(lines):
        chars = list(line)

        for j, char in enumerate(chars):
            if i == 0:
                digitStringList.append(char)
            else:
                digitStringList[j] += char
    
    return digitStringList

def getGammaBinary(digitStringList):
    gammaBin = ''

    for digitStr in digitStringList:
        countZero = 0
        countOne = 0

        for digit in digitStr:
            if digit == '0':
                countZero += 1
            else:
                countOne += 1
        
        if countZero > countOne:
            gammaBin += '0'
        else:
            gammaBin += '1'
    
    return gammaBin

def getEpsilonBinary(gammaBin):
    epsilonBin = ''

    for char in gammaBin:
        if char == '0':
            epsilonBin += '1'
        else:
            epsilonBin += '0'
    
    return epsilonBin

def getBinaryToDecimal(binary):
    return int(binary, 2)

def getBinaryStringsList(file):
    """
    Given a list of binary numbers
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
    binListCopy = binList[:]

    for binStr in binList:
        if binStr[digitPos] != digit:
            binListCopy.remove(binStr)
    
    return binListCopy

def getZeroAndOneCountForPos(binList, digitPos):
    countZero = 0
    countOne = 0

    for binStr in binList:
        if binStr[digitPos] == '0':
            countZero += 1
        else:
            countOne += 1
    
    return (countZero, countOne)

def getOxygenGeneratorRatingBinary(binList):
    # keep track of the digit pos
    digitPos = 0

    while (len(binList) != 1):
        (countZero, countOne) = getZeroAndOneCountForPos(binList, digitPos)

        if countZero > countOne:
            binList = getPrunedBinaryList(binList, digitPos, '0')
        else:
            binList = getPrunedBinaryList(binList, digitPos, '1')
        
        digitPos += 1
    
    # list has a single element, the oxygen generator rating
    return binList[0]

def getCO2ScrubberRatingBinary(binList):
    # keep track of the digit pos
    digitPos = 0

    while (len(binList) != 1):
        (countZero, countOne) = getZeroAndOneCountForPos(binList, digitPos)

        if countZero <= countOne:
            binList = getPrunedBinaryList(binList, digitPos, '0')
        else:
            binList = getPrunedBinaryList(binList, digitPos, '1')
        
        digitPos += 1
    
    # list has a single element, the co2 scrubber rating
    return binList[0]

def main():
    # PART 1
    digitStringList = getDigitStringList(COMMANDS_FILE)
    gammaBin = getGammaBinary(digitStringList)
    epsilonBin = getEpsilonBinary(gammaBin)
    
    gamma = getBinaryToDecimal(gammaBin)
    epsilon = getBinaryToDecimal(epsilonBin)
    powerConsumption = gamma * epsilon
    print("Power Consumption is {}".format(powerConsumption))

    # PART 2
    binaryStrings = getBinaryStringsList(COMMANDS_FILE)
    oxygenGeneratorRatingBin = getOxygenGeneratorRatingBinary(binaryStrings)
    co2ScrubberRatingBin = getCO2ScrubberRatingBinary(binaryStrings)

    oxygenGeneratorRating = getBinaryToDecimal(oxygenGeneratorRatingBin)
    co2ScrubberRating = getBinaryToDecimal(co2ScrubberRatingBin)
    lifeSupportRating = oxygenGeneratorRating * co2ScrubberRating
    print("Life Support Rating is {}".format(lifeSupportRating))

if __name__ == '__main__':
    main()
    