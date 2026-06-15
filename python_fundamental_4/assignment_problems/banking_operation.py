# Concept: Class and Objects
# Create a class BankAccount with attributes:account_number,owner_name,balance
# Add methods to:deposit,withdraw,check_balance

class BankAccount:
    def __init__(self,account_number,owner_name,balance):
        self.account_number=account_number
        self.owner_name=owner_name
        self.balance=balance

    def deposit(self,amount):
        self.balance=self.balance+amount
        print(self.owner_name,"your new balance is",self.balance)

    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance=self.balance-amount
            print(self.owner_name," your new balance is",self.balance)
        else:
            print(self.owner_name,"withdraw amount is more than balance!!")

    def check_balance(self):
        print(self.owner_name,"your current balance is",self.balance)

acc1=BankAccount(2345,"sanchali",50_000)
acc2=BankAccount(2346,"uma",100_000)
acc1.deposit(30_000)
acc2.withdraw(100_00)
acc2.check_balance()