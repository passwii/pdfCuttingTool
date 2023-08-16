from PyPDF2 import PdfWriter, PdfReader
import os

reader = PdfReader("inputs/box_1.pdf")
writer = PdfWriter()
page = reader.pages[0]

print(page.cropbox.lower_left)
print(page.cropbox.upper_right)

print(page.extract_text())
