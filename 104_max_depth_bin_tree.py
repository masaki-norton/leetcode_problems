"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
"""

from toolbox import listToTree, TreeNode

def maxDepth(root: TreeNode) -> int:
    # Base Casae
    if not root:
        return 0

    return 1 + (max(maxDepth(root.left), maxDepth(root.right)))

# Test Cases

root1 = [3,9,20,None,None,15,7] # 3
root2 = [1,None,2]  # 2

def main():
    print(maxDepth(listToTree(root1)))
    print(maxDepth(listToTree(root2)))
    return None

if __name__ == "__main__":
    main()
