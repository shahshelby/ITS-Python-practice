import datetime
todayWithTime = datetime.datetime.now() #today with the time
# print current datetime with all format
print(todayWithTime)
# print just Hour, Minute, Second
print("The current time is", datetime.datetime.strftime(todayWithTime, "%H:%M:%S"))
# get the day in the week
print(datetime.datetime.weekday(todayWithTime))

