"""
https://leetcode.com/problems/contiguous-array/?envType=daily-question&envId=2024-03-16

Famous problem, basically find longest substring with equal number of 0's and 1's.
Method is to replace 0's with -1's, create a "sum" array, then see where the
same sum appears twice in the sum array. Monitor max distance with a map.
"""



def findMaxLength(nums: list[int]) -> int:
    nums = [-1 if x == 0 else x for x in nums]
    totals = [0]
    for i in range(len(nums)):
        totals.append(totals[-1] + nums[i])
    visited_nums = {}
    max_distance = 0
    for i, x in enumerate(totals):
        if x not in visited_nums:
            visited_nums[x] = i
        else:
            max_distance = max(max_distance, i - visited_nums[x])
    return max_distance

# Test Cases
nums1 = [0,1,0,0,0,1,0,1,1,0,1,0]
nums2 = [0,1,0,1]

def main() -> None:
    # print(f"{findMaxLength(nums1) = }")
    print(f"{findMaxLength(nums2) = }")
    return None

if __name__ == "__main__":
    main()
