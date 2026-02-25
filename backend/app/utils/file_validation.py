# app/utils/file_validation.py
ALLOWED_EXTENSIONS = {"pdf"}
ALLOWED_MIME = {
    "application/pdf",
}

def validate_file(file):
    if not file:
        return False, "No file provided"

    if "." not in file.filename:
        return False, "Invalid filename"

    ext = file.filename.rsplit(".", 1)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        return False, "Invalid extension"

    if file.mimetype not in ALLOWED_MIME:
        return False, "Invalid MIME type"

    return True, None