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
    Each square has the value and a flag to indicate if the number has already
    been seen in the game so far.
    """
    def __init__(self, num, marked):
        self.num = num
        self.marked = marked
    
    def getNum(self):
        return self.num
    
    def getMarked(self):
        return self.marked
    
    def setMarked(self, marked):
        self.marked = marked

class Board:
    def __init__(self, grid):
        self.grid = grid
        self.isCompleted = False
    
    def getIsCompleted(self):
        return self.isCompleted
    
    def setIsCompleted(self, isCompleted):
        self.isCompleted = isCompleted

    def mark(self, num):
        for square in self.grid:
            if square.num == num:
                square.setMarked(True)

    def isRowMarked(self):
        for i in range(0, ROWS * COLUMNS, 5):
            count = 0
            for j in range(i, ROWS * COLUMNS):
                if self.grid[j].getMarked() == True:
                    count += 1
                else:
                    # found one that isn't marked, skip this row
                    break
                
                if count == ROWS:
                    return True
            
        return False

    def isColumnMarked(self):
        for i in range(0, ROWS):
            count = 0
            for j in range(i, ROWS * COLUMNS, 5):
                if self.grid[j].getMarked() == True:
                    count += 1
                else:
                    # found one that isn't marked, skip this column
                    break
                
                if count == COLUMNS:
                    return True
            
        return False

    def isComplete(self):
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
                score += square.num
        
        score *= num

        return score
    
    def markSquare(self, num):
        for square in self.grid:
            if num == square.getNum():
                square.setMarked(True)

class Bingo:
    def __init__(self, boards, nums):
        self.boards = boards
        self.nums = nums
    
    def playGame(self):
        for num in self.nums:
            for board in self.boards:
                # mark this number on each board
                board.markSquare(num)

                # this board has won the game! 
                if board.isComplete() == True:
                    score = board.getScore(num)
                    return (board, score)
        
        # there was no winning board
        return (None, None)
    
    def playGameLastWins(self):
        for num in self.nums:
            for board in self.boards:
                # mark this number on each board
                board.markSquare(num)

                if board.getIsCompleted() == True:
                    # move on, we want to find that last board that wins the game
                    continue
                elif board.isComplete() == True: 
                    score = board.getScore(num)
                    board.setIsCompleted(True)
                    lastScore = score
                    lastBoard = board
        
        # there was no winning board
        return (lastBoard, lastScore)    

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

    nums = [int(num) for num in nums]
    return nums

def getListOfLines(file):
    try:
        inFile = open(file, 'r')
    except OSError:
        print("Could not open file")
        raise FileNotFoundError

    lines = inFile.readlines()

    # strip the trailing newline at the end of each line
    lines = [line.strip() for line in lines]

    inFile.close()

    return lines

def getRawGrids(lines):
    rawGrids = []
    rawGrid = []

    for line in lines:
        if line == '':
            # end of one grid
            rawGrids.append(rawGrid)
            # reset 
            rawGrid = []
        else:
            rawNums = line.split(" ")
            nums = rawNums[:]
            for num in rawNums:
                if num == '':
                    nums.remove(num)
                else:
                    rawGrid.append(int(num))
    
    # append the last raw grid to the list
    rawGrids.append(rawGrid)
    return rawGrids

def getBingoBoardsFromRawGrids(rawGrids):
    boards = []

    for rawGrid in rawGrids:
        board = getBingoBoardFromRawGrid(rawGrid)
        boards.append(board)
    
    return boards

def getBingoBoardFromRawGrid(rawGrid):
    grid = []

    for i in range(ROWS * COLUMNS):
        square = Square(rawGrid[i], False)
        grid.append(square)
    
    board = Board(grid)
    return board

def main():
    # Setup
    nums = getNumList(INPUT_NUMBERS)
    lines = getListOfLines(BINGO_BOARDS)
    rawGrids = getRawGrids(lines)
    boards = getBingoBoardsFromRawGrids(rawGrids)

    bingo = Bingo(boards, nums)
    (board, score) = bingo.playGame()

    # PART 1: Find the first board that wins the game and it's score
    if board == None and score == None:
        print("No winning board")
    else:
        print("Winning board score: {}".format(score))
        print("The board has: ")
        for square in board.grid:
            print(square.getNum(), end=" ")
        print("\n")

    # PART 2: Find the last board that wins the game and it's score
    (lastboard, lastscore) = bingo.playGameLastWins()
    print("Last winning board score: {}".format(lastscore))
    print("The board has: ")
    for square in lastboard.grid:
        print(square.getNum(), end=" ")
    print("\n")

if __name__ == '__main__':
    main()