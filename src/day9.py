"""
Implementatin of Day 9 of Advent of Code 2021.
More details of the challenge can be found here:
https://adventofcode.com/2021/day/9
"""
import queue
from typing import Final
from collections import Counter
from utilities.Coordinate import Coordinate

HEIGHTS: Final = "/workspaces/advent2021/src/inputs/day9.txt"
MAX_HEIGHT: Final = 9

def getRawHeights(file):
    """
    Given a file where each line is a sequence of digits 0-9, returns each line of the file as
    a separate string.
    """
    try:
        inFile = open(file, 'r')
    except OSError:
        print("Could not open file")
        raise FileNotFoundError

    rawHeights = inFile.readlines()

    # strip the trailing newline at the end of each line
    rawHeights = [line.strip() for line in rawHeights]

    inFile.close()

    return rawHeights

class Height():
    """
    Models a height object as defined in Day 9 of the Advent calender 2021.
    Every height has a value indicating it's height, a boolean to indicate if it is a low point
    and a basin, which is a list of all the heights that flow into a particular low point. 
    Note that a height has a basin only if it is a low point.
    """
    def __init__(self, height):
        self.height = height
        self.isLowPoint = False
        self.colour = 0

    def getHeight(self):
        return self.height
    
    def getIsLowPoint(self):
        return self.isLowPoint
    
    def setIsLowPoint(self,isLowPoint):
        self.isLowPoint = isLowPoint
    
    def setColour(self, colour):
        self.colour = colour
    
    def getColour(self):
        return self.colour
    
    def isColourSet(self):
        return True if self.colour > 0 else False

class HeightGrid():
    def __init__(self, rawHeights):
        self.heightGrid = self.buildHeightGrid(rawHeights)
    
    def buildHeightGrid(self, rawHeights):
        heightGrid = {}

        rows = len(rawHeights)
        columns = len(rawHeights[0])

        for row in range(rows):
            # get the list of energy levels associated with this row
            heightList = list(rawHeights[row])

            for column in range(columns):
                coordinate = Coordinate(row, column)
                height = Height(int(heightList[column]))
                heightGrid[coordinate] = height
        
        return heightGrid

    def getHeightGrid(self):
        return self.heightGrid
    
    def getHeightForCoordinate(self, coordinate):
        return self.heightGrid[coordinate].getHeight()
    
    def markLowPoint(self, coordinate):
        neighbours = self.getNeighbours(coordinate)
        
        # get the height of this coordinate
        height = self.getHeightForCoordinate(coordinate)

        # check if its height is lower than all its neighbours
        if all(height < self.getHeightForCoordinate(neighbour) 
                for neighbour in neighbours):
            self.heightGrid[coordinate].setIsLowPoint(True)

    def markLowPoints(self):
        for coordinate in self.heightGrid:
            self.markLowPoint(coordinate)        
    
    def getRiskLevel(self):
        riskLevel = sum ([height.getHeight() + 1 for height in self.heightGrid.values()
                        if height.getIsLowPoint()])

        return riskLevel
    
    def getNeighbours(self, coordinate):
        potentialNeighbours = [
            coordinate.getOffset(0, -1),
            coordinate.getOffset(0, 1), # left and right neighbours
            coordinate.getOffset(-1, 0),
            coordinate.getOffset(+1, 0)] # top and bottom neighbours

        validNeighbours = [neighbour for neighbour in potentialNeighbours
                            if neighbour in self.heightGrid]
                            
        return validNeighbours

    def getBasinNeighbours(self, coordinate):
        basinNeighbours = [neighbour for neighbour in self.getNeighbours(coordinate)
                            if self.heightGrid[neighbour].getHeight() != MAX_HEIGHT]

        return basinNeighbours

    def setColourForCoordinate(self, coordinate, colour):
        self.heightGrid[coordinate].setColour(colour)

    def colourGrid(self):
        colourableCoordinates = [coordinate for coordinate in self.heightGrid.keys()
                            if self.heightGrid[coordinate].getHeight() != MAX_HEIGHT]
        colour = 1
        Q = queue.Queue()

        for coordinate in colourableCoordinates:
            
            if self.heightGrid[coordinate].isColourSet():
                continue

            Q.put(coordinate)

            while not Q.empty():
                u = Q.get()

                # colour this coordinate
                self.setColourForCoordinate(u, colour)

                basinNeighbours = self.getBasinNeighbours(u)

                for v in basinNeighbours:
                    if not self.heightGrid[v].isColourSet():
                        # if this neighbour is not coloured, add it to the queue
                        Q.put(v)
                
            colour += 1

def getOrderedBasinSizes(heightGrid):
    heights = [heightGrid[coordinate] for coordinate in heightGrid.keys()
                if heightGrid[coordinate].getHeight() != MAX_HEIGHT]

    colours = [height.colour for height in heights]

    colourCounts = Counter(colours)
    sortedColours = dict(sorted(colourCounts.items(), key=lambda item: item[1], reverse=True))
    return sortedColours

def getFinalResult(sortedColours):
    basinSizes = list(sortedColours.values())
    return (basinSizes[0] * basinSizes[1] * basinSizes[2])

def main():
    rawHeights = getRawHeights(HEIGHTS)

    # PART 1
    heightGrid = HeightGrid(rawHeights)
    heightGrid.markLowPoints()
    riskLevel = heightGrid.getRiskLevel()
    print("Risk Level = {}".format(riskLevel))

    # PART 2
    heightGrid = HeightGrid(rawHeights)
    heightGrid.colourGrid()
    sortedColours = getOrderedBasinSizes(heightGrid.getHeightGrid())
    result = getFinalResult(sortedColours)
    print("Final Result = {}".format(result))

if __name__ == "__main__":
    main()