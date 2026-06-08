# Given a list of words:
# words = ["apple", "banana", "kiwi", "cherry", "mango"]
# Create a dictionary that maps each word to its length.
# Example:{"apple": 5, "banana": 6, "kiwi": 4, ...}

words={}
n=int(input("enter the number of elements:"))
for i in range(0,n):
    element=input("enter the word:")
    words.update({
        element:len(element)
    })
print("the dictionary is-",words)