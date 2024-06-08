'''
https://leetcode.com/problems/largest-rectangle-in-histogram/description/
'''

def largestRectangleArea(heights: list[int]) -> int:
    stack = []
    max_height = 0
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            popped = stack.pop()
             # be careful choosing boundries of our rectangle here
            max_height = max(max_height, heights[popped] * (i - (stack[-1] + 1) if stack else i))
        stack.append(i)
    while stack:
        popped = stack.pop()
        # be careful choosing boundries of our rectangle here
        max_height = max(max_height, heights[popped] * (len(heights) - (stack[-1] + 1) if stack else len(heights)))
    return max_height

# test cases
heights1 = [2,1,5,6,2,3]    # 10
heights2 = [2,4]    # 4
heights3 = [2, 1, 2]    # 3
heights4 = [5, 4, 1, 2] # 8
heights5 = [9, 0]   # 9
heights6 = [4,2,0,3,2,5]    # 6
heights7 = [3,6,5,7,4,8,1,0]    # 20

def main():
    print(largestRectangleArea(heights1))
    print(largestRectangleArea(heights2))
    print(largestRectangleArea(heights3))
    print(largestRectangleArea(heights4))
    print(largestRectangleArea(heights5))
    print(largestRectangleArea(heights6))
    print(largestRectangleArea(heights7))
    return None

if __name__ == "__main__":
    main()
