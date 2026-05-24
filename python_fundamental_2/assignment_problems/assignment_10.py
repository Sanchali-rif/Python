# Let's create a "Number Guessing Game".
# Given a secret number (already decided by you),
# write a program that asks the user to guess it and prints:
# "Too high"  -> if the guess is above the number
# "Too low"   -> if the guess is below the number
# "Correct!"  -> if the guess matches the secret number

a=12
b=int(input("guess the num:"))
if(a==b):
    print("correct!")
elif(a>b):
    print("too low")
else:
    print("too high")