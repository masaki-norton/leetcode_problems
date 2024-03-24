"""
https://leetcode.com/problems/find-the-duplicate-number/description/?envType=daily-question&envId=2024-03-24
"""

def findDuplicate(nums: list[int]) -> int:
    for x in nums:
        i = abs(x) - 1
        if nums[i] < 0:
            return abs(x)
        nums[i] = nums[i] * -1
    return -1

# test cases
test1 = [1,3,4,2,2] # 2
test2 = [3,1,3,4,2] # 3
test3 = [3,3,3,3,3] # 3

def main() -> None:
    print(findDuplicate(test1))
    print(findDuplicate(test2))
    print(findDuplicate(test3))
    return None

if __name__ == "__main__":
    main()
