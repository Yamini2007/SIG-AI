import streamlit as st
from chatbot import get_response  # Import the Groq API response function

st.title("Chatbot")

user_input = st.text_input("You: ", "")

if user_input:
    # Get the response from Groq API
    response = get_response(user_input)
    st.write("Chatbot: " + response)
