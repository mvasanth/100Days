"""
Implementatin of Day 7 of Advent of Code 2021.
More details of the challenge can be found here:
https://adventofcode.com/2021/day/11
"""
from typing import Final
from utilities.Coordinate import Coordinate

ENERGY_LEVLES: Final = "/workspaces/advent2021/src/inputs/day11.txt"
INVALID_ENERGY_LEVEL: Final = -1
INVALID_FLASH_COUNT: Final = -1
HIGHEST_ENERGY_LEVEL: Final = 9

def getOctopusEnergyLevelStrings(file):
    """
    Given a file where each line is a sequence of digits 0-9, returns each line of the file as
    a separate string.
    """
    try:
        inFile = open(file, 'r')
    except OSError:
        print("Could not open file")
        raise FileNotFoundError

    energyLevels = inFile.readlines()

    # strip the trailing newline at the end of each line
    energyLevels = [line.strip() for line in energyLevels]

    inFile.close()

    return energyLevels

class Octopus():
    """
    Models an octopus. Every octopus has an energy level and a flash count indicating the number of
    times it has flashed. Exposes APIs to modify energy levels and flash counts.
    """
    def __init__(self, energy, flashes):
        self.energy = energy
        self.flashes = flashes
        self.hasFlashed = False
    
    def getEnergy(self):
        return self.energy
    
    def getFlashes(self):
        return self.flashes
    
    def incrementEnergy(self):
        self.energy += 1
    
    def resetEnergy(self):
        self.energy = 0
    
    def incrementFlashes(self):
        self.flashes += 1

    def setHasFlashed(self, hasFlashed):
        self.hasFlashed = hasFlashed

    def getHasFlashed(self):
        return self.hasFlashed

