# 🎓 DSA RAG - Data Structures & Algorithms RAG System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-121212?style=for-the-badge&logo=chainlink&logoColor=white)

**An intelligent AI-powered tutoring system for Data Structures & Algorithms**

*Ask questions, get instant answers from your DSA materials*

[Features](#-features) • [Quick Start](#-quick-start) • [Usage](#-usage) • [Architecture](#-architecture) • [Contributing](#-contributing)

</div>

---

## 📸 Screenshots

### 🏠 Home Interface
<img width="1899" height="885" alt="image" src="https://github.com/user-attachments/assets/6508191e-4eb7-4bc6-8968-8a9498413a69" />


### 💬 Query & Response
<img width="1908" height="894" alt="image" src="https://github.com/user-attachments/assets/665b99c8-0b48-404c-a1ad-a99caac8ef89" />



## 🌟 Overview

DSA RAG transforms your Data Structures & Algorithms PDF materials into an intelligent Q&A system. Upload your textbooks, lecture notes, or study materials, and get accurate, context-aware answers powered by cutting-edge AI.

### ✨ What Makes It Special?

- 🚀 **Lightning Fast**: Powered by Groq API for instant responses
- 🎯 **Context-Aware**: Understands your questions and retrieves relevant information
- 📚 **Multi-Document**: Process multiple PDFs at once
- 🔍 **Semantic Search**: Find answers based on meaning, not just keywords
- 💾 **Persistent Storage**: PostgreSQL with vector embeddings for efficient retrieval

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER INTERFACE                          │
│                     (Flask Web Application)                     │
└────────────────────────────────┬────────────────────────────────┘
                                 │
                    ┌────────────┴────────────┐
                    │                         │
           ┌────────▼────────┐      ┌────────▼─────────┐
           │  📄 /ingest     │      │   💬 /ask        │
           │  Upload PDFs    │      │  Ask Questions   │
           └────────┬────────┘      └────────┬─────────┘
                    │                        │
                    │                        │
           ┌────────▼────────┐      ┌────────▼─────────┐
           │  PDF Processing │      │  Query Embedding │
           │  Text Chunking  │      │                  │
           └────────┬────────┘      └────────┬─────────┘
                    │                        │
                    │                        │
           ┌────────▼────────┐      ┌────────▼─────────┐
           │  🧮 Embeddings  │      │  🔍 Vector Search│
           │  (384-dim)      │      │  (Top-K Results) │
           └────────┬────────┘      └────────┬─────────┘
                    │                        │
                    └────────┬───────────────┘
                             │
                    ┌────────▼─────────┐
                    │  🗄️  PostgreSQL  │
                    │    + pgvector    │
                    │  Vector Database │
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
                    │  🤖 Groq LLM     │
                    │  Context + Query │
                    │  → Answer        │
                    └──────────────────┘
```

---

## 📦 Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| 🎯 **Framework** | LangChain | LLM orchestration and workflow |
| ⚡ **LLM** | Groq API | Ultra-fast inference engine |
| 🧮 **Embeddings** | Sentence Transformers | Text-to-vector conversion (384-dim) |
| 🗄️ **Database** | PostgreSQL + pgvector | Vector storage and similarity search |
| 🌐 **Web Server** | Flask | REST API and web interface |
| 📄 **PDF Processing** | PyMuPDF | Document text extraction |
| 🔐 **Config** | python-dotenv | Environment management |

---

## 🚀 Quick Start

### Prerequisites

- ✅ Python 3.8 or higher
- ✅ PostgreSQL with pgvector extension
- ✅ Groq API key ([Get one here](https://console.groq.com))

### Installation

**1️⃣ Clone the repository**

```bash
git clone https://github.com/Amrit114/DSA_RAG.git
cd DSA_RAG
```

**2️⃣ Create virtual environment**

```bash
# Create venv
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate
```

**3️⃣ Install dependencies**

```bash
pip install -r requirements.txt
```

**4️⃣ Setup PostgreSQL**

```sql
-- Create database
CREATE DATABASE rag_db;

-- Connect to database
\c rag_db

-- Enable pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Create documents table
CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    content TEXT,
    embedding VECTOR(384)
);

-- Create index for faster searches (optional but recommended)
CREATE INDEX ON documents USING ivfflat (embedding vector_cosine_ops);
```

**5️⃣ Configure environment**

Create a `.env` file in the project root:

```env
# Groq API Configuration
GROQ_API_KEY=your_groq_api_key_here

# Database Configuration
DB_NAME=rag_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

# Optional: Customize paths
PDF_DIR=data/pdf
```

**6️⃣ Add your DSA materials**

```bash
# Place your PDF files in the data directory
mkdir -p data/pdf
# Copy your PDFs to data/pdf/
```

---

## 💻 Usage

### Starting the Server

```bash
python app.py
```

The server will start at `http://localhost:5000`

### Using the Web Interface

1. 🌐 Open your browser and navigate to `http://localhost:5000`
2. 📤 Click "Ingest Documents" to process PDFs (first time only)
3. 💬 Type your question in the input box
4. ✨ Get instant AI-powered answers!

### Using the API

**Ingest Documents**

```bash
curl -X POST http://localhost:5000/ingest
```

**Ask a Question**

```bash
curl -X POST http://localhost:5000/ask \
  -H "Content-Type: application/json" \
  -d '{
    "question": "What is a binary search tree and how does it work?"
  }'
```

**Response Format**

```json
{
  "answer": "A binary search tree is a hierarchical data structure...",
  "status": "success"
}
```

### Using Python Code

