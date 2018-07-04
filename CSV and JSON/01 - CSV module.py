# The CSV Module

import csv

# Reading Files #

file = open("example.csv")
reader = csv.reader(file)
data = list(reader)

# Print every value from the list
print(data)

# Works like ' someList[row][column] '
print(data[0][4])

# Getting CSV data in a for loop

file = open("example.csv")
loopReader = csv.reader(file)

for row in loopReader:
    print("Row number " + str(reader.line_num) + " " + str(row))


# Writing Files #

writeFile = open("write.csv", "w", newline='')

writer = csv.writer(writeFile)

writer.writerow(['Hey', 'I', 'Can', 'Write'])
writer.writerow(['And', 'I', 'Can', 'Read'])
writer.writerow(['But', 'I', 'Can\'t', 'Sleep', 'Help'])

writeFile.close()

newFile = open("write.csv")
newRead = csv.reader(newFile)

for row in newRead:
    print(row)

# Delimiters and line terminators #

csvFile = open("write.csv", "a", newline='')
# Separates the values with a tab instead of a comma
# On the ond of the line, two line breaks will follow
writeCSV = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
writeCSV.writerow([1,2,3,4])
writeCSV.writerow([4,3,2,1])
csvFile.close()





