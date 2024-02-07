annualSales = 200000
# newCustomer = False
newCustomer = True

if annualSales >= 500000:
    print("Gold Customer")
elif annualSales >= 300000:
    print("Silver Customer")
elif annualSales >= 100000 and newCustomer:  # newCustomer == True
    print("Bronze Customer and first-time prize winner")
# Compound conditional with "and" or "or"
elif annualSales >= 100000:
    print("Bronze Customer")
print("Thank you for your business")
