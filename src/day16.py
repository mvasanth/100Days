"""
Implementatin of Day 16 of Advent of Code 2021.
More details of the challenge can be found here:
https://adventofcode.com/2021/day/16
"""
from typing import Final

def getLine(file):
    """
    Given an input file, returns a list of lines.
    """
    try:
        inFile = open(file, 'r')
    except OSError:
        print("Could not open file")
        raise FileNotFoundError

    line = inFile.readline()

    return line

def main():
    RISK_LEVELS: Final = "/workspaces/advent2021/src/inputs/day16.txt"
    line = getLine(RISK_LEVELS)
    
if __name__ == "__main__":
    main()
