'''
https://leetcode.com/problems/binary-search/description/
'''

def search(nums: list[int], target:int) -> int:
    l, r = 0, len(nums) - 1
    m = (r - l) // 2

    while l < r:
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m + 1
            m = (r + l) // 2
        else:
            r = m - 1
            m = (r + l) // 2
    return -1

# test cases
nums1 = [-1,0,3,5,9,12]
target1 = 9 # 4

nums2 = [-1,0,3,5,9,12]
target2 = 2 # -1

def main():
    print(search(nums1, target1))
    print(search(nums2, target2))
    return None

if __name__ == "__main__":
    main()
