import os
from pypdf import PdfReader


def load_documents(data_folder="data"):
    documents = []

    for filename in os.listdir(data_folder):
        filepath = os.path.join(data_folder, filename)

        # PDF Files
        if filename.endswith(".pdf"):
            try:
                reader = PdfReader(filepath)

                for page_num, page in enumerate(reader.pages):
                    text = page.extract_text()

                    if text:
                        documents.append({
                            "text": text,
                            "source": filename,
                            "page": page_num + 1
                        })

            except Exception as e:
                print(f"Error reading PDF {filename}: {e}")

        # TXT Files
        elif filename.endswith(".txt"):
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    text = f.read()

                    documents.append({
                        "text": text,
                        "source": filename,
                        "page": 1
                    })

            except Exception as e:
                print(f"Error reading TXT {filename}: {e}")

    return documents