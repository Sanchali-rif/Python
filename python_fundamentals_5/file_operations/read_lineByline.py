f = open(r"C:\Users\sahas\OneDrive\Desktop\vscode\Python\python_fundamentals_5\sample.txt", "r") #file object   

line=f.readline() #reads the the data line by line
print(line)

line=f.readline() #reads the the data after the 1st line
print(line)

f.close()