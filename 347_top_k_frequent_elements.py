'''
https://leetcode.com/problems/top-k-frequent-elements/description/
'''

def topKFrequent(nums: list[int], k: int) -> list[int]:
    count = {}
    for n in nums:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    sorted_count = list(dict(sorted(count.items(), key=lambda x: x[1], reverse=True)).keys())

    return [sorted_count[x] for x in range(k)]

# test cases
nums1 = [1,1,1,2,2,3]
k1 = 2  # [1,2]

nums2 = [1]
k2 = 1  # [1]

def main():
    print(topKFrequent(nums1, k1))
    print(topKFrequent(nums2, k2))

if __name__ == "__main__":
    main()
