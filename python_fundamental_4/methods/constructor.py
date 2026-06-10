class method:
    def __init__(self):
        print("constructor was called...")
p=method()

class student:
    def __init__(self,name,cgpa):
        self.name=name
        self.cgpa=cgpa

stu1=student("sanchali",9.62)
stu2=student("uma",8.80)
stu3=student("riya",7.67)

print(stu1.cgpa)
print(stu2.name)
print(stu3.name)