import streamlit as st
#from send_email import send_email

st.header("Contact Us")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message here")
    message = message + "\n" + user_email
    button = st.form_submit_button("Submit")
    print(button)
    # if button:
    #     send_email(message)
