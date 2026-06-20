import os
import pickle
from dotenv import load_dotenv
from groq import Groq
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def ask_question(question):

    # Load saved files
    with open("db/vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)

    with open("db/chunks.pkl", "rb") as f:
        chunks = pickle.load(f)

    with open("db/vectors.pkl", "rb") as f:
        vectors = pickle.load(f)

    # Convert question to vector
    query_vector = vectorizer.transform([question])

    # Similarity search
    scores = cosine_similarity(query_vector, vectors)[0]

    # Get top 10 chunks
    top_indices = scores.argsort()[-10:][::-1]

    context = ""
    citations = []

    for idx in top_indices:
        chunk = chunks[idx]

        context += chunk["text"] + "\n\n"

        source = f"{chunk['source']} (Page {chunk['page']})"

        if source not in citations:
            citations.append(source)

    # Better prompt
    prompt = f"""
You are an AI Document Question Answering Assistant.

Use the information provided in the context to answer the question.

If the answer is partially available, provide the best possible answer.

Do not simply say that the answer is unavailable.

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        max_tokens=1000
    )

    answer = response.choices[0].message.content

    return answer, citations