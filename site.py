import streamlit as st

# Define function to create navigation menu
def navigation_menu():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to:", ("Homepage", "Location", "RSVP"))
    return page

# Homepage
def homepage():
    st.title("Welcome to Valentina and Luca's Wedding Website")
    st.write("We are excited to celebrate this special day with you!")

# Location
def location():
    st.title("Location")
    st.write("The wedding will take place at Ristorante alla Madonnina di Barni.")
    st.write("ia alla Madonnina, 22030, Barni, Italy")
    st.map(location=["ia alla Madonnina, 22030, Barni, Italy"])

# RSVP
def rsvp():
    st.title("RSVP")
    st.write("Please RSVP by filling out the form below:")
    name = st.text_input("Your Name:")
    email = st.text_input("Your Email:")
    attending = st.selectbox("Are you attending?", ("Yes", "No", "Maybe"))
    st.write(f"Name: {name}")
    st.write(f"Email: {email}")
    st.write(f"Attending: {attending}")

# Main function to run the app
def main():
    st.set_page_config(page_title="Valentina and Luca's Wedding", layout="wide")
    page = navigation_menu()

    if page == "Homepage":
        homepage()
    elif page == "Location":
        location()
    elif page == "RSVP":
        rsvp()

if __name__ == "__main__":
    main()
