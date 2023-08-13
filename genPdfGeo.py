from PyPDF2 import PdfWriter, PdfReader

reader = PdfReader("inputs/tmp.pdf")
writer = PdfWriter()

page1 = reader.pages[0]
print(page1.cropbox.lower_left[0])
print(page1.cropbox.lower_right[0])
print(page1.cropbox.lower_left[1])
print(page1.cropbox.upper_right[1])
