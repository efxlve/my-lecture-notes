#Convert BST to Greater Tree

#Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

#As a reminder, a binary search tree is a tree that satisfies these constraints:

#The left subtree of a node contains only nodes with keys less than the node's key.
#The right subtree of a node contains only nodes with keys greater than the node's key.
#Both the left and right subtrees must also be binary search trees.

#Example:

#Input: The root of a Binary Search Tree like this:
#              5
#            /   \
#           2     13

#Output: The root of a Greater Tree like this:
#             18
#            /   \
#          20     13

#Solution
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:

        sumOfValues = 0

        def traverse(node):
            nonlocal sumOfValues
            if node is None:
                return
            if node.right:
                traverse(node.right)
            node.val += sumOfValues
            sumOfValues = node.val
            if node.left:
                traverse(node.left)

        traverse(root)
        return root

root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(13)
solution = Solution()
print(solution.convertBST(root)) # 18, 20, 13



