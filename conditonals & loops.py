
# conditionals --- based on certain conditions, we execute different blocks of code

age = 24

if age < 18:                         # it will execute if this condition is "True"
    print("You are Minor.")
elif 18 <= age < 60:                 # if the above condition is False, this is another condition
    print("You are an Adult.")
else:                                # if the above conditions are False, then the correct one is "Else"
    print("You are Senior Citizen.")




# loops  ---  used to execute blocks of code repeatedly based on condition or an iteration over a sequence
# For loop
#Range in for loop - range(5) is 0,1,2,3,4
for i in range(5):
    print(i)


# iterating over a list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


# iterating over a string
name = "Balaji"

for letter in name:
    print(letter)





# while loop ---
# 1. Basic while loop:

count = 0

while count < 5:
    print("Count is: ", count)
    count = count + 1


# 2. while loop with break:

count = 0

while True:   #this is infinite loop
    if count == 5:
        break   # break means we exit the loop
    print("count is: ", count)
    count = count + 1  


# 3. while loop with continue:

count = 0

while count < 10:
    count = count + 1
    if count % 2 == 0:
        continue  # skip print statement for even numbers
    print("count is: ", count)







# control statements
# break - exits the loop immediately
for i in range(10):
    if i == 5:
        break
    print(i)

# continue - skips the rest of the code inside the loop & moves to the next iteration. 
for i in range(10):
    if i == 5:
        continue
    print(i)
