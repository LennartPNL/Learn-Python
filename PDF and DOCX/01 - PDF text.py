# Getting text from PDF Files and manipulating PDFs
# pip install PyPDF2

import PyPDF2

pdfObject = open('example.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfObject)

# Counts all pages of a PDF file
print(pdfReader.numPages)

# Sets the pageobject to the first page
pageObject = pdfReader.getPage(0)

# Gets all text from the page
print(pageObject.extractText())

# File Decryption #

encrReader = PyPDF2.PdfFileReader(open('enc.pdf', 'rb'))

# Checking if the file is encrypted
print(encrReader.isEncrypted)

try:
    # This will not work, the file is password protected
    encrReader.getPage(0)
except Exception as e:
    print(e)


try:
    encrReader.decrypt('skittles')
    page = encrReader.getPage(0)
    print(page.extractText())
except Exception as e:
    print(e)




