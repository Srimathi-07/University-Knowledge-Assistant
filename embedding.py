from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

text = "Students must maintain 75% attendance."

embedding = model.encode(text)

print(embedding)