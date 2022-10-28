# agrs ---- *number
# def add(*numbers):
#     print(type(numbers)) #-------- Tuple
#     sum = 0
#     for n in numbers:
#         sum += n
#     return sum


# print(add(1,2,3,4,5))


# kwags ----- **numbers

# def calculate(n, **numbers):
    # print(type(numbers))    #------ Dict
    # print(numbers)

    # for key, value in numbers.items():
    #     print(key, value)

#     n += numbers["add"]
#     n *= numbers["multiply"]
#     print(n)


# calculate(2, add = 3, multiply = 5)


class Car:
    
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")

my_car = Car(make = "Nissan", model = "GT-8")

print(my_car.model)
