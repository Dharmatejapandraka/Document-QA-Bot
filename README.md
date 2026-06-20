# AI Document Q&A Bot

A Retrieval-Augmented Generation (RAG) application built using:

- Streamlit
- Groq LLM
- Scikit-Learn TF-IDF Retrieval
- PDF/TXT Document Processing

## Features

- Ask questions from uploaded knowledge documents
- Supports PDF and TXT files
- Source citations
- Fast retrieval
- Railway deployment ready

## Run Locally

```bash
pip install -r requirements.txt
python ingest.py
streamlit run app.py