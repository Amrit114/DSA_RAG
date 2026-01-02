from db.connection import get_connection
from embeddings.embedder import get_embedding_model

embedding_model = get_embedding_model()

def store_documents(chunks):
    conn = get_connection()
    cur = conn.cursor()

    for chunk in chunks:
        vector = embedding_model.embed_query(chunk.page_content)
        cur.execute(
            "INSERT INTO documents (content, embedding) VALUES (%s, %s)",
            (chunk.page_content, vector)
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
