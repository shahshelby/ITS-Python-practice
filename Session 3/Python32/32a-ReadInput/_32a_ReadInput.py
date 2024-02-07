# Reading input from console and making sure it works
location = ""
while location != "HQ" and location != "North" and location != "south":
    location = input("Enter HQ, North, or South for a location ")

print(location)