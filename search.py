import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB
client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_collection(
    name="university_documents"
)

# User question
question = "What is the minimum attendance required?"

# Convert question into embedding
question_embedding = model.encode(question)

# Search ChromaDB
results = collection.query(
    query_embeddings=[question_embedding.tolist()],
    n_results=2
)

# Display results
print("\nRelevant information:")
print(results["documents"])

print("\nMetadata:")
print(results["metadatas"])