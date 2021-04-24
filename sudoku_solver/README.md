# Sudoku solver using the Backtracking Algorithm

## About the project
Given an unsolved sudoku board, the Backtracking Algorithm solves the sudoku board.

### About the Backtracking Algorithm
The Backtracking Algorithm solves the board recursively. 
- It finds empty spots on the board and tries inserting every number from 1 to 9. 
- If the number to be inserted is valid in that spot, then it is inserted.
- After every insertion, it checks if the board is solved (basically a board is solved if there are no more empty spots in the board).
- If the spot is not valid to be inserted, then the algorithm backtracks and replaces the previously inserted numbers, this process repeats.
- If no empty spot is found, then the board is solved and the algorithm ends.