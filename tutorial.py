import streamlit as st
import base64


# video_url = "https://www.canva.com/design/DAFkfYQ5ib0/v0ySOeG4uRylgKCALuEwlA/edit?utm_content=DAFkfYQ5ib0
# &utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton" video_file = st.video(video_url) video_file =
# open('tutorialWorkEff.mp4', 'rb') video_bytes = video_file.read()

def playTut():
    st.title("Not Sure How to use this AI Model?")

    font_size = 24

    # Apply CSS styling to change the font size of st.title
    st.markdown(f"<h1 style='font-size: {font_size}px;'>Take a quantum leap towards skyrocketing your efficiency with Jarvis, empowering you to unlock your maximum potential.</h1>",
                unsafe_allow_html=True)

    # st.title('')
    tut = st.button('How to get the best out of Jarvis?')

    if tut:
        st.markdown(
            f"<h1 style='font-size: {font_size}px;'>I couldn't upload the video because of the constraints of "
            f"GitHub.(It was more than maximum video size)</h1>",
            unsafe_allow_html=True)

        st.markdown(
            f"<h1 style='font-size: {font_size}px;'>I am uploading a Tutorial Video link and PDF for deeply exploring "
            f"my Website.</h1>",
            unsafe_allow_html=True)

        # Reading the Tutorial file
        with open("tutorial.pdf", "rb") as file:
            file_data = file.read()

        # Convert file data to base64
        encoded_file = base64.b64encode(file_data).decode('utf-8')

        # Create a download link
        href = f'<h2><a href="data:application/pdf;base64,{encoded_file}" download="file.pdf">Get the Tutorial in PDF Format</a></h2>'
        st.markdown(href, unsafe_allow_html=True)

        video_link = "https://youtu.be/xX9MMByubos"

        st.title(f"[Watch the Video Tutorial]({video_link})")



