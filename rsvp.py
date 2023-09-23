import streamlit as st

@st.experimental_memo
def render_rsvp():
    st.title("RSVP")
    st.write("Please RSVP by filling out the form below:")
    
    # Create a form with CSS styles
    st.markdown('<link rel="stylesheet" href="style.css">', unsafe_allow_html=True)
    with st.form(key="rsvp-form", id="rsvp-form"):
        st.subheader("Personal Information")
        name = st.text_input("Your Name:", key="name")
        email = st.text_input("Your Email:", key="email")
        phone = st.text_input("Phone Number:", key="phone")
        allergies = st.text_area("Allergies (if any):", key="allergies")

        st.subheader("Number of Guests")
        num_guests = st.number_input("Number of Guests (including yourself):", min_value=1, step=1, key="num_guests")

        submit_button = st.form_submit_button("Submit")

    # Handle form submission
    if submit_button:
        # Access the form values using the keys
        st.write(f"Name: {name}")
        st.write(f"Email: {email}")
        st.write(f"Phone Number: {phone}")
        st.write(f"Allergies: {allergies}")
        st.write(f"Number of Guests: {num_guests}")
