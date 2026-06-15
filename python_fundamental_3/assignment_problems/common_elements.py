# Write a program to check whether two lists share no common elements.

L1=[]
L2=[]

a=int(input("enter number of elements in list 1:"))
for i in range(1,a+1):
    b=int(input("enter elemnt:"))
    L1.append(b)

y=int(input("enter number of elements in list 2:"))
for i in range(1,y+1):
    b=int(input("enter elemnt:"))
    L2.append(b)
print("the list are-",L1,L2)
s=set()
c=set()
x=set()
for i in L1:
    s.add(i,)
for i in L2:
    c.add(i,)
common=s.intersection(c)
if len(common)==0:
    print("no common elements")
else:
    print("common elements are-",common)