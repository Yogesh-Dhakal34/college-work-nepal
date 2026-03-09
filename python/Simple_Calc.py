# WAP to create a simple calculator using function with paramter and return type.

def sum(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    if y == 0:
        return("Error!")
    else:
        z = x / y
        return z
    
a = int(input("Enter a whole number: "))
b = int(input("Enter a whole number: "))


Choice = input("Enter your choice, (sum-subtract-multiply-divide) : ")

if Choice == 'sum':
    print(sum(a, b))
elif Choice == 'subtract':
    print(subtract(a, b))
elif Choice == 'multiply':
    print(multiply(a, b))
elif Choice == 'divide':
    print(divide(a, b))
else:
    print("ERROR!!!")
