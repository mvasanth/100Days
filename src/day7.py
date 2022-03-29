"""
Implementatin of Day 7 of Advent of Code 2021.
More details of the challenge can be found here:
https://adventofcode.com/2021/day/7
"""
from typing import Final

POSITION_FILE: Final = "/workspaces/advent2021/src/day7.txt"

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

def getFuelConsumptionForPosition(positions):
    """
    Given a list of positions, returns a list of tuples where each tuple has the position and
    the fixed fuel consumption associated with that position.
    """
    maxP = max(positions)
    posAndFuels = []

    for i in range(maxP + 1):
        fuel = 0

        for pos in positions:
            fuel += abs(pos - i)
        
        posAndFuels.append((i, fuel))

    return posAndFuels

def getVariableRateFuelConsumption(positions):
    """
    Given a list of positions, returns a list of tuples where each tuple has the position and
    the variable fuel consumption associated with that position.
    """
    maxP = max(positions)
    posAndFuels = []

    for i in range(maxP + 1):
        fuel = 0
        steps = 0

        for pos in positions:
            steps = abs(pos - i)
            fuel += sum([ x for x in range(steps + 1)])
        
        posAndFuels.append((i, fuel))

    return posAndFuels

def getBestFuelConsumption(posAndFuels):
    fuels = [x[1] for x in posAndFuels]
    bestFuel = min(fuels)
    return bestFuel

def main():
    positions = getCrabPositions(POSITION_FILE)
    posAndFuels = getFuelConsumptionForPosition(positions)
    bestFuel = getBestFuelConsumption(posAndFuels)
    print("The least amount of fuel that can be consumed is {}".format(bestFuel))

    varPosAndFuels = getVariableRateFuelConsumption(positions)
    bestVarFuel = getBestFuelConsumption(varPosAndFuels)
    print("The least amount of fuel that can be consumed with variable fuel consumption is {}".format(bestVarFuel))

if __name__ == "__main__":
    main()
