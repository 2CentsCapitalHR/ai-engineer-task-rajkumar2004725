# checklists.py
# Based on ADGM checklists (e.g., branch-non-financial-services-checklist.pdf, private-company-limited-checklist.pdf)

checklists = {
    "Company Incorporation": [
        "Articles of Association (AoA)",
        "Memorandum of Association (MoA/MoU)",
        "Board Resolution Templates",
        "Shareholder Resolution Templates",
        "Incorporation Application Form",
        "UBO Declaration Form",
        "Register of Members and Directors",
        "Certificate of Incorporation or Registration",
        "Certificate of Good Standing",
        "Evidence of Authorization (e.g., Legal Opinion)"
    ],
    "Employment HR Contracts": [
        "Standard Employment Contract",
        "Appropriate Policy Document (Data Protection)"
    ],
    # Add more processes (e.g., Licensing, Compliance) as needed
}

def get_missing_documents(process, uploaded_docs):
    """Check for missing documents in the checklist for a given process."""
    required = checklists.get(process, [])
    missing = [doc for doc in required if doc not in uploaded_docs]
    return missing