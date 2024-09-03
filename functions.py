
# Functions - Block of code that performs specific task
#basic funtion defining
def greet():
    print("Hello, World!")

greet()    # i called the function




# functions can accept parameters(Arguments) that allow you to pass data into the function

def greet(name):
    print(f"Hello, {name}!")

greet("Balaji")



# return statement
# functions can return a value using the 'return' keyword. if funct doesnt have return statement, itll take 'None" by default.

def add(a, b):
    return a+b
result = add(2,4)
print(result)


# keyword arguments - when you pass arguments to a function using their parameters names
def display_info(name, age):
    print(f"Name : {name}, Age : {age}")

display_info(age = 24, name = "Balaji")


# *args - allows a function to accept any no of positional arguments 
# **kwargs - allows a function to accept any number of keyword arguments
def print_numbers(*args):
    for number in args:
        print(number)

print_numbers(1, 2, 3,)


def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}, {value}")

print_details(name="Balaji", age= 24)



# Lambda functions - are small anonymous function - lambda keyword - they can have any no of parameters, but only one expression.
add = lambda x, y: x + y
print(add(2,5))


