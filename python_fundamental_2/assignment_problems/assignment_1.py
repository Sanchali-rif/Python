# Write a program that takes salary as input.
# Using conditional statements, calculate the final tax based on these rules:

# If salary < 30000  -> Tax rate = 5%
# If salary is between 30000 and 70000 -> Tax rate = 15%
# If salary > 70000 -> Tax rate = 25%

sal=int(input("enter your salary:"))
if (sal<30000):
    tax=sal*(5/100)
    print("your tax is 5 percent of your salary that is",tax,"rupees")
elif(sal>30000 and sal<70000):
    tax=sal*(15/100)
    print("your tax is 15 percent of your salary that is",tax,"rupees")
else:
    tax=sal*(25/100)
    print("your tax is 25 percent of your salary that is",tax,"rupees")