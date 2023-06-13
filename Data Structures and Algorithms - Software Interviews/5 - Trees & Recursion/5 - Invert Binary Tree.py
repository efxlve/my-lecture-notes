#Invert Binary Tree
# Given the root of a binary tree, invert the tree, and return its root.

# Example 1:
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

# Example 2:
# Input: root = [2,1,3]
# Output: [2,3,1]

# Example 3:
# Input: root = []
# Output: []

# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Follow up: Recursive solution is trivial, could you do it iteratively?

# Solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        #exit condition
        if root is None:
            return None
        
        root.left, root.right = root.right, root.left
        
        #recursion
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
    
    def printTree(self, root: TreeNode) -> None:
        if root is None:
            return None
        
        self.printTree(root.left)
        print(root.val)
        self.printTree(root.right)

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

solution = Solution()
solution.printTree(root)
print("\n")
solution.invertTree(root)
solution.printTree(root)

# Output:
# 1
# 2
# 3
# 4
# 6
# 7
# 9
