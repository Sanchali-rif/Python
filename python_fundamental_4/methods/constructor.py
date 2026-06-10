class method:
    def __init__(self): # this is called default constructor since it has only one parameter which is self
        print("constructor was called...")
p=method()

class student:
    def __init__(self,name,cgpa): #inisializes an object , self, name,cgpa are parameters
        self.name=name #self.name=memeory where the name is going to be saved
        self.cgpa=cgpa

stu1=student("sanchali",9.62) #puting the value of name and cgpa dynamicslly
stu2=student("uma",8.80)
stu3=student("riya",7.67)

print(stu1.cgpa)
print(stu2.name)
print(stu3.name)