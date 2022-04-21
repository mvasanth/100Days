"""
Implementatin of Day 8 of Advent of Code 2021.
More details of the challenge can be found here:
https://adventofcode.com/2021/day/8
"""
from typing import Final

# The number of segments that need to be turned on to make the digit on the left in a 
# seven segment display
NUM_SEGMENTS_ONE: Final = 2
NUM_SEGMENTS_FOUR: Final = 4
NUM_SEGMENTS_SEVEN: Final = 3
NUM_SEGMENTS_EIGHT: Final = 7

def getLines(file):
    """
    Given an input file, retuns a list of lines, where each line is a string representing the
    signal pattern for a seven segment display system.
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

class SevenSegmentDisplay():
    """
    Models a seven segment display that has signals and outputs.
    The signals are strings representing the digits 0-9.
    The outputs are the actual digits that are displayed on the seven segment display.
    """
    def __init__(self, line):
        signalsAndOutputs = line.split(" ")
        self.signals = signalsAndOutputs[:10]
        self.outputs = signalsAndOutputs[11:]

        # sort each string in signals and outputs lexicographically
        self.signals = [''.join(sorted(s)) for s in self.signals]
        self.outputs = [''.join(sorted(o)) for o in self.outputs]

def getSevenSegmentDisplays(lines):
    """
    Input: A list of strings.
    
    Output: Returns a list of seven segment displays which includes both the signals and the outputs.
    """
    sevenSegmentDisplays = [SevenSegmentDisplay(line) for line in lines]
    return sevenSegmentDisplays

def getOutputValues(sevenSegmentDisplays):
    """
    Input: A list of seven segment displays with both signals and outputs.
    
    Output: A list of integers representing the output values, i.e, takes in the strings for the 
            output values and returns the integers represented by the strings.
    """
    outputVals = []

    for s in sevenSegmentDisplays:
        ssdict = getSevenSegmentDict(s.signals)
        outputVal = getOutputValue(s.outputs, ssdict)
        outputVals.append(outputVal)

    return outputVals

def set_difference(a, b):
    """
    Input: Two strings a and b.
    
    Output: Converts each string to a set, computes the set difference and returns a string of the
            subtracted set.
    """
    setA = set(a)
    setB = set(b)
    return "".join(setA - setB)

def getSevenSegmentDict(signals):
    """
    Input: A list of strings representing all the 10 digits (0-9).
    
    Output: A dictionary that is keyed by the string representation of a digit, and the value is
            the digit itself.
    """
    # get the ones that have unique lengths first
    one = [s for s in signals if len(s) == NUM_SEGMENTS_ONE][0]
    four = [s for s in signals if len(s) == NUM_SEGMENTS_FOUR][0]
    seven = [s for s in signals if len(s) == NUM_SEGMENTS_SEVEN][0]
    eight = [s for s in signals if len(s) == NUM_SEGMENTS_EIGHT][0]
    
    # build the rest based on the unique digits
    nine = [s for s in signals
            if len(s) == 6 
            and len(set_difference(four, s)) == 0
            and len(set_difference(seven, s)) == 0][0]
    
    six = [s for s in signals
            if len(s) == 6 
            and len(set_difference(one, s)) == 1][0]
    
    zero = [s for s in signals
            if len(s) == 6
            and s != six 
            and s != nine][0]
    
    three = [s for s in signals
             if len(s) == 5
             and len(set_difference(s, seven)) == 2][0]
    
    five = [s for s in signals
            if len(s) == 5
            and len(set_difference(s, four)) == 2
            and s != three][0]
    
    two = [s for s in signals
            if len(s) == 5
            and s != five
            and s != three][0]
    
    # store them in a dictionary for quick lookup
    sevenSegmentDict = {
        zero: '0',
        one: '1',
        two: '2',
        three: '3',
        four: '4',
        five: '5',
        six: '6',
        seven: '7',
        eight: '8',
        nine: '9'
    }

    return sevenSegmentDict

def getOutputValue(output, sevenSegmentDict):
    """
    Given a list of strings representing a single four digit output, returns the integer value
    of the output strings.
    """
    outputValue = "".join([sevenSegmentDict[o] for o in output])
    return int(outputValue)

def getUniqueOutputCount(sevenSegmentDisplays):
    """
    Input: A list of seven segment displays that have both signals and outputs. 
    
    Output: The count of the number of times the digits 1, 4, 7 and 8 appear in the outputs.
    """
    # get all the outputs
    outputs = [ssd.outputs for ssd in sevenSegmentDisplays]
    outputs = [o for sublist in outputs for o in sublist]

    # get a count of all the ones that have unique length
    uniqueOutputCount = len( [o for o in outputs
                                if len(o) == NUM_SEGMENTS_ONE
                                or len(o) == NUM_SEGMENTS_FOUR
                                or len(o) == NUM_SEGMENTS_SEVEN
                                or len(o) == NUM_SEGMENTS_EIGHT] )
    
    return uniqueOutputCount

def main():
    SIGNALS_AND_OUTPUTS: Final = "/workspaces/advent2021/src/inputs/day8.txt"
    lines = getLines(SIGNALS_AND_OUTPUTS)

    # Part 1: Get the count of the occurrences of 1, 4, 7 and 8 in the outputs.
    sevenSegmentDisplays = getSevenSegmentDisplays(lines)
    uniqueOutputCount = getUniqueOutputCount(sevenSegmentDisplays)
    print("Count of the number of output signals made of unique digits are: {}"
    .format(uniqueOutputCount))

    # Part 2: Get the sum of all the 4 digit outputs.
    sevenSegmentDisplays = getSevenSegmentDisplays(lines)
    outputValues = getOutputValues(sevenSegmentDisplays)
    print("Sum of all the output values = {}".format(sum(outputValues)))

if __name__ == "__main__":
    main()