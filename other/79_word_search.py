"""
https://leetcode.com/problems/word-search/
"""
from collections import deque

def dfs(visited, row, col, board, word, letter):
    # this letter is wrong
    if (row < 0 or row >= len(board) or col < 0 or col >= len(board[row])\
        or board[row][col] != word[letter] or [row, col] in visited):
        return False

    # this letter is correct, log in visited, and move onto next letter
    visited.append([row, col])
    letter += 1
    if len(visited) == len(word):
        return True

    if dfs(visited, row - 1, col, board, word, letter): # up
        return True
    if dfs(visited, row + 1, col, board, word, letter): # down
        return True
    if dfs(visited, row, col - 1, board, word, letter): # left
        return True
    if dfs(visited, row, col + 1, board, word, letter): # right
        return True

    visited.pop()
    return False

def exists(board: list[list[str]], word: str) -> bool:

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == word[0]:  # first letter match
                visited = deque([])
                letter = 0
                if dfs(visited, row, col, board, word, letter):
                    return True
    return False

# Test Cases
board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]    # True
board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]    # True
board3 = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]    # True

word1 = "ABCCED"
word2 = "SEE"
word3 = "ABCESEEEFS"

def main() -> None:
    print(exists(board3, word3))
    return

if __name__ == "__main__":
    main()
