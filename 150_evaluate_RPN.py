'''
https://leetcode.com/problems/evaluate-reverse-polish-notation/
'''

def evalRPN(tokens: list[str]) -> int:
    stack = []

    operators = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: b - a,
        "*": lambda a, b: a * b,
        "/": lambda a, b: int(b/a)
    }
    ops = operators.keys()

    for entry in tokens:
        if entry not in ops:
            stack.append(entry)
        else:
            stack.append(operators[entry](int(stack.pop()), int(stack.pop())))
    return int(stack[0])

# test cases
tokens1 = ["2","1","+","3","*"]     # 9
tokens2 = ["4","13","5","/","+"]    # 6
tokens3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"] # 22
tokens4 = ["4","3","-"] # 1
tokens5 = ["4","-2","/","2","-3","-","-"]   # -7

def main():
    print(evalRPN(tokens5))
    return None

if __name__ == "__main__":
    main()
