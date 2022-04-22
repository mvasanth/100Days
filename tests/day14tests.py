import unittest
import sys
from unittest import result
sys.path.insert(1, '/workspaces/advent2021/src')
import day14

class testDay14(unittest.TestCase):
    def testApplyStep(self):
        template = "NNCB"
        rules = [
            "CH -> B",
            "HH -> N",
            "CB -> H",
            "NH -> C",
            "HB -> C",
            "HC -> B",
            "HN -> C",
            "NN -> C",
            "BH -> H",
            "NC -> B",
            "NB -> B",
            "BN -> B",
            "BB -> N",
            "BC -> B",
            "CC -> N",
            "CN -> C"
        ]
        ruleDict = day14.getRuleDict(rules)
        self.assertEqual(16, len(ruleDict))
        template = day14.applyStep(template, ruleDict)
        self.assertEqual("NCNBCHB", template)
    
    def testDay14Part1(self):
        template = "NNCB"
        rules = [
            "CH -> B",
            "HH -> N",
            "CB -> H",
            "NH -> C",
            "HB -> C",
            "HC -> B",
            "HN -> C",
            "NN -> C",
            "BH -> H",
            "NC -> B",
            "NB -> B",
            "BN -> B",
            "BB -> N",
            "BC -> B",
            "CC -> N",
            "CN -> C"
        ]
        ruleDict = day14.getRuleDict(rules)
        template = day14.applySteps(template, ruleDict, 10)
        self.assertEqual(3073, len(template))
        result = day14.getPartOneResult(template)
        self.assertEqual(1588, result)
    
if __name__ == '__main__':
    unittest.main()