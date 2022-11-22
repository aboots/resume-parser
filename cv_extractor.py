from PyPDF2 import PdfReader

reader = PdfReader("cv_test.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
print(text)