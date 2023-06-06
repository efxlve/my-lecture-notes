#scope
number = 10
print(number) # 10

def multiply(number):
    number *= 2
    print(number) # 20

multiply(10) # 20
print(number) # 10

#legb -> local, enclosing, global, built-in

myName = "James" # global

def printName():
    myName = "Bond" # enclosing
    print(myName)
    def printName2():
        myName = "Jason"
        print(myName) # local
    printName2()

printName() # Jason

#global keyword
y = 10
def newFunc():
    global y
    y = 5
    print(y)

newFunc() # 5
print(y) # 5