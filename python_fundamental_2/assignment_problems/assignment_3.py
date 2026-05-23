# Write a function that prints the digits of a number n.
# For example:
# In 312, there are 3 digits: 3, 1, and 2,
# and we need to print them.

def digits(n):
    while n>0:
        print(n%10)
        n=n//10

n=int(input("enter num:"))
print("the digits are-")
digits(n)