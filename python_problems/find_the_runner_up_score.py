"""
Problem: Find the Runner-Up Score!
Platform: HackerRank
Difficulty: Easy
Concepts: Lists, Loops, max(), Conditional Statements

Problem Link:
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
"""
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    maxMarks=max(arr)
    runnerUp=[]
    for i in arr:
        if(maxMarks>i):
            runnerUp.append(i)
    print(max(runnerUp))