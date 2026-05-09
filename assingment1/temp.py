#Ask the user for a temperature in Celsius (string input). Convert it to a float, then calculate and print the temperature in Fahrenheit.
cel=input("enter the temp in celsius:")
cel=float(cel)
fTemp=(cel*(9/5))+32
print("Fahrenheit tempreture = ",fTemp,"F")