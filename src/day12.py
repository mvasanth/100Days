"""
Implementatin of Day 12 of Advent of Code 2021.
More details of the challenge can be found here:
https://adventofcode.com/2021/day/12
"""
from typing import Final

def getLines(file):
    """
    Given an input file, retuns a list of lines, where each line is a string representing the
    connectivity between two caves.
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

def getCaveMap(lines):
    """
    Input: A list of strings, where each string represents the connectivity between two caves.
    
    Output: A dictionary, where the key is a particular cave, and the value is a list of all the
            neighbouring caves.
    """
    caveMap = {}

    for line in lines:
        caves = line.split("-")

        if caves[0] not in caveMap.keys():
            caveMap[caves[0]] = [caves[1]]
        else:
            caveMap[caves[0]].append(caves[1])
    
    return caveMap

def main():
    CAVE_MAP: Final = "/workspaces/advent2021/src/inputs/day12.txt"
    lines = getLines(CAVE_MAP)

    caveMap = getCaveMap(lines)

if __name__ == "__main__":
    main()
