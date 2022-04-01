"""
Implementatin of Day 9 of Advent of Code 2021.
More details of the challenge can be found here:
https://adventofcode.com/2021/day/9
"""
from typing import Final

HEIGHTS: Final = "/workspaces/advent2021/src/inputs/day9.txt"
FIRST_ROW:Final = 0
FIRST_COLUMN: Final = 0

def getHeightLines(file):
    """
    Given a file where each line is a sequence of digits 0-9, returns each line of the file as
    a separate string.
    """
    try:
        inFile = open(file, 'r')
    except OSError:
        print("Could not open file")
        raise FileNotFoundError

    heightLines = inFile.readlines()

    # strip the trailing newline at the end of each line
    heightLines = [line.strip() for line in heightLines]

    inFile.close()

    return heightLines

def getHeightMap(heightLines):
    """
    Given a list of strings of equal length where each string is a sequence of digits, return a
    dictionary where the key is a tuple with the row and column (the position of the height in the map),
    and the value is an integer representing the height.
    """
    row = 0
    heightMap = {}

    for heightLine in heightLines:
        column = 0

        for height in heightLine:
            key = (row, column)
            heightMap[key] = int(height)
            column += 1
        
        row += 1
    
    return (heightMap, row, column)

def isLowPoint(point, row, column, rows, columns, heightMap):

    # generate offset positions (0, +1), (0, -1), (+1, 0), (-1, 0)
    neighbours = [ point.OffsetBy(0, 1), point.OffsetBy(0, -1), point.OffsetBy(1, 0), point.OffsetBy(-1, 0) ]

    # filter out invalid positions
    validNeighbours = [ n for n in neighbours if n.x >= 0 and n.x < columns and n.y >= 0 and n.y < rows ]

    # use a loop over valid positions to see if `point` is lowest
    neighbourHeights = [ heightMap(n.x, n.y) for n in validNeighbours ]
    
    pointHeight = heightMap(point.x, point.y)

    if (neighbourHeights.All(h => h < pointHeight))
    {
        # we have found a low point.
    }

    if row == FIRST_ROW:
        if column == FIRST_COLUMN:
            # this is the top left corner
            if (point < heightMap[(row, column + 1)]
                and point < heightMap[(row + 1, column)]):
                return True
            else:
                return False
        
        elif column == columns - 1:
            # this is the top right corner
            if (point < heightMap[(row, column - 1)]
                and point < heightMap[row + 1, column]):
                return True
            else:
                return False
        else:
            # this is the top edge of the map
            if (point < heightMap[(row, column - 1)]
                and point < heightMap[(row, column + 1)]
                and point < heightMap[row + 1, column]):
                return True
            else:
                return False
    
    if row == rows - 1:
        if column == FIRST_COLUMN:
            # this is the bottom left corner
            if (point < heightMap[(row - 1, column)]
                and point < heightMap[(row, column + 1)]):
                return True
            else:
                return False
    
        elif column == columns - 1:
            # this is the bottom right corner
            if (point < heightMap[(row - 1, column)]
                and point < heightMap[(row, column - 1)]):
                return True
            else:
                return False
    
        else:
            # this is the bottom edge
            if (point < heightMap[(row, column - 1)]
                and point < heightMap[(row, column + 1)]
                and point < heightMap[(row - 1, column)]):
                return True
            else:
                return False
    
    if column == FIRST_COLUMN:
        # this is the left edge
        if (point < heightMap[(row - 1, column)]
            and point < heightMap[(row + 1, column)]
            and point < heightMap[(row, column + 1)]):
            return True
        else:
            return False

    if column == columns - 1:
        # this is the right edge
        if (point < heightMap[(row - 1, column)]
            and point < heightMap[(row + 1, column)]
            and point < heightMap[(row, column - 1)]):
            return True
        else:
            return False

    # general case
    if (point < heightMap[(row, column + 1)]
        and point < heightMap[row, column - 1]
        and point < heightMap[row + 1, column]
        and point < heightMap[row - 1, column]):
        return True
    
    return False

def getLowPoints(heightMap, rows, columns):
    lowPoints = []

    for row in range(rows):
        for column in range(columns):
            point = heightMap[(row, column)]

            if isLowPoint(point, row, column, rows, columns, heightMap):
                lowPoints.append(point)
    
    return lowPoints

def getTotalRiskLevel(lowPoints):
    riskLevel = 0

    for lowPoint in lowPoints:
        # The risk level of a low point is 1 plus it's height
        riskLevel += lowPoint + 1

    return riskLevel
                
def main():
    heightLines = getHeightLines(HEIGHTS)
    (heightMap, rows, columns) = getHeightMap(heightLines)
    lowPoints = getLowPoints(heightMap, rows, columns)
    riskLevel = getTotalRiskLevel(lowPoints)
    print("Risk Level = {}".format(riskLevel))

if __name__ == "__main__":
    main()