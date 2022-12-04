def findNextEmpty(puzzle):
  # find next row, col on the puzzle that's not filled yet (-1)
  # 0 <= (row, col) <= 8

  for r in range(9):
    for c in range(9):
      if puzzle[r][c] == -1:
        return r, c
  
  return None, None

def isValid(puzzle, guess, row, col):
  # check if guess in row/col is valid
  # return True if valid, False otherwise

  # get row
  rowValues = puzzle[row]

  # get column
  colValues = []
  for i in range(9):
    colValues.append(puzzle[i][col])
  
  # check the guess is already in that row or column
  if guess in rowValues or guess in colValues:
    return False

  # get the square
  rowStart = (row // 3) * 3 # 1 // 3 = 0, 5 // 3 = 1
  colStart = (col // 3) * 3

  for r in range(rowStart, rowStart + 3):
    for c in range(colStart, colStart + 3):
      if guess == puzzle[r][c]:
        return False

  return True

def solveSudoku(puzzle):
  # solve sudoku using backtracking

  # 1: find the next empty space
  row, col = findNextEmpty(puzzle)

  # 1.1: if the puzzle is filled, done
  if row is None:
    return True

  # 2: guess the number in the space found previously
  for guess in range(1, 10):
    # 3: check if the number is valid
    if isValid(puzzle, guess, row, col):
      # 3.1: if valid, place the guess on the puzzle
      puzzle[row][col] = guess
      # recusion time!!
      # 4: call this function recusively
      if solveSudoku(puzzle):
        return True

    # 5: if not valid || if the guess did not solve the puzzle, backtrack and true a new number
    puzzle[row][col] = -1

  # 6: if none of the number is correct, the puzzle is unsolvable
  return False

if __name__ == '__main__':
  board = [
    [-1, -1, -1, -1, -1, -1, 3, 4, 5],
    [5, -1, -1, 7, -1, 8, -1, -1, -1],
    [-1, 1, -1, -1, 3, 5, -1, -1, -1],
    [-1, 3, -1, -1, 5, -1, -1, -1, 1],
    [1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, 5, -1, -1, -1, 2, 3, -1],
    [-1, -1, -1, 8, -1, -1, -1, 2, -1],
    [-1, -1, 1, -1, 4, -1, -1, -1, 9],
    [-1, -1, 7, -1, 1, -1, -1, -1, -1],
  ]

  solveSudoku(board)
  for row in board:
    print(row)
  