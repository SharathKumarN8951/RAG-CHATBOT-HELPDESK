import os
from langchain_community.vectorstores import FAISS


def create_vectorstore(chunks, embeddings, index_path):
    # If index already exists → load it
    if os.path.exists(index_path):
        print("Loading existing FAISS index...")
        return FAISS.load_local(
            index_path,
            embeddings,
            allow_dangerous_deserialization=True
        )

    # Else → create new and save
    print("Creating new FAISS index...")
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(index_path)

    return vectorstore


def get_retriever(vectorstore, top_k):
    return vectorstore.as_retriever(search_kwargs={"k": top_k})
