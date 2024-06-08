'''
https://leetcode.com/problems/valid-parentheses/description/
'''

def isValid(s: str) -> bool:
    parens = {
        "[": "]",
        "{": "}",
        "(": ")",
    }
    stack = []
    for x in s:
        if x in parens.keys():
            stack.append(x)
        elif len(stack) == 0 or parens[stack.pop()] != x:
            return False
    return len(stack) == 0

# test cases
s1 = "()"
s2 = "()[]{}"
s3 = "(]"

def main():
    print(isValid(s1))
    print(isValid(s2))
    print(isValid(s3))
    return None

if __name__ == "__main__":
    main()
