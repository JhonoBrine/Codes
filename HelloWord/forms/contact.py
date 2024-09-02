import streamlit as st
import re
import requests
import time




WEBHOOK_URL = st.secrets["WEBHOOK_URL"]

def is_valid_email(email):
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

##

def contact_form():
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email Address")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            if not WEBHOOK_URL:
                st.error("Email service is not set up. Please try again later.", icon="📧")
                st.stop()

            if not name:
                st.error("Please enter your name!", icon="🙂")
                st.stop()

            if not email:
                st.error("Please enter your email address!", icon="📨")
                st.stop()

            if not is_valid_email(email):
                st.error("Please provide a valid email address!", icon="📧")
                st.stop()

            if not message:
                st.error("Please enter your message!", icon="💬")
                st.stop()

            data = {"email": email, "name": name, "message": message}
            response = requests.post(WEBHOOK_URL, json=data)

            with st.spinner('Sending 📨...🖥️'):
                time.sleep(5)
                if response.status_code == 200:
                    st.success("Your message has been sent successfully!", icon="🚀")
                else:
                    st.error("There was an error sending your message!", icon="😥")

def add_pdf_download_button(pdf_path, button_label="📄Sample Resume"):

    with open(pdf_path, 'rb') as pdf_file:
        pdf_data = pdf_file.read()

    st.download_button(
        label=button_label,
        data=pdf_data,
        file_name="PABROA_Sample-Resume.pdf",
        mime="application/pdf",
        type="primary"
)