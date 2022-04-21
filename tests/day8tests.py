from importlib.machinery import BYTECODE_SUFFIXES
import unittest
import sys
sys.path.insert(1, '/workspaces/advent2021/src')
import day8
from day8 import SevenSegmentDisplay

class testCommand(unittest.TestCase):
    def testGetUniqueOutputCount(self):
        lines = [
            "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
            "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
            "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
            "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
            "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
            "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
            "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
            "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
            "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
            "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"
        ]
        sevenSegmentDisplays = day8.getSevenSegmentDisplays(lines)
        uniqueOutputCount = day8.getUniqueOutputCount(sevenSegmentDisplays)
        self.assertEqual(26, uniqueOutputCount)

    def testGetSevenSegmentDict(self):
        signals = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcfefg", "abcdfg"]
        sevenSegmentDict = day8.getSevenSegmentDict(signals)
        self.assertEqual(10, len(sevenSegmentDict))
        for number, signal in enumerate(signals):
            self.assertEqual(number, int(sevenSegmentDict[signal]))
    
    def testGetOutputValue(self):
        line = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
        sevenSegmentDisplay = SevenSegmentDisplay(line)
        ssDict = day8.getSevenSegmentDict(sevenSegmentDisplay.signals)
        outputVal = day8.getOutputValue(sevenSegmentDisplay.outputs, ssDict)
        self.assertEqual(5353, outputVal)
    
    def testGetSevenSegmentDisplays(self):
        lines = [
            "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
            "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
            "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
            "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
            "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
            "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
            "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
            "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
            "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
            "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"
        ]
        sevenSegmentDisplays = day8.getSevenSegmentDisplays(lines)
        outputVals = day8.getOutputValues(sevenSegmentDisplays)
        self.assertEqual(61229, sum(outputVals))

if __name__ == '__main__':
    unittest.main()