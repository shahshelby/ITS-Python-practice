annualSales = 300000
if annualSales >= 500000:
    print("Gold Customer")
elif annualSales >= 300000:
    print("Silver Customer")
elif annualSales >= 100000:
    print("Bronze Customer")
# if and elif statement will always stop after first match // >= 300000
# run step by step so only Silver Customer will show not Bronze even if its >= 100000
print("Thank you for your business")
