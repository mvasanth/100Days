"""
Implementatin of Day 4 of Advent of Code 2021.
More details of the challenge can be found here:
https://adventofcode.com/2021/day/4
"""
from typing import Final

INPUT_NUMBERS: Final = "/workspaces/advent2021/src/day4_1.txt"
BINGO_BOARDS: Final = "/workspaces/advent2021/src/day4.txt"
ROWS: Final = 5
COLUMNS: Final = 5

class Square:
    """
    Models one square in a Bingo Board game.
    Each square has a row, a column, the value and a flag to indicate if the number has already
    been seen in the game so far.
    """
    def __init__(self, num, row, column, marked):
        self.num = num
        self.row = row
        self.column = column
        self.marked = marked
    
    def getNum(self):
        return self.num
    
    def getRow(self):
        return self.row
    
    def getColumn(self):
        return self.column
    
    def getMarked(self):
        return self.marked

class Board:
    def __init__(self, grid):
        self.grid = grid

    def mark(self, num):
        for square in self.grid:
            if square.num == num:
                square.marked = True

    def isRowMarked(self):
        for row in range(ROWS):
            if self.grid[row].marked == False:
                return False
        
        return True

    def isColumnMarked(self):
        for column in range(COLUMNS):
            if self.grid[column].marked == False:
                return False
        
        return True

    def isMarked(self):
        if self.isRowMarked() or self.isColumnMarked():
            return True
        
        return False
    
    def getScore(self, num):
        """
        The score of a game of Bingo is calculated as the sum of all the unmarked numbers,
        multiplied by the last number that gave the win.
        
        Input: Last num that completed the game.
        
        Output: Score for this score."""
        score = 0

        for square in self.grid:
            if not square.marked:
                score += int(square.num)
        
        score *= int(num)

        return score

class Bingo:
    def __init__(self, boards):
        self.boards = boards
    
    def playGame(self):
        pass

def getNumList(file):
    """
    Given an input file comma separated numbers, return a list of integers.
    """
    try:
        inFile = open(file, 'r')
    except OSError:
        print("Could not open file")
        raise FileNotFoundError

    line = inFile.readline()

    nums = line.split(',')

    inFile.close()

    return nums

def main():
    nums = getNumList(INPUT_NUMBERS)

if __name__ == '__main__':
    main()

class Day4:
    def __init__(self, boards):
        self.boards = boards
    
