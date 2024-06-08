"""
https://leetcode.com/problems/find-all-duplicates-in-an-array/description/?envType=daily-question&envId=2024-03-25
"""

def findDuplicates(nums: list[int]) -> list[int]:
    return None

# Test Cases
test1 = [4,3,2,7,8,2,3,1]   # [2,3]
test2 = [1,1,2] # [1]
test3 = [1]     # []

def main():
    print(findDuplicates(test1))
    print(findDuplicates(test2))
    print(findDuplicates(test3))
    return None

if __name__ == "__main__":
    main()
