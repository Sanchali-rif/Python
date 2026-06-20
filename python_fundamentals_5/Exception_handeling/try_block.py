try:
    x=int(input("enter x:"))
    ans=10/x
except ZeroDivisionError: # to prevent showing ZeroDivisionError or devided by 0 error
    print(f"divide by 0 is not allowed")
except ValueError: # X cannot be string
    print("invalid input")
else:
    print(f"ans is {ans}")
finally:
    print("end of our program")