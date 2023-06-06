#classes
class Musician:
    job = "Musician"
    def __init__(self, name, age, instrument):
        self.name = name
        self.age = age
        self.instrument = instrument
    def play_something(self):
        print(f"{self.name} is playing {self.instrument}")
    def __len__(self):
        return self.age
    def __str__(self):
        return f"{self.name} is {self.age} years old and plays {self.instrument}"

james = Musician("James", 50, "Guitar")
james.play_something() # James is playing Guitar
print(james.job) # Musician
print(james.name) # James
print(james.age) # 50
print(james.instrument) # Guitar
print(len(james)) # 50
print(james.__len__()) # 50
print(james) # James is 50 years old and plays Guitar

#inheritance

class Class1():
    def __init__(self):
        print("Class1 __init__")
    def method1(self):
        print("Class1 method1")
    def method2(self):
        print("Class1 method2")

class1Instance = Class1() # Class1 __init__

class Class2(Class1):
    def __init__(self):
        super().__init__()
        print("Class2 __init__")
    def method1(self):
        super().method1()
        print("Class2 method1")
    def method2(self):
        super().method2()
        print("Class2 method2")

class2Instance = Class2() # Class1 __init__ Class2 __init__
class2Instance.method1() # Class1 method1 Class2 method1
class2Instance.method2() # Class1 method2 Class2 method2

#polymorphism
class Apple():
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight
    def __str__(self):
        return f"Apple[color={self.color}, weight={self.weight}]"
    
class Banana():
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight
    def __str__(self):
        return f"Banana[color={self.color}, weight={self.weight}]"
    
apple = Apple("red", 100) # Apple[color=red, weight=100]
banana = Banana("yellow", 200) # Banana[color=yellow, weight=200]

fruitList = [apple, banana]
for fruit in fruitList:
    print(fruit.__str__()) # Apple[color=red, weight=100] Banana[color=yellow, weight=200]