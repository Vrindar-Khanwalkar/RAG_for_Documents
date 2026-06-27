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
