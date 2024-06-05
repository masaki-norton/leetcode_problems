'''
https://leetcode.com/problems/min-stack/
'''

class MinStack:
    def __init__(self):
        self.num_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # adds element onto stack
        self.num_stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # removes the top element of the stack
        if self.num_stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        # returns the top element of the stack
        return self.num_stack[-1]

    def getMin(self) -> int:
        # returns the min value in stack
        return self.min_stack[-1]


# test cases

def main():
    minStack = MinStack()
    print(minStack.push(-2))
    print(minStack.push(0))
    print(minStack.push(-3))
    print(minStack.getMin())# return -3
    print(minStack.pop())
    print(minStack.top())   # return 0
    print(minStack.getMin()) # return -2
    return None

if __name__ == "__main__":
    main()
