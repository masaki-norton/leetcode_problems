'''
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/?envType=daily-question&envId=2024-05-29
'''

def numSteps(s: str) -> int:
    steps = 0
    while s != "1":
        steps += 1
        if s[-1] == "1":
            s = bin(int(s, 2) + 1)[2:]
        else:
            s = s[:-1]
    return steps

# test cases
s1 = "1101" # 6
s2 = "10"   # 1
s3 = "1"    # 0

def main():
    print(numSteps(s1))
    print(numSteps(s2))
    print(numSteps(s3))

if __name__ == "__main__":
    main()
