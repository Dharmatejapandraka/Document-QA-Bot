import os
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer

from utils.loader import load_documents
from utils.chunker import chunk_documents

print("Loading documents...")
documents = load_documents()

print("Chunking documents...")
chunks = chunk_documents(documents)

texts = [chunk["text"] for chunk in chunks]

print("Creating TF-IDF vectors...")
vectorizer = TfidfVectorizer(stop_words="english")

vectors = vectorizer.fit_transform(texts)

os.makedirs("db", exist_ok=True)

with open("db/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

with open("db/chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)

with open("db/vectors.pkl", "wb") as f:
    pickle.dump(vectors, f)

print("Indexing complete!")
print(f"Stored {len(chunks)} chunks")