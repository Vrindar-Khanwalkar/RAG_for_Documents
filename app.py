import gradio as gr
import os
MAX_FILE_SIZE_MB = 25
MAX_FILES = 5

def ingest(files):

    if len(files) > MAX_FILES:
        return f"Maximum {MAX_FILES} files allowed"

    if not files:
        return "No files selected"

    # Validate file sizes
    for file in files:

        size_mb = os.path.getsize(file.name) / (1024 * 1024)

        if size_mb > MAX_FILE_SIZE_MB:
            return f"{os.path.basename(file.name)} exceeds {MAX_FILE_SIZE_MB} MB limit"

    # Placeholder for future ingestion logic
    file_names = [
        os.path.basename(file.name)
        for file in files
    ]

    return (
        "Documents ready:\n\n"
        + "\n".join(file_names)
    )


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