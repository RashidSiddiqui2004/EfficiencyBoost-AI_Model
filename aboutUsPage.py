import pandas as pd
import streamlit as st
from PIL import Image

linkedInURL = "https://www.linkedin.com/in/rashid-siddiqui-b014ba264"
instaURl = "https://www.instagram.com/in"
gitHubUrl = "https://github.com/RashidSiddiqui2004"

# Add CSS styling to position the image
st.markdown(
    """
    <style>
    .center {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 450px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def init():
    st.title("---Author's Details---")

    st.image("ProfilePic.jpeg", width=300)

    st.title("NAME: Rashid Siddiqui")
    st.title("College: Netaji Subhash University of Technology")

    st.title("SOCIAL MEDIA HANDLES")

    font_size = 24  # Adjust the value as needed

    # Apply CSS styling to change the font size of st.title
    st.markdown(f"<h1 style='font-size: {font_size}px;'>Let's Connect and Grow Together on LinkedIn!</h1>", unsafe_allow_html=True)
    st.markdown(f'''
    <a href={linkedInURL}><button style="background-color: #6C757D ; font-color: #FFFFFF">LinkedIn ID</button></a>
    ''', unsafe_allow_html=True)

    st.markdown(f"<h1 style='font-size: {font_size}px;'>Github Profile Link</h1>",
                unsafe_allow_html=True)

    st.markdown(f'''
           <a href={gitHubUrl}><button style="background-color:#6C757D; font-color: #FFFFFF">GitHub Profile Link</button></a>
           ''', unsafe_allow_html=True)

    st.markdown(f"<h1 style='font-size: {font_size}px;'>Follow me on Instagram</h1>",
                unsafe_allow_html=True)

    st.markdown(f'''
       <a href={instaURl}><button style="background-color:#6C757D; font-color: #FFFFFF">Instagram ID</button></a>
       ''', unsafe_allow_html=True)
