import pandas
import streamlit as st
import pandas as pd
def Row_gap(gap):
    while (gap):
        st.write("")
        gap=gap-1

st.set_page_config(page_title="Portfolio",layout="wide")


col1,col2=st.columns(2)



with col1:
    st.image("images/photo.jpg")

about_me_str="""
Hello, this is Aviral. I enjoy coding and am passionate about developing firmwares for hardware 
prototypes as well as developing software applications using python.
"""

with col2:
    st.title("About Me")
    st.info(about_me_str)


st.header("You can find the applications that I have coded using python")

#declare 2 new columns
col3,col4=st.columns(2)

df=pandas.read_csv("data.csv",sep=";")      #data being read separated by ;

with col3:
    for index, row in df[0:10].iterrows():        #Print first 10 rows of csv with title
        st.subheader(row["title"])

with col4:
    for index, row in df[10:].iterrows():        #Print next 10 rows of csv with title
        st.subheader(row["title"])