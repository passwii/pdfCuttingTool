from PyPDF2 import PdfWriter, PdfReader
import os

inDir = r'inputs'
outDir = r'outputs\{package}'.format(package='package-FBA1781SY190')

# print all file name under inputs folder
for file in os.listdir(inDir):
    print(file)

pdfReader = PdfReader(os.path.join(inDir, "tmp.pdf"))

print(len(pdfReader.pages))

for page_no in range(len(pdfReader.pages)):
    page = pdfReader.pages[page_no]
    pdf_writer = PdfWriter()
    pdf_writer.add_page(page)

    file = '{package} - {page_no}.pdf'.format(package='package-FBA1781SY190', page_no = page_no + 1)
    outfile = os.path.join(outDir, file)

    with open(outfile, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)
print('PDF Split Done')
