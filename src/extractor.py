import os


def extract_text_from_pdf(file_path):
    """Extract text from a PDF file using pdfplumber."""
    text = ""
    try:
        import pdfplumber
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(f"[WARNING] Could not read PDF {file_path}: {e}")
    return text


def extract_text_from_docx(file_path):
    """Extract text from a DOCX file using python-docx."""
    text = ""
    try:
        from docx import Document
        doc = Document(file_path)
        for para in doc.paragraphs:
            if para.text.strip():
                text += para.text + "\n"
        # Also extract text inside tables
        for table in doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    if cell.text.strip():
                        text += cell.text + " "
                text += "\n"
    except Exception as e:
        print(f"[WARNING] Could not read DOCX {file_path}: {e}")
    return text


def extract_text_from_txt(file_path):
    """Extract text from a plain TXT file."""
    text = ""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()
    except Exception as e:
        print(f"[WARNING] Could not read TXT {file_path}: {e}")
    return text


def extract_resume_text(file_path):
    """Detect file extension and extract text accordingly."""
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.pdf':
        return extract_text_from_pdf(file_path)
    elif ext == '.docx':
        return extract_text_from_docx(file_path)
    elif ext == '.txt':
        return extract_text_from_txt(file_path)
    else:
        print(f"[WARNING] Unsupported file type: {file_path}")
        return ""


def load_all_resumes(resume_folder):
    """Load and extract text from all resumes in a folder.

    Returns a dict: {filename: raw_text}
    """
    resumes = {}
    if not os.path.exists(resume_folder):
        print(f"[ERROR] Resume folder not found: {resume_folder}")
        return resumes

    for filename in os.listdir(resume_folder):
        file_path = os.path.join(resume_folder, filename)
        if os.path.isfile(file_path):
            text = extract_resume_text(file_path)
            if text.strip():
                resumes[filename] = text
            else:
                print(f"[WARNING] No text extracted from {filename}")
    return resumes
