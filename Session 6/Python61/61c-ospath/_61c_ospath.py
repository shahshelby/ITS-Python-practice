import os
#if log.txt exists, open it in append mode

#if log.txt does not exists, open it in write mode

toLog = input("What do you want to write to the log? ")
writeFile.write("\n" + toLog)
writeFile.close()

