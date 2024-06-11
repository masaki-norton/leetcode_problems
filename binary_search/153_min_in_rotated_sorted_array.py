"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
"""

def findMin(nums: list[int]) -> int:
    l, r = 0, len(nums) - 1
    m = (l + r) // 2

    while l <= r:
        if nums[m] < nums[r]: # throw right side away
            r = m
            m = (l + r) // 2
        else:   # throw left side away
            l = m + 1
            m = (l + r) // 2

    return nums[m]

# Test Cases
nums1 = [11,13,15,17]   # 11
nums2 = [4,5,6,7,0,1,2] # 0
nums3 = [3,4,5,1,2]     # 1
nums4 = [3,1,2] # 1

def main():
    print(findMin(nums1))
    print(findMin(nums2))
    print(findMin(nums3))
    print(findMin(nums4))
    return None

if __name__ == "__main__":
    main()
