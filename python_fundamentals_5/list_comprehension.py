square=[] #way 1 
for i in range(1,6):
    square.append(i**2)
print(square)

sq=[i*i for i in range(1,6)] #way 2
print(sq)

odd_sq=[i*i for i in range(1,6) if i%2!=0] #can also add condition
print(odd_sq)

num=[-2,3,0,7,-4,8,-3]
num=[0 if val<0 else val for val in num] # replace -ve number into 0
print(num)

words=["sanchali","saha","rcciit"]
words=[val.upper() for val in words] # make all the words uppercase
print(words)