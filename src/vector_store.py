
vector_store= []

def add_chunks(chunks):
    vector_store.extend(chunks)

def get_chunks():
    return vector_store


def clear_store():
    vector_store.clear()

def count():
    return len(vector_store)