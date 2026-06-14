class employee:
    def get_designation(self):
        print("designation=employee")
        
class teacher(employee):
    def get_designation(self):
        print("designation = teacher")

t1=teacher()
t1.get_designation()
    