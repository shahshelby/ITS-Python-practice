import random

#for i in range(5):
#    guess = int(input("Enter a number between 1 and 10. "))
#    randNum = randint(1,10)
#    if guess == randNum:
#        print("We matched!")
#       break
#   else:
#        print("We did not match. Try again")

print(random.randrange(1,10,2))

print(random.sample(range(0,100),5))

cars = ["sedan","jeep","ford","ferrari"]
print(random.choice(cars))

cars = ["sedan","jeep","ford","ferrari"]
random.shuffle(cars)
print(cars)

"""
Python have builtin module that can be import
Math module have builtin math function
Datetime module works with date and time formatting
IO module for files and data streams
Sys module accesses system features
OS module accesses operating system functions
Random helps with randomizing
"""