'''
https://leetcode.com/problems/longest-repeating-character-replacement/description/
'''

def characterReplacement(s: str, k: int) -> int:
    l, r, output = 0, 0, 0
    char_count = [0] * 26
    while r < len(s):
        char_count[ord(s[r]) - 65] += 1
        if sum(char_count) - max(char_count) > k:
            char_count[ord(s[l]) - 65] -= 1
            l += 1
        output = max(output, r - l + 1)
        r += 1
    return output

# test cases
s1 = "ABAB"
k1 = 2  # 4

s2 = "AABABBA"
k2 = 1  # 4

def main():
    print(ord("A"))
    print(characterReplacement(s1, k1))
    print(characterReplacement(s2, k2))
    return None

if __name__ == "__main__":
    main()
