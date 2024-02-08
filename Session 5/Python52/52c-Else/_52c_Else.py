a = float(input("Enter a number. "))
b = float(input("Enter a number to divide by. "))

try:
    print(f"The answer is {a / b}.")
except:  # it will try first and then if error happen then the except part will do
    print("This is division by zero")
else:  # it works
    print("Division feature Successfully work")
