#Tree

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

myTree = BinarySearchTree()
myTree.insert(10) # True
myTree.insert(10) # False
myTree.insert(8) # True
myTree.insert(20) # True
myTree.insert(25) # True
myTree.insert(16) # True
myTree.contains(16) # True
myTree.contains(10) # True
myTree.contains(19) # False
print(myTree.root.val) # 10
print(myTree.root.right.val) # 
print(myTree.root.right.right.val) # 25
print(myTree.root.left.val) # 8
print(myTree.root.left.left) # None
myTree.minOfTree(myTree.root) # 8
myTree.maxOfTree(myTree.root) # 25