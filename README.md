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
