'''
https://leetcode.com/problems/koko-eating-bananas/description/
'''

def minEatingSpeed(piles: list[int], h: int) -> int:
    def can_eat(x):
        return h >= sum([-(p // -x) for p in piles])

    l, r = 1, max(piles)
    m = (l + r) // 2

    while l <= r:
        if can_eat(m):
            r = m - 1
            m = (l + r) // 2
        else:
            l = m + 1
            m = (l + r) // 2
    return m + 1

# test cases
piles1 = [3,6,7,11]
h1 = 8  # 4
piles2 = [30,11,23,4,20]
h2 = 5  # 30
piles3 = [30,11,23,4,20]
h3 = 6  # 23
piles4 = [31]
h4 = 5  # 7
piles5 = [2, 2]
h5 = 4  # 1


def main():
    print(minEatingSpeed(piles1, h1))
    print(minEatingSpeed(piles2, h2))
    print(minEatingSpeed(piles3, h3))
    print(minEatingSpeed(piles4, h4))
    print(minEatingSpeed(piles5, h5))
    return None

if __name__ == "__main__":
    main()
