import numpy as np
import random
from time import time
from sys import stdout

N = 6

def incrementBoard(board,N):
   board = np.zeros((N,N), dtype='int')

   #Populate board with 8 queens
   for i in xrange(N):
      queenps = random.randint(0,N-1)
      board[i][queenps] = 1

   return board
   
def vertical(board):
   s = np.sum(board, axis = 0)

   if (s == np.ones(N)).all():
      return 0
   else:
      return 1

   
def diagonal(board):
   for i in xrange(-N,N):
      if np.sum(np.diagonal(board,i)) > 1:
         return 1

   fp = np.fliplr(board)
   
   for i in xrange(-N,N):
      if np.sum(np.diagonal(fp,i)) > 1:
         return 1

   return 0


if __name__ == "__main__":
   #create board
   timer = time()
   board = []
         
   board = incrementBoard(board,N)

   done = False
   trial = 0

   while not done:
      trial += 1
      stdout.write(" Trials" + "\r%d" % trial)
      stdout.flush()
      exitcheck = 0
      board = incrementBoard(board,N)
      exitcheck = vertical(board)
      if exitcheck == 1:
         continue
      exitcheck = diagonal(board)
      if exitcheck == 1:
         continue   
      
      if exitcheck == 0:
         print "\n\nDone!\n"
         print board
         print "\nTime: %3.4f" %((time()-timer))
         exit()