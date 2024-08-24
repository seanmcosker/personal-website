import streamlit as st
st.title("Sean Chat :wave:")
st.markdown("If you're feeling lazy, use the chat below to ask questions about me and my experience.")
st.markdown("This is powered by a RAG workflow... if you're curious about this, all code is in my github repo")
st.chat_input("I'm your personal Sean expert!")


OPENAI_API_KEY = ""

if not OPENAI_API_KEY:
    with st.sidebar:
        OPENAI_API_KEY = st.text_input(label = "Enter API key")