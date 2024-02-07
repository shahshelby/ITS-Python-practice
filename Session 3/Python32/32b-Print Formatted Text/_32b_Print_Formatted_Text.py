price = 3.95
widgets = 5
msg = ("The price of the widget is {price: .2f}")
print(f"We have {widgets} in stock.")
#  overriding the price from 3.95 to 4
print(msg.format(price=4))
#  not overriding
print(msg.format(price=price))
"""
with statement ensure file properly closed
input statement for capturing user data
formatted text with {} curly brackets to indicate the placeholder for vars
"""