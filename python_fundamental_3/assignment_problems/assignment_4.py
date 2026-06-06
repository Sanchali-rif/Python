# Given a tuple of integers, create:
# A tuple of all even numbers
# A tuple of all odd numbers

n=int(input("enter number of elements for tupple:"))
tup=()
for i in range(1,n+1):
    x=int(input("enter the number:"))
    tup=tup+(x,)

even_tup=()
odd_tup=()
for i in tup:
    if i%2==0:
        even_tup=even_tup+(i,)
    else:
        odd_tup=odd_tup+(i,)
print("the even elements are-",even_tup)
print("the odd elements are-",odd_tup)