import unittest
import sys
from unittest import result
sys.path.insert(1, '/workspaces/advent2021/src')
import day14

class testDay14(unittest.TestCase):
    def testDay14(self):
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

        # PART 1
        templateDict = day14.applySteps(template, ruleDict, 10)
        letterDict = day14.getLetterDict(templateDict)
        result = day14.getFinalResult(letterDict)
        self.assertEqual(1588, result)

        # PART 2
        templateDict = day14.applySteps(template, ruleDict, 40)
        letterDict = day14.getLetterDict(templateDict)
        result = day14.getFinalResult(letterDict)
        self.assertEqual(2188189693529, result)
    
if __name__ == '__main__':
    unittest.main()