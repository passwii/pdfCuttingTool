from PyPDF2 import PdfWriter, PdfReader
import os

# set directions
indir = r"inputs"
outdir = r"outputs"

# print(indir)
# print("Success Sourced")

# set inputfile path
infile = os.path.join(indir, "tmp.pdf")

pdfReader = PdfReader(infile)
title = pdfReader.getDocumentInfo().title

for page_no in range(pdfReader.numPages):
    page = pdfReader.getPage(page_no)
    pdf_writer = PdfWriter()
    pdf_writer.addPage(page)

    file = '{0}.pdf'.format(page_no + 1)
    outfile = os.path.join(outdir, file)

    with open(outfile, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

print('PDF Split Done')
