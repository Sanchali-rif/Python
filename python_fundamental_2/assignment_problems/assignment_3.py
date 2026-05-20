# Write a function that prints the digits of a number n.
# For example:
# In 312, there are 3 digits: 3, 1, and 2,
# and we need to print them.
def NumOfDigits(n):
    num=0
    while n>0:
        num=num+1
        n=n//10
    return num

n=int(input("enter the number:"))
print("so the number of digits in",n,"is",NumOfDigits(n))