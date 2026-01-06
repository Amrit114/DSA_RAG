from pathlib import Path
from langchain_community.document_loaders import  PyMuPDFLoader 
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_and_split_pdfs_from_directory(pdf_directory):
    
    all_documents = []
    pdf_dir = Path(pdf_directory)

    
    pdf_files = list(pdf_dir.glob("**/*.pdf"))
    print(f"Found {len(pdf_files)} PDF files")

    for pdf_file in pdf_files:
        print(f"Processing: {pdf_file.name}")
        try:
            loader = PyMuPDFLoader(str(pdf_file))
            documents = loader.load()

            
            for doc in documents:
                doc.metadata["source_file"] = pdf_file.name
                doc.metadata["source_path"] = str(pdf_file)

            all_documents.extend(documents)

        except Exception as e:
            print(f"Error loading {pdf_file.name}: {e}")

    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    return splitter.split_documents(all_documents)
