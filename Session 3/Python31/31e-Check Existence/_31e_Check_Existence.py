import os
if os.path.isfile("log.txt"):
    writeFile = open("log.txt", "a")
else:
    writeFile = open("log.txt", "w")

toLog = input("What do you want to write to the log? ")
#  tab the first line with \n and then add toLog to file
writeFile.write("\n" + toLog)
writeFile.close()
