'''
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
'''

def twoSum(nums: list[int], target: int) -> list[int]:
    # two pointer approach
    l = 0
    r = len(nums) - 1
    while l < r:
        if nums[l] + nums[r] == target:
            return [l + 1, r + 1]
        elif nums[l] + nums[r] < target:
            l += 1
        else:
            r -= 1

# test cases

numbers1 = [2,7,11,15]
target1 = 9 # [1, 2]
numbers2 = [2,3,4]
target2 = 6 # [1, 3]
numbers3 = [-1,0]
target3 = -1    # [1, 2]

def main():
    print(twoSum(numbers1, target1))
    print(twoSum(numbers2, target2))
    print(twoSum(numbers3, target3))

if __name__ == "__main__":
    main()
