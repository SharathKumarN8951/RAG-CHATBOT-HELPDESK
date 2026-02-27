from langchain_community.vectorstores import FAISS


def create_vectorstore(chunks, embeddings):
    """
    Create FAISS vectorstore in memory (non-persistent).
    Suitable for Streamlit Cloud deployment.
    """
    vectorstore = FAISS.from_documents(chunks, embeddings)
    return vectorstore


def get_retriever(vectorstore, top_k):
    return vectorstore.as_retriever(search_kwargs={"k": top_k})
