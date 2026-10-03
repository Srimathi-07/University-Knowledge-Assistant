import pdfplumber

pdf_path = "document/UNIVERSITY _ATTENDANCE_ REGULATIONS.pdf"

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        print(text)