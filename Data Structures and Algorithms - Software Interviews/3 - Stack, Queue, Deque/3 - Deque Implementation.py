#Deque

'''
Deque()

addRight()
addLeft()
removeRight()
removeLeft()
peekRight()
peekLeft()
isEmpty()
size()
'''

class Deque:
    def __init__(self):
        self.deque = []
    
    def addRight(self, item):
        self.deque.append(item)
    
    def addLeft(self, item):
        self.deque.insert(0, item)
    
    def removeRight(self):
        if self.deque:
            return self.deque.pop()
        else:
            return None
    
    def removeLeft(self):
        if self.deque:
            return self.deque.pop(0)
        else:
            return None
    
    def peekRight(self):
        if self.deque:
            return self.deque[-1]
        else:
            return None
    
    def peekLeft(self):
        if self.deque:
            return self.deque[0]
        else:
            return None
    
    def isEmpty(self):
        return self.deque == []
    
    def size(self):
        return len(self.deque)
    
myDeque = Deque()
myDeque.addRight(1)
myDeque.addRight(10)
myDeque.addRight(100)
print(myDeque.removeLeft()) #1
print(myDeque.removeLeft()) #10
print(myDeque.removeLeft()) #100
print(myDeque.removeLeft()) #None
print(myDeque.peekLeft()) #None
print(myDeque.size()) #0
print(myDeque.isEmpty()) #True
myDeque.addRight(1)
myDeque.addRight(10)
myDeque.addRight(100)
print(myDeque.peekLeft()) #1
print(myDeque.size()) #3
print(myDeque.isEmpty()) #False
myDeque.addLeft(1)
myDeque.addLeft(10)
myDeque.addLeft(100)
print(myDeque.peekLeft()) #100
print(myDeque.size()) #6
print(myDeque.isEmpty()) #False
print(myDeque.peekRight()) #100
print(myDeque.size()) #6
print(myDeque.isEmpty()) #False
print(myDeque.removeRight()) #100
print(myDeque.size()) #5
print(myDeque.isEmpty()) #False
print(myDeque.removeRight()) #10
print(myDeque.size()) #4
print(myDeque.isEmpty()) #False
print(myDeque.removeRight()) #1
print(myDeque.size()) #3
print(myDeque.isEmpty()) #False
print(myDeque.removeRight()) #100
print(myDeque.size()) #2
print(myDeque.isEmpty()) #False
print(myDeque.removeRight()) #10
print(myDeque.size()) #1
print(myDeque.isEmpty()) #False
print(myDeque.removeRight()) #1
print(myDeque.size()) #0
print(myDeque.isEmpty()) #True

# Time: O(1) for addRight, addLeft, removeRight, removeLeft, peekRight, peekLeft, isEmpty, size
# Space: O(n) for deque