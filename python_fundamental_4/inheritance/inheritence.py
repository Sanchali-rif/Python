class employee: # parent class
    start_time="8am"
    end_time="4pm"
    
class teacher(employee): # child clas
    def __init__(self,name,subject):
        self.name=name
        self.subject=subject
        
    def change_time(self,newStartTime,newEndTime):
        self.start_time=newStartTime
        self.end_time=newEndTime

t1=teacher("sohini mam","science")
print(t1.name,t1.subject,t1.start_time,t1.end_time)

t1.change_time("8.15am","4.30pm")
print(t1.name,t1.subject,t1.start_time,t1.end_time)