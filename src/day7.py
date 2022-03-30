"""
Implementatin of Day 7 of Advent of Code 2021.
More details of the challenge can be found here:
https://adventofcode.com/2021/day/7
"""
from typing import Final

POSITION_FILE: Final = "/workspaces/advent2021/src/inputs/day7.txt"

def getCrabPositions(file):
    """
    Given a string with comma separated list of integers representing the horizontal positions of crabs,
    returns a list of integers where each integer corresponds to the horizontal position of a crab.
    """
    try:
        inFile = open(file, 'r')
    except OSError:
        print("Could not open file")
        raise FileNotFoundError

    positions = inFile.readline()

    inFile.close()

    positions = positions.split(",")

    positions = [int(timer) for timer in positions]

    return positions

class CrabFuelConsumption:
    """
    Models the rate at which fuel is consumed by crabs as they move to their most optimal position. 
    Needs a list of horizontal positions (list of integers) and provides APIs to determine the least
    fuel consumed for fixed rate and variable rate.
    """
    def __init__(self, positions):
        self.positions = positions
        self.sumDict = self.buildSumDict(max(positions) + 1)
    
    def getFixedRateFuelConsumption(self):
        """
        Given a list of positions, returns a list of tuples where each tuple has the position and
        the fixed fuel consumption associated with that position.
        """
        maxP = max(self.positions)
        posAndFuels = []

        for i in range(maxP + 1):
            fuel = 0

            for pos in self.positions:
                fuel += abs(pos - i)
            
            posAndFuels.append((i, fuel))

        return posAndFuels
    
    def buildSumDict(self, steps):
        sumDict = {}

        for i in range(steps):
            sum = 0
            for val in range(i + 1):
                sum += val
            
            sumDict[i] = sum

        return sumDict
    
    def getVariableRateFuelConsumption(self):
        """
        Given a list of positions, returns a list of tuples where each tuple has the position and
        the variable fuel consumption associated with that position.
        """
        maxP = max(self.positions)
        posAndFuels = []

        for i in range(maxP + 1):
            fuel = 0
            steps = 0

            for pos in self.positions:
                steps = abs(pos - i)
                fuel += self.sumDict[steps]
            
            posAndFuels.append((i, fuel))

        return posAndFuels

def getBestFuelConsumption(posAndFuels):
    """
    Given a list of tuples of postions and the fuel consumption associated with that position,
    returns the least/most efficient fuel that can be consumed by the crabs to move to the
    optimal position.
    """
    fuels = [x[1] for x in posAndFuels]
    bestFuel = min(fuels)
    return bestFuel

def main():
    """
    Implementation of Day 7 of the Advent Calender 2021.
    """
    positions = getCrabPositions(POSITION_FILE)
    crabFuelConsumption = CrabFuelConsumption(positions)

    # Part 1: Get the least fixed rate fuel consumption
    posAndFuels = crabFuelConsumption.getFixedRateFuelConsumption()
    bestFuel = getBestFuelConsumption(posAndFuels)
    print("The least amount of fuel that can be consumed is {}".format(bestFuel))

    # Part 2: Get the least variable rage fuel consumption
    varPosAndFuels = crabFuelConsumption.getVariableRateFuelConsumption()
    bestVarFuel = getBestFuelConsumption(varPosAndFuels)
    print("The least amount of fuel that can be consumed with variable fuel consumption is {}"
    .format(bestVarFuel))

if __name__ == "__main__":
    main()