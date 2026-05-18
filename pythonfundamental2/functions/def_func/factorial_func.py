def fact(n):
    mul=1
    for i in range(1,n+1):
        mul=mul*i
    return mul
n=int(input("enter the number for factorial:"))
print("the factorail of",n,"is",fact(n))
