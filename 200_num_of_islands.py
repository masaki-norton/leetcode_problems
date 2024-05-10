"""
https://leetcode.com/problems/number-of-islands/
"""

def numIslands(grid: list[list[str]]) -> int:
    counter = 0

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
    print(numIslands(grid1))
    return None

if __name__ == "__main__":
    main()
