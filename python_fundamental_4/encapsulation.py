class Bank:
    def __init__(self,name,id,balance):
        self.name=name #public data
        self._id=id #protected data
        self.__balance=balance #private data - data mangling

    def get_balance(self): #getter for privateb data
        return self.__balance
    def set_balance(self,newbalance): #setter for private data
        self.__balance=newbalance
    
acc1=Bank("sanchali","23REFF",10000000000)
acc1.set_balance(900000000)
print(acc1.name,acc1._id,acc1.get_balance())