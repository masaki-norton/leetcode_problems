'''
https://leetcode.com/problems/median-of-two-sorted-arrays/description/
'''

def findMedianSortedArrays(numsa: list[int], numsb: list[int]) -> int:
    print(f"{numsa = }")
    print(f"{numsb = }")
    # helper method for binary search validation
    def isValidPartition(numsa_index, numsb_index):
        print(f"{numsa[numsa_index] = }")
        print(f"{numsb[numsb_index + 1] = }")
        print(f"{numsb[numsb_index] = }")
        print(f"{numsa[numsa_index + 1] = }")
        return numsa[numsa_index] <= numsb[numsb_index + 1] and \
            numsb[numsb_index] <= numsa[numsa_index + 1]

    # if either array is empty, return median
    if len(numsa) == 0 or len(numsb) == 0:
        numsa += numsb
        if len(numsa) % 2 == 1:
            return numsa[len(numsa)//2]
        else:
            return (numsa[len(numsa)//2] + numsa[len(numsa)//2 - 1]) / 2

    left_partition_index = (len(numsa) + len(numsb) - 2) // 2
    print(f"{left_partition_index = }")

    l, r = 0, left_partition_index
    m = (l + r) // 2

    while l < r:
        print('=====================')
        print(f"{(l, m, r) = }")
        if isValidPartition(m, left_partition_index - m - 1):
            print(f"partition index: {m = }")
            break
        elif numsa[m] > numsb[left_partition_index - m - 1]:
            r = m - 1
            m = (l + r) // 2
        else:
            l = m +
            m = (l + r) // 2
    print(f"partition index: {r = }")
    return None

# test cases
nums1a = [1,3]
nums1b = [2]    # 2.00000

nums2a = [1,2]
nums2b = [3,4]  # 2.5

nums3a = [1,2,3,4,5,7]
nums3b = [1,2,3,9,10,11]
'''
combined [1, 1, 2, 2, 3, 3, 4, 5, 7, 9, 10, 11]
ouput: 3.5
'''

nums4a = [1,2,3,4,5,7]
nums4b = [6,7,8,9,11]
'''
combined [1,2,3,4,5,6,7,7,8,9,11]
ouput: 6
left_partition_index = (6 + 5 - 2) // 2 = 4 -> index where left side ends in
    combined sorted array.
'''


def main():
    print('=====================')
    print('=====================')
    print('=====================')
    print(findMedianSortedArrays(nums1a, nums1b))
    print('=====================')
    print('=====================')
    print('=====================')
    print(findMedianSortedArrays(nums2a, nums2b))
    print('=====================')
    print('=====================')
    print('=====================')
    print(findMedianSortedArrays(nums3a, nums3b))
    print('=====================')
    print('=====================')
    print('=====================')
    print(findMedianSortedArrays(nums4a, nums4b))
    return None

if __name__ == "__main__":
    main()
