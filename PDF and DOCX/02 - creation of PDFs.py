# Making PDFs and some basic visual manipulation

import PyPDF2

# with this module, you can only copy stuff from other PDFs and do some basic visual tricks
pdf1 = open('example.pdf', 'rb')
pdf2 = open('example2.pdf', 'rb')

firstReader = PyPDF2.PdfFileReader(pdf1)
secondReader = PyPDF2.PdfFileReader(pdf2)

pdfWriter = PyPDF2.PdfFileWriter()

# Writing all pages of the file to an pdfWriter
for page in range(firstReader.numPages):
    pageObject = firstReader.getPage(page)
    pdfWriter.addPage(pageObject)

for page in range(secondReader.numPages):
    pageObject = secondReader.getPage(page)
    pdfWriter.addPage(pageObject)

# Creating the output file
outputFile = open('created.pdf', 'wb')

# Writing everythin to the file
pdfWriter.write(outputFile)

pdf1.close()

pdf2.close()

outputFile.close()


# Rotating Pages #

manipFile = open('created.pdf', 'rb')

manipReader = PyPDF2.PdfFileReader(manipFile)

page = manipReader.getPage(0)

# Telling it to put the page horizontally
page.rotateClockwise(90)

writer = PyPDF2.PdfFileWriter()

writer.addPage(page)

result = open('rotate.pdf', 'wb')

writer.write(result)

manipFile.close()

result.close()

# Encrypting PDFs #

file = open('created.pdf', 'rb')

read = PyPDF2.PdfFileReader(file)

write = PyPDF2.PdfFileWriter()

write.addPage(read.getPage(0))

# Setting a password for the file straightforward
write.encrypt('nipple')

res = open('encrypted.pdf', 'wb')

write.write(res)

res.close()

