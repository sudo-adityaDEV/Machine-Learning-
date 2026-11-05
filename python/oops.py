class Car:
    def __init__ (self,model,year,for_sale):
        self.model = model
        self.year = year
        self.for_sale = for_sale

    def drive(self):
        print(f"You are driving a {self.model}.")
    
    def describe(self):
        print(f"This is a {self.year} {self.model}.")

car1 = Car("XUV300",2020,False)

car2 = Car("Alto", 2015,False)
print(car1.model)
print(car1.for_sale)

print(car2.model)
car1.describe()
car2.describe()
car1.drive()




# Inheritance :

class Animal:
    def __init__ (self,name):
        self.name = name


    def eat(self):
        print(f"{self.name} is eating.")

            
    def sleep(self):
        print(f" {self.name} is sleeping .")



class dog(Animal):
    pass

class cat(Animal):
    pass

class mouse(Animal):
    pass



a1 = dog("Oreo")

print(a1.name)
a1.eat()

a2 = cat("Pussy")

print(a2.name)
a2.eat()
