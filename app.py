from docx import Document

doc = Document("FGB.docx")

for p in doc.paragraphs:
    print(p)
