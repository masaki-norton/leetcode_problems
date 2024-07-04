'''
https://leetcode.com/problems/minimum-window-substring/description/
'''

def minWindow(s: str, t: str) -> str:
    counter_t = {}
    for letter in t:
        if letter in counter_t:
            counter_t[letter] += 1
        else:
            counter_t[letter] = 1

    counter_s = {key: 0 for key in counter_t.keys()}

    l, r = 0, 0


    return counter_s

# test cases
s1 = "ADOBECODEBANC"
t1 = "ABC"  # "BANC"

s2 = "a"
t2 = "a"    # "a"

s3 = "a"
t3 = "aa"   # ""

def main():
    print(minWindow(s1, t1))
    print(minWindow(s2, t2))
    print(minWindow(s3, t3))
    return None

if __name__ == "__main__":
    main()
