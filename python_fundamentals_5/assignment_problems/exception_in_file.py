# Write a program that tries to open "data.txt" in read mode.
# If the file does not exist, catch the exception and print "File not found!".

try:
    with open(r"C:\Users\sahas\OneDrive\Desktop\vscode\Python\python_fundamentals_5\data.txt", "r")as f:
        data=f.read()
        print(data)

except FileNotFoundError:
    print("File not found")