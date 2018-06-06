# Reading data From spreadsheet
# This program extracts all url's about a certain subject from the file

import openpyxl

# Opens the workbook file (xlsx)
wb = openpyxl.load_workbook('workbook.xlsx')

workSheet = wb.active

# Getting rows and columns
trumpList =[]
trumpCount = 0
for row in workSheet['A1':'O689']:
# getting each value trump from every column
    for obj in row:
        if 'trump' in str(obj.value).lower():
            trumpList.append([obj.coordinate, obj.value])
            trumpCount = trumpCount + 1

print(str(trumpCount) + ' Items found about Trump!')

urlList = []
for items in trumpList:
    if 'www.' in items[1]:
        urlList.append(items[1])

print(str(len(urlList)) + ' Urls found ')
f = open('trumpUrls.txt', 'w')

# Writing all found URLs to a text file
for i in urlList:
    f.write(i + '\n')

print('Urls written to trumpUrls.txt')

f.close()



