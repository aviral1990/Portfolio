import pandas
import streamlit as st

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


st.subheader("You can find the applications that I have coded using python")
st.subheader("")
st.subheader("")

#declare 2 new columns
col3,empty_col,col4=st.columns([1.5,0.5,1.5])     #Ratio of column width

df=pandas.read_csv("data.csv",sep=";")      #data being read separated by ;

with col3:
    for index, row in df[0:10].iterrows():        #Print first 10 rows of csv with title
        st.subheader(row["title"])
        st.write(row["description"])              #Print descriptions from csv
        st.image("images/" + row["image"])        #in directory images, title image in csv
        st.write(f"[Source Code]({row['url']})")  #Label the link from csv as source code

with col4:
    for index, row in df[10:].iterrows():        #Print next 10 rows of csv with title
        st.subheader(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])  # in directory images, title image in csv
        st.write(f"[Source Code]({row['url']})")  # Label the link from csv as source code