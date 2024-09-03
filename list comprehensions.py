
# effecient way to create lists
# Simple list comprehension
# (basic syntax- expression for item in iterable)

# question- Create a list of squares of numbers from 0 to 9
squares = [x**2 for x in range(10)]
print(squares)


# list comprehension with condition
# question- create a list of even numbers from 0 to 9
evens = [x for x in range(10) if x % 2 == 0]
print(evens)


# list comprehension with condition & expression
# question- create a list of squares with even numbers from 0 to 9
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)


# using functions within list comprehensions
# question- convert a temperature from celsius to fahrenhiet
celsius = [0, 5, 10, 15, 20]
fahrenhiet = [temperature * (9/5) + 32 for temperature in celsius]
print(fahrenhiet)