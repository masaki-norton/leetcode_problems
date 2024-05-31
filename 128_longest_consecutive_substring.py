'''
https://leetcode.com/problems/longest-consecutive-sequence/description/
'''

def longestConsecutive(nums: list[int]) -> int:
    max_len = 0
    hash_set = set(nums)
    for x in nums:
        new_max = 1
        if x-1 not in hash_set:
            a = x
            while a+1 in hash_set:
                new_max += 1
                a += 1
            max_len = max(max_len, new_max)
    return max_len

# test cases
nums1 = [100,4,200,1,3,2]   # 4
nums2 = [0,3,7,2,5,8,4,6,0,1]   # 9
nums3 = [2,20,4,10,3,4,5]   # 4

def main():
    print(longestConsecutive(nums1))
    print(longestConsecutive(nums2))
    print(longestConsecutive(nums3))


if __name__ == "__main__":
    main()
