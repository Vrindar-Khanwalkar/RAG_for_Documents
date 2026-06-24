from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

def generate_embedding(text):
    """
    Generate embedding for a single text.
    """

    embedding = model.encode(text)

    return embedding.tolist()


def embed_chunks(chunks):
    """
    Add embeddings to all chunks.
    """

    embedded_chunks = []
    texts = [ chunk["chunk_text"] for chunk in chunks]
    embeddings = model.encode(texts)

    for chunk, embedding in zip(chunks, embeddings):
        chunk["embedding"] = embedding.tolist()
        embedded_chunks.append(chunk)

    return embedded_chunks