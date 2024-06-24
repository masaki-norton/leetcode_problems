'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
'''

def maxProfit(prices: list[int]) -> int:
    max_prof = 0
    buy = prices[0]
    for i in range(1, len(prices)):
        if buy > prices[i]:
            buy = prices[i]
        max_prof = max(max_prof, prices[i] - buy)
    return max_prof

# test cases
prices1 = [7,1,5,3,6,4] # 5
prices2 = [7,6,4,3,1]   # 0

def main():
    print(maxProfit(prices1))
    print(maxProfit(prices2))
    return None

if __name__ == "__main__":
    main()
