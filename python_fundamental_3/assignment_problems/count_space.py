# Write a program that takes a string from the user
# and prints the number of spaces in the string.

a=input("enter the sentence:")
count=0
for i in a:
    if i==" ":
        count=count+1
print(f"number of spacing in this sentence is {count}")