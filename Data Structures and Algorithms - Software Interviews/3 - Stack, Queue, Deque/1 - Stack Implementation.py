#Stack

'''
Stack()

push(item)
pop()
showLast()
size()
isEmpty()
'''

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return None
    
    def showLast(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None
    
    def size(self):
        return len(self.stack)
    
    def isEmpty(self):
        return self.stack == []

myStack = Stack()
myStack.push(1)
myStack.push(10)
myStack.push(100)
print(myStack.pop()) #100
print(myStack.pop()) #10
print(myStack.pop()) #1
print(myStack.pop()) #None
print(myStack.showLast()) #None
print(myStack.size()) #0
print(myStack.isEmpty()) #True
myStack.push(1)
myStack.push(10)
myStack.push(100)
print(myStack.showLast()) #100
print(myStack.size()) #3
print(myStack.isEmpty()) #False

# Time: O(1) for push, pop, showLast, size, isEmpty
# Space: O(n) for stack

