s={1,2,3,4}
s2={4,5,6,7,8}
x={33,"k",89.9}

s.add(10) #add a val
print(s)

s.remove(10) #remove a val
print(s)

print(s.union(s2)) #returns new union

print(s.intersection(s2)) #returns new intersection

x.pop() #remove random val
print(x)

x.clear() #returns empty set
print(x)