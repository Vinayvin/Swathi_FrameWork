class Book:
    def __init__(self,id,cost):
        self.id=id
        self.cost=cost

ob=Book(1001,"Rs.250")
print("Book Id:",ob.id)
print("Book price:",ob.cost)
