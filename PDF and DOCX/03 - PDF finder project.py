# Finds all PDFs in a specified folder, adds them to a list and adds the first page to a new pdf

import PyPDF2
import os

absPath = 'D:\\OneDrive\\Leren\\Boeken\\Ondernemen'

pdfs = []

for file in os.listdir(absPath):
    # Adding all PDFs to the list
    if file.endswith('.pdf'):
        pdfs.append(absPath + '\\' + file)

writer = PyPDF2.PdfFileWriter()

for f in pdfs:
    pdfFileObject = open(f, 'rb')
    pdfFileReader = PyPDF2.PdfFileReader(pdfFileObject)
    pageObject = pdfFileReader.getPage(0)
    writer.addPage(pageObject)

output = open('coversOfAllMyPDFs.pdf', 'wb')

writer.write(output)

output.close()