regions = ["North", "South", "East", "West"]
sales = [30000, 20000, 40000, 35000]
employees = ["Alice", "Vera", "Flo", "Mel"]
locations = []

for employee in employees:
    print(employee)

employees.append("Belle")  # add new item to list (goes to the bottom)
employees.remove("Flo")  # remove an item from list
employees.sort()  # sort items in the list alphabetically
print(" ")

for employee in employees:
    print(employee)
