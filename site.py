import streamlit as st
from homepage import render_homepage
from location import render_location
from rsvp import render_rsvp

# Define function to create navigation menu
def navigation_menu():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to:", ("Homepage", "Location", "RSVP"))
    return page

# Main function to run the app
def main():
    st.set_page_config(page_title="Valentina and Luca's Wedding", layout="wide")
    page = navigation_menu()

    if page == "Homepage":
        render_homepage()
    elif page == "Location":
        render_location()
    elif page == "RSVP":
        render_rsvp()

if __name__ == "__main__":
    main()
