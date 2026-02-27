from langchain_groq import ChatGroq

def get_llm(model_name):
    return ChatGroq(model=model_name)