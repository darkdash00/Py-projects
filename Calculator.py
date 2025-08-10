def add(x, y):
    return x + y

def divide(x, y):
    # Add a check to prevent division by zero
    if y == 0:
        return "Error: Division by zero"
    return x / y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y




a=input("add,subtract,divide,multiply : ")
x=int(input("enter the first number : "))
y=int(input("enter the second number : "))


if a =="add" : result = add(x,y)
elif a =="subtract" : rsult = subtract(x,y)
elif a =="divide" : result = divide(x,y)
elif a =="multiply" : result = multiply(x,y)

print(result)

