#functions

def my_function():
    print("Hello from a function")

my_function() # Hello from a function

def my_function2(name):
    print(f"Hello {name}")

my_function2("John") # Hello John

def my_function3(number1, number2):
    print(number1 + number2)

my_function3(5, 6) # 11

x = my_function3(5, 6) # 11
print(x) # None
type(x) # NoneType

if x is None:
    print("x is None") # x is None

def my_function4(number1, number2):
    return number1 + number2

x = my_function4(5, 6)
print(x) # 11
type(x) # int

def my_function5(str):
    return str.upper()

x = my_function5("hello world")
print(x) # HELLO WORLD

def my_function6(name = "John"):
    print(name)

my_function6() # John
my_function6("Eric") # Eric
