'''
https://leetcode.com/problems/permutation-in-string/description/
'''

def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    char_count1 = [0] * 26
    char_count2 = [0] * 26

    for x in range(len(s1)):
        char_count1[ord(s1[x]) - 97] += 1
        char_count2[ord(s2[x]) - 97] += 1

    if char_count1 == char_count2:
        return True

    l = 0
    r = len(s1)

    while r < len(s2):
        char_count2[ord(s2[l]) - 97] -= 1
        char_count2[ord(s2[r]) - 97] += 1

        if char_count1 == char_count2:
            return True

        l += 1
        r += 1

    return False

# test cases
s1 = ("ab", "eidbaooo") # true
s2 = ("ab", "eidboaoo") # false

def main():
    print(checkInclusion(s1[0], s1[1]))
    print(checkInclusion(s2[0], s2[1]))
    return None

if __name__ == "__main__":
    main()
