import unittest
import sys
sys.path.insert(1, '/workspaces/advent2021/src')
import day10
from day10 import SyntaxErrorHandling

class testSyntaxNavSubsystem(unittest.TestCase):
    def testMiddleScore(self):
        syntaxLines = ['[({(<(())[]>[[{[]{<()<>>',
                       '[(()[<>])]({[<{<<[]>>(',
                       '{([(<{}[<>[]}>{[]{[(<()>',
                       '(((({<>}<{<{<>}{[]{[]{}',
                       '[[<[([]))<([[{}[[()]]]',
                       '[{[{({}]{}}([{[{{{}}([]',
                       '{<[[]]>}<{[{[{[]{()[[[]',
                       '[<(<(<(<{}))><([]([]()',
                       '<{([([[(<>()){}]>(<<{{',
                       '<{([{{}}[<[[[<>{}]]]>[]]']
        
        (illegalCharDict, matchStrings) = day10.getIllegalCharDictAndMatchStrings(syntaxLines)
        syntaxErrorHandling = SyntaxErrorHandling(illegalCharDict)
        totalErrors = syntaxErrorHandling.getTotalSyntaxErrorScore()
        self.assertEqual(26397, totalErrors)

        self.assertEqual(5, len(matchStrings))
        completionStrs = day10.getCompletionStrings(matchStrings)
        self.assertEqual(5, len(completionStrs))

        scores = day10.getScoresList(completionStrs)
        self.assertEqual(5, len(scores))
        middleScore = day10.getMiddleScore(scores)
        self.assertEqual(288957, middleScore)

if __name__ == '__main__':
    unittest.main()