class OctoGrid():
    """
    Models the grid consisting of coordinates and octopus associated with this coordinate.
    The grid is represented using a dictionary, where the key is the coordinate and the value
    is an octopus object. Exposes APIs to simulate a step taken by the octopus and modifies the
    grid.
    """
    def __init__(self, energyLevels):
        self.energyLevels = energyLevels
        self.octoGrid = self.buildOctoGrid()
    
    def getOctoGrid(self):
        return self.octoGrid
    
    def buildOctoGrid(self):
        octoGrid = {}

        # For ease of finding neighbours of a given coordinate in the grid, we will also populate
        # the edges outside the given set of coordinates i.e, row: -1 and row: max + 1 and
        # column: -1 and column: max + 1. 

        rows = len(self.energyLevels)
        columns = len(self.energyLevels[0])

        for row in range(-1, rows + 1):
            # get the list of energy levels associated with this row
            if not (row == -1 or row == rows):
                energyList = list(self.energyLevels[row])

            for column in range(-1, columns + 1):
                coordinate = Coordinate(row, column)

                if row == -1 or row == rows or column == -1 or column == columns:
                    octopus = Octopus(INVALID_ENERGY_LEVEL, INVALID_FLASH_COUNT)
                    octoGrid[coordinate] = octopus
                else:
                    octopus = Octopus(int(energyList[column]), 0)
                    octoGrid[coordinate] = octopus
        
        return octoGrid
    
    def simulateStep(self):
        """
        Simulates a sinle step taken by the octopi.
        During a single step, the following occurs:

        - First, the energy level of each octopus increases by 1.
        - Then, any octopus with an energy level greater than 9 flashes. 
          This increases the energy level of all adjacent octopuses by 1, including octopuses 
          that are diagonally adjacent. If this causes an octopus to have an energy level greater than 9,
          it also flashes. This process continues as long as new octopuses keep having their energy level
          increased beyond 9. (An octopus can only flash at most once per step.)
        - Finally, any octopus that flashed during this step has its energy level set to 0,
          as it used all of its energy to flash.
        """
        # get a list of all the valid coordinates
        validCoordinates = [coordinate for coordinate in self.octoGrid
                        if self.octoGrid[coordinate].getEnergy() != INVALID_ENERGY_LEVEL]
        
        # clear flashed states from the previous step
        [self.octoGrid[coordinate].setHasFlashed(False) for coordinate in validCoordinates]
        
        # increment the energy level of all octopi
        [self.octoGrid[coordinate].incrementEnergy() for coordinate in validCoordinates]

        # get a list of all coordinates whose octopus has flashed (energy level > highest)
        highEnergyCoordinates = [coordinate for coordinate in validCoordinates
                                if self.octoGrid[coordinate].getEnergy() > HIGHEST_ENERGY_LEVEL]
        
        # as they have exceed the highest energy limit, these octopi have flashed
        [self.octoGrid[coordinate].setHasFlashed(True) for coordinate in highEnergyCoordinates]
        [self.octoGrid[coordinate].incrementFlashes() for coordinate in highEnergyCoordinates]

        # Reset the energy for these octopi as they have used up all their energy by flashing
        [self.octoGrid[coordinate].resetEnergy() for coordinate in highEnergyCoordinates]

        # neighbours of high energy octopi have benefits too!
        for coordinate in highEnergyCoordinates:
            
            x = coordinate.getX()
            y = coordinate.getY()

            # get all it's neighbours 
            neighbours = [coordinate.getOffset(0, -1), coordinate.getOffset(0, 1), # left and right neighbours
                          coordinate.getOffset(-1, 0), coordinate.getOffset(+1, 0), # top and bottom neighbours
                          coordinate.getOffset(-1, -1), coordinate.getOffset(-1, +1), # top diagonal neighbours
                          coordinate.getOffset(1, -1), coordinate.getOffset(1, 1)] # bottom diagonal neighbours
            
            validNeighbours = [neighbour for neighbour in neighbours
                                if self.octoGrid[neighbour].getEnergy() != INVALID_ENERGY_LEVEL]
            
            for neighbour in validNeighbours:

                if self.octoGrid[neighbour].getHasFlashed():
                    # an octopus can only flash once per step
                    continue
                else:
                    # increment energy
                    octopus = self.octoGrid[neighbour]
                    octopus.incrementEnergy()

                    if octopus.getEnergy() > HIGHEST_ENERGY_LEVEL:
                        # this octopus flashes too
                        octopus.setHasFlashed(True)
                        octopus.incrementFlashes()
                        octopus.resetEnergy()
                        highEnergyCoordinates.append(neighbour)
    
    def printGrid(self):
        validOctopi = [octopus for octopus in self.octoGrid.values() 
                        if octopus.getEnergy() != INVALID_ENERGY_LEVEL]

        i = 0
        for octopus in validOctopi:
            print(octopus.getEnergy(), end=" ")
            i += 1
            if i % 10 == 0:
                print("\n")
        
        print("\n")
    
    def allEqual(self, energyLevels):
        return all(energy == 0 for energy in energyLevels)

    def simulateSteps(self, steps):
        for _ in range(steps):
            self.simulateStep()
    
    def getAllOctopiSynchronizedStep(self):
        step = 0
        energyLevels = [octopus.getEnergy() for octopus in self.octoGrid.values()
                            if octopus.getEnergy() != INVALID_ENERGY_LEVEL]
            
        while not self.allEqual(energyLevels):
            step += 1
            self.simulateStep()
            energyLevels = [octopus.getEnergy() for octopus in self.octoGrid.values()
                            if octopus.getEnergy() != INVALID_ENERGY_LEVEL]
            
        return step
    
    def getTotalFlashes(self):
        totalFlashes = 0

        validOctopi = [octopus for octopus in self.octoGrid.values()
                        if octopus.getEnergy() != INVALID_ENERGY_LEVEL]

        for octopus in validOctopi:
            totalFlashes += octopus.getFlashes()
        
        return totalFlashes

def main():
    energyLevels = getOctopusEnergyLevelStrings(ENERGY_LEVLES)
    octoGrid = OctoGrid(energyLevels)

    # PART 1
    octoGrid.simulateSteps(100)
    flashes = octoGrid.getTotalFlashes()
    print("Total number of flashes = {}".format(flashes))

    # PART 2
    step = octoGrid.getAllOctopiSynchronizedStep()
    print("All octopi synchronize at step {}".format(step))

if __name__ == "__main__":
    main()