```python
from rag.rag_pipeline import rag_answer

# Ask a question
question = "Explain the time complexity of quicksort"
answer = rag_answer(question)
print(answer)
```

---

## 📁 Project Structure

```
DSA_RAG/
│
├── 📄 app.py                    # Flask application (API + Web UI)
├── ⚙️  config.py                 # Configuration settings
├── 🚀 main.py                   # CLI interface
├── 📋 requirements.txt          # Python dependencies
├── 🔐 .env                      # Environment variables (create this)
│
├── 📂 data/
│   ├── 📚 pdf/                  # Place your PDF files here
│   └── 📝 text/                 # Text files (optional)
│
├── 🗄️  db/
│   ├── 🔗 connection.py         # PostgreSQL connection handler
│   └── 🔍 vector_store.py       # Vector storage and similarity search
│
├── 🧮 embeddings/
│   └── 📊 embedder.py           # Text embedding generation
│
├── 🤖 llm/
│   └── 💬 groq_llm.py           # Groq LLM integration
│
├── 📦 loaders/
│   └── 📥 pdf_loader.py         # PDF document processing
│
├── 🔄 rag/
│   └── ⚡ rag_pipeline.py       # RAG pipeline orchestration
│
├── 🎨 templates/
│   └── 📄 index.html            # Web interface
│
└── 📊 static/
    └── 💻 script.js             # Frontend JavaScript
```

---

## ✨ Features

### Current Features

- ✅ **PDF Document Processing** - Automatically extract and chunk text from PDFs
- ✅ **Vector Similarity Search** - Fast semantic search using pgvector
- ✅ **Context-Aware Responses** - LLM generates answers based on retrieved context
- ✅ **REST API** - Easy integration with other applications
- ✅ **Web Interface** - User-friendly UI for asking questions
- ✅ **Persistent Storage** - PostgreSQL database for scalability
- ✅ **Customizable Embeddings** - Choose your preferred embedding model
- ✅ **Fast Inference** - Powered by Groq's optimized infrastructure

### Coming Soon 🔜

- 🔲 Enhanced web UI with chat history
- 🔲 Support for multiple document formats (DOCX, TXT, Markdown)
- 🔲 Answer source citations with page numbers
- 🔲 User authentication and personal document spaces
- 🔲 Fine-tuned embeddings for DSA domain
- 🔲 Conversation memory across sessions
- 🔲 Export chat history
- 🔲 Real-time document updates

---

## 🔧 Configuration

### config.py Settings

```python
# PDF Directory
PDF_DIR = "data/pdf"

# Database Configuration
DB_CONFIG = {
    "dbname": "rag_db",
    "user": "postgres",
    "password": "your_password",
    "host": "localhost",
    "port": "5432"
}

# Embedding Model (384-dimensional)
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Groq Configuration
GROQ_MODEL = "mixtral-8x7b-32768"
GROQ_API_KEY = "your_api_key"
```

### Changing Embedding Model

If you use a different embedding model, update the vector dimension:

```sql
-- For 768-dim models like BERT
ALTER TABLE documents ALTER COLUMN embedding TYPE VECTOR(768);
```

---

## 🐛 Troubleshooting

### Database Connection Issues

**Problem:** `Connection refused` or `could not connect to server`

**Solution:**
```bash
# Check if PostgreSQL is running
sudo systemctl status postgresql  # Linux
brew services list               # macOS

# Verify credentials in .env match your PostgreSQL setup
```

### No PDFs Found During Ingestion

**Problem:** `/ingest` reports no documents found

**Solution:**
```bash
# Check PDF directory path
ls data/pdf/

# Verify PDF_DIR in config.py matches actual location
```

### Embedding Generation Errors

**Problem:** Model download fails or embeddings error

**Solution:**
```bash
# Ensure you have internet connection
# Check disk space for model cache (~500MB)

# Clear cache and retry
rm -rf ~/.cache/huggingface/
```

### Groq API Errors

**Problem:** Invalid API key or rate limit errors

**Solution:**
```bash
# Verify API key in .env
echo $GROQ_API_KEY

# Check rate limits at console.groq.com
# Free tier: 30 requests/minute
```

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### How to Contribute

1. 🍴 **Fork** the repository
2. 🌿 **Create** a feature branch
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. 💾 **Commit** your changes
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. 🚀 **Push** to the branch
   ```bash
   git push origin feature/AmazingFeature
   ```
5. 📝 **Open** a Pull Request

### Contribution Ideas

- 🐛 Bug fixes
- ✨ New features
- 📚 Documentation improvements
- 🎨 UI/UX enhancements
- ⚡ Performance optimizations
- 🧪 Test coverage

---

## 📄 License

This project is open source. See the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- ⚡ **Groq** - For blazing fast LLM inference
- 🔗 **LangChain** - For excellent LLM orchestration framework
- 🤗 **Hugging Face** - For sentence transformers and model hosting
- 🐘 **PostgreSQL** - For pgvector extension and robust database
- 🎓 **DSA Community** - For educational resources and inspiration

---

## 📞 Contact & Support

<div align="center">

👤 **Amrit Raj Singh**

[![GitHub](https://img.shields.io/badge/GitHub-Amrit114-181717?style=for-the-badge&logo=github)](https://github.com/Amrit114)
[![Repository](https://img.shields.io/badge/Repo-DSA__RAG-blue?style=for-the-badge&logo=github)](https://github.com/Amrit114/DSA_RAG)

**Found a bug?** [Report it here](https://github.com/Amrit114/DSA_RAG/issues)

**Have questions?** Open a [discussion](https://github.com/Amrit114/DSA_RAG/discussions)

</div>

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

Made with ❤️ for the DSA learning community

</div>
