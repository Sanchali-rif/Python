"""
Problem: Nested Lists
Platform: HackerRank
Difficulty: Easy
Concepts: Nested Lists, Lists, Loops, Sorting

Problem Link:
https://www.hackerrank.com/challenges/nested-list/problem
"""
if __name__ == '__main__':
    student=[]
    for i in range(int(input())):
        name = input()
        score = float(input())
        student.append([name,score])
    marks=[]
    stu_name=[]
    for i in student:
        marks.append(i[1])
    min_marks=min(marks)
    while min_marks in marks:
        marks.remove(min_marks)
    for i in student:
        if i[1]==min(marks):
            stu_name.append(i[0])
    stu_name.sort()
    for i in stu_name:
        print(i)