from PyPDF2 import PdfWriter, PdfReader

reader = PdfReader("example.pdf")
writer = PdfWriter()

# add page 3 from reader, but crop it to half size:
page3 = reader.pages[2]
page3.mediabox.upper_right = (
    page3.mediabox.right / 2,
    page3.mediabox.top / 2,
)
writer.add_page(page3)

# add some Javascript to launch the print window on opening this PDF.

writer.add_js("this.print({bUI:true,bSilent:false,bShrinkToFit:true});")

# write to document-box_1.pdf
with open("PyPDF2-box_1.pdf", "wb") as fp:
    writer.write(fp)
