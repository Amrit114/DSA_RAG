# DSA RAG - Data Structures & Algorithms RAG System

A Retrieval-Augmented Generation (RAG) system that enables intelligent Q&A over Data Structures & Algorithms (DSA) educational materials using LLMs and vector databases.

## Overview

DSA RAG is an AI-powered tutoring system that processes PDF documents containing DSA concepts and provides accurate, context-aware answers to user queries. It combines:

- **Document Processing**: Loads and processes PDF documents
- **Embeddings**: Converts text into vector embeddings using sentence transformers
- **Vector Database**: Stores embeddings in PostgreSQL with pgvector extension
- **LLM Integration**: Uses Groq's API for fast inference
- **RAG Pipeline**: Retrieves relevant context and generates answers

## Architecture

```
User Query
    ↓
Similarity Search (Vector DB)
    ↓
Context Retrieval
    ↓
LLM Processing (Groq)
    ↓
Generated Answer
```

## Project Structure

```
DSA_RAG/
├── app.py                 # Main application entry point
├── config.py              # Configuration settings
├── main.py                # CLI interface
├── requirements.txt       # Python dependencies
├── data/
│   ├── pdf/              # PDF documents (DSA books/materials)
│   └── text/             # Text files
├── db/
│   ├── connection.py      # Database connection utilities
│   └── vector_store.py    # Vector store and similarity search
├── embeddings/
│   └── embedder.py        # Text embedding functions
├── llm/
│   └── groq_llm.py        # Groq LLM integration
├── loaders/
│   └── pdf_loader.py      # PDF document loading
└── rag/
    └── rag_pipeline.py    # RAG pipeline logic
```

## Installation

### Prerequisites

- Python 3.8+
- PostgreSQL with pgvector extension
- Groq API key

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Amrit114/DSA_RAG.git
   cd DSA_RAG
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   Create a `.env` file in the project root:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   DB_NAME=rag_db
   DB_USER=postgres
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=5432
   ```

5. **Setup PostgreSQL**
   ```sql
   CREATE DATABASE rag_db;
   CREATE EXTENSION IF NOT EXISTS vector;
   ```

6. **Add DSA materials**
   - Place PDF files in `data/pdf/` directory
   - Update the `PDF_PATH` in `config.py` if needed

## Usage

### Loading Documents

Documents are automatically loaded from the configured PDF path. The system:
1. Extracts text from PDFs
2. Splits text into chunks
3. Generates embeddings
4. Stores in vector database

### Running Queries

```python
from rag.rag_pipeline import rag_answer

question = "What is a binary search tree?"
answer = rag_answer(question)
print(answer)
```

### Command Line Interface

```bash
python main.py
```

## Technologies Used

- **LangChain**: LLM framework and orchestration
- **Groq**: Fast LLM inference API
- **Sentence Transformers**: Text embedding model
- **PostgreSQL + pgvector**: Vector database
- **PyPDF/PyMuPDF**: PDF document loading
- **Python-dotenv**: Environment variable management

## Configuration

Edit `config.py` to customize:

- `PDF_PATH`: Location of PDF documents
- `EMBEDDING_MODEL`: Sentence transformer model
- `GROQ_MODEL`: LLM model selection
- `DB_CONFIG`: Database connection details

## Dependencies

See [requirements.txt](requirements.txt) for complete list:

- langchain
- langchain-groq
- sentence-transformers
- psycopg2-binary
- pgvector
- pypdf
- python-dotenv

## Features

✅ Multi-document PDF processing  
✅ Vector similarity search  
✅ Context-aware LLM responses  
✅ PostgreSQL integration  
✅ Fast inference with Groq API  
✅ Customizable embeddings and models  

## API Keys & Credentials

⚠️ **Security Note**: Never commit API keys or credentials. Use `.env` file for sensitive information.

### Getting API Keys

1. **Groq API**: Sign up at [console.groq.com](https://console.groq.com)
2. **PostgreSQL**: Set up locally or use cloud provider

## Roadmap

- [ ] Web UI (Streamlit/FastAPI)
- [ ] Support for multiple document formats
- [ ] Fine-tuned embeddings
- [ ] Conversation history tracking
- [ ] Answer source citation
- [ ] Performance analytics

## Troubleshooting

### Database Connection Issues
- Ensure PostgreSQL is running
- Verify DB_CONFIG in config.py
- Check pgvector extension is installed

### Embedding Generation Errors
- Check internet connection (for model download)
- Verify disk space for model storage
- Ensure sufficient RAM

### LLM Response Issues
- Verify Groq API key is valid
- Check rate limits
- Review context relevance

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Open a Pull Request

## License

This project is open source. Check LICENSE file for details.

## Contact & Support

- **Author**: Amrit Raj Singh
- **Repository**: https://github.com/Amrit114/DSA_RAG
- **Issues**: Report bugs on GitHub issues

## Acknowledgments

- Groq for fast LLM inference
- LangChain for excellent LLM orchestration
- Hugging Face for sentence transformers
- PostgreSQL community for pgvector
