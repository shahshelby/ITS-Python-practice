a = float(input("Enter a number. "))
b = float(input("Enter a number to divide by. "))

# will cause runtime error be ZeroDivisionError
# so I added if statement to countermeasure

if b == 0:
    print("cant divide by 0")
else:
    print(f"The answer is {a/b}.")
