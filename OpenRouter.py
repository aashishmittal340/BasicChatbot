# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

client = OpenAI(api_key=os.environ.get('OPENROUTER_API_KEY'), base_url="https://openrouter.ai/api/v1")

# response = client.chat.completions.create(
#     model="deepseek/deepseek-chat-v3.1:free",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant"},
#         {"role": "user", "content": "Hello"},
#     ],
#     stream=False
# )

# print(response.choices[0].message.content)


st.set_page_config(page_title="DeepSeek Chat", page_icon="🤖", layout="centered")

st.title("🤖 DeepSeek Chatbot")
st.write("Chat with **DeepSeek (via OpenRouter)** using Streamlit UI")

# Chat input
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "You are a helpful assistant"}
    ]

for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.write(msg["content"])
    elif msg["role"] == "assistant":
        with st.chat_message("assistant"):
            st.write(msg["content"])

# User input box
if prompt := st.chat_input("Type your message..."):
    # Add user message
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Call OpenRouter API
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="deepseek/deepseek-chat-v3.1:free",
                messages=st.session_state["messages"],
            )
            reply = response.choices[0].message.content
            st.write(reply)

    # Save assistant message
    st.session_state["messages"].append({"role": "assistant", "content": reply})