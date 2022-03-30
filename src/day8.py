"""
Implementatin of Day 8 of Advent of Code 2021.
More details of the challenge can be found here:
https://adventofcode.com/2021/day/8
"""
from typing import Final
import re

SIGNAL_PATTERNS: Final = "/workspaces/advent2021/src/inputs/day8.txt"
# The number of segments that need to be turned on to make the digit on the left in a 
# seven segment display
ONE: Final = 2
FOUR: Final = 4
SEVEN: Final = 3
EIGHT: Final = 7

digitStringsDict: Final = {
    "acedgfb": 8,
    "cdfbe": 5,
    "gcdfa": 2,
    "fbcad": 3,
    "dab": 7,
    "cefabd": 9,
    "cdfgeb": 6,
    "eafb": 4,
    "cagedb": 0,
    "ab": 1
}

def getSignalPatterns(file):
    """
    Given an input file, retuns a list of lines, where each line is a string representing the
    signal pattern for a seven segment display system.
    """
    try:
        inFile = open(file, 'r')
    except OSError:
        print("Could not open file")
        raise FileNotFoundError

    signalPatterns = inFile.readlines()

    # strip the trailing newline at the end of each line
    signalPatterns = [line.strip() for line in signalPatterns]

    inFile.close()

    return signalPatterns

def getCompleteListOfFourDigitOutputSignals(signalPatterns, begin, end):
    """
    Given a list of strings representing the signal patterns (includes both input and output patterns),
    returns a list of lists, where each inner list has four strings corresponding to each digit in the 
    four digit output signal.
    """
    outputSignals = []

    for pattern in signalPatterns:
        signal = []
        m = re.match(r'([a-z]+) ([a-z]+) ([a-z]+) ([a-z]+) ([a-z]+) ([a-z]+) ([a-z]+) ([a-z]+) ([a-z]+) ([a-z]+) \| ([a-z]+) ([a-z]+) ([a-z]+) ([a-z]+)', pattern)

        # we only care about match groups 11-14, which is the four digit output signal
        # ignore the rest
        for i in range(begin, end):
            signal.append(m.group(i))
        
        outputSignals.append(signal)
        
    return outputSignals

def getUniqueDigitSignalCount(outputSignals):
    """
    Given a list of strings where each string represents an output signal, returns the number of
    output signals that are composed of unique number of seven segment codes, i.e, the number of
    occurrences of 1, 4, 7, and 8 in the output signals.
    """
    count = 0

    for signal in outputSignals:
        for digit in signal:
            if len(digit) == ONE or len(digit) == FOUR or len(digit) == SEVEN or len(digit) == EIGHT:
                count += 1
    
    return count

def getFourDigitOutput(fourDigitOutput):
    """
    Given a list of four strings where each string corresponds to a digit in the seven segment display,
    returns the number that these four strings represent.
    """
    output = 0
    outputStr = ''

    for digit in fourDigitOutput:
        outputStr += digitStringsDict[digit]
    
    output = int(outputStr)
    return output

def getTotalOfOutputSignals(outputSignals):
    total = 0

    for signal in outputSignals:
        total += getFourDigitOutput(signal)
    
    return total

def main():
    signalPatterns = getSignalPatterns(SIGNAL_PATTERNS)
    outputSignals = getCompleteListOfFourDigitOutputSignals(signalPatterns, 11, 15)

    # Part 1
    numberUniqueDigits = getUniqueDigitSignalCount(outputSignals)
    print("Count of the number of output signals made of unique digits are: {}"
    .format(numberUniqueDigits))

    # Part 2
    total = getTotalOfOutputSignals(outputSignals)
    print("Sum of all the four digit signals is {}".format(total))

if __name__ == "__main__":
    main()