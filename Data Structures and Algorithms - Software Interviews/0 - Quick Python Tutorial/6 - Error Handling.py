#error handling
try:
    a = int(input("first number: "))
    b = int(input("second number: "))
    print(a/b)
except ValueError:
    print("Please enter a valid input.")
except ZeroDivisionError:
    print("You cannot divide a number by 0.")
except:
    print("An error occurred.")
finally:
    print("The process is completed.")