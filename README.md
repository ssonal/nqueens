NQUEENS
=======
The NQueens problem is a chess problem where N queens must be placed on an NxN sized chess-board such that none of them threaten each other. 

![8 Queens](/http://schinckel.net/images/2008/06/8queens.jpg)

The problem was published by chess composer Max Bezzel in 1848. It has since caught the fancy of many a programmer, and is commonly used as an example to illustrate [Constraint Satisfaction Problems](http://en.wikipedia.org/wiki/Constraint_satisfaction_problem). 

In this repository I have attempted to employ different techniques to solve this problem including random selections/monte-carlo, backtracking and so on. The repository has been created to play with various programming concepts and python libraries such as [numpy](https://github.com/numpy/numpy).

- [queens.py](https://github.com/sonal-saldanha/nqueens/blob/master/queens.py) is a traditional brute-force approach modified by using some randomness. 
- [queensAlg.py](https://github.com/sonal-saldanha/nqueens/blob/master/queenAlg.py) is another implementation leveraging the power of bitwise representation of numbers and hence, bounds on the positions of queens in adjacent rows/columns.

