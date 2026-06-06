# Input two lists of integers from the user.
# Merge them into one list and sort the result.

n=int(input("enter number of elements for list_1:"))
L1=[]
for i in range(1,n+1):
    x=int(input("enter the number:"))
    L1.append(x)

n=int(input("enter number of elements for list_2:"))
L2=[]
for i in range(1,n+1):
    x=int(input("enter the number:"))
    L2.append(x)

print("the list_1 is:",L1)
print("the list_2 is:",L2)

L3=[]
for i in L1:
    L3.append(i)
for j in L2:
    L3.append(j)

L3.sort()

print("final list sorted list",L3)