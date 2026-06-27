# 📚 Document RAG Assistant

An end-to-end Retrieval-Augmented Generation (RAG) application built from scratch using Python. This project allows users to upload documents, automatically generate embeddings, retrieve the most relevant context using semantic search, and answer questions locally using an LLM running on Ollama.

Unlike many RAG tutorials that rely heavily on high-level frameworks, this project implements the core pipeline manually to better understand how modern RAG systems work internally.

---

## Features

* Upload PDF, DOCX and TXT documents
* Automatic document ingestion and validation
* Token-based document chunking
* Embedding generation using Sentence Transformers (MiniLM)
* Custom in-memory vector store
* Cosine similarity search
* Top-K semantic retrieval
* Prompt engineering for grounded responses
* Local LLM inference using Ollama (Phi-3)
* Interactive Gradio interface

---

## Architecture

```
                User Uploads Documents
                         │
                         ▼
               Document Ingestion
                         │
                         ▼
                 Document Chunking
                         │
                         ▼
              Embedding Generation
                         │
                         ▼
                 Custom Vector Store
                         │
                         ▼
                   User Question
                         │
                         ▼
              Query Embedding Generation
                         │
                         ▼
             Cosine Similarity Retrieval
                         │
                         ▼
                Top-K Relevant Chunks
                         │
                         ▼
                  Prompt Construction
                         │
                         ▼
                 Ollama (Phi-3 LLM)
                         │
                         ▼
                     Final Answer
```

---

## Tech Stack

| Component         | Technology                             |
| ----------------- | -------------------------------------- |
| Language          | Python                                 |
| UI                | Gradio                                 |
| Embeddings        | sentence-transformers/all-MiniLM-L6-v2 |
| Vector Store      | Custom Python Implementation           |
| Similarity Search | Cosine Similarity                      |
| Local LLM         | Ollama (Phi-3)                         |
| PDF Parsing       | PyPDF                                  |
| DOCX Parsing      | python-docx                            |
| Tokenization      | HuggingFace Transformers               |

---
## Installation & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/RAG_Document.git
cd RAG_Document
```

---

### 2. Create a Virtual Environment

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Install Ollama

Download and install Ollama from:

https://ollama.com/download

---

### 5. Download the Phi-3 Model

```bash
ollama pull phi3
```

Verify the installation:

```bash
ollama list
```

Expected output:

```text
NAME
phi3:latest
```

---

### 6. Start the Ollama Server

Normally, Ollama starts automatically after installation.

If needed, start it manually:

```bash
ollama serve
```

---

### 7. Run the Application

```bash
python app.py
```

Gradio will launch and display a local URL similar to:

```text
Running on local URL: http://127.0.0.1:7860
```

Open the URL in your browser.

---

## Using the Application

1. Open the **Upload Documents** tab.
2. Upload one or more PDF, DOCX, or TXT files.
3. Click **Ingest Documents**.
4. Wait for embeddings to be generated.
5. Switch to the **Chat** tab.
6. Ask questions about the uploaded documents.
7. The application retrieves the most relevant chunks and generates an answer using the local Phi-3 model.

---

## Requirements

* Python 3.10+
* Ollama
* Phi-3 Model
* Internet connection (only required for the initial model download)

## Project Structure

```
.
├── app.py
├── requirements.txt
├── README.md
├── PROJECT_CONTEXT.md
│
└── src
    ├── ingest.py
    ├── chunking.py
    ├── embeddings.py
    ├── vector_store.py
    ├── retrieval.py
    └── llm.py
```

---

## How It Works

### 1. Document Ingestion

Documents are validated, parsed and converted into a standardized internal format.

Supported file types:

* PDF
* DOCX
* TXT

---

### 2. Chunking

Large documents are split into overlapping token-based chunks to improve semantic retrieval.

Current configuration:

* Chunk Size: 1000 tokens
* Chunk Overlap: 200 tokens

---

### 3. Embeddings

Each chunk is converted into a 384-dimensional embedding using the Sentence Transformers MiniLM model.

---

### 4. Vector Search

Embeddings are stored in a custom in-memory vector store.

For every user query:

* Generate query embedding
* Compute cosine similarity against all stored vectors
* Retrieve the Top-K most relevant chunks

---

### 5. Answer Generation

The retrieved chunks are combined into a prompt and passed to a locally running Phi-3 model via Ollama.

The model is instructed to answer only using the retrieved context.

---

## Example Workflow

```
Upload Documents
        │
        ▼
Generate Chunks
        │
        ▼
Generate Embeddings
        │
        ▼
Store Vectors
        │
        ▼
Ask Question
        │
        ▼
Retrieve Relevant Chunks
        │
        ▼
Generate Answer
```

---

## Current Limitations

* Uses an in-memory vector store (data is not persisted)
* Retrieval quality depends on chunk size and Top-K configuration
* No reranking of retrieved chunks
* No conversation memory
* Optimized for learning rather than production deployment

---

## Known Issues

* Retrieval quality depends on chunk size and Top-K configuration.
* Large Ollama context sizes may require significant RAM and can cause out-of-memory errors.
* The vector store is currently in-memory and is cleared whenever new documents are ingested.
* This project is intended as a learning implementation of RAG rather than a production deployment.


## Future Improvements

* FAISS integration
* ChromaDB support
* Hybrid Search (BM25 + Vector Search)
* Cross-Encoder Reranking
* Persistent Vector Storage
* Streaming Responses
* Source Citations
* Conversation Memory
* Retrieval Evaluation Metrics

---

## Key Learnings

This project was built to understand the internal mechanics of Retrieval-Augmented Generation rather than relying on abstraction libraries.

Core concepts explored include:

* Tokenization
* Document Chunking
* Embeddings
* Vector Databases
* Cosine Similarity
* Semantic Search
* Prompt Engineering
* Local LLM Deployment
* Retrieval-Augmented Generation (RAG)

---

## Author

Built by Vrindar as part of a hands-on AI Engineering learning journey focused on understanding and implementing modern LLM applications from first principles.
