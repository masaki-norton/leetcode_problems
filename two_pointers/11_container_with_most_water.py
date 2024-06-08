'''
https://leetcode.com/problems/container-with-most-water/description/
'''

def maxArea(height: list[int]) -> int:
    output = 0
    l = 0
    r = len(height) - 1
    while l < r:
        curr_area = min(height[l], height[r]) * (r - l)
        output = max(output, curr_area)
        left = height[l]
        right = height[r]
        if height[l] < height[r]:
            l += 1
            while left > height[l] and l < r:
                l += 1
        else:
            r -= 1
            while right > height[r] and l < r:
                r -= 1
    return output

# test cases
height1 = [1,8,6,2,5,4,8,3,7]    # 49
height2 = [1,1]  # 1

def main():
    print(maxArea(height1))
    print(maxArea(height2))

if __name__ == "__main__":
    main()
