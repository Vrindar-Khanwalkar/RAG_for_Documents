from src.retrieval import retrieve_top_chunks
from ollama import chat


def build_prompt(chunks, question):
    """
    Build a prompt for the LLM using the retrieved chunks and the user's question.
    """
    context = "\n\n".join([chunk["chunk_text"] for chunk in chunks])
    prompt = f"""
    You are answering questions about uploaded documents.

Rules:
- Use ONLY the context below.
- If the answer is not explicitly contained in the context, reply:
"I don't know based on the provided documents."
- Keep the answer under 3 sentences.
- Do not use outside knowledge.

======================
CONTEXT
======================
{context}

======================
QUESTION
======================
{question}

======================
ANSWER
======================
    """
    print(context)
    return prompt


def ask_llm(prompt):
    """
    Send the prompt to the LLM and return the response.
    """
    # Placeholder for LLM interaction
    # In a real implementation, this would call the LLM API
    response = chat(model="phi3", messages=[{"role": "system", "content": "You are a helpful AI assistant."}, {"role": "user", "content": prompt}],  options={"temperature": 0,"num_predict": 128,})
    return response["message"]["content"]

def generate_answer(question):
    """
    Generate an answer to the user's question by retrieving relevant chunks
    and querying the LLM.
    """
    top_chunks = retrieve_top_chunks(question)
    if not top_chunks:
        return "No relevant information found in the uploaded documents."

    prompt = build_prompt(top_chunks, question)
    answer = ask_llm(prompt)
    return answer