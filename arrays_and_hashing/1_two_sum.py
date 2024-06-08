'''
https://leetcode.com/problems/two-sum/description/
'''

def twoSum(nums, target):
    subtracted = [target - x for x in nums]
    for i, x in enumerate(subtracted):
        if x in nums and nums.index(x) != i:
            return [i, nums.index(x)]

# test cases
nums1 = [2,7,11,15]
    #   [7, 2, -2, -6]
target1 = 9 # [0, 1]

nums2 = [3,2,4]
target2 = 6 # [1, 2]

nums3 = [3,3]
target3 = 6 # [0, 1]

def main():
    print(twoSum(nums1, target1))
    print(twoSum(nums2, target2))
    print(twoSum(nums3, target3))

if __name__ == "__main__":
    main()
