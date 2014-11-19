import sys
import numpy as np

sys.setrecursionlimit(1000000)


class NQueens:

    def __init__(self, boardSize):
        self.size = boardSize
        self.rowBinary = [] * self.size
        self.backtrackCount = 0

    def place(self, startRow=0):
        if len(self.rowBinary) == self.size:
            print('Solution found.')
            print('total backtracks: '+str(self.backtrackCount))
            return self.rowBinary

        else:
            for row in range(startRow, self.size):
                if self.isSafe(len(self.rowBinary), row) is True:
                    self.rowBinary.append(row)
                    return self.place()

            else:
                lastRow = self.rowBinary.pop()
                self.backtrackCount += 1
                return self.place(startRow=lastRow + 1)

    def isSafe(self, col, row):
        for threatRow in self.rowBinary:
            threatCol = self.rowBinary.index(threatRow)
            if row == threatRow or col == self.rowBinary.index(threatRow):
                return False
            elif threatRow + threatCol == row + col or threatRow - threatCol == row - col:
                return False
        return True

n = 5
queens = NQueens(n)
queens.place(0)

board = np.array([['|_|'] * n] * n)
for queen in queens.rowBinary:
    board[queens.rowBinary.index(queen), queen] = '|Q|'


for row in board:
    print ' '.join(row)
