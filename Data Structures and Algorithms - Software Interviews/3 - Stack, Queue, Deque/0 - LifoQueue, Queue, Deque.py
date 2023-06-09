#LIFO Queue
from queue import LifoQueue
lifoQueue = LifoQueue()
lifoQueue.put(1)
lifoQueue.put(10)
lifoQueue.put(100)
print(lifoQueue.get()) #100
print(lifoQueue.get()) #10
print(lifoQueue.get()) #1
print(lifoQueue.get()) #Empty

#Queue
from queue import Queue
queue = Queue()
queue.put(1)
queue.put(10)
queue.put(100)
print(queue.get()) #1
print(queue.get()) #10
print(queue.get()) #100
print(queue.get()) #Empty

#Deque
from collections import deque
deque = deque()
deque.append(1)
deque.append(10)
deque.append(100)
deque.appendleft(1000)
print(deque.pop()) #100
print(deque.popleft()) #1000
print(deque.pop()) #10
print(deque.pop()) #1
