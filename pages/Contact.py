import streamlit as st
import send_email

st.title("Contact Me")

with st.form(key="form"):         #Create a form
    user_email=st.text_input(label="Your Email")
    message=st.text_area("Your Message",key="text_area")
    button=st.form_submit_button(label="submit")
    if button:      #Send email
        send_email.send_email("Subject: Portfolio Webpage"+"\n"+message+"\n"+user_email)
        st.info("Email sent successfully")



print(message)
