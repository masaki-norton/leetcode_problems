'''
https://leetcode.com/problems/trapping-rain-water/description/
'''

def trap(height: list[int]) -> int:
    # create mound array
    mound_array = [height[0]]
    top = max(height)
    left = 0
    right = 1
    # left to right
    while height[right] < top:
        while height[left] >= height[right] and height[right] < top:
            right += 1
        mound_array += ([height[left]] * (right-left-1) + [height[right]])
        left = right
        right = left + 1
        print(mound_array)
        if height[right] == top:
            break
    return mound_array


# test cases
height1 = [0,1,0,2,1,0,1,3,2,1,2,1]  # 6
height2 = [4,2,0,3,2,5]  # 9

def main():
    print(trap(height1))
    print(trap(height2))

if __name__ == "__main__":
    main()
