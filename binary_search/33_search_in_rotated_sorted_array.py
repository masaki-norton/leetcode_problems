'''
https://leetcode.com/problems/search-in-rotated-sorted-array/description/
'''

def search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    m = (l + r) // 2

    while l < r:
        print(f"st w: {(l,m,r) = }")
        print(f"{nums[l] = }")
        print(f"{nums[m] = }")
        print(f"{nums[r] = }")
        if nums[m] == target:
            return m
        elif nums[l] <= target < nums[m]:
            r = m - 1
            m = (l + r) // 2
        else:
            r = l + 1
            m = (l + r) // 2
    return -1

# test cases
nums1 = [4,5,6,7,0,1,2]
target1 = 0 # 4
nums2 = [4,5,6,7,0,1,2]
target2 = 6 # 2
nums3 = [6,7,0,1,2,3,4]
target3 = 7 # 1
nums4 = [1]
target4 = 0 # -1

def main():
    print(search(nums1, target1))
    # print(search(nums2, target2))
    # print(search(nums3, target3))
    # print(search(nums4, target4))
    return None

if __name__ == "__main__":
    main()
