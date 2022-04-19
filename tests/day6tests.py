import unittest
import sys
sys.path.insert(1, '/workspaces/advent2021/src')
import day6

class testDay6(unittest.TestCase):
    def testSimulateLanternfishGrowth(self):
        timers = [3,4,3,1,2]
        # check after 18 days
        fishCount = day6.getFishCountList(timers)
        fishCount = day6.simulateDays(fishCount, 18)
        self.assertEqual(26, sum(fishCount))
        
        # check after 80 days
        fishCount = day6.getFishCountList(timers)
        fishCount = day6.simulateDays(fishCount, 80)
        self.assertEqual(5934, sum(fishCount))
        
        # check after 256 days
        fishCount = day6.getFishCountList(timers)
        fishCount = day6.simulateDays(fishCount, 256)
        self.assertEqual(26984457539, sum(fishCount))

if __name__ == '__main__':
    unittest.main()