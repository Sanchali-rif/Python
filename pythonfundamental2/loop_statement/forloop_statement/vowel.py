a=input("enter the word:")
count=0
for i in a:
    if "a"==i or "e"==i or "i"==i or"o"==i or"u"==i:
        count=count+1
print("total number of vowels in",a,"is",count)