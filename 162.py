"""
https://leetcode.com/problems/find-peak-element/description/

"""

def findPeakElement(nums: list[int]) -> int:
    l = 0
    r = len(nums) - 1
    m = (l + r) // 2

    while l <= r:
        if m > 0 and nums[m] < nums[m - 1]:
            r = m - 1
            m = (l + r) // 2
        elif m < (len(nums) - 1) and nums[m] < nums[m + 1]:
            l = m + 1
            m = (l + r) // 2
        else:
            return m


### Test Cases
nums1 = [1,2,3,1]   # 2
nums2 = [1,2,1,3,5,6,4] # 5, 1

def main() -> None:
    print(findPeakElement(nums2))
    return None

if __name__ == "__main__":
    main()
