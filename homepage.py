import streamlit as st

@st.experimental_memo
def render_homepage():
    st.title("Welcome to Valentina and Luca's Wedding Website")
    st.write("We are excited to celebrate this special day with you!")
