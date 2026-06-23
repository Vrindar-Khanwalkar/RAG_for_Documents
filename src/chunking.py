from transformers import AutoTokenizer


CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
tokenizer = AutoTokenizer.from_pretrained(
    "sentence-transformers/all-MiniLM-L6-v2")
def count_tokens(text):
    
    tokens = tokenizer.encode(
        text,
        add_special_tokens=False
    )

    return len(tokens)


def chunk_document(document):

    content = document["content"]
    document_id = document["document_id"]
    filename = document["filename"]

    chunks = []

    tokens = tokenizer.encode(
        content,
        add_special_tokens=False
    )

    # Small document
    if len(tokens) <= CHUNK_SIZE:

        chunk = {
            "chunk_id": f"{document_id}_0",
            "document_id": document_id,
            "filename": filename,
            "chunk_index": 0,
            "chunk_text": content,
            "metadata":{"source_type": document["file_type"],
                            "chunk_size": CHUNK_SIZE,
                            "chunk_overlap": CHUNK_OVERLAP,
                            "token_count": len(tokens)}
            }

        chunks.append(chunk)

        return chunks

    # Large document
    start = 0
    chunk_index = 0

    while start < len(tokens):

        end = start + CHUNK_SIZE

        chunk_tokens = tokens[start:end]

        if chunk_tokens:

            chunk_text = tokenizer.decode(
                chunk_tokens,
                skip_special_tokens=True
            )

            chunk = {
                "chunk_id": f"{document_id}_{chunk_index}",
                "document_id": document_id,
                "filename": filename,
                "chunk_index": chunk_index,
                "chunk_text": chunk_text,
                "metadata":{"source_type": document["file_type"],
                            "chunk_size": CHUNK_SIZE,
                            "chunk_overlap": CHUNK_OVERLAP,
                            "token_count": len(tokens)}
            }

            chunks.append(chunk)

        start += CHUNK_SIZE - CHUNK_OVERLAP
        chunk_index += 1

    return chunks



def chunk_documents(documents):
    all_chunks = []
    for document in documents:
        chunks = chunk_document(document)
        all_chunks.extend(chunks)
    return all_chunks