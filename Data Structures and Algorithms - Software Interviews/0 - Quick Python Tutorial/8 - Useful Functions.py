#range
list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(5, 10)) # [5, 6, 7, 8, 9]
list(range(0, 10, 2)) # [0, 2, 4, 6, 8]

myList = ["10, 20 ,30, 40, 50"]
for index in range(len(myList)):
    print(myList[index]) # 10 20 30 40 50

myList2 = ["a", "b", "c", "d", "e"]
for index in range(len(myList2)):
    print(myList2[index]) # a b c d e

#enumerate
myList = list(range(5,15))
for index, value in enumerate(myList):
    print("index: {} value: {}".format(index, value))   # index: 0 value: 5
                                                        # index: 1 value: 6
                                                        # index: 2 value: 7
                                                        # index: 3 value: 8
                                                        # index: 4 value: 9
                                                        # index: 5 value: 10
                                                        # index: 6 value: 11
                                                        # index: 7 value: 12
                                                        # index: 8 value: 13
                                                        # index: 9 value: 14

for element in enumerate(myList):
    print(element)  # (0, 5)
                    # (1, 6)
                    # (2, 7)
                    # (3, 8)
                    # (4, 9)
                    # (5, 10)
                    # (6, 11)
                    # (7, 12)
                    # (8, 13)
                    # (9, 14)

for (index, number) in enumerate(myList):
    print(f"index: {index} number: {number}")   # index: 0 number: 5
                                                # index: 1 number: 6  
                                                # index: 2 number: 7
                                                # index: 3 number: 8
                                                # index: 4 number: 9
                                                # index: 5 number: 10
                                                # index: 6 number: 11
                                                # index: 7 number: 12
                                                # index: 8 number: 13
                                                # index: 9 number: 14

newList = []
myString = "Hello"
for letter in myString:
    newList.append(letter)
newList # ['H', 'e', 'l', 'l', 'o']

#one liner
newList = [letter for letter in myString]
newList # ['H', 'e', 'l', 'l', 'o']