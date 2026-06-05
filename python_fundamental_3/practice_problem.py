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
course=set()
for tup in info:
    course.add(tup[1])
print("All unique courses are-",course)

print("\nAll students enrolled in English:")
for name,course in info:
    if course=="english":
        print(name)

dict={}
student_set=set()
for tup in info:
    student_set.add(tup[0])
for student in student_set:
        dict.update({student:set()})
for name,course in info:
     for i in dict:
          if name==i:
               dict[i].add(course)
print("\nthe dictionary is -",dict)