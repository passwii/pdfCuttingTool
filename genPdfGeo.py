from PyPDF2 import PdfWriter, PdfReader
import os

reader = PdfReader("inputs/tmp.pdf")
writer = PdfWriter()
page = reader.pages[0]

print(page.cropbox.lower_left)
print(page.cropbox.upper_right)
