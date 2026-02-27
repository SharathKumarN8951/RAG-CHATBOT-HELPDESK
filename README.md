# 📚 ProjectNest Help Desk Chatbot (RAG Powered) https://rag-chatbot-appdesk-ycdetjgof2mzv78q7cooip.streamlit.app

A professional AI-powered Help Desk Chatbot built using **LangChain, Groq LLM, FAISS, and Streamlit**.

This chatbot acts as the official ProjectNest Help Desk Assistant and answers student queries regarding academic project services.

---

## 🚀 Features

- 🤖 Groq LLM Powered Responses
- 📄 Multi-PDF Knowledge Base Support
- 🔎 Semantic Search using FAISS
- 💬 ChatGPT-style UI (Streamlit)
- 🧠 Retrieval-Augmented Generation (RAG)
- 📚 Automatically loads all PDFs from `documents/`
- 🔐 Secure API key handling via `.env`

---

## 🏢 About ProjectNest

ProjectNest provides academic projects for:

- MCA
- BCA
- Engineering Students

### Services Include:
- Project Abstract & Problem Statement
- Database Design & Architecture
- Complete Source Code
- Execution Steps & Output Screens
- Viva Q&A
- Submission-ready Documentation (Report + PPT)
- University Syllabus Customization

---

## 💰 Pricing

| Project Type       | Price  |
|-------------------|--------|
| Mini Project      | ₹499   |
| Final Year Project| ₹1999  |
| Premium Project   | ₹3999  |

---

## 🛠️ Tech Stack

- Python 3.12
- Streamlit
- LangChain
- Groq API
- FAISS Vector Database
- Sentence Transformers
- PyPDF

---

## 📂 Project Structure
RAG-CHATBOT/
│
├── app.py
├── config.py
├── requirements.txt
├── .env
│
├── documents/
│ └── (All PDF files)
│
└── src/
├── loader.py
├── splitter.py
├── embeddings.py
├── vectorstore.py
├── llm.py
└── rag_chain.py


---

## ⚙️ Installation

### 1️⃣ Clone Repository

git clone https://github.com/your-username/projectnest-helpdesk.git
cd projectnest-helpdesk`

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Add Groq API Key

Create a .env file in root directory:

GROQ_API_KEY=your_groq_api_key_here
▶️ Run Application
python -m streamlit run app.py

🎯 How It Works

Loads all PDFs from documents/

Splits into chunks

Converts chunks into embeddings

Stores embeddings in FAISS vector DB

Retrieves relevant chunks based on user query

Sends context + query to Groq LLM

Displays structured answer

🔐 Security

API keys stored securely in .env

No sensitive data exposed

Strict prompt rules prevent unrelated queries

📞 Contact

Email: sharathnsharu@gmail.com

WhatsApp: +91-8951663634
Instagram: thinksphere_official

Managed by @prajwal.cv_

👨‍💼 Management

CEO Team:

PRAJWAL

SHARATH KUMAR N

RAKESH GN

📌 Future Improvements

Persistent Vector Storage

Source Document Display

Page Number References

Admin Dashboard

Deployment to Cloud

⭐ If you like this project

Give it a ⭐ on GitHub!
