'''
https://leetcode.com/problems/generate-parentheses/description/
'''

def generateParenthesis(n: int) -> list[str]:
    stack = []
    output = []

    def search(opens, closes):
        # if stack satisfies valid parens, add to output
        if opens == closes == n:
            output.append("".join(stack))
            return

        if opens > closes:
            stack.append(")")
            search(opens, closes + 1)
            stack.pop()

        if n > opens:
            stack.append("(")
            search(opens+1, closes)
            stack.pop()

    # run recursion
    search(0, 0)
    return output

# test cases
n1 = 3  # ["((()))","(()())","(())()","()(())","()()()"]
n2 = 1  # ["()"]

def main():
    print(generateParenthesis(n1))
    print(generateParenthesis(n2))
    return None

if __name__ == "__main__":
    main()
