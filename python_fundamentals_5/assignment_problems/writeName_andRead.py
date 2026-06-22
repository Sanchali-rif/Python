# Create a program that:
# 1. Opens a file in write mode "names.txt"
# 2. Writes 5 names (one per line) entered by the user
# 3. Opens the same file in read mode and prints all names
with open(r"C:\Users\sahas\OneDrive\Desktop\vscode\Python\python_fundamentals_5\names.txt","w")as f:
    for i in range(0,5):
        name=input("enter the name: ")
        f.write(name)
        f.write("\n")

with open(r"C:\Users\sahas\OneDrive\Desktop\vscode\Python\python_fundamentals_5\names.txt","r")as r:
    name=r.read()
    print("all the names",name)