from PyPDF2 import PdfWriter, PdfReader
import os

inDir = r'inputs\{packageID}'.format(packageID='package-FBA1781SY190')
outDir = r'outputs\{packageID}'.format(packageID='package-FBA1781SY190')

# pdf_reader = PdfReader(os.path.join(inDir, r'{}.pdf'.format('package-FBA1781SY190')))

# pdf_reader = PdfReader(os.path.join(inDir, 'package-FBA1791SY190.pdf'))
infile = os.path.join(inDir, r'{packageID}.pdf'.format(packageID='package-FBA1781SY190'))
outfile = os.path.join(outDir, r'{packageID}.pdf'.format(packageID='package-FBA1781SY190'))

pdf_reader = PdfReader(infile)
# with open(outfile, 'wb') as output_pdf:
#     pdfWriter = PdfWriter()
#     pdfWriter.add_page(pdf_reader.pages[0])
#     pdfWriter.write(output_pdf)
#
