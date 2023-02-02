import streamlit as st

st.set_page_config(page_title="Portfolio",layout="wide")


col1,col2=st.columns(2)



with col1:
    st.image("images/photo.jpg")
    st.subheader("TO-Do App")

about_me_str="""
Hello, this is Aviral. I enjoy coding and am passionate about developing firmwares for hardware 
prototypes as well as developing software applications using python.
"""

with col2:
    st.title("About Me")
    st.info(about_me_str)