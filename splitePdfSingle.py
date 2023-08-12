# 这是单个PDF文件拆解，拆解成单页PDF
from PyPDF2 import PdfWriter, PdfReader
import os

inDir = r'inputs'
outDir = r'outputs\{packageID}'.format(packageID='package-FBA1781SY190')

# print all file name under inputs folder
for file in os.listdir(inDir):
    print(file)

pdfReader = PdfReader(os.path.join(inDir, "tmp.pdf"))

print(len(pdfReader.pages))

for page_no in range(len(pdfReader.pages)):
    page = pdfReader.pages[page_no]
    pdf_writer = PdfWriter()
    pdf_writer.add_page(page)

    file = '{packageID}_{pageID}.pdf'.format(packageID='package-FBA1781SY190', pageID=page_no + 1)
    outfile = os.path.join(outDir, file)

    with open(outfile, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)
print('PDF Split Done')
