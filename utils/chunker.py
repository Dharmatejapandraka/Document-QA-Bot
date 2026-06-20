def chunk_documents(documents, chunk_size=500, overlap=100):
    chunks = []

    for doc in documents:
        text = doc["text"]

        start = 0

        while start < len(text):
            end = start + chunk_size

            chunk_text = text[start:end]

            chunks.append({
                "text": chunk_text,
                "source": doc["source"],
                "page": doc["page"]
            })

            start += (chunk_size - overlap)

    return chunks