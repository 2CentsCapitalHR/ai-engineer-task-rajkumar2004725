import streamlit as st
from document_parser import parse_docx, identify_document_type, detect_red_flags, add_inline_comments
from checklists import get_missing_documents
from rag_pipeline import rag_chain
import os

st.title("ADGM Corporate Agent")

uploaded_files = st.file_uploader("Upload .docx documents", type="docx", accept_multiple_files=True)

if uploaded_files:
    doc_types = []
    all_red_flags = []
    reviewed_files = []

    for uploaded_file in uploaded_files:
        with open(f"samples/{uploaded_file.name}", "wb") as f:
            f.write(uploaded_file.getbuffer())
        parsed = parse_docx(f"samples/{uploaded_file.name}")
        if parsed:
            doc_type = identify_document_type(parsed, rag_chain)
            doc_types.append(doc_type)
            red_flags = detect_red_flags(parsed, rag_chain)
            all_red_flags.append({"file": uploaded_file.name, "flags": red_flags})
            if red_flags:
                reviewed_file = add_inline_comments(f"samples/{uploaded_file.name}", red_flags)
                reviewed_files.append(reviewed_file)

    # Checklist verification
    process = "Company Incorporation"
    missing = get_missing_documents(process, doc_types)
    if missing:
        st.warning(f"Missing documents for {process}: {', '.join(missing)}")
    else:
        st.success("All required documents uploaded!")

    # Display red flags
    for item in all_red_flags:
        if item["flags"]:
            st.subheader(f"Red Flags in {item['file']}")
            for flag in item["flags"]:
                st.write(f"- **Issue**: {flag['issue']}")
                st.write(f"  - **Section**: {flag['section']}")
                st.write(f"  - **Severity**: {flag['severity']}")
                st.write(f"  - **Suggestion**: {flag['suggestion']}")
                st.write("---")

    # Download reviewed files
    for reviewed_file in reviewed_files:
        with open(reviewed_file, "rb") as f:
            st.download_button(
                label=f"Download Reviewed {reviewed_file}",
                data=f,
                file_name=reviewed_file,
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )