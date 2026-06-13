class employee: # parent class
    start_time="8am"
    end_time="4pm"
    
class AdminStaff(employee): # child clas
    def __init__(self,role):
        self.role=role

class Accountant(AdminStaff):
    def __init__(self,salary,role):
        super().__init__(role)
        self.salary=salary
acc1=Accountant("25_000","CA")
print(acc1.role,acc1.start_time,acc1.end_time,acc1.salary)