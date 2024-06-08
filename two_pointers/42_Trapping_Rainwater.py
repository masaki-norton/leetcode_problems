'''
https://leetcode.com/problems/trapping-rain-water/description/
'''

def trap(height: list[int]) -> int:
    water = 0
    left = 0
    right = len(height) - 1
    left_max = height[left]
    right_max = height[right]

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(height[left], left_max)
            water += left_max - height[left]
        else:
            right -= 1
            right_max = max(height[right], right_max)
            water += right_max - height[right]

    return water

    # left_max_index = height.index(max(height))
    # right_max_index = len(height) - 1 - height[::-1].index(max(height))

    # # go left to right until left max, filling in the mound array
    # x = 0
    # mound_array_left = []
    # while x < left_max_index:
    #     if x == 0:
    #         mound_array_left = [height[0]]
    #     else:
    #         mound_array_left += [max(mound_array_left[x-1], height[x])]
    #     x += 1

    # # same thing on right side, except flipped
    # y = 0
    # mound_array_right = []
    # while y < (len(height) - right_max_index - 1):
    #     if y == 0:
    #         mound_array_right = [height[-1]]
    #     else:
    #         mound_array_right += [max(mound_array_right[y-1], height[::-1][y])]
    #     y += 1

    # # construct mound layer
    # mound_array = mound_array_left + [max(height)] * (right_max_index - left_max_index + 1)\
    #     + mound_array_right[::-1]

    # return sum([mound_array[z] - height[z] for z in range(len(height))])

# test cases
height1 = [0,1,0,2,1,0,1,3,2,1,2,1]  # 6
height2 = [4,2,0,3,2,5]  # 9


def main():
    print(trap(height1))
    print(trap(height2))

if __name__ == "__main__":
    main()
