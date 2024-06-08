'''
https://leetcode.com/problems/contains-duplicate/description/
'''

def containsDuplicate(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))

# Test Cases
nums1 = [1,2,3,1]   # true
nums2 = [1,2,3,4]   # false
nums3 = [1,1,1,3,3,4,3,2,4,2]   # true

def main():
    print(containsDuplicate(nums1))
    print(containsDuplicate(nums2))
    print(containsDuplicate(nums3))

if __name__ == "__main__":
    main()
