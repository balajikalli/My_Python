# OOPs is programming paradigm that uses objects and classes to organize & structure your code

# Class - attributed and functions

class vehicle:
    def __init__(thing, name, year):
        thing.name = name
        thing.year = year
    
    def sound(thing):
        return "Horn!"
    


# Object - instance of class

my_vehicle = vehicle("name: Car", "year: 2012")
print(my_vehicle.name)
print(my_vehicle.year)


