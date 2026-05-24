# Write a function to return the sum of digits of a number n.

def sum(n):
    s=0
    while n>0:
        s=s+(n%10)
        n=n//10
    return s

n=int(input("enter num:"))
print("the sum digits is",sum(n))