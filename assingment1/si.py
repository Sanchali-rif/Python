'''Ask the user for:
Principal (P)
Rate (R)
Time (T)
Convert all the values to floats and compute the Simple Interest using the formula:
SI=(P∗R∗T)/100
'''
P=int(input("enter the principal:"))
R=int(input("enter the rate:"))
T=int(input("enter the time:"))
SI=(P*R*T)/100
print("simple interest:",SI)