initialSalesGoal = 20000
multiplier = 100
offMonth = False

for monthlyGoal in range(1, 13):
    if monthlyGoal == 6 and offMonth:  # and (both needs to be True)
        print("No goal for month 6")
        continue
    monthlySalesGoal = initialSalesGoal + (monthlyGoal * multiplier)

    print("Your sales goal for month " + str(monthlyGoal) + " is " + str(monthlySalesGoal))
    for weeklyGoal in range(1, 5):
        print("Your goal for week " + str(weeklyGoal) + " is " + str(monthlySalesGoal / 4))
print("Good luck with your goals.")

'''
Block part belong to for loop,if,while statements with indented part
if to check for condition if its true or false
multiple condition with Elif for other possibilities
else (all of above are False then do this)
order matters
while loop is best when number of times in loop is predict upon a condition
for loop run a set number of times
break to quit loop, continue to go up to next iteration of loop
pass is placeholder
'''
