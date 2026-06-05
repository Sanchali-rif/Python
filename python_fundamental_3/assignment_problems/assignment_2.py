# Given a list of integers, compute the average of all numbers in the list.
n=int(input("enter number of elements:"))
a=[]
for i in range(1,n+1):
    x=int(input("enter the number:"))
    a.append(x)
print("the list is:",a)
s=0
for i in a:
    s=s+i
print("the avg of the list is:",s/n)