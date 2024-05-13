"""
https://leetcode.com/problems/number-of-islands/
"""

def numIslands(grid: list[list[str]]) -> int:
    if len(grid) == 0:
        return 0

    counter = 0

    def bfs(grid, row, col):
        if (row < 0 or \
            row >= len(grid) or \
            col < 0 or \
            col >= len(grid[row]) or \
            grid[row][col] == "0"):   # if out of bounds or equal to zero
            return

        grid[row][col] = "0"

        bfs(grid, row + 1, col) # up
        bfs(grid, row - 1, col) # down
        bfs(grid, row, col + 1) # right
        bfs(grid, row, col - 1) # left

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "1":
                counter += 1
                bfs(grid, row, col)


    return counter

# Test Cases
grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]   # 1

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]   # 3

def main() -> None:
    print(numIslands(grid1))
    print(numIslands(grid2))
    return None

if __name__ == "__main__":
    main()
