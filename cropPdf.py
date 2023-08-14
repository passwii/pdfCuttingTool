from PyPDF2 import PdfWriter, PdfReader
import os

reader = PdfReader("inputs/tmp.pdf")
writer = PdfWriter()
page = reader.pages[0]

x01 = page.cropbox.lower_left[0]
x02 = page.cropbox.lower_right[0]
y01 = page.cropbox.lower_left[1]
y02 = page.cropbox.upper_left[1]

freshPageCo1 = page.cropbox.lower_left = (x01, y01 + 35)
freshPageCo2 = page.cropbox.upper_right = (x02, y02 - 35)

page = writer.add_page(page)
x1 = page.cropbox.lower_left[0] # 0
x2 = page.cropbox.lower_right[0] #612
y1 = page.cropbox.lower_left[1] #35
y2 = page.cropbox.upper_left[1] #757

width = round((x2 - x1) / 2, 2) # 306
height = round((y2 - y1) / 3, 2) #240

labelID = 1
# print('width', width, 'height', height)
# print('PDF 按标签拆分, Start')
for pages in range(len(reader.pages)):
    for cols in range(2): # 0开始
        for rows in range(3): # 0 - 1 - 2递增
            label_x1 = x1 + cols * width
            label_y1 = y1 + (2 - rows) * height
            label_x2 = label_x1 + width
            label_y2 = label_y1 + height

            page.cropbox.lower_left = (label_x1, label_y1)
            page.cropbox.upper_right = (label_x2, label_y2)

            outFile = os.path.join("outputs\package-FBA1781SY190",
                                   r'{package}_L{label}.pdf'.format(
                                       package='package-FBA1791SY190', label=labelID))
            labelID += 1

            with open(outFile, 'wb') as output_pdf:
                pdf_writer = PdfWriter()
                pdf_writer.add_page(page)
                pdf_writer.write(output_pdf)

print('PDF 按标签拆分, Done')
