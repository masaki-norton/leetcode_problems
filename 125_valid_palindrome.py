'''
https://leetcode.com/problems/valid-palindrome/
'''

def validPalindrome(s: str) -> bool:
    stripped = "".join([c for c in s if c.isalnum()]).lower()
    l = 0
    r = len(stripped) - 1
    while r-l > 0:
        if stripped[l] != stripped[r]:
            return False
        l += 1
        r -= 1
    return True

# test cases
phrase1 = "A man, a plan, a canal: Panama"
phrase2 = "race a car"
phrase3 = " "

def main():
    print(validPalindrome(phrase1))
    print(validPalindrome(phrase2))
    print(validPalindrome(phrase3))

if __name__ == "__main__":
    main()
