# Create a program that:
# 1. Opens a file in append mode "log.txt"
# 2. Adds a new log entry (e.g., "Program run successfully")
# 3. Opens the file in read mode and prints all logs

log=input("enter the log: ")
with open(r"C:\Users\sahas\OneDrive\Desktop\vscode\Python\python_fundamentals_5\nlog.txt","a")as f:
    f.write(log)
with open(r"C:\Users\sahas\OneDrive\Desktop\vscode\Python\python_fundamentals_5\nlog.txt","r")as r:
    all_logs=r.read()
    print(all_logs)
