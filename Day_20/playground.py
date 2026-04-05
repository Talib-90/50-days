# Unlimited arguments,This is a tuple
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum
    
# print(add(3,4,5,6,7, 5.5))

# Unlimited keywords arguments, This is a dictionary
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

# calculate(7, add = 5, multiply = 4)

class Car:

    def __init__(self, **kwargs):
        # self.make = kwargs["make"]
        # self.model = kwargs["model"]
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")
        
myCar = Car(model = "GT-R")
print(myCar.make)