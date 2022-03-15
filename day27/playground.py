# args
from mimetypes import init


def add(*args):
    #args is a tuple, allowing for access by position
    print(sum(args))

#kwargs
#kwargs is basically a dictionary, allowing for access by key
def calculate(n, **kwargs):

    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    n += kwargs["add"]
    n *= kwargs["multiply"]

    print(n)

add(8, 5, 34, 6, 6, 4, 5, 2)
calculate(2, add=3, multiply=5)

# we can use the .get() method to grab the value from the dictionary, and if there is nothing it will just set it to None
class Car:

    def __init__(self, **kwarg) -> None:
        
        self.make = kwarg.get("make")
        self.model = kwarg.get("model")
        self.colour = kwarg.get("colour")
        self.seats = kwarg.get("seats")

my_car = Car(make="Nissan", colour="black")
print(my_car.make, my_car.colour)