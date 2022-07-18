"""
Implementatin of Day 13 of Advent of Code 2021.
More details of the challenge can be found here:
https://adventofcode.com/2021/day/13
"""
from typing import Final
from utilities.Coordinate import Coordinate

def getLines(file):
    """
    Given an input file, returns a list of lines.
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

def parseLines(lines):
    grid = {}
    foldInstructions = []

    for line in lines:
        if line.startswith("fold"):
            # these are fold instructions
            inst = line.split(" ")

            # the instruction to fold along x or y axis is at index 2
            foldInstructions.append(inst[2])
        elif line == "":
            continue
        else:
            # these are the coordinates
            rawCoord = line.split(",")
            coordinate = Coordinate(int(rawCoord[0]), int(rawCoord[1]))
            grid[coordinate] = "#"
    
    return (grid, foldInstructions)

def foldUp(grid, fold):
    minimum = 0
    maximum = max([coordinate.getY() for coordinate in grid.keys()])
    gridCopy = grid.copy()

    for coordinate in grid.keys():
        # if the coordinate is along the fold, then remove this coordinate from the grid
        if coordinate.getY() == int(fold):
            gridCopy.pop(coordinate)
        
        # if the coordinate is on the top part of the fold, do nothing
        elif coordinate.getY() < int(fold):
            continue

        # if the coordinate is on the bottom of the fold, do the fold
        else:
            newY = minimum + (maximum - coordinate.getY())
            newCoord = Coordinate(coordinate.getX(), newY)
            if newCoord not in grid:
                gridCopy[newCoord] = '#'
            gridCopy.pop(coordinate)
    
    return gridCopy

def foldLeft(grid, fold):
    minimum = 0
    maximum = max([coordinate.getX() for coordinate in grid.keys()])
    gridCopy = grid.copy()

    for coordinate in grid.keys():
        # if the coordinate is along the fold, then remove this coordinate from the grid
        if coordinate.getX() == int(fold):
            gridCopy.pop(coordinate)
        
        # if the coordinate is to the left part of the fold, do nothing
        elif coordinate.getX() < int(fold):
            continue

        # if the coordinate is to the right of the fold, do the fold
        else:
            newX = minimum + (maximum - coordinate.getX())
            newCoord = Coordinate(newX, coordinate.getY())
            if newCoord not in grid:
                gridCopy[newCoord] = '#'
            gridCopy.pop(coordinate)
    
    return gridCopy

def executeInstructions(grid, foldInstructions):
    for inst in foldInstructions:
        if inst[0] == "x":
            grid = foldLeft(grid, inst[2:])
        elif inst[0] == "y":
            grid = foldUp(grid, inst[2:])
    
    return grid

def main():
    FOLD_INSTRUCTIONS: Final = "/workspaces/advent2021/src/inputs/day13.txt"
    lines = getLines(FOLD_INSTRUCTIONS)
    (grid, foldInstructions) = parseLines(lines)
    grid = executeInstructions(grid, [foldInstructions[0]])
    for coord in grid.keys():
            print("x = {}, y = {}".format(coord.getX(), coord.getY()))
    print("Number of dots visible after first fold instruction: {}".format(len(grid)))

if __name__ == "__main__":
    main()