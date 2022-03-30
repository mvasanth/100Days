"""
Implementatin of Day 5 of Advent of Code 2021.
More details of the challenge can be found here:
https://adventofcode.com/2021/day/5
"""
from typing import Final

COORDINATE_LINES: Final = "/workspaces/advent2021/src/inputs/day5.txt"
OVERLAPPED_LINES: Final = 2

class Coordinate:
    """
    Models a single coordinate.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def __eq__(self, other):
        if not isinstance(other, Coordinate):
            # don't attempt to compare against unrelated types
            return NotImplemented
        
        return self.x == other.getX() and self.y == other.getY()
    
    def __hash__(self):
        return hash((self.x, self.y))

class Grid:
    """
    Models a grid of coordinates. Represented as a dictionary, where the keys are coordinates and
    the values that a count of the number of lines that pass through that coordinate.
    """
    def __init__(self):
        self.coordinateDict = {}
    
    def getCoordinateDict(self):
        return self.coordinateDict
    
    def addCoordinate(self, coordinate):
        if coordinate in self.coordinateDict:
            self.coordinateDict[coordinate] += 1
        else:
            self.coordinateDict[coordinate] = 1

    def getMultipleLinesOverlapCount(self):
        """
        Given a coordinate dictionary, returns a count of all the coordinates that are
        overlapped by two or more lines.
        """
        count = 0

        for count in self.coordinateDict.values():
            if count >= OVERLAPPED_LINES:
                count += 1
        
        return count

class MalformedLineError(Exception):
    """
    Raised when a line in the given input file does not conform to the following syntax:
    x1,y1 -> x2,y2.
    """
    pass

class Input:
    """
    Abstracts all the input file processing and retuns an input that can be readily used by
    the Grid class.
    """
    def __init__(self, file):
        self.inputFile = file
        self.coordinateList = []
    
    def getCoordinateLines(self):
        """
        Given an input file, retuns a list of lines, where each line is an item in the list.
        
        Input: File, given at the time of class construction.
        
        Output: A list containing all the lines in the file.
        """
        try:
            inFile = open(self.inputFile, 'r')
        except OSError:
            print("Could not open file")
            raise FileNotFoundError

        lines = inFile.readlines()

        # strip the trailing newline at the end of each line
        lines = [line.strip() for line in lines]

        inFile.close()

        return lines
    
    def getCoordinateEnds(self, line):
        """
        Given a string that is of the format '0,9 -> 5,9', returns two coordinate objects, 
        corresponding to (0,9) - the start coordiante and (5,9) - the stop coordinate.

        Input: A string of the format listed above.

        Output: A tuple of two coordinate objects.
        """
        try:
            elements = line.split(" ")

            rawCoordinateOne = elements[0].split(",")
            left = Coordinate(int(rawCoordinateOne[0]), int(rawCoordinateOne[1]))

            rawCoordinateTwo = elements[2].split(",")
            right = Coordinate(int(rawCoordinateTwo[0]), int(rawCoordinateTwo[1]))

            return (left, right)
        
        except ValueError:
            raise MalformedLineError
    
    def getCoordinateLine(self, coordinateOne, coordinateTwo):
        """
        Input: Two coordinate objects.
        
        Output: List of coordinate objects, including the two ends.
        """
        coordinateLine = []

        if coordinateOne.getX() == coordinateTwo.getX():
            # the x coordinate is the same, the line is vertical
            if coordinateOne.getY() < coordinateTwo.getY():
                start = coordinateOne.getY()
                end = coordinateTwo.getY() + 1
            else:
                start = coordinateTwo.getY()
                end = coordinateOne.getY() + 1
            
            for y in range (start, end):
                # create a new coordinate with the same x, but different y
                coordinate = Coordinate(coordinateOne.getX(), y)
                coordinateLine.append(coordinate)
            
        # elif coordinateOne.getY() == coordinateTwo.getY():
        #     # the y coordinate is the same, the line is horizontal
        #     if coordinateOne.getX() < coordinateTwo.getX():
        #         start = coordinateOne.getX()
        #         end = coordinateTwo.getX() + 1
        #     else:
        #         start = coordinateTwo.getX()
        #         end = coordinateOne.getX() + 1
            
        #     for x in range(start, end):
        #         # create a new coordinate with the same x, but different y
        #         coordinate = Coordinate(x, coordinateOne.getY())
        #         coordinateLine.append(coordinate)
        
        else:
            slope = ((coordinateTwo.getY() - coordinateOne.getY()) // (coordinateTwo.getX() - coordinateOne.getX()))
            yIntercept = coordinateOne.getY() - slope * coordinateOne.getX()

            if coordinateOne.getX() < coordinateTwo.getX():
                for x in range(coordinateOne.getX(), coordinateTwo.getX()):
                    y = slope * x + yIntercept
                    coordinate = Coordinate(x, y)
                    coordinateLine.append(coordinate)
            else:
                for x in range(coordinateOne.getX(), coordinateTwo.getX(), -1):
                    y = slope * x + yIntercept
                    coordinate = Coordinate(x, y)
                    coordinateLine.append(coordinate)

            # the lines are diagonal at a 45 degree angle
            # if coordinateOne.getX() < coordinateTwo.getX():
            #     startX = coordinateOne.getX()
            #     endX = coordinateTwo.getX() + 1
            # else:
            #     startX = coordinateTwo.getX()
            #     endX = coordinateOne.getX() - 1
            
            # if coordinateOne.getY() < coordinateTwo.getY():
            #     startY = coordinateOne.getY()
            #     endY = coordinateTwo.getY() + 1
            # else:
            #     startY = coordinateTwo.getY()
            #     endY = coordinateOne.getY() -1 
            
            # for x, y in zip(range(startX, endX), range(startY, endY)):
            #     # create a new coordinate
            #     coordinate = Coordinate(x, y)
            #     coordinateLine.append(coordinate)
        
        return coordinateLine
    
    def getCoordinateListFromLines(self, lines):
        """        
        Input: List of strings comprising the lines of the input file.
        
        Output: List of coordinates, includes all the coordinates of all the lines of the grid.
        """
        coordinateList = []

        for line in lines:
            (coordinateOne, coordinateTwo) = self.getCoordinateEnds(line)

            coordinateLine = self.getCoordinateLine(coordinateOne, coordinateTwo)

            coordinateList.extend(coordinateLine)
        
        return coordinateList
    
    def setCoordinateList(self, lines):
        self.coordinateList = self.getCoordinateListFromLines(lines)
    
    def getCoordinateList(self):
        return self.coordinateList

def main():
    input = Input(COORDINATE_LINES)
    lines = input.getCoordinateLines()
    input.setCoordinateList(lines)
    coordinateList = input.getCoordinateList()

    grid = Grid()
    for coordinate in coordinateList:
        grid.addCoordinate(coordinate)

    count = len([v for v in grid.getCoordinateDict().values() if v >= OVERLAPPED_LINES])

    print("The number of coordinates that are overlapped by more than {} lines are {}"
    .format(OVERLAPPED_LINES, count))

if __name__ == '__main__':
    main()