a=5
b=10
sum=a+b
print("sum is {}".format(sum)) #normal formatting
print("sum of {} and {} is {}".format(a,b,sum)) #with multiple placeholder
print("language is {}".format("python"))#normal formatting

#index based formatting
print("sum of {1} and {0} is {2}".format(a,b,sum))

#value based formatting
print("value of vars {a} & {b}".format(a=5,b=10))
x=3
y=4
#best using f-string
print(f"sum of {x} and {y} is {x+y}")
print(f"avg of {x} and {y} is {(x+y)/2}")