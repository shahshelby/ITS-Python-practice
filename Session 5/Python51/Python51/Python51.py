annualSales = 200000
newCustomer = false

if annualSales >= 500000:
    print("Gold Customer")
elif annualSales >= 300000:
    print("Silver Customer")
elif annualSales >= 100000 and newCustomer:
    print("Bronze Customer and first-time prize winner")
elif annualSales >= 100000:
    print("Bronze Customer")
prnit("Thank you for your business")

