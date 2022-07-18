"""
Implementatin of Day 15 of Advent of Code 2021.
More details of the challenge can be found here:
https://adventofcode.com/2021/day/15
"""
from queue import PriorityQueue
from typing import Final
from utilities.Coordinate import Coordinate

class RiskLevel:
    def __init__(self, riskLevel):
        max_distance: Final = 10000000

        self.riskLevel = riskLevel
        self.visited = False
        self.distance = max_distance
    
    def markVisisted(self):
        self.visited = True
    
    def isVisited(self):
        return self.visited
    
    def setDistance(self, distance):
        self.distance = distance
    
    def getDistance(self):
        return self.distance

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

def getRiskLevelGrid(lines):
    riskLevelGrid = {}

    rows = len(lines)
    columns = len(lines[0])

    for row in range(rows):
        # get the list of energy levels associated with this row
        riskLevelList = list(lines[row])

        for column in range(columns):
            coordinate = Coordinate(row, column)
            riskLevelGrid[coordinate] = RiskLevel(int(riskLevelList[column]))
    
    return riskLevelGrid

def getNeighbours(coordinate, riskLevelGrid):
    potentialNeighbours = [
        coordinate.getOffset(0, -1),
        coordinate.getOffset(0, 1), # left and right neighbours
        coordinate.getOffset(-1, 0),
        coordinate.getOffset(+1, 0)] # top and bottom neighbours

    validNeighbours = [neighbour for neighbour in potentialNeighbours
                        if neighbour in riskLevelGrid]
                        
    return validNeighbours

def dijkstra(riskLevelGrid):

    pq = PriorityQueue()

    for coordinate in riskLevelGrid.keys():

        # nothing to do if this node is already visited
        if riskLevelGrid[coordinate].isVisited():
            continue
        
        riskLevelGrid[coordinate].setDistance = 0
        pq.put(coordinate)

        while not pq.empty():
            u = pq.pop()

            # get all the neighbours of this node
            neighbours = getNeighbours(coordinate, riskLevelGrid)
            
        



    # get the source coordinate, set its distance to 0
    source = riskLevelGrid[coordinate]
    riskLevelGrid[coordinate].setDistance = 0

    # push the source vertex to the Priority Queue
    vertices = PriorityQueue()
    vertices.put(source.getDistance(), coordinate)

    while not vertices.empty():
        u = vertices.get()



def main():
    RISK_LEVELS: Final = "/workspaces/advent2021/src/inputs/day15.txt"
    lines = getLines(RISK_LEVELS)
    riskLevelGrid = getRiskLevelGrid(lines)
    dijkstra(riskLevelGrid)
    
if __name__ == "__main__":
    main()