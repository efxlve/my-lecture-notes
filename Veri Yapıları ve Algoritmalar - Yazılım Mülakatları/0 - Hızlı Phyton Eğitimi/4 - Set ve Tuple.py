#Set 
mySet = {}
print(type(mySet)) # dict

mySet2 = {1,2,3,4,5,6,7,8,9,10}
print(type(mySet2)) # set

mySet3 = set()
print(type(mySet3)) # set

mySet4 = {1,2,3,4,5,6,7,8,9,10,1,2,3,4,5}
print(mySet4) # {1,2,3,4,5,6,7,8,9,10}

mySet5 = {"a","b","c","d","e"}
print(mySet5) # {"a","b","c","d","e"}
mySet5.add("f")
print(mySet5) # {"a","b","c","d","e","f"}

#Tuple
myTuple = (1,2,3,4,5,6,7,8,9,10)
print(type(myTuple)) # tuple

myOtherTuple = tuple()
print(type(myOtherTuple)) # tuple

myTuple2 = (1,2,3,4,5,6,7,8,9,10,1,2,3,4,5)
print(myTuple2) # (1,2,3,4,5,6,7,8,9,10,1,2,3,4,5)
myTuple2[0] # 1
myTuple2[0] = 100 # TypeError: 'tuple' object does not support item assignment
myTuple2[0:3] # (1,2,3)
myTuple2[0:3] = [100,200,300] # TypeError: 'tuple' object does not support item assignment
myTuple2.count(1) # 2

#Tuple Unpacking
(myTuple3, myTuple4) = (1,2)
print(myTuple3) # 1
print(myTuple4) # 2
myTemp = myTuple3
myTuple3 = myTuple4
myTuple4 = myTemp
print(myTuple3) # 2
print(myTuple4) # 1

(x,y) = (10,20)
(x,y) = (y,x)
print(x) # 20
print(y) # 10