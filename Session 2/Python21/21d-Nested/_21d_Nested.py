annualSales = 300000
# region = "North"
region = "West"

if annualSales >= 500000:
    print("Gold Customer")
elif annualSales >= 300000:
    print("Silver Customer")
    if region == "North":
        print("Send a snowboard")
    else:
        print("Send a baseball bat")
# Nested if statement is an if statement inside another if statement
elif annualSales >= 100000:
    print("Bronze Customer")
print("Thank you for your business")

