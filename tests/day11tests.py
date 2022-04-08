import unittest
import sys
sys.path.insert(1, '/workspaces/advent2021/src')
from day11 import OctoGrid

class testDay11(unittest.TestCase):
    def testGetTotalFlashesSmallInput(self):
        energyLevels = ['11111', '19991', '19191', '19991', '11111']
        octoGrid = OctoGrid(energyLevels)
        self.assertEqual(49, len(octoGrid.getOctoGrid()))
        octoGrid.simulateSteps(2)
        flashes = octoGrid.getTotalFlashes()
        self.assertEqual(9, flashes)
    
    def testGetTotalFlashesLargeInput(self):
        energyLevels = ['5483143223', '2745854711', '5264556173', '6141336146', '6357385478',
                        '4167524645', '2176841721', '6882881134', '4846848554', '5283751526']
        octoGrid = OctoGrid(energyLevels)
        octoGrid.simulateSteps(10)
        flashes = octoGrid.getTotalFlashes()
        self.assertEqual(204, flashes)
    
    def testAllOctopiFlashing(self):
        energyLevels = ['5483143223', '2745854711', '5264556173', '6141336146', '6357385478',
                        '4167524645', '2176841721', '6882881134', '4846848554', '5283751526']
        octoGrid = OctoGrid(energyLevels)
        step = octoGrid.getAllOctopiSynchronizedStep()
        self.assertEqual(195, step)
    
if __name__ == '__main__':
    unittest.main()