#Lets start with the basics of Python 
# # Numeric type
#its numerics
# integer - with numbers
a= 10
print(type(a))

# Float - with decimal numbers
b= 10.5
print(type(b))

# complex - with real and imaginary part
c= 8+6j
print(type(c))




# set types
# set - unordered collection of unique items-no duplicates
s= {1, 2, 3, 4, 5}
print(type(s))

# frozen set - represents immutable sets- elements cannont be changed
fs= frozenset([1,2,3,4,5])
print(type(fs))

# Boolean - just True or False
boolean = False
print(type(boolean))



# Type Checking- the python type of function will return the type of that argument. we can use this to check whether our arg is int/str.
# isinstance(obj, type) - it shows True or False
x = 100
print(isinstance(x, int))

y = "Balaji"
print(isinstance(y, str))

z = 10.55
print(isinstance(z, int))




# comments

"""
list to set - removes duplicates
s = [1,2,2,3,3,4]
ss = set(s)
print(ss)

"""
