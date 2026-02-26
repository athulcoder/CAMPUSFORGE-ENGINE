import fitz


def extract_text_from_pdf(path: str) -> str:
    """
    Extracts clean text from a PDF using PyMuPDF.
    """
    text_parts = []

    with fitz.open(path) as doc:
        for page in doc:
            text = page.get_text("text")
            if text:
                text_parts.append(text)

    return "\n".join(text_parts).strip()