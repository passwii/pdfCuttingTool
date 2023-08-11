from PyPDF2 import PdfWriter, PdfReader

reader = PdfReader("package.pdf")
writer = PdfWriter()

page1 = reader.pages[0]
page1.mediabox.upper_right = (page1.mediabox.right / 2,
                              page1.mediabox.top / 2.5)

writer.add_page(page1)
with open("page1-1.pdf", "wb") as fp:
    writer.write(fp)
