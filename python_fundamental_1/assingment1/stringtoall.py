'''The user enters a string containing a number (e.g., "45"). Convert it to:

* an integer
* a float
* a string again

Print all three values along with their data types.
'''
a=input("enter the num:")
print(int(a),"is",type(int(a)))
print(float(a),"is",type(float(a)))
print(a,"is",type(a))