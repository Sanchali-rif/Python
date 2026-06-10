class laptop:
    storage_type="SSD"
    def __init__(self,RAM,storage):
        self.RAM=RAM
        self.storage=storage

    def get_detail(self): #instance methode , since it has only 1 parameter that is self
        print(f"laptop has {self.RAM} RAM ,{self.storage} of storage and storage type is {self.storage_type}")

L1=laptop("16gb","512gb")
L2=laptop("8gb","256gb")
L1.get_detail()