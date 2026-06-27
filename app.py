import gradio as gr
import os

from src.ingest import load_documents
from src.chunking import chunk_documents
from src.embeddings import embed_chunks
from src.vector_store import add_chunks, count
from src.vector_store import clear_store
from src.llm import generate_answer

MAX_FILE_SIZE_MB = 25
MAX_FILES = 5


def ingest(files):

    if not files:
        return "No files selected"

    if len(files) > MAX_FILES:
        return f"Maximum {MAX_FILES} files allowed"

    for file in files:

        size_mb = os.path.getsize(file.name) / (1024 * 1024)

        if size_mb > MAX_FILE_SIZE_MB:
            return (
                f"{os.path.basename(file.name)} "
                f"exceeds {MAX_FILE_SIZE_MB} MB limit"
            )

    result = load_documents(files)

    loaded_documents = result["loaded_documents"]
    failed_documents = result["failed_documents"]

    if not loaded_documents:
        return "No valid documents loaded"

    all_chunks = chunk_documents(loaded_documents)
    if not all_chunks:
        return "Chunking failed"
    
    embedded_chunks = embed_chunks(all_chunks)
    if not embedded_chunks:
        return "Embedding generation failed"
    clear_store()
    add_chunks(embedded_chunks)

    if len(embedded_chunks[0]["embedding"]) != 384:
        return (
            "Embedding dimension mismatch. "
            f"Expected 384, got "
            f"{len(embedded_chunks[0]['embedding'])}"
        )

    # Count chunks per document
    chunk_counts = {}

    for chunk in all_chunks:

        doc_id = chunk["document_id"]

        chunk_counts[doc_id] = (
            chunk_counts.get(doc_id, 0) + 1
        )

    response = []

    response.append(
        f"Documents Loaded: {len(loaded_documents)}"
    )

    response.append(
        f"Chunks Created: {len(all_chunks)}"
    )

    response.append(f"Embeddings Generated: {len(embedded_chunks)}")
    response.append(f"Vectors Stored: {count()}")

    response.append(
        f"Embedding Dimensions: "
        f"{len(embedded_chunks[0]['embedding'])}"
    )

    response.append("\nLoaded Documents:\n")

    for doc in loaded_documents:

        doc_chunks = chunk_counts.get(
            doc["document_id"],
            0
        )

        response.append(
            f"✓ {doc['filename']} "
            f"({doc['character_count']} chars, "
            f"{doc_chunks} chunks)"
        )

    response.append("\nFailed Documents:\n")

    for doc in failed_documents:

        response.append(
            f"✗ {doc['filename']} - {doc['reason']}"
        )

    return "\n".join(response)


def ask_question(question):

    if not question.strip():
        return "Please enter a question."

    answer = generate_answer(question)

    return answer

with gr.Blocks(title="Document RAG Assistant") as demo:

    gr.Markdown("# 📚 Document RAG Assistant")

    with gr.Tab("Upload Documents"):

        files = gr.File(
            file_count="multiple",
            label="Upload Documents"
        )

        ingest_btn = gr.Button(
            "Ingest Documents"
        )

        status = gr.Textbox(
            label="Status",
            lines=10
        )

        ingest_btn.click(
            ingest,
            inputs=files,
            outputs=status
        )

    with gr.Tab("Chat"):

        question = gr.Textbox(
            label="Ask a Question"
        )

        ask_btn = gr.Button("Ask")

        answer = gr.Textbox(
            label="Answer",
            lines=8
        )

        ask_btn.click(
            ask_question,
            inputs=question,
            outputs=answer
        )

demo.launch(debug=True)