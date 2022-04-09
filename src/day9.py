"""
Implementatin of Day 9 of Advent of Code 2021.
More details of the challenge can be found here:
https://adventofcode.com/2021/day/9
"""
from typing import Final
from utilities.Coordinate import Coordinate

HEIGHTS: Final = "/workspaces/advent2021/src/inputs/day9.txt"
INVALID_HEIGHT: Final = -1

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
        self.basin = []

    def getHeight(self):
        return self.height
    
    def getIsLowPoint(self):
        return self.isLowPoint
    
    def getBasin(self):
        return self.basin
    
    def setIsLowPoint(self,isLowPoint):
        self.isLowPoint = isLowPoint
    
    def addToBasin(self, height):
        self.basin.append(height)

class HeightGrid():
    def __init__(self, rawHeights):
        self.rawHeights = rawHeights
        self.heightGrid = self.buildHeightGrid()
    
    def buildHeightGrid(self):
        heightGrid = {}

        # For ease of finding neighbours of a given coordinate in the grid, we will also populate
        # the edges outside the given set of coordinates i.e, row: -1 and row: max + 1 and
        # column: -1 and column: max + 1. 

        rows = len(self.rawHeights)
        columns = len(self.rawHeights[0])

        for row in range(-1, rows + 1):
            # get the list of energy levels associated with this row
            if not (row == -1 or row == rows):
                heightList = list(self.rawHeights[row])

            for column in range(-1, columns + 1):
                coordinate = Coordinate(row, column)

                if row == -1 or row == rows or column == -1 or column == columns:
                    height = Height(INVALID_HEIGHT)
                    heightGrid[coordinate] = height
                else:
                    height = Height(int(heightList[column]))
                    heightGrid[coordinate] = height
        
        return heightGrid

    def getHeightGrid(self):
        return self.heightGrid
    
    def getHeightForCoordinate(self, coordinate):
        return self.heightGrid[coordinate].getHeight()
    
    def setLowPointForCoordinate(self, coordinate, isLowPoint):
        self.heightGrid[coordinate].setIsLowPoint(isLowPoint)
    
    def markLowPoint(self, coordinate):
        if self.getHeightForCoordinate(coordinate) == INVALID_HEIGHT:
            return 
        
        # get all it's neighbours, this is a list of coordinates
        neighbours = [coordinate.getOffset(0, -1), coordinate.getOffset(0, 1), # left and right neighbours
                      coordinate.getOffset(-1, 0), coordinate.getOffset(+1, 0)] # top and bottom neighbours

        # filter out the invalid neighbours    
        validNeighbours = [neighbour for neighbour in neighbours
                            if self.getHeightForCoordinate(neighbour) != INVALID_HEIGHT]
        
        # get the height of this coordinate
        height = self.getHeightForCoordinate(coordinate)

        # check if it's height is lower than all it's neighbours
        if all(height < self.getHeightForCoordinate(neighbour) 
                for neighbour in validNeighbours):
            self.setLowPointForCoordinate(coordinate, True)

    def markLowPoints(self):
        for coordinate in self.heightGrid:
            self.markLowPoint(coordinate)        
    
    def getRiskLevel(self):
        riskLevel = sum ([height.getHeight() + 1 for height in self.heightGrid.values()
                        if height.getIsLowPoint()])

        return riskLevel

    def updateLowPointCoordinateBasin(self, lowPoint, coordinate):
        self.heightGrid[lowPoint].addToBasin(self.getHeightForCoordinate(coordinate))
    
    def populateLowPointBasins(self):
        lowPointCoordinates = [coordinate for coordinate in self.heightGrid.keys()
                                if self.heightGrid[coordinate].getIsLowPoint()]
        
        validCoordinates = [coordinate for coordinate in self.heightGrid.keys() 
                            if self.getHeightForCoordinate(coordinate) != INVALID_HEIGHT]
        
        basinCoordinates = [coordinate for coordinate in validCoordinates
                            if self.getHeightForCoordinate(coordinate) != 9]

        for coordinate in basinCoordinates:
            # get the distance of this coordinate with all the low points
            distCoords = ([((coordinate.getDistance(lpCoordinate)), lpCoordinate) for lpCoordinate in lowPointCoordinates])

            # get the low point that has the least distance with this coordinate
            minDistCoord = min(distCoords, key = lambda t: t[0])

            # add this coordinate to this low point's basin
            self.updateLowPointCoordinateBasin(minDistCoord[1], coordinate)
    
    def getLowPoints(self):
        lowPoints = [self.heightGrid[coordinate] for coordinate in self.heightGrid
                        if self.heightGrid[coordinate].getIsLowPoint()]
        
        return lowPoints
        
def main():
    rawHeights = getRawHeights(HEIGHTS)
    heightGrid = HeightGrid(rawHeights)
    heightGrid.markLowPoints()
    riskLevel = heightGrid.getRiskLevel()
    print("Risk Level = {}".format(riskLevel))

if __name__ == "__main__":
    main()