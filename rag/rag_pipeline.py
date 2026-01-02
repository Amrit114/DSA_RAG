from db.vector_store import similarity_search
from llm.groq_llm import get_llm

llm = get_llm()

def rag_answer(question):
    context = similarity_search(question)

    prompt = f"""
    You are a helpful tutor.
    Use ONLY the given context.
    If the answer is not in the context, say:
    "This information is not available in the provided data."

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    response = llm.invoke(prompt)
    return response.content
