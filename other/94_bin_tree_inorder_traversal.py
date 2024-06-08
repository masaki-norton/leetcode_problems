"""
https://leetcode.com/problems/binary-tree-inorder-traversal/description/
"""

from toolbox import listToTree, TreeNode
from collections import deque

# Recursive Solution
def inorderTraversal(root: [TreeNode]) -> list[int]:
    output = []
    def inorder(root):
        if not root:
            return
        inorder(root.left)
        output.append(root.val) # because we read left to right
        inorder(root.right)
    inorder(root)
    return output

# Iterative Solution


# Test Cases
root1 = [1,None,2,3]    # [1,3,2]
root2 = []  # []
root3 = [1] # [1]

def main():
    print(inorderTraversal(root=listToTree(root1)))
    return None

if __name__ == "__main__":
    main()
