import streamlit as st

@st.experimental_memo
def render_location():
    st.title("Location")
    st.write("The wedding will take place at a beautiful venue.")
    st.write("Address: 123 Wedding Lane, City, Country")
    st.map(location=["123 Wedding Lane, City, Country"])
