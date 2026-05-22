# Write a function that prints the digits of a number n.
# For example:
# In 312, there are 3 digits: 3, 1, and 2,
# and we need to print them.
def print_digits(n):
    if n < 10:
        print(n)
    else:
        print_digits(n // 10)  
        print(n % 10)          

n = int(input("enter num: "))
print("the digits are-")
print_digits(n)