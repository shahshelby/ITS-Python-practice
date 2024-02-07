import os
if os.path.isfile("log_old.txt"):
    os.remove("log_old.txt")
    print("Remove log_old file")
else:
    print("There was no log_old file to remove.")
    writeFile = open("log_old.txt", "w")  # create a new file
