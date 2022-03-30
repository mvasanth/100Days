"""
Implementatin of Day 8 of Advent of Code 2021.
More details of the challenge can be found here:
https://adventofcode.com/2021/day/8
"""
from typing import Final
import re

SIGNAL_PATTERNS: Final = "/workspaces/advent2021/src/day8.txt"
# The number of segments that need to be turned on to make the digit on the left in a 
# seven segment display
ONE: Final = 2
FOUR: Final = 4
SEVEN: Final = 3
EIGHT: Final = 7

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
    returns a list of strings that has the output signals from all the input strings.
    """
    outputSignals = []

    for pattern in signalPatterns:
        m = re.match(r'([a-z]+) ([a-z]+) ([a-z]+) ([a-z]+) ([a-z]+) ([a-z]+) ([a-z]+) ([a-z]+) ([a-z]+) ([a-z]+) \| ([a-z]+) ([a-z]+) ([a-z]+) ([a-z]+)', pattern)

        # we only care about match groups 11-14, which is the four digit output signal
        # ignore the rest
        for i in range(begin, end):
            outputSignals.append(m.group(i))
        
    return outputSignals

def getUniqueDigitSignalCount(outputSignals):
    """
    Given a list of strings where each string represents an output signal, returns the number of
    output signals that are composed of unique number of seven segment codes, i.e, the number of
    occurrences of 1, 4, 7, and 8 in the output signals.
    """
    count = 0

    for signal in outputSignals:
        if len(signal) == ONE or len(signal) == FOUR or len(signal) == SEVEN or len(signal) == EIGHT:
            count += 1
    
    return count

def main():
    signalPatterns = getSignalPatterns(SIGNAL_PATTERNS)
    outputSignals = getCompleteListOfFourDigitOutputSignals(signalPatterns, 11, 15)
    numberUniqueDigits = getUniqueDigitSignalCount(outputSignals)
    print("Count of the number of output signals made of unique digits are: {}"
    .format(numberUniqueDigits))

if __name__ == "__main__":
    main()