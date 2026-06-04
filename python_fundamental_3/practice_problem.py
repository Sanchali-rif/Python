# Given a list of tuples containing information in the form (name, subject):
# Write a program to:
# 1. List all unique courses.
# 2. List all students enrolled in English.
# 3. Create a dictionary where:
# key   = student name
# value = set of courses taken by that student.

info=[
    ("alice","math"),
    ("bob","science"),
    ("alice","science"),
    ("charlie","math"),
    ("bob","math"),
    ("alice","english"),
    ("charlie","english"),
]
s=set()
for i in info:
    print(i)
