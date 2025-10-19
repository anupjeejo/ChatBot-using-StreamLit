import os
from dotenv import load_dotenv
import strealit as st
from lanchain_groq import ChatGroq

#load the env variables
load_dotenv()

#streamLit page setup
st.set_page_config(
    page_title="chatBot",
    page_icon="🤖",
    layout="centered"
)

st.title("💬 Generative AI chatBot")