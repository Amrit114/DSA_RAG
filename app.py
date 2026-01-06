from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

from loaders.pdf_loader import load_and_split_pdfs_from_directory
from db.vector_store import store_documents
from rag.rag_pipeline import rag_answer
from config import PDF_DIR

app = Flask(__name__)
CORS(app)



@app.route("/")
def home():
    return render_template("index.html")



@app.route("/ingest", methods=["POST"])
def ingest():
    chunks = load_and_split_pdfs_from_directory(PDF_DIR)
    store_documents(chunks)
    return jsonify({"status": "PDFs ingested successfully"})



@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(force=True)
    question = data.get("question", "").strip()

    if not question:
        return jsonify({"error": "Question required"}), 400

    answer = rag_answer(question)
    return jsonify({
        "question": question,
        "answer": answer
    })



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
