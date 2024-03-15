"""
https://leetcode.com/problems/product-of-array-except-self/description/?envType=daily-question&envId=2024-03-15
"""

def productExceptSelf(nums: list[int]) -> list[int]:
    output = [1] * len(nums)

    # Pass going from left to right
    x = 1
    for i in range(len(nums)):
        output[i] *= x
        x *= nums[i]

    # Pass going from right to left
    x = 1
    for i in range(len(nums) - 1, -1, -1):
        output[i] *= x
        x *= nums[i]

    return output

# Test Cases
nums1 = [1,2,3,4]
nums2 = [-1,1,0,-3,3]


def main() -> None:
    print(f"{productExceptSelf(nums1) = }")
    print(f"{productExceptSelf(nums2) = }")

if __name__ == "__main__":
    main()


"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]



Constraints:

    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

"""
