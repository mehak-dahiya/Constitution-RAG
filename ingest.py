from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

print("Loading Constitution PDF...")

# Load the PDF
loader = PyPDFLoader("Data/Data.pdf")
documents = loader.load()

print(f"Loaded {len(documents)} pages.")

# Split into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(documents)

print(f"Created {len(chunks)} chunks.")

# Load embedding model
print("Loading embedding model...")

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5",
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": True}
)

# Create FAISS index
print("Creating FAISS vector database...")

vectorstore = FAISS.from_documents(chunks, embeddings)

# Save the database
vectorstore.save_local("vector_db")

print("\n✅ Vector database created successfully!")