# Sorting Algorithms

class SortingAlgorithms:
    def bubbleSort(self, arr):
        for i in range(len(arr) - 1, 0, -1):
            for j in range(i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    def selectionSort(self, arr):
        for i in range(len(arr)-1):
            minIndex = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[minIndex]:
                    minIndex = j
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
        return arr

    def insertionSort(self, arr):
        for i in range(1, len(arr)):
            currentValue = arr[i]
            position = i
            while position > 0 and arr[position-1] > currentValue:
                arr[position] = arr[position-1]
                position -= 1
            arr[position] = currentValue
        return arr

    def merge(self, arr1, arr2):
        firstPointer = 0
        secondPointer = 0
        mergedList = []
        while firstPointer < len(arr1) and secondPointer < len(arr2):
            if arr1[firstPointer] < arr2[secondPointer]:
                mergedList.append(arr1[firstPointer])
                firstPointer += 1
            else:
                mergedList.append(arr2[secondPointer])
                secondPointer += 1
        while firstPointer < len(arr1):
            mergedList.append(arr1[firstPointer])
            firstPointer += 1
        while secondPointer < len(arr2):
            mergedList.append(arr2[secondPointer])
            secondPointer += 1
        return mergedList

    def mergeSort(self, arr):
        if len(arr) == 1:
            return arr
        midPoint = int(len(arr)/2)
        leftPart = arr[:midPoint]
        rightPart = arr[midPoint:]
        return self.merge(self.mergeSort(leftPart), self.mergeSort(rightPart))
    
    def pivot(self, arr, pivotIndex, endIndex):
        swapIndex = pivotIndex
        for i in range(pivotIndex + 1, endIndex + 1):
            if arr[i] < arr[pivotIndex]:
                swapIndex += 1
                arr[swapIndex], arr[i] = arr[i], arr[swapIndex]
        arr[pivotIndex], arr[swapIndex] = arr[swapIndex], arr[pivotIndex]
        return swapIndex

    def quickSort(self,arr, leftPointer = 0, rightPointer = None):
        if rightPointer == None:
            rightPointer = len(arr) - 1
        if leftPointer < rightPointer:
            pivotIndex = self.pivot(arr, leftPointer, rightPointer)
            self.quickSort(arr, leftPointer, pivotIndex-1)  
            self.quickSort(arr, pivotIndex+1, rightPointer)       
        return arr
    
    def heapify(self,arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[largest] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)
        
    def heapSort(self,arr):
        n = len(arr)

        # Build a MAX_HEAP.
        for i in range(n, -1, -1):
            self.heapify(arr, n, i)

        # Swap nodes with root to sort
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)
        return arr


sortingAlgorithms = SortingAlgorithms()

print(sortingAlgorithms.bubbleSort([5, 1, 3, 4, 2, 8, 6, 10])) # [1, 2, 3, 4, 5, 6, 8, 10]
print(sortingAlgorithms.selectionSort([5, 1, 3, 4, 2, 8, 6, 10])) # [1, 2, 3, 4, 5, 6, 8, 10]
print(sortingAlgorithms.insertionSort([5, 1, 3, 4, 2, 8, 6, 10])) # [1, 2, 3, 4, 5, 6, 8, 10]
print(sortingAlgorithms.mergeSort([5, 1, 3, 4, 2, 8, 6, 10])) # [1, 2, 3, 4, 5, 6, 8, 10]
print(sortingAlgorithms.quickSort([5, 1, 3, 4, 2, 8, 6, 10])) # [1, 2, 3, 4, 5, 6, 8, 10]
print(sortingAlgorithms.heapSort([5, 1, 3, 4, 2, 8, 6, 10])) # [1, 2, 3, 4, 5, 6, 8, 10]
