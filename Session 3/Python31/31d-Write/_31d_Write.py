writeFile = open("log.txt", "w")
toLog = input("What to write in the file? ")
writeFile.write(toLog)
writeFile.close()
# the write function will overwritten if the file already existed and will create a file if it doesn't exist
