class student:
    college_name="RCCIIT" #class attribute

    def __init__(self,name,cgpa): #instance attribute
        self.name=name
        self.cgpa=cgpa

stu1=student("sanchali",9.63)
print(stu1.college_name,stu1.name,stu1.cgpa)