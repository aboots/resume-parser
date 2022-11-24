from PyPDF2 import PdfReader


def run(address, use_pos=True, output_file='output.txt'):
    final_text = ''
    reader = PdfReader(address)
    for page in reader.pages:
        text = page.extract_text()
        final_text += text
    print(final_text)
