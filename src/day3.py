"""
Implementatin of Day 3 of Advent of Code 2021.
More details of the challenge can be found here:
https://adventofcode.com/2021/day/3
"""

COMMANDS_FILE = "/workspaces/advent2021/src/day3.txt"

def getDigitStringList(file):
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
    pass

def getGammaDecimal(gammaBin):
    return getBinaryToDecimal(gammaBin)

def getEpsilonDecimal(epsilonBin):
    return getBinaryToDecimal(epsilonBin)

def getPowerConsumption(gamma, epsilon):
    return (gamma * epsilon)

def main():
    lines = getDigitStringList(COMMANDS_FILE)
    pass

if __name__ == '__main__':
    main()
    