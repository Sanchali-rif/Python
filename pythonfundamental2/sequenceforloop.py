a=input("enter the word:")
b=input("letter to find:")
count=0
for i in a:
    if b==i:
        count=count+1
print("total number of",b,"in","a","is",count)