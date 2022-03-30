import unittest
import sys
sys.path.insert(1, '/workspaces/advent2021/src')
import day4
from day4 import Bingo

class testCommand(unittest.TestCase):
    def testGetListOfLines(self):
        lines = day4.getListOfLines("/workspaces/advent2021/tests/inputs/day4test.txt")
        self.assertIsNotNone(lines)
        self.assertEqual(17, len(lines))
    
    def testGetRawGridsFromLines(self):
        lines = day4.getListOfLines("/workspaces/advent2021/tests/inputs/day4test.txt")
        nums = day4.getNumList("/workspaces/advent2021/tests/inputs/day4test_1.txt")
        rawGrids = day4.getRawGrids(lines)
        self.assertIsNotNone(rawGrids)
        self.assertEqual(3, len(rawGrids))
        self.assertEqual(25, len(rawGrids[0]))
        self.assertEqual(25, len(rawGrids[1]))
        self.assertEqual(25, len(rawGrids[2]))
        boards = day4.getBingoBoardsFromRawGrids(rawGrids)
        bingo = Bingo(boards, nums)
        (board, score) = bingo.playGame()
        self.assertEqual(4512, score)
        (lastboard, lastscore) = bingo.playGameLastWins()
        self.assertEqual(1924, lastscore)
    
    def testIsColumnMarked(self):
        grid = [22, 13, 17, 11, 0, 8, 2, 23, 4, 24, 21, 9, 14, 16, 7, 6, 10, 3, 18, 5, 1, 12, 20, 15, 19]
        board = day4.getBingoBoardFromRawGrid(grid)
        board.markSquare(17)
        board.markSquare(23)
        board.markSquare(14)
        board.markSquare(3)
        board.markSquare(20)
        self.assertEqual(True, board.isColumnMarked())
    
    def testIsRowMarked(self):
        grid = [22, 13, 17, 11, 0, 8, 2, 23, 4, 24, 21, 9, 14, 16, 7, 6, 10, 3, 18, 5, 1, 12, 20, 15, 19]
        board = day4.getBingoBoardFromRawGrid(grid)
        board.markSquare(6)
        board.markSquare(10)
        board.markSquare(3)
        board.markSquare(18)
        board.markSquare(5)
        self.assertEqual(True, board.isRowMarked())

if __name__ == '__main__':
    unittest.main()
