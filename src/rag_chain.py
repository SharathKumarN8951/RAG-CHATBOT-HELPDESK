from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser


def create_rag_chain(llm, retriever):

    prompt = ChatPromptTemplate.from_template(
    """
    You are a professional IT Help Desk Assistant.

    Answer clearly and professionally.
    If the answer is not in the provided context, say:
    "I do not have that information in the knowledge base."

    Context:
    {context}

    Question:
    {question}
    """
)

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    rag_chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough(),
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain