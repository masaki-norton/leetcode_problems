'''
https://leetcode.com/problems/valid-sudoku/
'''

def isValidSudoku(board: list[list[str]]) -> bool:
    # check rows
    for row in board:
        nums = [x for x in row if x != "."]
        if sorted(list(set(nums))) != sorted(nums):
            return False

    # check cols
    for i in range(9):
        col = [x for x in [row[i] for row in board] if x!="."]
        if sorted(list(set(col))) != sorted(col):
            return False

    # check 3x3 grids
    for a in range(0,9,3):
        for b in range(0,9,3):
            curr_grid = []
            for y in range(a, a+3):
                for z in range(b, b+3):
                    curr_grid.append(board[y][z])
            nums = [x for x in curr_grid if x != "."]
            if sorted(list(set(nums))) != sorted(nums):
                return False
    return True

# test cases
board1 = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]   # true

board2 = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]   # false

def main():
    print(isValidSudoku(board1))
    print(isValidSudoku(board2))

if __name__ == "__main__":
    main()
