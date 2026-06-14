class teacher():
    def get_designation(self): #duck typing
        print("designation = teacher")

class Accountant():
    def get_designation(self): #duck typing
        print("designation = Accountant")

t1=teacher()
t1.get_designation()

acc1=Accountant()
acc1.get_designation()