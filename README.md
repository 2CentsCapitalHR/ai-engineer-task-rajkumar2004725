[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/vgbm4cZ0)



ADGM Corporate Agent

The ADGM Corporate Agent is an AI-powered legal assistant designed to assist with reviewing, validating, and preparing documentation for business incorporation and compliance within the Abu Dhabi Global Market (ADGM) jurisdiction. It accepts .docx documents, verifies completeness based on ADGM rules, highlights red flags, inserts contextual comments, and generates reviewed, downloadable files along with a structured report.

Features

Upload and parse .docx documents.
Identify document types (e.g., Articles of Association, Memorandum of Association).
Verify documents against ADGM checklists.
Detect legal red flags (e.g., incorrect jurisdiction, missing signatures).
Insert inline comments with ADGM rule citations.
Generate a downloadable reviewed .docx file and a JSON report summarizing findings.


Installation

Clone the Repository:

    git clone https://github.com/your-username/corporate-agent.git
    cd corporate-agent

Set Up a Virtual Environment:

    python -m venv myenv
    myenv\Scripts\activate  # On Windows
    source myenv/bin/activate  # On macOS/Linux


Install Dependencies:

    pip install -r requirements.txt


Configure API Key:

    Obtain a Groq API key from Groq Console.
    Set the environment variable:setx GROQ_API_KEY "your_api_key_here"  # On Windows (reopen terminal)
    export GROQ_API_KEY="your_api_key_here"  # On macOS/Linux


    Alternatively, add it to a .env file and load with python-dotenv.


Download ADGM References:

Create a references/ folder and manually download ADGM documents (e.g., checklists, templates) from links in Data Sources.pdf. Save them with descriptive names (e.g., adgm-incorporation-checklist.pdf).
Preprocess them by running:python preprocess_references.py




Create Sample Files:

Create a samples/ folder and add a test .docx file (e.g., sample_aoa.docx) with sample content.



Usage

Run the Application:

    streamlit run app.py


Open the displayed URL (e.g., http://localhost:8501) in your browser.


Upload Documents:

Drag and drop .docx files into the Streamlit interface.
The app will:
Identify document types.
Check against the ADGM checklist for missing documents.
Detect red flags and suggest fixes.
Generate a reviewed .docx file with inline comments.
Provide a download link for the reviewed file.




View Results:

Check the UI for missing documents and red flag details.
Download the reviewed file to see comments in Microsoft Word.



Project Structure

    corporate-agent/
    ├── app.py              # Streamlit UI and main logic
    
    ├── rag_pipeline.py     # RAG setup with Groq and FAISS
    
    ├── document_parser.py  # Document parsing and red flag detection
    
    ├── checklists.py       # ADGM checklists
    
    ├── preprocess_references.py  # Text extraction from references
    
    ├── references/         # ADGM reference documents
    
    ├── reviewed_samples/   # Reviewed .docx files
    
    ├── samples/            # Sample .docx files for testing
    
    ├── requirements.txt    # Python dependencies
    
    ├── README.md           # This file
    
    └── myenv/              # Virtual environment (optional)



Video Link

    https://youtu.be/-jDIV7wDqdk
