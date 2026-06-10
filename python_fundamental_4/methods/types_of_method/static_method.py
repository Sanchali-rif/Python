class laptop:
    storage_type="SSD"
    def __init__(self,RAM,storage):
        self.RAM=RAM
        self.storage=storage

    @classmethod  
    def get_storage_type(cls): 
        print(f"storage type = {cls.storage_type}")

    def get_detail(self): 
        print(f"laptop has {self.RAM} RAM ,{self.storage} of storage and storage type is {self.storage_type}")

    @staticmethod
    def discount(price,discount):
        final_price=price-(price*discount/100)
        print(f"the final price is {final_price}")

L1=laptop("16gb","512gb")
L1.discount(40_000,10)