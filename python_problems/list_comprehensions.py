"""
Problem: List Comprehensions
Platform: HackerRank
Difficulty: Easy
Concepts: List Comprehensions, Nested Loops, Conditional Filtering

Problem Link:
https://www.hackerrank.com/challenges/list-comprehensions/problem
"""
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    li=[[i,j,k] 
        for i in range(x+1) 
        for j in range(y+1) 
        for k in range(z+1)
        if i+j+k!=n]
    print(li)