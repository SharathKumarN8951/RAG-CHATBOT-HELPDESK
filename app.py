import os
import streamlit as st
from dotenv import load_dotenv

from config import *
from src.loader import load_documents
from src.splitter import split_documents
from src.embeddings import get_embeddings
from src.vectorstore import create_vectorstore, get_retriever
from src.llm import get_llm
from src.rag_chain import create_rag_chain


# ------------------ ENV SETUP ------------------ #
load_dotenv()

groq_key = os.getenv("GROQ_API_KEY")

if not groq_key:
    st.error("GROQ_API_KEY not found. Add it to .env file.")
    st.stop()

os.environ["GROQ_API_KEY"] = groq_key


# ------------------ PAGE CONFIG ------------------ #
st.set_page_config(page_title="RAG Chatbot", layout="wide")
st.title("📚 RAG Chatbot(Help Disk)")
st.caption("Multi-PDF RAG Chatbot built with Streamlit")


# ------------------ INITIALIZE RAG ------------------ #
@st.cache_resource
def initialize_rag():
    documents = load_documents(DOCUMENT_PATH)

    if not documents:
        st.error("No PDF files found in documents folder.")
        st.stop()

    chunks = split_documents(documents, CHUNK_SIZE, CHUNK_OVERLAP)

    embeddings = get_embeddings(EMBEDDING_MODEL)
    vectorstore = create_vectorstore(chunks, embeddings, FAISS_INDEX_PATH)
    retriever = get_retriever(vectorstore, TOP_K)

    llm = get_llm(GROQ_MODEL)
    rag_chain = create_rag_chain(llm, retriever)

    return rag_chain


qa_chain = initialize_rag()


# ------------------ CHAT MEMORY ------------------ #
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ------------------ CHAT INPUT WITH SUBMIT BUTTON ------------------ #
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your question...")
    submitted = st.form_submit_button("Send")

if submitted and user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = qa_chain.invoke(user_input)
            st.markdown(response)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}

    )
