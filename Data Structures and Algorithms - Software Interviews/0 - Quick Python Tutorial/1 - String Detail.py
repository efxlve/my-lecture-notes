myString = "Hello World"

myString[0] # H
myString[1] # e
len(myString) # 11
myString[len(myString)-1] # d
myString[-1] # d
myString[-2] # l
myString * 2 # Hello WorldHello World
myString + " " + "I'm here" # Hello World I'm here

myString.capitalize() # Hello world
myString.upper() # HELLO WORLD
myString.lower() # hello world
myString.title() # Hello World
myString.split() # ['Hello', 'World']
myString.split("o") # ['Hell', ' W', 'rld']
myString.strip() # Hello World
myString.strip("H") # ello World
myString.strip("d") # Hello Worl
myString.strip("Hd") # ello Worl
myString.count("l") # 3

# String Slicing
myString[3:] # lo World     
myString[:3] # Hel             
myString[3:7] # lo W       

barcode = "12345678910"
product = barcode[0:3] + "-" + barcode[3:7] + "-" + barcode[7:12]
product # 123-4567-8910