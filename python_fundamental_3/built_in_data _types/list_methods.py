nums=[43,8,1,15,50]
print("list is",nums)

nums.append(4) #appends at the end of the list
print("append '4' at the end of the listn -",nums)

nums.reverse() #reverse the entire list
print("reverse the entire list - ",nums)

nums.insert(2,10)
print("insert '10' at index 2 -",nums)

nums.sort() #sorting in ascending order
print("sorted the list in ascending order - ",nums)

nums.sort(reverse=True) #sorting in descending order
print("sorted the list in descending order - ",nums)
