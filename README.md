# DSA RAG

A small Retrieval-Augmented Generation (RAG) service that exposes a Flask frontend and API to query PDF-based Data Structures & Algorithms materials. The project extracts text from PDFs, creates embeddings, stores them in PostgreSQL (with pgvector), and uses a Groq LLM for context-aware answers.

## Quick summary

- Web app: `app.py` serves a simple frontend and two endpoints: `POST /ingest` to ingest PDFs and `POST /ask` to query.
- PDF loading & splitting: `loaders/pdf_loader.py` uses PyMuPDF via LangChain community loader and splits into chunks.
- Embeddings: `embeddings/embedder.py` creates embeddings via `HuggingFaceEmbeddings` configured in `config.py`.
- Vector store: `db/vector_store.py` stores and searches embeddings in PostgreSQL (`documents` table).
- LLM: `llm/groq_llm.py` wraps the Groq Chat model; prompts are composed in `rag/rag_pipeline.py`.

## Prerequisites

- Python 3.8+
- PostgreSQL with the `pgvector` extension
- A Groq API key (set in environment variable `GROQ_API_KEY`)

## Install

1. Create and activate a virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create the database and extension (example using psql):

```sql
CREATE DATABASE rag_db;
\c rag_db
CREATE EXTENSION IF NOT EXISTS vector;
```

4. Create the `documents` table used by the code:

```sql
CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    content TEXT,
    embedding VECTOR(384)
);
```

Update `DB_CONFIG` in `config.py` if your database credentials differ.

## Configuration

Edit `config.py` or use a `.env` file to set environment variables. Relevant values in `config.py`:

- `PDF_DIR` — default: `data/pdf` (where PDF files should be placed)
- `DB_CONFIG` — connection information for PostgreSQL
- `EMBEDDING_MODEL` — Hugging Face model name used for embeddings
- `GROQ_MODEL` and `GROQ_API_KEY` — Groq LLM configuration

## Usage

1. Place your PDF files into the `data/pdf/` directory.

2. Start the Flask server:

```bash
python app.py
```

3. Ingest PDFs (via the server endpoint):

```bash
curl -X POST http://localhost:5000/ingest
```

The `/ingest` endpoint runs `load_and_split_pdfs_from_directory(PDF_DIR)` and then `store_documents(...)` to save embeddings to the database.

4. Ask a question (example):

```bash
curl -X POST http://localhost:5000/ask \
  -H "Content-Type: application/json" \
  -d '{"question":"What is a binary search tree?"}'
```

The request calls `rag.rag_pipeline.rag_answer(question)`, which performs a similarity search and invokes the Groq LLM with the retrieved context.

## Files & Responsibilities

- `app.py` — Flask app with `/` (frontend), `/ingest`, and `/ask` endpoints.
- `loaders/pdf_loader.py` — Finds PDFs in `data/pdf/`, loads them using PyMuPDF and splits text into chunks.
- `embeddings/embedder.py` — Returns the `HuggingFaceEmbeddings` model used to embed text.
- `db/connection.py` — Returns a psycopg2 connection using `DB_CONFIG` from `config.py`.
- `db/vector_store.py` — `store_documents(chunks)` inserts text+embedding into `documents`; `similarity_search(query, top_k=5)` returns concatenated text results.
- `llm/groq_llm.py` — Builds a `ChatGroq` client used to invoke the LLM.
- `rag/rag_pipeline.py` — Composes prompt, retrieves context via `similarity_search`, and calls the LLM.
- `templates/index.html` & `static/script.js` — Minimal frontend to ask questions and display answers.
- `main.py` — tiny CLI stub.

## Notes & Recommendations

- Security: Keep `GROQ_API_KEY` and DB credentials out of version control; use a `.env` file or secrets manager.
- Embedding dimensionality: The code assumes a 384-dim model (see `EMBEDDING_MODEL` in `config.py`). If you change the model, update the database `VECTOR(...)` size accordingly.
- Production: For concurrency and stability, run the Flask app behind a production server (e.g., Gunicorn) and secure the DB and API keys.

## Troubleshooting

