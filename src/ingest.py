from pathlib import Path
from unittest import loader
import uuid, datetime
from pypdf import PdfReader
from gradio_client import file
from docx import Document



def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def load_txt(file_path: str) -> dict:

    print(file_path)
    print(type(file_path))
    content = read_text_file(file_path)
    return {
        "document_id": f"{Path(file_path).stem}_{uuid.uuid4().hex[:8]}",
        "filename": Path(file_path).name,
        "content": content,
        "file_type": Path(file_path).suffix.lower(),
        "character_count": len(content),
        "metadata":{}
    }

def load_pdf_file(file_path):
    reader = PdfReader(file_path)
    page_count = len(reader.pages)
    pages_text = []
    for page in reader.pages:
        text = page.extract_text()
        if text:
            pages_text.append(text)
    content = "\n".join(pages_text)
    return  {
        "document_id": f"{Path(file_path).stem}_{uuid.uuid4().hex[:8]}",
        "filename": Path(file_path).name,
        "content": content,
        "file_type": Path(file_path).suffix.lower(),
        "character_count": len(content),
        "metadata":{
            "pages": page_count
        }
    }

def load_docx_file(file_path):
    doc = Document(file_path)
    paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
    content = "\n".join(paragraphs)
    return  {
        "document_id": f"{Path(file_path).stem}_{uuid.uuid4().hex[:8]}",
        "filename": Path(file_path).name,
        "content": content,
        "file_type": Path(file_path).suffix.lower(),
        "character_count": len(content),
        "metadata":{
            "paragraphs": len(paragraphs),
            "empty": len(content.strip()) == 0
        }
    }

LOADERS = {
    ".txt": load_txt,
    ".pdf": load_pdf_file,
    ".docx": load_docx_file
}
def load_documents(files):

    loaded_documents = []
    failed_documents = []
    
    for file in files:

        extension = Path(file.name).suffix.lower()

        # Unsupported file
        if extension not in LOADERS:

            failed_documents.append({
                "filename": Path(file.name).name,
                "reason": "Unsupported file type"
            })

            continue

        try:

            loader = LOADERS[extension]
            print(extension)
            print(loader)
            document = loader(file.name)
            print(document)
            loaded_documents.append(document)

        except Exception as e:

            failed_documents.append({
                "filename": Path(file.name).name,
                "reason": str(e)
            })

    return {
        "loaded_documents": loaded_documents,
        "failed_documents": failed_documents
    }

