import streamlit as st
import pandas as pd
import os

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
    st.write("The wedding will take place at Ristorante alla Madonnina di Barni, at Via alla Madonnina, 22030, Barni, Italy")
    # st.map(location=["ia alla Madonnina, 22030, Barni, Italy"])

    # Embedded Google Maps map
    map_url = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d13376.58358882849!2d9.279663353971735!3d45.903857368447824!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47842494b52cf5ed%3A0xefa8dd191f0d6360!2sYour%20Wedding%20Location!5e0!3m2!1sen!2sus!4v1568286161380!5m2!1sen!2sus"
    # map_html = f'<iframe width="100%" height="450" frameborder="0" style="border:0" src="{map_url}" allowfullscreen></iframe>'
    st.markdown(f'<iframe width="600" height="400" frameborder="0" style="border:0" src="{map_url}" allowfullscreen></iframe>', unsafe_allow_html=True)

# RSVP
def rsvp():
#    st.title("RSVP")
#    st.write("Please RSVP by filling out the form below:")
#    name = st.text_input("Your Name:")
#    email = st.text_input("Your Email:")
#    attending = st.selectbox("Are you attending?", ("Yes", "No", "Maybe"))
#    st.write(f"Name: {name}")
#    st.write(f"Email: {email}")
#    st.write(f"Attending: {attending}")

# Define the CSV file path
    csv_file_path = "data/rsvp_data.csv"

    # Create a function to display and handle the RSVP form
    st.title("RSVP")
    st.write("Please RSVP by filling out the form below:")

    # Create the form for RSVP
    with st.form(key="rsvp-form"):
        name = st.text_input("Your Name:")
        num_guests = st.number_input("Number of Guests (including yourself):", min_value=1, step=1)
        email = st.text_input("Your Email:")
        phone = st.text_input("Phone Number:")
        allergies = st.text_area("Do you have any allergies? (if any):")
        menu_type = st.selectbox("Do you have any restictions?, ("No","Vegetarian","Vegan","No fish","No meat"))

        submit_button = st.form_submit_button("Submit RSVP")

    # Handle form submission
    if submit_button:
        # Check if the CSV file exists, and create it if not
        if not os.path.exists(csv_file_path):
            with open(csv_file_path, "w") as file:
                file.write("Name,Number of Guests,Email,Phone,Allergies,MenuType\n")

     # Append the RSVP data to the CSV fill
        with open(csv_file_path, "a") as file:
            file.write(f"{name},{num_guests},{email},{phone},{allergies},{menu_type}\n")

    # Display a confirmation message
        st.success("Thank you for your RSVP! We look forward to seeing you at the wedding.")
    
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
