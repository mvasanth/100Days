from turtle import pos
import unittest
import sys
sys.path.insert(1, '/workspaces/advent2021/src')
import day7
from day7 import CrabFuelConsumption

class testCommand(unittest.TestCase):
    def testGetLeastFixedRateFuel(self):
        positions = [16,1,2,0,4,2,7,1,2,14]
        crabFuelConsumption = CrabFuelConsumption(positions)
        posAndFuels = crabFuelConsumption.getFixedRateFuelConsumption()
        self.assertEqual(17, len(posAndFuels))
        self.assertEqual(37, day7.getBestFuelConsumption(posAndFuels))
    
    def testGetLeastVariableRateFuel(self):
        positions = [16,1,2,0,4,2,7,1,2,14]
        crabFuelConsumption = CrabFuelConsumption(positions)
        posAndFuels = crabFuelConsumption.getVariableRateFuelConsumption()
        self.assertEqual(17, len(posAndFuels))
        self.assertEqual(168, day7.getBestFuelConsumption(posAndFuels))
    
if __name__ == '__main__':
    unittest.main()