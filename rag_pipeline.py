import os
from langchain_community.embeddings import HuggingFaceEmbeddings  
from langchain_community.vectorstores import FAISS


from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
import PyPDF2
import docx2txt
from dotenv import load_dotenv

load_dotenv()
groq_key = os.getenv("GROQ_API_KEY")
# Suppress Pydantic warning (optional)
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="pydantic._internal._fields")

# From preprocess_references.py 
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

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def build_vector_store(ref_dir='refrences/'):
    docs = []
    for file in os.listdir(ref_dir):
        if file.endswith(('.pdf', '.docx')):
            text = extract_text(os.path.join(ref_dir, file))
            splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=100)
            chunks = splitter.split_text(text)
            docs.extend([Document(page_content=chunk, metadata={"source": file}) for chunk in chunks])
    
    vector_store = FAISS.from_documents(docs, embeddings)
    vector_store.save_local("faiss_index")
    print("Vector store built and saved!")
    return vector_store

# Build if not exists
if not os.path.exists("faiss_index"):
    build_vector_store()

# Load LLM and RAG chain
llm = ChatGroq(model="llama-3.1-8b-instant",
               temperature=0.0  # Lower temperature for factual responses,
               ,api_key=groq_key)

vector_store = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
retriever = vector_store.as_retriever(search_kwargs={"k": 5})
rag_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

# Test query
query = "What are the required documents for ADGM company incorporation?"
result = rag_chain.invoke({"query": query})
print(f"Query: {query}\nResponse: {result['result']}")