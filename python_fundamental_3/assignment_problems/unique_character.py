# Ask the user for a string and print:
# - All unique characters
# - The count of unique characters

string="sanchali"
s=set(string)
print("all the unique characters are -")
for i in s:
    print(i,end=",")
print("\nthe count of unique characters -",len(s))