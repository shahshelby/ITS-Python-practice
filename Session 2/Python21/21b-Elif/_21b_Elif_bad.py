annualSales = 600000
if annualSales >= 100000:
    print("Bronze Customer")
elif annualSales >= 300000:
    print("Silver Customer")
elif annualSales >= 500000:
    print("Gold Customer")
# if and elif statement will always stop after first match // >= 100000
# put the largest on top to fix this
print("Thank you for your business")
