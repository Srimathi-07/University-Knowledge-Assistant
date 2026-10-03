import pdfplumber
from sentence_transformers import SentenceTransformer
import chromadb

# 1. PDF path
pdf_path = "document/UNIVERSITY _ATTENDANCE_ REGULATIONS.pdf"

# 2. Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# 3. Read PDF and create chunks
chunks = []
metadatas = []

with pdfplumber.open(pdf_path) as pdf:

    for page_number, page in enumerate(pdf.pages, start=1):

        page_text = page.extract_text()

        if page_text:
            words = page_text.split()

            chunk_size = 50

            for i in range(0, len(words), chunk_size):
                chunk = " ".join(words[i:i + chunk_size])

                chunks.append(chunk)

                metadatas.append({
                    "source": "UNIVERSITY ATTENDANCE REGULATIONS",
                    "page": page_number
                })

print("Number of chunks:", len(chunks))

# 4. Create embeddings
embeddings = model.encode(chunks)

# 5. Connect to ChromaDB
client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="university_documents"
)

# 6. Store chunks + embeddings + metadata
collection.upsert(
    ids=[f"chunk_{i}" for i in range(len(chunks))],
    documents=chunks,
    embeddings=embeddings.tolist(),
    metadatas=metadatas
)

print("Embeddings and metadata stored successfully!")