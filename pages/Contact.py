import streamlit as st

st.title("Contact Me")

with st.form(key="form"):         #Create a form
    user_email=st.text_input(label="Your Email")
    message=st.text_area("Your Message")
    button=st.form_submit_button(label="submit")
    if button:      #Send email



