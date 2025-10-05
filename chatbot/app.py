from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st


prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant and your name is \"Zen\".. Please respond to the user queries in a sarcastic way but not mean or offensive."),
    ("user", "Question: {question}")
])


st.title("Chatbot with LangChain, Ollama, and Streamlit")
input_text = st.text_input("Enter your message:")


llm = Ollama(model="gemma3:1b")


output_parser = StrOutputParser()


chain = prompt | llm | output_parser


if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)
