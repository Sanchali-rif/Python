"""
Problem: sWAP cASE
Platform: HackerRank
Difficulty: Easy
Concepts: Strings, Functions, Character Methods

Problem Link:
https://www.hackerrank.com/challenges/swap-case/problem
"""
def swap_case(s):
    swap=""
    for i in s:
        if i.isupper()==True:
            swap=swap+i.lower()
        elif i.islower()==True:
            swap=swap+i.upper()
        else:
            swap=swap+i
    return swap

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)