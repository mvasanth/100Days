import unittest
import sys
sys.path.insert(1, '/workspaces/advent2021/src')
import day6

class testCommand(unittest.TestCase):
    def testSimulateLanternfishGrowth(self):
        timers = [3,4,3,1,2]
        lanternfishes = day6.getLanternfishes(timers)
        growth = day6.LanternfishGrowth(lanternfishes, 80)
        count = growth.simulateLanternfishGrowth()
        #self.assertEqual(26984457539, count)
        self.assertEqual(5934, count)

if __name__ == '__main__':
    unittest.main()