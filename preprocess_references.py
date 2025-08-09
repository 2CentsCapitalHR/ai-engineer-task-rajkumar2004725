#testing functionn for extracting text from PDF and DOCX files
#This code is for preprocessing references, extracting text from files, and saving it to a text file.
#It is not part of the main RAG pipeline but is used to prepare data for it
import os
import PyPDF2
import docx2txt

def extract_text(file_path):
    if file_path.endswith('.pdf'):
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = ''.join(page.extract_text() for page in reader.pages if page.extract_text())
    elif file_path.endswith('.docx'):
        text = docx2txt.process(file_path)
    else:
        raise ValueError("Unsupported file type")
    return text

ref_dir = 'refrences/'
texts = {}
for file in os.listdir(ref_dir):
    if file.endswith(('.pdf', '.docx')):
        texts[file] = extract_text(os.path.join(ref_dir, file))

with open('extracted_texts.txt', 'w', encoding='utf-8') as f:
    for file, text in texts.items():
        f.write(f"--- {file} ---\n{text}\n\n")

print("Preprocessing complete! Check extracted_texts.txt for output.")