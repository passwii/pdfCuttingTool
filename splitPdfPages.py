# 这是多页PDF文件拆解，按照运营需求拆解对应的页码，适用于海外仓挪货等时候
from PyPDF2 import PdfWriter, PdfReader
import os

inDir = r'inputs'
outDir = r'outputs\{packageID}'.format(packageID='package-FBA1781SY190-Pages')

pdfReader = PdfReader(os.path.join(inDir, "tmp.pdf"))
pdf_writer = PdfWriter()

startPage = 3
endPage = 5

for page_no in range(startPage-1, endPage):
    page = pdfReader.pages[page_no]
    pdf_writer.add_page(page)

file = '{packageID}_{startID}-{endID}.pdf'.format(
    packageID='package-FBA1781SY190', startID=startPage, endID=endPage
)

outfile = os.path.join(outDir, file)
with open(outfile, 'wb') as output_pdf:
    pdf_writer.write(output_pdf)

