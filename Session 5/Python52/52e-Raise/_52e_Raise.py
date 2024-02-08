def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return x / y

x = float(input("Enter a number. "))
y = float(input("Enter a number to divide by. "))


try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(e)
