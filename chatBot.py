from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq

#load the env variables
load_dotenv()

#streamLit page setup
st.set_page_config(
    page_title="chatBot",
    page_icon="🤖",
    layout="centered"
)

st.title("💬 Generative AI chatBot")

#initiate chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    
#show chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
#llm initiate
llm = ChatGroq(
    model = "openai/gpt-oss-120b",
    temperature = 0.0
)

#input box
#user enters input here
user_prompt = st.chat_input("Ask chatbot...")

if user_prompt:
    #display user prompt on UI
    st.chat_message("user").markdown(user_prompt)
    
    #add the user promt to chat history
    st.session_state.chat_history.append(
        {
            "role": "user", 
            "content": user_prompt
        }
    )
    
    #call the llm with and pass the chat history along with it
    response = llm.invoke(
        input = [
                {
                    "role": "system",
                    "content": "You are a helpful assistant",
                },
                *st.session_state.chat_history
            ]
    )
    
    #store llm response to chat history
    assistant_response = response.content
    st.session_state.chat_history.append(
        {
            "role": "assistant",
            "content": assistant_response,
        }
    )
    
    #display llm response
    with st.chat_message("assistant"):
        st.markdown(assistant_response)