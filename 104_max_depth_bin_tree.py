"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
"""

from toolbox import listToTree, TreeNode
from collections import deque

def maxDepth(root: TreeNode) -> int:
    # DFS
    # Base Casae
    if not root:
        return 0

    return 1 + (max(maxDepth(root.left), maxDepth(root.right)))

def maxDepth2(root: TreeNode) -> int:
    # BFS
    if not root:
        return 0

    level = 0
    q = deque([root])

    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1
    return level

def maxDepth3(root: TreeNode) -> int:
    # recursive DFS
    stack = [[root, 1]]
    result = 0

    while stack:
        node, depth = stack.pop()
        if node:
            result = max(result, depth)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])
    return result

# Test Cases
root1 = [3,9,20,None,None,15,7] # 3
root2 = [1,None,2]  # 2

def main():
    print(maxDepth3(listToTree(root1)))
    print(maxDepth3(listToTree(root2)))
    return None

if __name__ == "__main__":
    main()
