class laptop:
    storage_type="SSD"
    def __init__(self,RAM,storage):
        self.RAM=RAM
        self.storage=storage

    @classmethod  #decorator function- changes the behavious of the function
    def get_storage_type(cls): #class method formed
        print(f"storage type = {cls.storage_type}")

    def get_detail(self): 
        print(f"laptop has {self.RAM} RAM ,{self.storage} of storage and storage type is {self.storage_type}")

L1=laptop("16gb","512gb")
L1.get_storage_type()