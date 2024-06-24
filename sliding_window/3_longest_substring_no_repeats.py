'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
'''

def lengthOfLongestSubstring(s: str) -> int:
    l, r, max_len = 0,0,0


# test cases
s1 = "abcabcbb" # 3
s2 = "bbbbb"    # 1
s3 = "pwwkew"   # 3

def main():
    print(lengthOfLongestSubstring(s1))
    print(lengthOfLongestSubstring(s2))
    print(lengthOfLongestSubstring(s3))
    return None

if __name__ == "__main__":
    main()
