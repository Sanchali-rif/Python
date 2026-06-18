#with keyword do not need explecit f.close() they automatically close the file once the operation is done
with open(r"C:\Users\sahas\OneDrive\Desktop\vscode\Python\python_fundamentals_5\sample.txt", "r") as f:
    print(len(f.read()))
