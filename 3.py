def lengthOfLongestSubstring(s: str) -> int:
    left = 0
    right = 0
    max_length = 0
    log = []

    while right < len(s):
        if s[right] not in log:
            log.append(s[right])
            right += 1
        else:
            log.remove(s[left])
            left += 1
        max_length = max(max_length, len(log))
    return max_length

s1 = "abcabcbb" # 3, abc is longest, so is bca
s2 = "bbbbb"    # 1, b is longest
s3 = "pwwkew"   # 3, wke is longest

print(lengthOfLongestSubstring(s1))
print(lengthOfLongestSubstring(s2))
print(lengthOfLongestSubstring(s3))
