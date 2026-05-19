# Write a function to return the count of digits in a number.

def NumOfDigits(n):
    num=0
    while n>0:
        num=num+1
        n=n//10
    return num

n=int(input("enter the number:"))
print("so the number of digits in",n,"is",NumOfDigits(n))