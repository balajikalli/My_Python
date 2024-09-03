# Type conversion
# implicit - python converts one data type to other without user involvement, like if we add or multiply
a =5
b = 1.44

sum = a+b
print(sum)
print(type(sum))  #int + float became float


# explicit - manually convert datatype using int(), float(), str()

# str to int
a = "10"
b = int(a)
print (a)

# int to str
c= 10
d = str(c)
print(d)

# str to list
h = "balaji"
hh = list(h)
print(hh)

# list to tuple
t = [1,2,3,4,5]
tt = tuple(t)
print(tt)

# list to set - removes duplicates
s = [1,2,2,3,3,4]
ss = set(s)
print(ss)
