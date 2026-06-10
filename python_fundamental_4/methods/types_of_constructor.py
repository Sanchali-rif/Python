class student:
    def __init__(self,name,cgpa): #this is paramiterized constructor since it has multiple parameters
        self.name=name #these are properties of an object hence these are called instance attributes
        self.cgpa=cgpa
    def get_cgpa(self): #this method is to return the cgpa of the student
        return self.cgpa # this is a behavior of an object hence this is called instance method

stu1=student("sanchali",9.6)
stu2=student("uma",8.80)
stu3=student("riya",7.67)

print(f"{stu1.name} has cgpa= {stu1.get_cgpa()}")