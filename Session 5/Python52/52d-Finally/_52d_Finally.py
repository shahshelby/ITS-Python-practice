a = float(input("Enter a number. "))
b = float(input("Enter a number to divide by. "))

try:
    print(f"The answer is {a/b}.")
except:
    print("This did not work. Did you try to divide by zero or something?")

# else: The else block is executed if the try block raises no exceptions.
# It's typically used to execute code that should run only if the try block does not raise any exceptions.5
else:
    print("You successfully used the division feature in Python")
# finally: The finally block is executed whether an exception occurs or not.
# It's typically used to execute cleanup code, such as closing files or releasing resources,
# regardless of whether an exception was raised.
finally:
    print("Thanks for playing")
