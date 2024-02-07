initialSalesGoal = 20000
multiplier = 100

# for loop is a loop that set to run on certain amount of time
# remember indexing from zero [0]
# for monthlyGoal in range(12): # this will do 0 to 11 (12 times)
# for monthlyGoal in range(1, 12): # this will do 1 to 12 (11 times)
for monthlyGoal in range(1, 13):  # this will do 1 to 13 (12 times)
    monthlySales = initialSalesGoal + (monthlyGoal * 100)
    print("Your sales goal for month " + str(monthlyGoal) + " is " + str(monthlySales))

print("Good luck")
