#Queue

'''
Queue()

enqueue(item)
dequeue()
showFirst()
size()
isEmpty()
'''

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            return None
    
    def showFirst(self):
        if self.queue:
            return self.queue[0]
        else:
            return None
    
    def size(self):
        return len(self.queue)
    
    def isEmpty(self):
        return self.queue == []
    
myQueue = Queue()
myQueue.enqueue(1)
myQueue.enqueue(10)
myQueue.enqueue(100)
print(myQueue.dequeue()) #1
print(myQueue.dequeue()) #10
print(myQueue.dequeue()) #100
print(myQueue.dequeue()) #None
print(myQueue.showFirst()) #None
print(myQueue.size()) #0
print(myQueue.isEmpty()) #True
myQueue.enqueue(1)
myQueue.enqueue(10)
myQueue.enqueue(100)
print(myQueue.showFirst()) #1
print(myQueue.size()) #3
print(myQueue.isEmpty()) #False

# Time: O(1) for enqueue, dequeue, showFirst, size, isEmpty
# Space: O(n) for queue