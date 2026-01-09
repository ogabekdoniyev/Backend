#OOP Asoslari 
#a=6
#def add():
#pass
#print(type(a))
#print(type(add()))

class Car:
    brend="GM"

    def __init__(self,year,price,color):
        self.year=year
        self.price=price
        self.color=color
        self.is_engine_on=False

    def __str__(self):
        return f"{self.year}-yilgi mashina"

    def __repr__(self):
        return f"Car(year={self.year},price={self.price})"

    def star_car(self):
        self.is_engine_on=True
        return f"Car is successfully turned on!"
        return f"car is already on you stupid"

    def drive(self):
        if self.is_engine_on:
            return f"we are driving look at on your road!"
        return f"you should start engine on first!"

gentra=Car(price=10000,color="qora",year=2023)
print(gentra.drive())
print(gentra.star_car())
print(gentra.star_car())
#print(gentra.star_car())
print(gentra.drive())
#print(gentra.drive())


# obj1=Car(year=2025,price=10000,color="oq")
# obj2=Car(year=2022,price=8000,color="qizil")
# obj3=Car(year=2000,price=100,color="qora")
# #list()
# #print(repr(obj1))
# print(repr(obj1))
# print(obj2.year)
# print(obj2.price)
# print(obj2.color)





