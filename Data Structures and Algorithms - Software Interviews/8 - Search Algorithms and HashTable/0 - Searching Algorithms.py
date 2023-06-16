#Searching Algorithms

class SearchingAlgorithms:
    def sequantialSearchUnordered(self, unorderedList, number):
        i = 0
        found = False
        while i < len(unorderedList) and not found:
            if unorderedList[i] == number:
                found = True
            else:
                i += 1
        return found

    def sequantialSearchOrdered(self, orderedList, number):
        i = 0
        found = False
        tooBig = False
        while i < len(orderedList) and not found and not tooBig:
            if orderedList[i] == number:
                found = True
            else:
                if orderedList[i] > number:
                    tooBig = True
                else:
                    i += 1
        return found

    def binarySearch(self, orderedList, number):
        firstPointer = 0
        lastPointer = len(orderedList) - 1
        found = False
        while firstPointer <= lastPointer and not found:
            middlePointer = (firstPointer + lastPointer) // 2
            if orderedList[middlePointer] == number:
                found = True
            else:
                if orderedList[middlePointer] > number:
                    lastPointer = middlePointer - 1
                else:
                    firstPointer = middlePointer + 1
        return found

search = SearchingAlgorithms()
print(search.sequantialSearchUnordered([1,2,3,4,5,6,7,8,9,10], 11)) #False
print(search.sequantialSearchUnordered([1,2,3,4,5,6,7,8,9,10], 10)) #True
myList = [40, 20, 10, 4, 5, 19, 80, 2, 0, 14]
print(search.sequantialSearchUnordered(myList, 80)) #True
myList.sort() #sort the list
print(search.sequantialSearchOrdered(myList, 80)) #True
print(search.sequantialSearchOrdered(myList, 81)) #False
print(search.binarySearch(myList, 80)) #True
print(search.binarySearch(myList, 81)) #False

