#Node --> Linked List

#Single Linked List
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

firstNode = Node(10) #head
secondNode = Node(20) #tail
thirdNode = Node(30) #tail
firstNode.next = secondNode #head --> tail
secondNode.next = thirdNode #head --> tail --> tail
firstNode.next.next.val #30

#Double Linked List
class Node2:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

firstNode = Node2(10) #head
secondNode = Node2(20) #tail
thirdNode = Node2(30) #tail
firstNode.next = secondNode #head --> tail
secondNode.prev = firstNode #head <-- tail
secondNode.next = thirdNode #head --> tail --> tail
thirdNode.prev = secondNode #head <-- tail <-- tail
firstNode.next.next.val #30
thirdNode.prev.prev.val #10