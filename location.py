import streamlit as st

@st.experimental_memo
def render_location():
    st.title("Location")
    st.write("The wedding will take place at a beautiful venue.")
    st.write("Via alla Madonnina, 22030, Barni, Italy")
    st.map(location=["Via alla Madonnina, 22030, Barni, Italy"])
    st.map(location=["Via alla Madonnina, 22030, Barni, Italy"])
