# 📚 Document RAG Assistant

A Retrieval-Augmented Generation (RAG) application built completely from scratch in Python.

The purpose of this project is to understand every stage of a RAG pipeline before using higher-level frameworks such as LangChain, LlamaIndex or vector databases.

---

## Current Features

### ✅ Document Ingestion
- Upload multiple PDF/TXT documents
- File validation
- Size limits
- Error handling

### ✅ Chunking
- Token-based chunking
- Configurable chunk size
- Configurable overlap
- Metadata generation
- Document tracking

### ✅ Embeddings
- SentenceTransformers
- all-MiniLM-L6-v2
- Batch embedding generation
- 384-dimensional vectors

### ✅ Vector Store
- In-memory vector storage
- Add vectors
- Retrieve vectors
- Clear vector store
- Count stored vectors

### ✅ Semantic Retrieval
- Query embedding generation
- Cosine similarity (implemented from scratch)
- Search across all stored vectors
- Rank by similarity
- Return Top-K most relevant chunks

---

## Tech Stack

- Python
- Gradio
- SentenceTransformers
- HuggingFace
- PyPDF
- NumPy (indirectly through SentenceTransformers)

---

## Current Pipeline

Upload Documents
↓
Load Documents
↓
Chunk Documents
↓
Generate Embeddings
↓
Store in Vector Store
↓
User Question
↓
Generate Query Embedding
↓
Cosine Similarity Search
↓
Sort by Similarity
↓
Return Top-K Chunks

---

## Project Structure

```
project/
│
├── app.py
│
└── src/
    ├── ingest.py
    ├── chunking.py
    ├── embeddings.py
    ├── retrieval.py
    └── vector_store.py
```

---

## Current Status

✅ Document Loading

✅ Chunking

✅ Embeddings

✅ In-memory Vector Store

✅ Semantic Retrieval

⬜ LLM Generation

⬜ Prompt Engineering

⬜ Conversation Memory

⬜ Persistent Vector Database (ChromaDB / FAISS)

---

## Next Steps

- Connect an LLM
- Build prompt template
- Generate answers using retrieved context
- Add citations
- Replace in-memory vector store with ChromaDB