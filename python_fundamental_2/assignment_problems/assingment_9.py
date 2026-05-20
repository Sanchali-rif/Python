# Write a function that returns True if a number is a prime number
# and otherwise returns False, using a loop.

def is_prime(n):
    count=0
    for i in range(1,n+1):
        if(n%i==0):
            count=count+1
    if(count==2):
        return True
    else:
        return False

n=int(input("enter a number:"))
print(is_prime(n))