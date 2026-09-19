# 🇮🇳 Constitution RAG Chatbot

A fully **local, privacy-first Retrieval-Augmented Generation (RAG) chatbot** that answers natural language questions about the **Constitution of India**. Built entirely with open-source tools — no OpenAI keys, no cloud APIs, no data ever leaves your machine.

---

## 📖 Overview

This project ingests the Constitution of India (PDF), splits it into semantically meaningful chunks, embeds them into a vector database, and uses a locally-running LLM (Llama 3.2 via Ollama) to answer user questions **grounded strictly in the source document**. If the answer isn't present in the Constitution, the bot explicitly says so instead of hallucinating.

---

## ✨ Features

- 🔒 **Fully Local & Private** — no internet connection or API keys required after setup
- 📄 **PDF Ingestion** — parses the Constitution of India directly from a PDF
- 🧩 **Smart Chunking** — `RecursiveCharacterTextSplitter` (1000 chars, 200 overlap) for coherent context
- 🔍 **Semantic Search** — FAISS vector database for fast, accurate retrieval
- 🤖 **Local LLM Inference** — powered by Llama 3.2 (3B) via Ollama
- 💬 **Interactive CLI Chat** — simple command-line Q&A interface
- ✅ **Grounded, Hallucination-Resistant Answers** — strict prompt ensures answers come only from retrieved context

---

## 🛠️ Tech Stack

| Component            | Tool/Library                          |
|-----------------------|----------------------------------------|
| PDF Parsing            | `pypdf`, `PyPDFLoader` (LangChain)     |
| Text Splitting         | `RecursiveCharacterTextSplitter`       |
| Embeddings              | `BAAI/bge-small-en-v1.5` (HuggingFace) |
| Vector Store            | `FAISS`                                |
| LLM                       | `Llama 3.2 (3B)` via `Ollama`          |
| Orchestration           | `LangChain`                            |

---

## 📂 Project Structure

```
Constitution-RAG/
│
├── Data/
│   └── Data.pdf              # Constitution of India (source PDF)
│
├── ingest.py                 # Loads PDF, chunks it, builds FAISS vector DB
├── check_pdf.py               # Quick sanity check that the PDF loads correctly
├── rag.py                    # Main chatbot — retrieval + LLM Q&A loop
├── vector_db/                 # Saved FAISS index (generated after running ingest.py)
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/mehak-dahiya/Constitution-RAG.git
cd Constitution-RAG
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install langchain langchain-community langchain-text-splitters langchain-huggingface langchain-ollama faiss-cpu pypdf sentence-transformers
```

### 4. Install & run Ollama
Download Ollama from [ollama.com](https://ollama.com), then pull the model:
```bash
ollama pull llama3.2:3b
```

### 5. Add your PDF
Place the Constitution of India PDF inside the `Data/` folder as `Data.pdf`.

---

## 🚀 Usage

### Step 1 — Verify the PDF loads correctly
```bash
python check_pdf.py
```

### Step 2 — Build the vector database
```bash
python ingest.py
```
This creates a `vector_db/` folder containing the FAISS index.

### Step 3 — Start the chatbot
```bash
python rag.py
```

Example session:
```
Indian Constitution Chatbot
Type 'exit' to quit.

You: What is Article 21?
Bot: Article 21 guarantees the right to life and personal liberty...
------------------------------------------------------------
```

---

## 🧠 How It Works

1. **Ingestion** — `ingest.py` loads the PDF, splits it into overlapping chunks, embeds each chunk using `bge-small-en-v1.5`, and stores the vectors in a local FAISS index.
2. **Retrieval** — `rag.py` embeds the user's question and retrieves the top-k most relevant chunks from FAISS.
3. **Generation** — The retrieved chunks are passed as context to Llama 3.2 (3B) via Ollama, along with a strict prompt instructing the model to answer *only* from the given context.
4. **Fallback** — If no relevant information is found, the bot responds: *"I could not find this information in the Constitution."*

---

## 🔮 Future Improvements

- [ ] Web-based UI (Streamlit / Gradio)
- [ ] Source citation with article/page numbers
- [ ] Support for multi-turn conversational memory
- [ ] Support for additional legal documents

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙋 Use Cases

Ideal for students, researchers, legal professionals, and civics enthusiasts who want fast, accurate, citation-grounded answers about constitutional provisions — without internet access or paid API subscriptions.
