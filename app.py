from loaders.pdf_loader import load_and_split_pdf
from db.vector_store import store_documents
from rag.rag_pipeline import rag_answer
from config import PDF_PATH

def ingest_data():
    chunks = load_and_split_pdf(PDF_PATH)
    store_documents(chunks)
    print("✅ Data stored in pgvector")

def chat():
    while True:
        question = input("\nAsk a question (type exit to quit): ")
        if question.lower() == "exit":
            break
        print("\nAnswer:")
        print(rag_answer(question))


if __name__ == "__main__":
    ingest_data()

    
    chat()
