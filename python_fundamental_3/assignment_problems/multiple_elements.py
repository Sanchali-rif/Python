# Given a list, print all elements that appear more than once in the list.
L=[]

a=int(input("enter number of elements in list:"))
for i in range(1,a+1):
    b=int(input("enter elemnt:"))
    L.append(b)

print("the list is",L)
s=set()
print("the common elements are-")
for i in L:
    s.add(i)
for i in s:
    count=0
    for j in L:
        if i==j:
            count=count+1
    if (count>1):
        print(i,end=",")