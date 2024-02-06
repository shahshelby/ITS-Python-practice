a = float(input("Enter a number. "))
b = float(input("Enter a number to divide by. "))

try:
    print(f"The answer is {a/b}.")
except:
    # add code for raise here
    #  
    print("This did not work. ")
else:
    print("You successfully used the division feature in Python")
finally:
    print("Thank you for playing.")
