# Design a program to continuously take a number n from the user
# and print whether it is positive or negative
# until the user enters "Quit".

while True:
    a = input("enter a number or type 'quit' to stop:")
    if a.lower() == "quit":
        print("goodbye!")
        break
    a = int(a)
    if a > 0:
        print("positive")
    elif a < 0:
        print("negative")
    else:
        print("zero")
