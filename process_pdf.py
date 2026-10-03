import pdfplumber

pdf_path = "document/UNIVERSITY _ATTENDANCE_ REGULATIONS.pdf"

# Read PDF
with pdfplumber.open(pdf_path) as pdf:
    text = ""

    for page in pdf.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

# Create chunks
words = text.split()

chunk_size = 50

chunks = []

for i in range(0, len(words), chunk_size):
    chunk = " ".join(words[i:i + chunk_size])
    chunks.append(chunk)

# Show chunks
for i, chunk in enumerate(chunks):
    print("CHUNK", i + 1)
    print(chunk)
    print("----------------")