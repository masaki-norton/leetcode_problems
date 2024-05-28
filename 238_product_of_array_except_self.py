"""
https://leetcode.com/problems/product-of-array-except-self/description/?envType=daily-question&envId=2024-03-15
"""

def productExceptSelf(nums: list[int]) -> list[int]:
    left = [1] * len(nums)
    right = [1] * len(nums)

    x = 1
    for i in range(1, len(nums)):
        x *= nums[i-1]
        left[i] = x

    y = 1
    for j in range(len(nums) - 2, -1, -1):
        y *= nums[j+1]
        right[j] = y

    return [a * b for a, b in zip(left, right)]

# Test Cases
nums1 = [1,2,3,4]
nums2 = [-1,1,0,-3,3]


def main() -> None:
    print(f"{productExceptSelf(nums1) = }")
    print(f"{productExceptSelf(nums2) = }")

if __name__ == "__main__":
    main()
