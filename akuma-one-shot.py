from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

llm =  HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-Coder-480B-A35B-Instruct",
    task="text-generation",
    timeout=10
)


model = ChatHuggingFace(llm=llm)

st.set_page_config(
    page_title="Akuma"
)
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://wallpapers.com/images/hd/akuma-silhouettewith-glowing-kanji-hjontbr90gbsiwbx.jpg");
        background-attachment: fixed;
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)
hide_menu = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)


st.title("Hey, I am AKUMA")
st.header("Ask Me Anything")
user_input = st.text_input("Enter your prompt")

if st.button('Generate'):
    result = model.invoke(user_input)
    st.write(result.content)


