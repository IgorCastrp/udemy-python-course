def add(*args):
    sum_1 = 0
    for n in args:
        sum_1 += n
    return sum_1


print(add(2, 3, 54, 54, 65, 65, 1000))


def calculate(n, **kwargs):
    print(kwargs)

    # for key, value in kwargs:
    #     print(key)
    #     print(value)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(model="GT-R")

print(my_car.make)

