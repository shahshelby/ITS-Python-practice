initialSalesGoal = 20000
multiplier = 100

for monthlyGoal in range(1, 12):
    if monthlyGoal == 6:
        print("skipping month 6")
        continue  # continue the loop (go back to for)
    monthlySalesGoal = initialSalesGoal + (monthlyGoal * multiplier)
    print("Your sales goal for month " + str(monthlyGoal) + " is " + str(monthlySalesGoal))

print("Good luck with your goals.")
