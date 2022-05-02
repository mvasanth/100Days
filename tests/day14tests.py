import unittest
import sys
from unittest import result
sys.path.insert(1, '/workspaces/advent2021/src')
import day14

class testDay14(unittest.TestCase):
    def testApplyStep(self):
        templateDict = "NNCB"
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
        templateDict = day14.getTemplateDict("NNCB")
        letterDict = day14.getLetterDict("NNCB")
        (letterDict, templateDict) = day14.applyStep(letterDict, templateDict, ruleDict)
        (letterDict, templateDict) = day14.applyStep(letterDict, templateDict, ruleDict)

        templateDict = day14.getTemplateDict("NNNN")
        templateDict = day14.applyStep(templateDict, ruleDict)
        self.assertEqual(2, len(templateDict))
    
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
        templateDict = day14.applySteps(template, ruleDict, 10)
        #self.assertEqual(3073, len(template))
        #result = day14.getPartOneResult(template)
        #self.assertEqual(1588, result)
        pass
    
if __name__ == '__main__':
    unittest.main()