import streamlit as st

from PIL import Image
import base64
import app
import aboutUsPage
import contactUs
import statistics
import tutorial


def add_logo(logo_path, width, height):
    """Read and return a resized logo"""
    logo = Image.open(logo_path)
    modified_logo = logo.resize((width, height))
    return modified_logo


icon = add_logo('workEffLogo.jpg', width=35, height=35)

# st.set_page_config(
#     page_title='EfficiencyBoost',
#     page_icon=icon
# )

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

padding = 0
st.markdown(f""" <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """, unsafe_allow_html=True)

my_logo = add_logo(logo_path="clientLOGO.jpg", width=150, height=150)

st.sidebar.image(my_logo)


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
        unsafe_allow_html=True
    )


add_bg_from_local('bg2.jpg')

image = Image.open('background.png')

st.sidebar.title('Work Efficiency Booster ')
st.sidebar.title('- EffiMax Solutions')

pageNavigation = st.sidebar.radio(label="", options=['Home', 'Statistics', 'Tutorial', 'Contact Us', 'About Us'])

if pageNavigation == 'Home':
    app.assistUser()

elif pageNavigation == 'Statistics':
    statistics.stats()

elif pageNavigation == 'Tutorial':
    tutorial.playTut()

elif pageNavigation == 'Contact Us':
    contactUs.contact_us()

elif pageNavigation == 'About Us':
    aboutUsPage.init()
