import docx

def get_text(filepath):
    doc = docx.Document(filepath)
    text = []
    for para in doc.paragraphs:
        text.append(para.text)
    return '\n'.join(text)
