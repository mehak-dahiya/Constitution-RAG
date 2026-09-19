from langchain_community.document_loaders import PyPDFLoader

# Load the Constitution PDF
loader = PyPDFLoader("Data/Data.pdf")

# Read all pages
documents = loader.load()

# Print total pages
print(f"Total Pages: {len(documents)}")

# Print first 1000 characters of the first page
print("\nFirst Page Preview:\n")
print(documents[0].page_content[:1000])
