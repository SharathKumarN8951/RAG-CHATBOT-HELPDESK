from langchain_community.document_loaders import PyPDFLoader
import os

def load_documents(folder_path):
    documents = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".pdf"):
            file_path = os.path.join(folder_path, file_name)
            loader = PyPDFLoader(file_path)
            docs = loader.load()
            documents.extend(docs)

    return documents