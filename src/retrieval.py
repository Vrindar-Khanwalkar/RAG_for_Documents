import math
from operator import itemgetter
from src.embeddings import generate_embedding
from src.vector_store import get_chunks


def generate_query_embedding(query):
    return generate_embedding(query)


def cosine_similarity(vec1, vec2):
    if len(vec1) != len(vec2):
        raise ValueError("Vectors must have the same dimension")
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    magnitude1 = math.sqrt(sum(a * a for a in vec1))
    magnitude2 = math.sqrt(sum(b * b for b in vec2))
    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0
    return dot_product / (magnitude1 * magnitude2)

def search_similar_chunks(query_embedding):
    """
    Compare the query embedding with all stored chunk embeddings
    and return a list of (similarity, chunk) tuples.
    """

    chunks = get_chunks()
    similarities = []

    for chunk in chunks:

        chunk_embedding = chunk.get("embedding")

        if chunk_embedding is None:
            continue

        similarity = cosine_similarity(
            query_embedding,
            chunk_embedding
        )

        similarities.append(
            (similarity, chunk)
        )

    return similarities


def retrieve_top_chunks(query, top_k=3):
    print(f"Query: {query}")
    query_embedding = generate_query_embedding(query)
    similar_chunks = search_similar_chunks(query_embedding)
    print(f"Similarities found: {len(similar_chunks)}")
    sorted_chunks = sorted(
        similar_chunks,
        key=itemgetter(0),
        reverse=True
    )

    return sorted_chunks[:top_k]