import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y!= 0:
        return x / y
    else:
        return "divition by ZeroDivisionError"
    
    
def square_root(x):
    if x > 0:
        return math.sqrt(x)
    else:
        return "cannot be square_root by Zero"
    
def power(x, y):
    return math.pow(x, y)

def calculation():
    print("select an opertaion to perform")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("5. square root")
    print("6. power")
    
    operation = input()
    
    if operation in input['1', '2', '3', '4', '6']:
        num1 = float(input("ENTER THE FIRST NUMBER: "))
        num2 = float(input("ENTER THE SECOND NUMBER: "))
    
        if operation == "1":
            result = add(num1, num2)
        elif operation == "2":
            result = subtract(num1, num2)
        elif operation == "3":
            result = multiply(num1, num2)
        elif operation == "4":
            result = divide(num1, num2)
        elif operation == "6":
            result = power(num1, num2)
            
            print("THE RESULT IS", result)
    
    elif operation == "5":
        num = float(input("ENTER THE NUMBER: "))
        result =square_root(num)
        print("THE RESULT IS: ".result)
        
    else:
     print("INVALID INPUT")