from checklists import get_missing_documents

process = "Company Incorporation"
uploaded = ["Articles of Association (AoA)", "Memorandum of Association (MoA/MoU)", "UBO Declaration Form"]
missing = get_missing_documents(process, uploaded)
print(f"Missing documents for {process}: {missing}")