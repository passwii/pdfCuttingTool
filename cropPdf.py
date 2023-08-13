from PyPDF2 import PdfWriter, PdfReader
import os

inDir = r'inputs'
outDir = r'outputs\{packageID}'.format(packageID='package-FBA1781SY190')

inFile = os.path.join(inDir, r'{packageID}.pdf'.format(packageID='package-FBA1791SY190'))
pdf_reader = PdfReader(inFile)

page = pdf_reader.pages[0]
num_pages = len(pdf_reader.pages)
pageNo = 1
# static refs
x1 = page.cropbox.lower_left[0]
x2 = page.cropbox.lower_right[0]
y1 = page.cropbox.lower_left[1]
y2 = page.cropbox.upper_left[1]
width = (x2 - x1) / 2
height = (y2 - y1) / 3
labelID = 1


for pages in range(num_pages):
    for rows in range(3):
        for cols in range(2):
            label_x1 = x1 + cols * width
            label_y1 = y1 + rows * height
            label_x2 = label_x1 + width
            label_y2 = label_y1 + height

            page.cropbox.lower_left = (label_x1, label_y1 + 20)
            page.cropbox.upper_right = (label_x2, label_y2 + 20)

            outFile = os.path.join(outDir, r'{package}_P{page}_L{label}.pdf'.format(package='package-FBA1791SY190', page=pageNo, label=labelID))
            labelID += 1

            with open(outFile, 'wb') as output_pdf:
                pdf_writer = PdfWriter()
                pdf_writer.add_page(page)
                pdf_writer.write(output_pdf)
    pageNo += 1
# # cropbox page into 2 colums and 3 rows
# x1 = page.cropbox.lower_left[0]
# x2 = page.cropbox.lower_right[0]
# y1 = page.cropbox.lower_left[1]
# y2 = page.cropbox.upper_left[1]
#
# width = (x2 - x1) / 2
# height = (y2 - y1) / 3
#
#
# labelID = 0
#
# # crop each into single page
# for rows in range(3):
#     for cols in range(2):
#         label_x1 = x1 + cols * width
#         label_y1 = y1 + rows * height
#         label_x2 = label_x1 + width
#         label_y2 = label_y1 + height
# #