- If ingestion reports no PDFs: confirm files are in `data/pdf/` and `PDF_DIR` path in `config.py` is correct.
- Database connection errors: verify PostgreSQL is running and `DB_CONFIG` matches your credentials.
- LLM errors: ensure `GROQ_API_KEY` is set and the configured `GROQ_MODEL` is available.

## Contributing

Contributions welcome. Typical flow:

1. Fork and create a feature branch
2. Add tests/local verification
3. Open a PR

## License

See repository license (if present).

---

If you'd like, I can also:

- Add a sample `.env.example` file
- Add a small script to initialize the DB schema
- Add a short guide to deploy the Flask app behind Gunicorn

# 🎓 DSA RAG - Data Structures & Algorithms RAG System

> An intelligent **Retrieval-Augmented Generation (RAG)** system for Data Structures & Algorithms learning

A powerful AI-driven tutoring system that enables intelligent Q&A over DSA educational materials using cutting-edge LLMs and vector databases.

## 🚀 Overview

DSA RAG is an **AI-powered tutoring system** that processes PDF documents containing DSA concepts and provides accurate, context-aware answers to user queries. 

### Key Components:

| Component | Description |
|-----------|-------------|
| 📄 **Document Processing** | Loads and processes PDF documents intelligently |
| 🧮 **Embeddings** | Converts text into vector embeddings using sentence transformers |
| 🗄️ **Vector Database** | Stores embeddings in PostgreSQL with pgvector extension |
| 🤖 **LLM Integration** | Uses Groq's API for ultra-fast inference |
| 🔄 **RAG Pipeline** | Retrieves relevant context and generates accurate answers |

## 🏗️ Architecture

```
┌─────────────────┐
│   User Query    │
└────────┬────────┘
         │
         ▼
┌─────────────────────────┐
│  Similarity Search      │
│   (Vector Database)     │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  Context Retrieval      │
│  (Top-K Results)        │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  LLM Processing         │
│  (Groq API)             │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  Generated Answer       │
│  (Context-Aware)        │
└─────────────────────────┘
```

## 📁 Project Structure

```
DSA_RAG/
├── 📄 app.py                 # Main application entry point
├── ⚙️  config.py              # Configuration settings
├── 🚀 main.py                # CLI interface
├── 📋 requirements.txt       # Python dependencies
├── 📂 data/
│   ├── 📚 pdf/              # PDF documents (DSA books/materials)
│   └── 📝 text/             # Text files
├── 🗄️  db/
│   ├── 🔗 connection.py      # Database connection utilities
│   └── 🔍 vector_store.py    # Vector store and similarity search
├── 🧮 embeddings/
│   └── 📊 embedder.py        # Text embedding functions
├── 🤖 llm/
│   └── 💬 groq_llm.py        # Groq LLM integration
├── 📦 loaders/
│   └── 📥 pdf_loader.py      # PDF document loading
└── 🔄 rag/
    └── ⚡ rag_pipeline.py    # RAG pipeline logic
```

## 📥 Installation

### ✅ Prerequisites

- Python 3.8+
- PostgreSQL with pgvector extension
- Groq API key

### 🔧 Setup Steps

1. **📦 Clone the repository**
   ```bash
   git clone https://github.com/Amrit114/DSA_RAG.git
   cd DSA_RAG
   ```

2. **🐍 Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **📚 Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **🔐 Configure environment variables**
   Create a `.env` file in the project root:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   DB_NAME=rag_db
   DB_USER=postgres
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=5432
   ```

5. **🗄️  Setup PostgreSQL**
   ```sql
   CREATE DATABASE rag_db;
   CREATE EXTENSION IF NOT EXISTS vector;
   ```

6. **📄 Add DSA materials**
   - Place PDF files in `data/pdf/` directory
   - Update the `PDF_PATH` in `config.py` if needed

## 📚 Usage

### Loading Documents

Documents are automatically loaded from the configured PDF path. The system:
1. Extracts text from PDFs
2. Splits text into chunks
3. Generates embeddings
4. Stores in vector database

### 🔍 Running Queries

```python
from rag.rag_pipeline import rag_answer

