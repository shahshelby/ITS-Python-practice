def subtotal(orderAmt, salesTax=.08):  # giving default values to function
    subtotal = float(orderAmt) * (1 + float(salesTax))
    return subtotal


firstOrderTotal = subtotal(300)  # will use default value for salesTax
secondOrderTotal = subtotal(400, .06)

thirdOrderAmount = input("What was the order amount? ")
thirdTax = input("Enter your sales tax rate. ")
thirdOrderTotal = subtotal(thirdOrderAmount, thirdTax)

fourthOrderTotal = subtotal(800)  # will use default value for salesTax

print("Your subtotal for the first order is %.2f" % firstOrderTotal)
print("Your subtotal for the second order is %.2f" % secondOrderTotal)
print("Your subtotal for the third order is %.2f" % thirdOrderTotal)
print("Your subtotal for the fourth order is %.2f" % fourthOrderTotal)