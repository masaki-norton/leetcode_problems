"""
https://leetcode.com/problems/search-in-rotated-sorted-array/description/
"""

def search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    m = (l + r) // 2

    while l <= r:
        if nums[m] <= nums[r]:    # right side sorted
            if nums[m] == target:   # found answer
                return m
            elif nums[m] < target <= nums[r]:   # is within right side
                l = m + 1
                m = (l + r) // 2
            else:                               # is not within right side
                r = m - 1
                m = (l + r) // 2
        else:               # left side sorted
            if nums[m] == target:   # found answer
                return m
            elif nums[l] <= target < nums[m]:   # is within left side
                r = m - 1
                m = (l + r) // 2
            else:                               # is not within left side
                l = m + 1
                m = (l + r) // 2
    return -1       # escaped while loop,

# Test Cases
nums1 = [4,5,6,7,0,1,2]
target1 = 0     # 4

nums2 = [4,5,6,7,0,1,2]
target2 = 4     # -1

nums3 = [1]
target3 = -1    # -1

def main():
    print(search(nums1, target1))
    print(search(nums2, target2))
    print(search(nums3, target3))
    return None

if __name__ == "__main__":
    main()
