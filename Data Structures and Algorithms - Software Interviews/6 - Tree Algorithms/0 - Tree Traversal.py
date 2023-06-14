#Tree Traversal

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, root):
        self.root = root

    def insert(self, val):
        newNode = Node(val)
        if self.root is None:
            self.root = newNode
            return True
        
        tempNode = self.root

        while True:
            if newNode.value == tempNode.value:
                return False
            if newNode.value < tempNode.value:
                if tempNode.left is None:
                    tempNode.left = newNode
                    return True
                tempNode = tempNode.left
            else:
                if tempNode.right is None:
                    tempNode.right = newNode
                    return True
                tempNode = tempNode.right

    def contains(self, val):
        if self.root is None:
            return False
        
        tempNode = self.root

        while tempNode:
            if val == tempNode.value:
                return True
            if val < tempNode.value:
                tempNode = tempNode.left
            else:
                tempNode = tempNode.right
        return False
    
    def minOfTree(self, currentNode):
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value
    
    def maxOfTree(self, currentNode):
        while currentNode.right is not None:
            currentNode = currentNode.right
        return currentNode.value
    
    # Breadth First Search
    def BFS(self):
        currentNode = self.root
        queue = []
        result = []
        queue.append(currentNode)

        while len(queue) > 0:
            currentNode = queue.pop(0)
            result.append(currentNode.value)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        return result
    
    # Depth First Search
    def DFS(self, order):
        result = []
        currentNode = self.root
        if order == "preorder":
            def traverse(node):
                result.append(node.value)
                if node.left:
                    traverse(node.left)
                if node.right:
                    traverse(node.right)
            traverse(currentNode)
        elif order == "postorder":
            def traverse(node):
                if node.left:
                    traverse(node.left)
                if node.right:
                    traverse(node.right)
                result.append(node.value)
            traverse(currentNode)
        elif order == "inorder":
            def traverse(node):
                if node.left:
                    traverse(node.left)
                result.append(node.value)
                if node.right:
                    traverse(node.right)
            traverse(currentNode)
        return result

myTree = BinarySearchTree()
myTree.insert(38)
myTree.insert(19)
myTree.insert(69)
myTree.insert(12)
myTree.insert(24)
myTree.insert(59)
myTree.insert(95)
myTree.BFS() # [38, 19, 69, 12, 24, 59, 95]
myTree.DFS("preorder") # [38, 19, 12, 24, 69, 59, 95]
myTree.DFS("postorder") # [12, 24, 19, 59, 95, 69, 38]
myTree.DFS("inorder") # [12, 19, 24, 38, 59, 69, 95]