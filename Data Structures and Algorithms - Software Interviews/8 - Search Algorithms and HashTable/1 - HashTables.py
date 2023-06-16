#HashTables


#Hash Function
def hashFunction0(key):
    myHash = 0
    for letter in key:
        myHash = (myHash + ord(letter) * 19)
    return myHash  

hashFunction0("apple") #10070

def hashFunction1(key):
    return sum(
        index * ord(character)
        for index, character in enumerate(repr(key).lstrip("'"), 1)
    )

hashFunction1("apple") #1828

#Hash Table
class HashTable:
    def __init__(self, size = 13):
        self.dataMap = [None] * size

    def hashFunction(self, key):
        myHash = 0
        for letter in key:
            myHash = (myHash + ord(letter) * 19) % len(self.dataMap)
        return myHash  

    def setItem(self, key, value):
        index = self.hashFunction(key)
        if self.dataMap[index] == None:
            self.dataMap[index] = []
        self.dataMap[index].append([key, value])

    def getItem(self, key):
        index = self.hashFunction(key)
        if self.dataMap[index] is not None:
            for pair in range(len(self.dataMap[index])):
                if self.dataMap[index][pair][0] == key:
                    return self.dataMap[index][pair][1]
        return None
    
    def getKeys(self):
        keys = []
        for pair in range(len(self.dataMap)):
            if self.dataMap[pair] is not None:
                for key in range(len(self.dataMap[pair])):
                    keys.append(self.dataMap[pair][key][0])
        return keys
    
    def printTable(self):
        for index, value in enumerate(self.dataMap):
            print(index, ": ", value)

myHashTable = HashTable()
myHashTable.setItem("apple", 100)
myHashTable.setItem("orange", 150)
myHashTable.setItem("banana", 250)
myHashTable.printTable()
# 0 :  None
# 1 :  [['banana', 250]]
# 2 :  None
# 3 :  None
# 4 :  None
# 5 :  None
# 6 :  None
# 7 :  [['orange', 150]]
# 8 :  [['apple', 100]]
# 9 :  None
# 10 :  None
# 11 :  None
# 12 :  None
myHashTable.setItem("Watermelon", 300)
myHashTable.setItem("Grape", 200)
myHashTable.setItem("Pineapple", 400)
myHashTable.printTable()
# 0 :  None
# 1 :  [['banana', 250]]
# 2 :  None
# 3 :  None
# 4 :  None
# 5 :  [['Pineapple', 400]]
# 6 :  [['Watermelon', 300], ['Grape', 200]]
# 7 :  [['orange', 150]]
# 8 :  [['apple', 100]]
# 9 :  None
# 10 :  None
# 11 :  None
# 12 :  None
print(myHashTable.getItem("apple")) #100
print(myHashTable.getItem("orange")) #150
print(myHashTable.getItem("banana")) #250
print(myHashTable.getItem("Watermelon")) #300
print(myHashTable.getItem("Grape")) #200
print(myHashTable.getItem("Pineapple")) #400
print(myHashTable.getItem("Pineapple1")) #None
print(myHashTable.getKeys()) #['banana', 'Pineapple', 'Watermelon', 'Grape', 'orange', 'apple']



