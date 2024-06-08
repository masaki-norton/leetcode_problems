'''
https://leetcode.com/problems/valid-anagram/
'''

def isAnagram(s: str, t: str) -> bool:
    counter = {}

    for x in s:
        if x in counter:
            counter[x] += 1
        else:
            counter[x] = 1

    for y in t:
        if y in counter:
            counter[y] -=1
        else:
            return False

    for value in counter.values():
        if value != 0:
            return False

    return True

# test cases
s1 = "anagram"
t1 = "nagaram"  # true
s2 = "rat"
t2 = "car"  # false

def main():
    print(isAnagram(s1, t1))
    print(isAnagram(s2, t2))

if __name__ == "__main__":
    main()
