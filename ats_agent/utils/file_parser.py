from io import BytesIO
from pypdf import PdfReader
from docx import Document


def extract_text_from_pdf(file_bytes: bytes) -> str:
    pdf_stream = BytesIO(file_bytes)   # ✅ FIX
    reader = PdfReader(pdf_stream)

    text = []
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text.append(page_text)

    return "\n".join(text)


def extract_text_from_docx(file_bytes: bytes) -> str:
    doc_stream = BytesIO(file_bytes)
    doc = Document(doc_stream)
    return "\n".join(p.text for p in doc.paragraphs)


def extract_resume_text(filename: str, file_bytes: bytes) -> str:
    filename = filename.lower()

    if filename.endswith(".pdf"):
        return extract_text_from_pdf(file_bytes)

    elif filename.endswith(".docx"):
        return extract_text_from_docx(file_bytes)

    elif filename.endswith(".txt"):
        return file_bytes.decode("utf-8")

    else:
        raise ValueError(f"Unsupported file format: {filename}")