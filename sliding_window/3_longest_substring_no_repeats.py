'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
'''

def lengthOfLongestSubstring(s: str) -> int:
    l, r, max_len = 0,0,0
    log = set()
    while r < len(s):
        if s[r] not in log:
            log.add(s[r])
            r += 1
        else:
            log.remove(s[l])
            l += 1
        max_len = max(max_len, r - l)
    return max_len

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
