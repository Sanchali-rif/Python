"""
Problem: Write a Function
Platform: HackerRank
Difficulty: Medium
Concepts: Functions, Conditional Statements, Leap Year Logic

Problem Link:
https://www.hackerrank.com/challenges/write-a-function/problem
"""

def is_leap(year):
    leap = False
    
    if year%4==0:
        if year%100!=0:
            leap = True
        elif year%100==0:
            if year%400==0:
                leap = True
            else:
                leap = False
    else:
        leap = False
    return leap

year = int(input())
print(is_leap(year))