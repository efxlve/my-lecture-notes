# Array, List, Stack, Queue, Deque

# list
myList = [1, 2, 3, 4, 5]
myList.append(6)   # [1, 2, 3, 4, 5, 6]
type(myList) # list

# list
myList = [1, 2, 3, 4, 5]
otherList = [6, 7, 8, 9, 10]
myList.extend(otherList)    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list
result = [0] * 10   # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
type(result)    # list
result[3] = 2   # [0, 0, 0, 2, 0, 0, 0, 0, 0, 0]

# list
import sys
n = 15
myDynamicArray = []
for i in range(n):
    myLength = len(myDynamicArray)
    myByteSize = sys.getsizeof(myDynamicArray)
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(myLength, myByteSize))
    myDynamicArray.append(n)    # Length:   0; Size in bytes:   64
                                # Length:   1; Size in bytes:   96
                                # Length:   2; Size in bytes:   96
                                # Length:   3; Size in bytes:   96
                                # Length:   4; Size in bytes:   96
                                # Length:   5; Size in bytes:  128
                                # Length:   6; Size in bytes:  128
                                # Length:   7; Size in bytes:  128
                                # Length:   8; Size in bytes:  128
                                # Length:   9; Size in bytes:  192
                                # Length:  10; Size in bytes:  192
                                # Length:  11; Size in bytes:  192
                                # Length:  12; Size in bytes:  192
                                # Length:  13; Size in bytes:  192
                                # Length:  14; Size in bytes:  192
type(myDynamicArray)    # list

# array
import array as arr
myArray = arr.array('i', [1, 2, 3, 4, 5])
myArray.append(6)   # array.array('i', [1, 2, 3, 4, 5, 6])
type(myArray) # array.array

# stack
myStack = []
myStack.append(1)   # [1]
myStack.append(2)   # [1, 2]
myStack.append(3)   # [1, 2, 3]
myStack.pop()       # [1, 2]
myStack.pop()       # [1]
myStack.pop()       # []

# queue
from collections import deque
myQueue = deque()
myQueue.append(1)   # deque([1])
myQueue.append(2)   # deque([1, 2])
myQueue.append(3)   # deque([1, 2, 3])
myQueue.popleft()   # deque([2, 3])
myQueue.popleft()   # deque([3])
myQueue.popleft()   # deque([])
myQueue.popleft()   # IndexError: pop from an empty deque

# deque
from collections import deque
myDeque = deque()
myDeque.append(1)   # deque([1])
myDeque.append(2)   # deque([1, 2])
myDeque.append(3)   # deque([1, 2, 3])
myDeque.appendleft(4)   # deque([4, 1, 2, 3])
myDeque.appendleft(5)   # deque([5, 4, 1, 2, 3])
myDeque.pop()       # deque([5, 4, 1, 2])
myDeque.popleft()   # deque([4, 1, 2])
myDeque.pop()       # deque([4, 1])
myDeque.pop()       # deque([4])
myDeque.pop()       # deque([])
myDeque.pop()       # IndexError: pop from an empty deque

