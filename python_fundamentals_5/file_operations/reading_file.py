f = open(r"C:\Users\sahas\OneDrive\Desktop\vscode\Python\python_fundamentals_5\sample.txt", "r") #file object   

data=f.read() #reading the entire file
print(data)

f.close()