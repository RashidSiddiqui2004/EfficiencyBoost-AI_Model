
import streamlit as st


def contact_us():
    st.title("Contact Us")
    st.write("Have questions or feedback? We'd love to hear from you!")

    # Contact form
    st.subheader("Send us a message")
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submit_button = st.button("Submit")

    if submit_button:
        # Perform validation and send the message
        if not name or not email or not message:
            st.error("Please fill in all the fields.")
        else:
            # Logic to send the message
            # You can integrate with your preferred email or messaging service here
            st.success("Your message has been sent successfully!")
            st.info("We will get back to you soon.")

    # Contact information
    st.subheader("Reach out to us")
    st.markdown(
        """
        **Email:** siddiqui20042007@gmail.com\n
        **Phone:** +91 8368417196\n
        **Address:** 123 Main Street, New Delhi, India
        """
    )
