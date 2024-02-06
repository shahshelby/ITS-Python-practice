# need library
# if the log file exists, append to it

# otherwise, open a new log

toLog = input("What do you want to write to the log? ")
writeFile.write("\n" + toLog)
writeFile.close()
