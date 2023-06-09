#Implement Stack Using Queue

'''
Implement Stack Using Queue

push(item)
pop()
top()
isEmpty()
'''

from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        for i in range(len(self.stack) - 1):
            self.stack.append(self.stack.popleft())
        return self.stack.popleft()
    
    def top(self):
        return self.stack[-1]
    
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
print(myStack.top()) #None
print(myStack.isEmpty()) #True
myStack.push(1)
myStack.push(10)
myStack.push(100)
print(myStack.top()) #100
print(myStack.isEmpty()) #False

# Time: O(n) for push, pop, top, isEmpty
# Space: O(n) for stack