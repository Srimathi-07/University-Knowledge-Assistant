import os
import chromadb
from sentence_transformers import SentenceTransformer
from google import genai
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

# Gemini
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# ChromaDB
db = chromadb.PersistentClient(path="chroma_db")
collection = db.get_collection(name="university_documents")

# User question
question = input("Ask your question: ")

# Convert question to embedding
question_embedding = model.encode(question)

# Search relevant information
results = collection.query(
    query_embeddings=[question_embedding.tolist()],
    n_results=2
)

# Get retrieved documents
documents = results["documents"][0]

# Get metadata
metadatas = results["metadatas"][0]

# Combine retrieved information
context = "\n".join(documents)

# Ask Gemini using retrieved information
prompt = f"""
Answer the question using ONLY the information provided below.

Information:
{context}

Question:
{question}

Give a simple and clear answer.
Do not add information that is not present in the provided information.
"""

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=prompt
)

# Display answer
print("\nAnswer:")
print(response.text)

# Display source
print("\nSource:")
for metadata in metadatas:
    print(f"- {metadata['source']} | Page {metadata['page']}")