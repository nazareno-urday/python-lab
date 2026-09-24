# This is just a little notebook of exercises to understand *args and **kwargs

def add(*args):
    result = [n for n in args]
    return sum(result)

def calculate (n,**kwargs):
    return (n + kwargs["add"]) * kwargs["multiply"]

print(add(2,3,7,4,71,8,63,76,67)) # First function
print(calculate(int(input("Choose a number: ")), add = int(5), multiply = int(2))) # Second function

# Class creation using **kwargs
class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

my_car = Car(make="Nissan", model="GT-R")
print(f"Your car is a {my_car.make} {my_car.model}.")
