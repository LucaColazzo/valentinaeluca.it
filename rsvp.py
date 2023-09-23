import streamlit as st

@st.experimental_memo
def render_rsvp():
    st.title("RSVP")
    st.write("Please RSVP by filling out the form below:")
    name = st.text_input("Your Name:")
    email = st.text_input("Your Email:")
    attending = st.selectbox("Are you attending?", ("Yes", "No", "Maybe"))
    st.write(f"Name: {name}")
    st.write(f"Email: {email}")
    st.write(f"Attending: {attending}")
