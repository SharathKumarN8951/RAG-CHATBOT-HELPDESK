# ProjectNest Help Desk Chatbot

A Retrieval-Augmented Generation (RAG) based chatbot developed to answer student queries related to ProjectNest's academic project services. The chatbot uses information from PDF documents as its knowledge source and provides relevant responses through a simple web interface.

Live Demo: https://rag-chatbot-appdesk-ycdetjgof2mzv78q7cooip.streamlit.app

## About the Project

The idea behind this project was to build a smart help desk assistant that can answer common questions about academic projects without requiring manual support. Instead of relying only on a language model, the chatbot retrieves information from a collection of documents and uses that context to generate accurate responses.

The application automatically processes PDF files, creates vector embeddings, and performs semantic search to find the most relevant information before generating an answer.

## Key Features

* Answers student queries related to ProjectNest services
* Uses PDF documents as the knowledge base
* Semantic search with FAISS vector database
* Retrieval-Augmented Generation (RAG) workflow
* Interactive chat interface built with Streamlit
* Automatically loads and processes PDF files
* Secure API key management using environment variables

## Technologies Used

* Python
* Streamlit
* LangChain
* Groq LLM
* FAISS
* Sentence Transformers
* PyPDF

## Project Structure

```text
RAG-CHATBOT/
│
├── app.py
├── config.py
├── requirements.txt
├── .env
│
├── documents/
│
└── src/
    ├── loader.py
    ├── splitter.py
    ├── embeddings.py
    ├── vectorstore.py
    ├── llm.py
    └── rag_chain.py
```

## Setup Instructions

Clone the repository:

```bash
git clone https://github.com/SharathKumarN8951/RAG-CHATBOT-HELPDESK.git
```

Navigate to the project folder:

```bash
cd RAG-CHATBOT-HELPDESK
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your Groq API key:

```env
GROQ_API_KEY=your_api_key_here
```

Run the application:

```bash
streamlit run app.py
```

## How It Works

1. PDF files are loaded from the `documents` folder.
2. The documents are split into smaller chunks.
3. Embeddings are generated for each chunk.
4. The embeddings are stored in a FAISS vector database.
5. When a user asks a question, relevant content is retrieved.
6. The retrieved context is sent to the Groq LLM.
7. The chatbot generates a response based on the document information.

## What I Learned

Working on this project helped me understand:

* Retrieval-Augmented Generation (RAG)
* Vector databases and semantic search
* LangChain workflows
* LLM integration using Groq
* Building AI applications with Streamlit

## Future Enhancements

Some improvements that can be added in future versions:

* Persistent vector database storage
* Source document references in responses
* Admin dashboard for document management
* Chat history support
* Deployment using Docker and cloud services

## Author

Sharath Kumar N

GitHub: https://github.com/SharathKumarN8951
