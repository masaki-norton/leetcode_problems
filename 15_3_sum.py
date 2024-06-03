'''
https://leetcode.com/problems/3sum/description/
'''

def threeSum(nums: list[int]) -> list[list[int]]:
    nums = sorted(nums)
    output = []
    for i in range(len(nums[:-2])):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]
            if curr_sum > 0:
                right -= 1
            elif curr_sum < 0:
                left += 1
            else:
                output.append([nums[i], nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
    return output

# test cases
nums1 = [-1,0,1,2,-1,-4] # [[-1,-1,2],[-1,0,1]]
nums2 = [0,1,1]  # []
nums3 = [0,0,0]  # [[0,0,0]]
nums4 = [0,0,0,0]   # [[0,0,0]]
nums5 = [-1,0,1,0] # [[-1,0,1]]

def main():
    print(threeSum(nums1))
    print(threeSum(nums2))
    print(threeSum(nums3))
    print(threeSum(nums4))
    print(threeSum(nums5))

if __name__ == "__main__":
    main()
