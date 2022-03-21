import unittest
import sys
sys.path.insert(1, '/workspaces/advent2021/src')
import day1

class testDay1(unittest.TestCase):

    def testGetDepthIncreaseCountNonEmptyList(self):
        depthList = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        self.assertEqual(7, day1.getDepthIncreaseCount(depthList))
    
    def testGetDepthIncreaseCountEmptyList(self):
        depthList = []
        self.assertEqual(0, day1.getDepthIncreaseCount(depthList))
    
    def testGetAggregateDepthListNonEmptyList(self):
        depthList = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        self.assertEqual([607, 618, 618, 617, 647, 716, 769, 792], day1.getAggregateDepthList(depthList))
    
    def testGetAggregateDepthListEmptyList(self):
        depthList = []
        self.assertEqual([], day1.getAggregateDepthList(depthList))

if __name__ == '__main__':
    unittest.main()