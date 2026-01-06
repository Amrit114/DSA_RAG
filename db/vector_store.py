from db.connection import get_connection
from embeddings.embedder import get_embedding_model

embedding_model = get_embedding_model()

def clean_text(text: str) -> str:
    if not text:
        return ""
    
    return text.replace("\x00", "").strip()


def store_documents(chunks):
    conn = get_connection()
    cur = conn.cursor()

    for chunk in chunks:
        
        cleaned_text = clean_text(chunk.page_content)

        
        if not cleaned_text:
            continue

        vector = embedding_model.embed_query(cleaned_text)

        
        cur.execute(
            "INSERT INTO documents (content, embedding) VALUES (%s, %s)",
            (cleaned_text, vector)
        )

    conn.commit()
    cur.close()
    conn.close()



def similarity_search(query, top_k=5):
    query_vector = embedding_model.embed_query(query)

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT content
        FROM documents
        ORDER BY embedding <-> %s::vector
        LIMIT %s
        """,
        (query_vector, top_k)
    )

    results = cur.fetchall()
    cur.close()
    conn.close()

    return "\n".join([r[0] for r in results])
