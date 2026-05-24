# Let's create a Simple Calculator.
# Create a function:
# calculator(a, b, operation)
# The function should perform arithmetic operations
# based on the operation parameter.
# operation can have the following values:
# '+'  -> Addition
# '-'  -> Subtraction
# '*'  -> Multiplication
# '/'  -> Division

def calculator(a, b, operation):
    match operation:
        case "+":
            print("the sum of",a,"and",b,"is",a+b)
        case "-":
            print("the diff of",a,"and",b,"is",a-b)
        case "*":
            print("the multiply of",a,"and",b,"is",a*b)
        case "/":
            print("the division of",a,"and",b,"is",a/b)
a=int(input("enter the num:"))
b=int(input("enter the num:"))
operation=input("enter the fuction:")
calculator(a, b, operation)