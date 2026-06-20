# 📚 AI Document Q&A Bot

## Overview

AI Document Q&A Bot is a Retrieval-Augmented Generation (RAG) application that allows users to ask questions from a collection of documents.

The system loads PDF and TXT documents, processes them into chunks, retrieves the most relevant information using TF-IDF similarity search, and generates answers using the Groq LLM.

---

## Features

- PDF document support
- TXT document support
- Automatic document loading
- Document chunking
- TF-IDF based retrieval
- AI-powered answer generation
- Source citations
- Streamlit web interface
- Railway deployment ready

---

## Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### Retrieval
- Scikit-Learn TF-IDF Vectorizer
- Cosine Similarity

### LLM
- Groq API
- Llama 3.3 70B Versatile

### Document Processing
- PyPDF
- Python File Handling

---

## Project Structure

```text
Document-QA-Bot/
│
├── data/
│   ├── ai.txt
│   ├── cloud_computing.txt
│   ├── cybersecurity.txt
│   ├── data_science.txt
│   └── Machine learning.pdf
│
├── db/
│   ├── chunks.pkl
│   ├── vectorizer.pkl
│   └── vectors.pkl
│
├── utils/
│   ├── loader.py
│   ├── chunker.py
│   └── rag.py
│
├── app.py
├── ingest.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── .gitignore
└── README.md
```

---

## System Workflow

### Step 1: Document Loading

The system loads all PDF and TXT documents from the data folder.

### Step 2: Chunking

Documents are split into smaller chunks for efficient retrieval.

### Step 3: Vectorization

TF-IDF converts document chunks into numerical vectors.

### Step 4: Retrieval

The system compares the user query against stored vectors using cosine similarity.

### Step 5: Answer Generation

Relevant chunks are sent to Groq Llama 3.3 70B for answer generation.

### Step 6: Source Citation

The bot displays the document sources used to generate the answer.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Document-QA-Bot.git
cd Document-QA-Bot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## Build Knowledge Base

Run:

```bash
python ingest.py
```

Expected Output:

```text
Loading documents...
Chunking documents...
Creating TF-IDF vectors...
Indexing complete!
Stored 555 chunks
```

---

## Run Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## Sample Questions

### Artificial Intelligence

- What is Artificial Intelligence?
- Explain AI applications.
- What are the advantages of AI?

### Cloud Computing

- What is Cloud Computing?
- Explain cloud service models.
- What are the benefits of cloud computing?

### Cybersecurity

- What is Cybersecurity?
- Explain cybersecurity threats.
- What are the advantages of cybersecurity?

### Data Science

- What is Data Science?
- Explain Data Science lifecycle.
- What are the applications of Data Science?

### Machine Learning

- What is Machine Learning?
- Explain supervised learning.
- What are machine learning algorithms?

---

## Deployment

### Railway

1. Push code to GitHub
2. Create Railway project
3. Connect GitHub repository
4. Add environment variable:

```env
GROQ_API_KEY=your_groq_api_key
```

5. Deploy application

---

## Limitations

- Answers depend on document quality.
- Uses TF-IDF retrieval instead of embedding models.
- Cannot answer questions outside the provided documents.
- Large document collections may require more advanced vector databases.

---

## Future Improvements

- PDF upload directly from the Streamlit UI
- Multiple PDF and document support
- Chat history and conversation memory
- Embedding-based retrieval for better semantic search
- ChromaDB or FAISS vector database integration
- Gemini API integration for answer generation
- OpenAI GPT integration
- Multi-LLM support (Groq, Gemini, OpenAI)
- Better user interface and dark mode
- User authentication and role-based access
- Answer confidence score
- Voice-based question answering
- Document summarization feature
- Support for DOCX, PPTX, and Excel files
- Advanced RAG pipeline with hybrid search

---

## Author

Dharmateja Pandraka

Final Year B.Tech (Information Technology)

AI Internship Assignment Project