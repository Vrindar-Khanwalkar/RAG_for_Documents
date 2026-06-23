# 📚 Document RAG Assistant

A Retrieval-Augmented Generation (RAG) application that ingests documents, performs token-based chunking, generates embeddings, and enables semantic retrieval over uploaded content.

## Features

### Document Ingestion

* TXT document support
* PDF document support
* DOCX document support
* File validation and size checks
* Unified document schema

### Intelligent Chunking

* Token-based chunking using Hugging Face tokenizers
* Configurable chunk size and overlap
* Metadata tracking for each chunk
* Multi-document processing

### User Interface

* Built with Gradio
* Multi-file upload support
* Document ingestion dashboard
* Future conversational chat interface

---

## Project Structure

```text
RAG_Document/
│
├── app.py
├── requirements.txt
├── README.md
│
├── src/
│   ├── ingest.py
│   ├── chunking.py
│   └── embeddings.py
│
└── data/
```

---

## Document Schema

```python
{
    "document_id": "...",
    "filename": "...",
    "content": "...",
    "file_type": "...",
    "character_count": 0,
    "metadata": {}
}
```

---

## Chunk Schema

```python
{
    "chunk_id": "...",
    "document_id": "...",
    "filename": "...",
    "chunk_index": 0,
    "chunk_text": "...",
    "metadata": {
        "source_type": ".pdf",
        "chunk_size": 1000,
        "chunk_overlap": 200,
        "token_count": 1000
    }
}
```

---

## Chunking Strategy

Current configuration:

```python
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
```

Sliding window approach:

```text
Chunk 1: 0-1000
Chunk 2: 800-1800
Chunk 3: 1600-2600
...
```

This preserves contextual continuity across chunk boundaries while maintaining retrieval quality.

---

## Technology Stack

* Python
* Gradio
* Hugging Face Transformers
* PyPDF
* python-docx
* Sentence Transformers

---

## Current Progress

### Completed

* [x] Gradio Interface
* [x] Multi-file Upload
* [x] TXT Loader
* [x] PDF Loader
* [x] DOCX Loader
* [x] Document Metadata Extraction
* [x] Token Counting
* [x] Token-Based Chunking
* [x] Overlapping Chunks
* [x] Chunk Metadata Generation
* [x] Multi-Document Chunk Processing
* [x] Embedding Model Initialization

### In Progress

* [ ] Embedding Generation
* [ ] Vector Database Integration
* [ ] Semantic Retrieval
* [ ] Retrieval Ranking
* [ ] Answer Generation
* [ ] Conversational Memory
* [ ] Evaluation Pipeline

---

## Installation

```bash
git clone <repository-url>

cd RAG_Document

python -m venv .venv

source .venv/bin/activate
# Windows:
# .venv\Scripts\activate

pip install -r requirements.txt
```

---

## Run Application

```bash
python app.py
```

The application launches locally using Gradio.

---

## Future Roadmap

1. Generate embeddings for document chunks
2. Store vectors in a vector database
3. Implement semantic similarity search
4. Build retrieval pipeline
5. Integrate LLM response generation
6. Add evaluation and monitoring metrics

---

## Author

Built as a hands-on implementation of Retrieval-Augmented Generation (RAG) systems to explore document ingestion, chunking strategies, semantic search, and LLM-powered question answering.
