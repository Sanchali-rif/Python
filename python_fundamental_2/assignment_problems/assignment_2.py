# Write a function that takes two integers a and b as input
# and prints all even numbers between them (inclusive).

def even(a,b):
    for i in range (a,b+1):
        if(i%2==0):
            print(i)

a=int(input("enter the starting num:"))
b=int(input("enter the ending num:"))
print("the even numers are:",even(a,b))