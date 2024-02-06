def subtotal(orderAmt, salesTax):
    subtotal = float(orderAmt) * (1 + float(salesTax))
    return subtotal


#add firstOrderTotal variable here
#add secondOrderTotal variable here
#add thirdOrderTotal variable here
thirdTax = input("Enter your sales tax rate.")
thirdOrderTotal = subtotal(thirdOrderAmount, thirdTax)

print ("Your subtotal for the first order is %.2f" %firstOrderTotal)
print ("Your subtotal for the second order is %.2f" %secondOrderTotal)
print ("Your subtotal for the third order is %.2f" %thirdOrderTotal)

