class Product:
    def __init__(self, name, desc, price,ratings):
        self.name = name
        self.description = desc
        self.price = price
        self.ratings = ratings

    def avg(self):
        return sum(self.ratings)/ len(self.ratings)
p1 = Product('iphne','hello', 10, [1,2,3,4,5])
print p1.avg()
print p1.name