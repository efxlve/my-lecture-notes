#Binary Tree Max Path Sum

#Given a non-empty binary tree, find the maximum path sum.
#For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections.
#The path must contain at least one node and does not need to go through the root.

#Example 1:
#Input: [1,2,3]
#       1
#      / \
#     2   3
#Output: 6
#Explanation: The maximum path sum is 3 + 2 + 1 = 6.

#Example 2:
#Input: [-10,9,20,null,null,15,7]
#   -10
#   / \
#  9  20
#    /  \
#   15   7
#Output: 42
#Explanation: The maximum path sum is 15 + 20 + 7 = 42.

#Solution
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTreeMaxPathSum:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxSum = float('-inf')

        def maxGain(node):
            if node is None:
                return 0

            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right), 0)

            priceNewPath = node.val + leftGain + rightGain

            self.maxSum = max(self.maxSum, priceNewPath)

            return node.val + max(leftGain, rightGain)

        maxGain(root)
        return self.maxSum
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
solution = BinaryTreeMaxPathSum()
print(solution.maxPathSum(root)) # 6


