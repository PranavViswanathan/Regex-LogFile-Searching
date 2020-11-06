import re # importiing the regular expression library

logFile = r"D:\Programming\Regex\SampleIBMLog.txt" #Location of log file on my device

# Function to read the lines of the log file
def readLines(logFile):
    with open(logFile) as f:
        for line in f:
            yield line # yeild is to prevent clogging up of memory


for line in readLines(logFile):
    mObj = re.match(r'(\d{2}/\d{2}) (\d{2}:\d{2}:\d{2}) warning:(.*)', line, re.I) # Matching to warning data with date and time info
    if mObj:
        print(line.strip())
        print(mObj.group(1), '->', mObj.group(2), '->', mObj.group(3)) # printing the warning
        print()
