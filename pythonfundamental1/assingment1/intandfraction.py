'''Take a decimal number as input (like 45.78) and output its:
Integer part → 45
Fractional part → 0.78
'''
a=float(input("enter the num:"))
print("Integer part:",int(a//1))
print("Fractional part:",round(a%1,2))