import fitz

def parse_pdf(pdf_bytes: bytes) -> str:
    text_parts = []
    with fitz.open(stream=pdf_bytes, filetype="pdf") as doc:
        for page in doc:
            t = page.get_text("text")
            if t:
                text_parts.append(t)
    return "\n".join(text_parts)