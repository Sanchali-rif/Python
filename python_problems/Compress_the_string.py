"""
Problem: Compress the String!
Platform: HackerRank
Difficulty: medium
Concepts: itertools.groupby(), Iterators, Strings

Problem Link:
https://www.hackerrank.com/challenges/compress-the-string/problem
"""
from itertools import groupby
s=input()
for key,group in groupby(s):
    print((len(list(group)),int(key)),end=" ")