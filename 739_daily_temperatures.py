"""
https://leetcode.com/problems/daily-temperatures/description/
"""

def dailyTemps(temps: list[int]) -> list[int]:
    stack = []
    output = []
    for t in temps:
        if len(stack) == 0:
            stack.append(t)
        elif t < stack[-1]:
            stack.append(t)
    return

# test cases
temperatures1 = [73,74,75,71,69,72,76,73]   # [1,1,4,2,1,1,0,0]
temperatures2 = [30,40,50,60]   # [1,1,1,0]
temperatures3 = [30,60,90]  # [1,1,0]

def main():
    print(dailyTemps(temperatures1))
    print(dailyTemps(temperatures2))
    print(dailyTemps(temperatures3))
    return None

if __name__ == "__main__":
    main()
