# Ask the user for a string and check if it is a palindrome.
# A palindrome reads the same forward and backward (e.g., "madam", "racecar").

a=input("enter the word:")
if(a==a[::-1]):
    print("palindrom number")
else:
    print("not palindrom")