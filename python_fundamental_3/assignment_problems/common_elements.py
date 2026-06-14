# Write a program to check whether two lists share no common elements.

L1=[1,2,3,4,]
L2=[5,6,7,8]
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