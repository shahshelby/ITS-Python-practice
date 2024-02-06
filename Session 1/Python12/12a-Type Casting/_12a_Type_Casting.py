price = 3.95
widgets = 5
print("The price of the widget is ", price)
# print("We have " + widgets + " in stock.")
# this above will cause error since you can't concat str with int

# Type casting to case type of one data to another (int to str)
print("We have " + str(widgets) + " in stock.")

print(price * widgets)  # this is float * int, then it convert to float no conversion needed

# converting price to integer and widgets to float
print("price =", int(price), "\nwidgets =", float(widgets))
