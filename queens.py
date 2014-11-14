import numpy as np
from time import time
from sys import stdout

N = 6

def incrementBoard(board,N):
   board = np.zeros((N,N), dtype='int')
   ar = np.zeros(N-1, dtype='int')
   ar = np.append(ar, [1])

   for i in xrange(N):
      np.random.shuffle(ar)
      board[i] = ar

   return board
   
def vertical(board):
   s = np.sum(board, axis = 0)

   return (s == np.ones(N)).all()

   
def diagonal(board):
   for i in xrange(-N,N):
      if np.sum(np.diagonal(board,i)) > 1:
         return False

   fp = np.fliplr(board)
   
   for i in xrange(-N,N):
      if np.sum(np.diagonal(fp,i)) > 1:
         return False

   return True


if __name__ == "__main__":
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
      if not vertical(board):
         continue
      if not diagonal(board):
         continue   
      
      print "\n\nDone!\n"
      print board
      print "\nTime: %3.3fs" %((time()-timer))
      exit()