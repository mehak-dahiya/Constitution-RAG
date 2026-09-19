from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama import ChatOllama

print("Loading embedding model...")

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5",
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": True}
)

print("Loading FAISS database...")

db = FAISS.load_local(
    "vector_db",
    embeddings,
    allow_dangerous_deserialization=True
)

print("Loading Llama 3.2...")

llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0
)

print("\nIndian Constitution Chatbot")
print("Type 'exit' to quit.\n")

while True:

    question = input("You: ")

    if question.lower() == "exit":
        break

    docs = db.similarity_search(question, k=4)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an expert assistant on the Constitution of India.

Answer ONLY using the context below.

If the answer is not found in the context, reply:
"I could not find this information in the Constitution."

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    print("\nBot:")
    print(response.content)
    print("-" * 60)