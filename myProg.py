import re

logFile = r"D:\Programming\Regex\SampleIBMLog.txt"


def readLines(logFile):
    with open(logFile) as f:
        for line in f:
            yield line


for line in readLines(logFile):
    mObj = re.match(r'(\d{2}/\d{2}) (\d{2}:\d{2}:\d{2}) warning:(.*)', line, re.I)
    #mObj = re.match(r'(\d{2}/\d{2}) (\d{2}:\d{2}:\d{2}) warning:(.*)', line, re.I)
    if mObj:
        print(line.strip())
        print(mObj.group(1), '->', mObj.group(2), '->', mObj.group(3))
        print()
