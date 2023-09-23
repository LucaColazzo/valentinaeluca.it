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
    st.write("Via alla Madonnina, 22030, Barni, Italy")
#    st.map(location=["ia alla Madonnina, 22030, Barni, Italy"])

    # Embedded Google Maps map
    map_url = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d13376.58358882849!2d9.279663353971735!3d45.903857368447824!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47842494b52cf5ed%3A0xefa8dd191f0d6360!2sYour%20Wedding%20Location!5e0!3m2!1sen!2sus!4v1568286161380!5m2!1sen!2sus"
    st.markdown(f'<iframe width="800" height="600" frameborder="0" style="border:0" src="{map_url}" allowfullscreen></iframe>', unsafe_allow_html=True)

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
