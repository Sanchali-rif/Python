# Design and create an online store for Products (name, price).
# Track the total number of products being created.
# Create a static method to calculate discount on each product
# based on a percentage (%) parameter.

class product_store:
    count=0

    def __init__(self,name,price): #initialize objects
        self.name=name
        self.price=price
        product_store.count=product_store.count+1
    
    def get_product_details(self): #instance method
        print(f"{self.name} of price {self.price}")
    
    @classmethod
    def get_count(cls):
        print(f"total {cls.count} products are created")

    @staticmethod
    def cal_discount(price,percentage):
        price=price-(price*percentage/100)
        print(f"final discounted price is {price}")

product1=product_store("laptop",70_000)
product2=product_store("phone",20_000)
product3=product_store("Iphone",80_000)

product1.get_product_details()
product_store.get_count()
product3.cal_discount(product3.price,10)