question = "What is a binary search tree?"
answer = rag_answer(question)
print(answer)
```

### 💻 Command Line Interface

```bash
python main.py
```

## 🛠️ Technologies Used

| Technology | Purpose |
|-----------|---------|
| **LangChain** | LLM framework and orchestration |
| **Groq** | ⚡ Fast LLM inference API |
| **Sentence Transformers** | Text embedding model (384-dim) |
| **PostgreSQL + pgvector** | 🗄️ Vector database |
| **PyPDF/PyMuPDF** | PDF document loading |
| **Python-dotenv** | Environment variable management |

## 💾 Database Schema

The system uses PostgreSQL with pgvector extension for storing and searching embeddings.

### Documents Table

```sql
CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    content TEXT,
    embedding VECTOR(384)
);
```

### 📊 Schema Details

| Column | Type | Description |
|--------|------|-------------|
| `id` | SERIAL PRIMARY KEY | Unique document identifier |
| `content` | TEXT | Document text content |
| `embedding` | VECTOR(384) | 384-dimensional vector representation (from sentence-transformers) |

### 🔑 Indexes (Recommended for Performance)

```sql
-- Create index for vector similarity search
CREATE INDEX ON documents USING ivfflat (embedding vector_cosine_ops);

-- Create index for faster lookups
CREATE INDEX ON documents(id);
```

### 💡 Usage Example

```python
# Embeddings are automatically generated and stored
# Vector search is performed using cosine similarity
from db.vector_store import similarity_search

results = similarity_search("binary search tree", k=5)
# Returns top 5 most similar documents
```

## 📦 Dependencies

See [requirements.txt](requirements.txt) for complete list:

```
langchain                 # LLM orchestration framework
langchain-groq           # Groq API integration
sentence-transformers    # Text embeddings
psycopg2-binary         # PostgreSQL adapter
pgvector                # Vector extension for PostgreSQL
pypdf                   # PDF processing
python-dotenv           # Environment variables
```

## ✨ Features

✅ **Multi-document PDF processing** - Handle multiple PDF files  
✅ **Vector similarity search** - Fast semantic search using pgvector  
✅ **Context-aware LLM responses** - Intelligent answers based on retrieved context  
✅ **PostgreSQL integration** - Robust database backend  
✅ **Fast inference** - Powered by Groq API  
✅ **Customizable embeddings** - Choose your embedding model  
✅ **Easy configuration** - Simple config.py for setup  

## 🔐 API Keys & Credentials

⚠️ **Security Note**: Never commit API keys or credentials. Use `.env` file for sensitive information.

### 🔑 Getting API Keys

1. **Groq API**: Sign up at [console.groq.com](https://console.groq.com) ⚡
2. **PostgreSQL**: Set up locally or use cloud provider ☁️

## 🗺️ Roadmap

- [ ] 🌐 Web UI (Streamlit/FastAPI)
- [ ] 📄 Support for multiple document formats
- [ ] 🎯 Fine-tuned embeddings
- [ ] 💬 Conversation history tracking
- [ ] 📌 Answer source citation
- [ ] 📊 Performance analytics
- [ ] 🔔 Real-time updates

## 🐛 Troubleshooting

### 🗄️ Database Connection Issues
```
❌ Error: Connection refused
✅ Solution: Ensure PostgreSQL is running and DB_CONFIG is correct
```

### 🧮 Embedding Generation Errors
```
❌ Error: Model not found
✅ Solution: Check internet connection and disk space for model download
```

### 🤖 LLM Response Issues
```
❌ Error: API key invalid
✅ Solution: Verify Groq API key and check rate limits
```

## 🤝 Contributing

Contributions are welcome! Please:

1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. 🚀 Push to the branch (`git push origin feature/AmazingFeature`)
5. 📝 Open a Pull Request

## 📄 License

This project is open source. Check LICENSE file for details.

## 📞 Contact & Support

- **👤 Author**: [Amrit Raj singh](https://github.com/Amrit114)
- **📦 Repository**: [DSA_RAG](https://github.com/Amrit114/DSA_RAG)
- **🐛 Issues**: [Report bugs on GitHub](https://github.com/Amrit114/DSA_RAG/issues)

## 🙏 Acknowledgments

- ⚡ **Groq** - for fast LLM inference
- 🔗 **LangChain** - for excellent LLM orchestration
- 🤗 **Hugging Face** - for sentence transformers
- 🐘 **PostgreSQL** - for pgvector extension
- 🎓 **DSA Community** - for educational resources
