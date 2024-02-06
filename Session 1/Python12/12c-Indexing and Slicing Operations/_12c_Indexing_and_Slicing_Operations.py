regions = ["North", "South", "East", "West"]
sales = [30000, 20000, 40000, 35000]
employees = ["Alice", "Vera", "Flo", "Mel"]

# Python = zero-based language (start with 0)
print("Region: ", regions[0], "\nSales: ", sales[0])
# [-1] represents the last item in a list, [-2] second to last
print("Region: ", regions[-1], "\nSales: ", sales[-1])

employees[2] = "Belle" # Changing data in a list at index "Flo" to "Belle"

for employee in employees:
    print(employee)