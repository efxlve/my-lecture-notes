#List
List = [1,2,3,4,5,6,7,8,9,10]
type(List) #list

myOtherList = list()
myOtherList.append(1)
myOtherList.append(2)
myOtherList # [1,2]

myMixedList = [1,2,3,"a","b","c",True,3.14]
myMixedList[3] # "a"

x = myMixedList[3] # "a"
type(x) # str

y = myMixedList[6] # True
type(y) # bool

myMixedList[1:3] # [2,3]

myNestedList = [[1,2,3],["a","b","c"],[True,False]]
myNestedList[1] # ["a","b","c"]
myNestedList[1][2] # "c"
myNestedList[0] = 100 # [[100,2,3],["a","b","c"],[True,False]]