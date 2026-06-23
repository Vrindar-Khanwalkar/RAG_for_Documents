import gradio as gr
import os
from src.ingest import load_documents
from src.chunking import chunk_documents
MAX_FILE_SIZE_MB = 25
MAX_FILES = 5

def ingest(files):

    if len(files) > MAX_FILES:
        return f"Maximum {MAX_FILES} files allowed"

    if not files:
        return "No files selected"

    for file in files:

        size_mb = os.path.getsize(file.name) / (1024 * 1024)

        if size_mb > MAX_FILE_SIZE_MB:
            return f"{os.path.basename(file.name)} exceeds {MAX_FILE_SIZE_MB} MB limit"

    result = load_documents(files)
    loaded_documents = result["loaded_documents"]
    failed_documents = result["failed_documents"]

    all_chunks = chunk_documents(loaded_documents)
    response = []

    response.append(
    f"Documents Loaded: {len(loaded_documents)}")

    response.append(
    f"Chunks Created: {len(all_chunks)}")
    response.append("\nLoaded Documents:\n")
    response.append("")
    for doc in loaded_documents:
        doc_chunks = len(
        chunk_documents([doc]))

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
    return f"Placeholder answer for: {question}"


with gr.Blocks(title="Document RAG Assistant") as demo:

    gr.Markdown("# 📚 Document RAG Assistant")

    with gr.Tab("Upload Documents"):

        files = gr.File(
            file_count="multiple",
            label="Upload Documents"
        )

        ingest_btn = gr.Button("Ingest Documents")

        status = gr.Textbox(
            label="Status",
            lines=5
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

demo.launch()