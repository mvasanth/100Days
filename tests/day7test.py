from turtle import pos
import unittest
import sys
sys.path.insert(1, '/workspaces/advent2021/src')
import day7

class testCommand(unittest.TestCase):
    def testGetPositionsAndFuelConsumption(self):
        positions = [16,1,2,0,4,2,7,1,2,14]
        posAndFuels = day7.getFuelConsumptionForPosition(positions)
        self.assertEqual(17, len(posAndFuels))
        print(posAndFuels)
    
    def testGetPositionsAndFuelConsumption(self):
        positions = [16,1,2,0,4,2,7,1,2,14]
        posAndFuels = day7.getVariableRateFuelConsumption(positions)
        self.assertEqual(17, len(posAndFuels))
        print(posAndFuels)
    
if __name__ == '__main__':
    unittest.main()